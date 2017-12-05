# encoding: UTF-8

""" This Program uses uiautomator to change Android device's system language and save is's screenshot
"""

import os, time
from uiautomator import Device

time_wait_action = 3
time_wait_screenshot = 5
device_serial = raw_input("Please input your device serial: ")
d = Device(device_serial)

def device_setup():
    if len(d.info) < 0:
        return
    d.screen.on() # open device's screen.
    time.sleep(time_wait_action) # wait an while.
    d.press.home() # set device to home.
    os.system("adb shell am start -n com.android.settings/.Settings") # launch system settings app.
    time.sleep(time_wait_action)
    d(text='Language & input', className='android.widget.TextView').click() # select the "Language & input" listitem and click into it.
    time.sleep(time_wait_action)

def go_to_lang_list():
    d(className="android.widget.ListView", resourceId="android:id/list") \
    .child(instance=1).click() 
    time.sleep(time_wait_action)

def change_lang():
    go_to_lang_list()
    language_count = d(className="android.widget.TextView", resourceId="android:id/locale").count # Get language's total number
    print language_count
    for i in range(language_count):
        curr_selector = d(className="android.widget.ListView", resourceId="android:id/list").child(instance = i + 1)
        lang_name = curr_selector.info["text"] # Get language's name which can be used for screenshot image name.
        curr_selector.click() # Change language
        time.sleep(time_wait_action)
        d.screenshot("language_{}.png".format(lang_name.encode("utf-8"))) # Save display screen language screenshot.
        time.sleep(time_wait_screenshot)
        go_to_lang_list()

if __name__ == "__main__":
    device_setup()
    change_lang()

