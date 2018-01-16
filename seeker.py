import os, time
from selenium import webdriver
from PIL import Image
from aip import AipOcr

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
driver_path = '/Applications/Google Chrome.app/Contents/MacOS/chromedriver'

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
driver = webdriver.Chrome(driver_path)
driver.get('https://www.baidu.com')
os.system("adb devices")

while True:
    text = input('下一题')
    start = time.time()
    imagepath = "tmp.png"
    regionpath = "problem_" + str(start) +".png"

    os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png")
    os.system("adb pull /sdcard/screenshot.png " + imagepath)

    im = Image.open(imagepath)
    w = im.size[0]
    h = im.size[1]
    #region = im.crop((80, 300, 1000, 520))  #1920*1080
    region = im.crop((w*0.075, h*0.160, w*0.925, h*0.330))  #16:9
    region.save(regionpath)
    image = get_file_content(regionpath)
    result = client.basicGeneral(image);
    
    words = result['words_result']
    keyword = ''
    for word in words:
        keyword += word['words']
    problem = keyword.split('.',1)[-1]
    print("problem=" + problem)
    driver.get('https://www.baidu.com/s?wd=' + problem)
    #driver.get('https://www.google.com/search?q=' + problem)

    end = time.time()
    print('cost=' + str(end - start) + 's\n')
