import requests
import time
run_time = time.time()
while True:
    a = requests.get("http://postman-echo.com/get?foo1=bar1")
    curr= time.time()
    print(a.text)
    if curr-run_time >= 60:
        break
