## Requirements

+ ADB
+ ChromeDriver
+ Baidu OCR SDK

## OCR
在[百度云](https://console.bce.baidu.com/)创建文字识别应用，将应用的AppID、API Key、Secret Key填到代码中：
```py
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
```

## Chrome
下载最新的[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)并配置路径`driver_path`

## Usage

    pip3 install -r requirements.txt
    python3 seeker.py
