import glob
import json
import os
import platform
import time
import uuid
import cv2
import numpy as np
import openai
import requests
from PIL import Image, ImageDraw, ImageFont


def test_for_makeing_json_from_dict():
	dict_example = {
		"company" : "fucking",
		"name" : "Lee",
		"role" : "학생",
		"phonenumber" : "010-1234-1234",
		"address" : "wherever",
		"email" : "whatever",
	}
	return json.dumps(dict_example)

def put_text(image, text, x, y, color=(0, 255, 0), font_size=22):
	if type(image) == np.ndarray:
		color_converted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		image = Image.fromarray(color_converted)
	
	if platform.system() == 'Darwin':
		font = 'AppleGothic.ttf'
	elif platform.system() == 'Windows':
		font = 'malgun.ttf'
	
	image_font = ImageFont.truetype(font, font_size)
	draw = ImageDraw.Draw(image)
	draw.text((x, y), text, font=image_font, fill=color)
	
	numpy_image = np.array(image)
	opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
	return opencv_image

def get_result():
	# OpenAI API 키 설정
	api_key = "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"
	openai.api_key = api_key
	
	# 이미지가 있는 폴더 경로 설정
	image_folder = '/Users/idogyeong/Desktop/namecard_backend_test/media/images/'
	
	# 이미지 폴더에서 모든 이미지 파일 가져오기
	list_of_files = glob.glob(os.path.join(image_folder, '*.*'))
	
	# 가장 최신 파일 선택 (파일의 생성시간을 기준으로)
	latest_file = max(list_of_files, key=os.path.getctime)
	
	# API 요청 및 결과 받아오기
	api_url = 'https://wpk791ljbg.apigw.ntruss.com/custom/v1/25541/c2ef5060da5b83a9ca0601d267709ba5b4bc07535d31673fbff23e413400fff1/general'
	secret_key = 'bmFDbVVvcEluaGFpVmxvZkNHUFJsSGRwR1l1RmduZ3Y='
	files = [('file', open(latest_file, 'rb'))]
	
	request_json = {
		'images': [{'format': 'png', 'name': 'demo'}],
		'requestId': str(uuid.uuid4()),
		'version': 'V2',
		'timestamp': int(round(time.time() * 1000))
	}
	payload = {'message': json.dumps(request_json).encode('UTF-8')}
	headers = {'X-OCR-SECRET': secret_key}
	
	response = requests.request("POST", api_url, headers=headers, data=payload, files=files)
	result = response.json()
	
	img = cv2.imread(latest_file)
	roi_img = img.copy()
	
	# OpenCV의 putText 함수를 이용하여 한글을 출력하는 경우 한글이 깨지는 문제를 해결하기 위한 함수
	
	# 추출된 텍스트와 해당 텍스트의 y 좌표를 저장
	text_coordinates = []
	for field in result['images'][0]['fields']:
		y_coord = sum([vertice['y'] for vertice in field['boundingPoly']['vertices']]) / 4
		text_coordinates.append((field['inferText'], y_coord))
	
	# y 좌표를 기준으로 텍스트들을 그룹화
	tolerance = 5  # y 좌표가 이 범위 내에 있으면 같은 그룹으로 취급
	grouped_texts = []
	current_group = [text_coordinates[0][0]]
	
	for i in range(1, len(text_coordinates)):
		if abs(text_coordinates[i][1] - text_coordinates[i - 1][1]) < tolerance:
			current_group.append(text_coordinates[i][0])
		else:
			grouped_texts.append(' '.join(current_group))
			current_group = [text_coordinates[i][0]]
	
	grouped_texts.append(' '.join(current_group))  # 마지막 그룹 저장
	
	text2 = ""
	for text in grouped_texts:
		text2 += text + "\n"
	
	# 결과에서 텍스트를 추출하고 bounding box를 그립니다.
	# 결과에서 텍스트를 추출하고 bounding box를 그립니다.
	for field in result['images'][0]['fields']:
		text = field['inferText']
		vertices_list = field['boundingPoly']['vertices']
		pts = [tuple(vertice.values()) for vertice in vertices_list]
		topLeft = [int(_) for _ in pts[0]]
		
		# 바운딩 박스 그리는 부분 제거
		roi_img = put_text(roi_img, text, topLeft[0], topLeft[1] - 10, font_size=30)
	
	# 정보 추출 요청
	response = openai.ChatCompletion.create(
		model="gpt-4",
		messages=[
			{"role": "system", "content": "You are a helpful assistant."},
			{"role": "user",
			 "content": f"다음 텍스트에서 Company : , Name : , Role : , PhoneNumber : , Address : , Email : 만 간략히 정리후 없는 내용은 없음으로 표시해줘 그리고 이름은 한글이름만 표시해줘: \"{text2}\""}
		]
	)
	
	info = response['choices'][0]['message']['content']
	
	# info 문자열을 줄바꿈으로 분할하여 리스트로 변환
	info_lines = info.strip().split("\n")
	
	# 딕셔너리 초기화
	info_dict = {}
	
	# 각 줄을 순회하며 딕셔너리에 추가
	for line in info_lines:
		# ":"로 분할할 수 있는지 확인
		if ":" in line:
			key, value = line.split(":", 1)  # 첫 번째 ":"에서만 분할
			info_dict[key.strip()] = value.strip()
	
	#result_json = json.dumps(info_dict)
	# 결과 출력 딕셔너리 형태로 반환
	return json.dumps(info_dict, ensure_ascii=False)

