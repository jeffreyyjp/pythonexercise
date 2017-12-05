# encoding: UTF-8

import fileinput, glob

lang_dict = {}
lang_files = glob.glob("language_*.js")
lang_all = "language-all.js"

def process(line):
    """ Dealing each line and save it to a dict

    """
    if line.find(':') != -1:
        key, item = line.split(' : ')[0], line.split(" : ")[1]
        file_name_flag = fileinput.filename().split("_")[1].replace(".js", "")
        lang_dict[key + "_" + file_name_flag] = item

for line in fileinput.input(lang_files):
    process(line)

with open("lang_all", "wb+") as f:
    f.write("Config.language = {\n")
    sorted_keys = lang_dict.keys()
    sorted_keys.sort()
    i = 0
    for key in sorted_keys:
        if i % len(lang_files) == 0:
            f.write("-" * 20 + " " + key.split('_')[0] + " " + "-" * 20 + "\n")
        f.write("{0} : {1}".format(key, lang_dict[key]))
        i += 1
    f.write("}")
