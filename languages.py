# encoding: UTF-8

import fileinput, glob

lang_item = {}

def process(line):
    if line.find(':') != -1:

        lang_item[line.split(" : ")[0] + "_" + fileinput.filename().split("_")[1]] = line.split(" : ")[1]

for line in fileinput.input(glob.glob('language_*.js')):
    process(line)

with open("language_all.js", "wb+") as f:
    f.write("Config.language = {\n")
    for key in lang_item.keys():
        f.write("{0} : {1}".format(key, lang_item(key)))
