from collections import Counter

import requests
import os
import pickle

import base64

ipfs = "http://127.0.0.1:5001/api/v0/"
func = "add"
get_func = "get"
cid = "QmVaiVga4BpZ2XGoB9gzH6rf8wuTpWx1KFRKiTJvfQU44u"
query = "?arg={cid}&output={output}&stream-channels=true".format(cid=cid, output=cid+".jpg")
# query = "?cid-version=1"
# data = {
#     'path':'test.txt'
# }
headers = {
    'Content-Type': 'application/x-directory',
    'Content-Type': "multipart/form-data;" , 
    'Content-Disposition': 'form-data; name="file"; filename="test.txt"',
}
req_string = ipfs + get_func + query
# files = {
#     "file": open("test.txt", "rb"),
# }

# req = requests.post(req_string, files=files)
req = requests.post(req_string, stream=True)

print(req.headers)
# with open("get_from_ipfs.txt", "wb") as f:
#     for chunk in req.iter_content(chunk_size=5000):
#         f.write(chunk)



# content = []
# for chunck in req["file"]["content"]:
#     content.append(chunck)
# buffer = []
# for c in content:
#     buffer.append
# print(req.text)
