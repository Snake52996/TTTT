#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from googletrans import Translator
translator = Translator(service_urls=['translate.google.cn'])
def operateSentense(sentense):
	if isinstance(sentense, str):
		print(sentense)
		temp0 = translator.translate(sentense, 'zh-cn').text
		print(temp0)
		while True:
			temp1 = translator.translate(temp0, 'ja').text
			print(temp1)
			temp2 = translator.translate(temp1, 'zh-cn').text
			print(temp2)
			if temp0 == temp2:
				return temp2
			temp0 = temp2
	else:
		print("Invalid paramater.")
file_path = input("Give me file: ")
try:
	input_file = open(file_path, 'r')
	output_file = open(file_path + ".out", "w")
	while True:
		text_line = input_file.readline().strip()
		if text_line:
			output_file.write(operateSentense(text_line) + "\n")
		else:
			break
finally:
	if input_file:
		input_file.close()
	if output_file:
		output_file.close()
"""
result = translator.translate("那你去找物管啊!")
print(result.text)
"""