from shutil import which
from seleniumwire  import webdriver
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
CHROMEPATH = which("chromium-browser")
options.binary_location=CHROMEPATH
wd = webdriver.Chrome(options=options)
wd.implicitly_wait(10)

import time, re, os, requests

wd.get("https://www.tutorialbar.com/")
elem = wd.find_element_by_css_selector(".col_item")
wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
for request in wd.requests:
    if request.response and request.method == 'POST' and ('admin-ajax' in request.url):
        req_body = request.body.decode('utf8')
        secure = req_body[req_body.rfind('security=')+len('security='):]
        break
        
wd.get("https://coursevania.com/courses/")
time.sleep(2)
elem = wd.find_element_by_css_selector("a.stm_lms_load_more_courses")
print(elem)
elem.click()
elem.click()
time.sleep(2)
wd
for request in wd.requests:
    # print(request.url)
    if 'admin-ajax' in request.url:
        # req_body = request.body.decode('utf8')
        secure = request.url[request.url.rfind('nonce=')+len('nonce='):request.url.rfind('&')]
        print(request.url, request.querystring)
        print(secure)
        break
        
import requests
url = 'https://jsonblob.com/api/jsonBlob/'+os.environ.get('jsonBlobID')
data = {
    "tutbar_sec": secure
}
r = requests.put(url, verify=False, json=data)
