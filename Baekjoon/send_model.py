import requests

url = "http://61.79.117.52:5000/dl/update_weight/"
headers = {"Content-Type": "application/json"}
json_data = {
    ## JSON 데이터
}
response = requests.post(url=url, headers=headers, json=json_data)