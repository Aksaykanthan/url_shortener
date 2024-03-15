
import requests

url = "https://www.youtube.com/results?search_query=building+expense+tracker+from+sms+messages"


x = requests.get(f"http://127.0.0.1:3000/shorten?url={url}")
short = x.json()['url']
print(f"shorten link : {short}")

y = requests.get(f"http://127.0.0.1:3000/unshorten?url={short}")
orig = y.json()['url']
print(f"orginal link : {orig}")

