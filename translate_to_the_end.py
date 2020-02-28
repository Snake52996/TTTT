#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import time
from googletrans import Translator
from setting_holder import getSetting
setting = getSetting()
translator = Translator(service_urls=[setting["translator"]["url"]])
def operateSentense(sentense):
	if isinstance(sentense, str):
		steps = setting["translation"]["steps"]
		print("Origin: %s" % sentense)
		temp_result = translator.translate(sentense, steps[0], setting["IO"]["input_file"]["language"]).text
		print("First step: %s -> %s => %s" % (setting["IO"]["input_file"]["language"], steps[0], temp_result))
		translate_round = 0
		step_index = 1
		result_dict = dict()
		while True:
			time.sleep(setting["translator"]["delay_milliseconds"] / 1000)
			temp_result = translator.translate(
				temp_result,
				steps[step_index],
				steps[(step_index - 1) if(step_index > 0) else (len(steps) - 1)]
			).text
			print("%s -> %s => %s" % (steps[(step_index - 1) if(step_index > 0) else (len(steps) - 1)], steps[step_index], temp_result))
			step_index += 1
			if step_index == len(steps):
				translate_round += 1
				if translate_round == setting["translation"]["rounds"]:
					return temp_result
				if result_dict.__contains__(temp_result):
					return temp_result
				else:
					result_dict[temp_result] = 1
					step_index = 0
	else:
		print("Invalid paramater.")
if setting["IO"]["input_file"]["path"] == None:
	input_file_path = input("Give me file: ")
else:
	input_file_path = setting["input_file"]["path"]
if setting["IO"]["output_file"]["path"] == None:
	output_file_path = input_file_path + ".out"
else:
	output_file_path = setting["output_file"]["path"]
try:
	input_file = open(input_file_path, 'r', encoding=setting["IO"]["input_file"]["encode"])
	output_file = open(output_file_path, "w", encoding=setting["IO"]["input_file"]["encode"])
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