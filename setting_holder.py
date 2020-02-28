#!/usr/bin/python3
import json
def stringToInt(origin_string):
    result = 0
    temp_string = origin_string.strip()
    for c in temp_string:
        if c >= '0' and c <= '9':
            result = result * 10 + (ord(c) - ord('0'))
        else:
            return -1
    return result
def getString(hint, default_value_hint, default_value):
    temp_input = input("%s(%s): " % (hint, default_value_hint))
    if temp_input != "":
        return temp_input
    else:
        return default_value
def getNumber(hint, default_value_hint, default_value):
    temp_input = input("%s(%s): " % (hint, default_value_hint))
    if temp_input == "" or stringToInt(temp_input) < 0:
        return default_value
    else:
        return stringToInt(temp_input)
def createNewSetting(a):
    new_setting = dict(a["settings"][0])
    new_setting["translator"]["url"] = getString(
        "What server url would you like to use?",
        new_setting["translator"]["url"],
        new_setting["translator"]["url"]
    )
    new_setting["translator"]["delay_milliseconds"] = getNumber(
        "Wait time between requests. It aims to limit the request rate for the access to translation server via this api may be canceled if the rate is too high.",
        "700",
        700
    )
    new_setting["IO"]["input_file"]["path"] = getString(
        "Read from which file?",
        "DESIDE AT RUNTIME",
        None
    )
    new_setting["IO"]["input_file"]["encode"] = getString(
        "Encodeing of input file?",
        "utf-8",
        "utf-8"
    )
    new_setting["IO"]["input_file"]["language"] = getString(
        "Language of input file.",
        "auto",
        "auto"
    )
    new_setting["IO"]["output_file"]["path"] = getString(
        "Write to which file?",
        "ADD .out AFTER INPUT PATH",
        None
    )
    new_setting["IO"]["output_file"]["encode"] = getString(
        "Encodeing of output file?",
        "utf-8",
        "utf-8"
    )
    temp = input("Now please tell me the route of translation language, one each line. End with a empty line?(ja zh-cn):\n")
    temp_list = list()
    while True:
        if temp == "":
            break
        temp_list.append(temp)
        temp = input()
    if len(temp_list) >= 2:
        new_setting["translation"]["steps"] = temp_list
    new_setting["translation"]["rounds"] = getNumber(
        "Translate for how many rounds. Set to 0 to translate until the result no longer changes.",
        "0",
        0
    )
    new_setting["name"] = input("Finally, give this setting a name: ")
    a["settings"].append(new_setting)
    temp = input("Set this setting default?[Y]/n: ")
    if temp == "" or temp == "y" or temp == "Y":
        a["default"] = len(a["settings"]) - 1
    try:
        file = open("settings.json", "w")
        if file.writable == False:
            print("Oops, can't save setting! Terminate......")
            exit()
        file.write(json.dumps(a, indent="\t"))
    finally:
        if file:
            file.close()
def getSetting():
    try:
        file = open("settings.json", "r")
        if file.readable() == False:
            print("Can't read setting file. Terminate.")
            exit()
        a = json.loads(file.read())
    finally:
        if file:
            file.close()
    current_index = 0
    for setting in a["settings"]:
        print("%d. %s%s" % (current_index, setting["name"], "(DEFAULT)" if(current_index == a["default"]) else ""))
        current_index += 1
    print("%d. CREATE A NEW SETTING" % current_index)
    selection = input("Please select a setting by its index, or <ENTER> for default: ")
    if selection == "":
        selected_setting = a["default"]
    else:
        selected_setting = stringToInt(selection)
    if selected_setting > current_index or selected_setting < 0:
        print("Invalid index. Use default.")
        selected_setting = a["default"]
    elif selected_setting == current_index:
        createNewSetting(a)
    return a["settings"][selected_setting]