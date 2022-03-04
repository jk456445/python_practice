import requests
r = requests.get('https://ithelp.ithome.com.tw/articles?tab=tech')
print(r.status_code)  #伺服器回應的狀態碼
print(r.text)