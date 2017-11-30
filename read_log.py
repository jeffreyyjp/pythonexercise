# encoding: UTF-8

"""read log fatal exception

This program reads a log file and search fatal exception info. Then saves all fatal exception info into a new file.
"""

count = 0
fatal_expection = []

with open("log.txt", "rb+") as f:
    for i in f:
        if i.find("E AndroidRuntime") == -1 and i.find("E/AndroidRuntime") == -1:
            continue
        if i.find("FATAL EXCEPTION") != -1:
                count += 1
        fatal_expection.append(i)

def get_fatal_exception():

    with open("result.txt", "wb+") as f:
        f.write("Total Fatal Exception : {}\n".format(count))
        if count <= 0:
            return
        f.write("-" * 96 + "\n" + "Detail:\n")
        index = 1
        for i in fatal_expection:
            if i.find("FATAL EXCEPTION") != -1:
                f.write("-" * 40 + " Index {} ".format(index) + "-" * 46 + "\n")
                index += 1
            f.write(i)
        f.write("-" * 40 + " End " + "-" * 50)

get_fatal_exception()
