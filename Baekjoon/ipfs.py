# import ipfsApi
import ipfshttpclient
client = ipfshttpclient.connect()

# ipfs_api = ipfsApi.Client("127.0.0.1", 5001)
# ipfs_response = ipfs_api.get("QmVaiVga4BpZ2XGoB9gzH6rf8wuTpWx1KFRKiTJvfQU44u")
ipfs_response = client.get("QmVaiVga4BpZ2XGoB9gzH6rf8wuTpWx1KFRKiTJvfQU44u")
print(ipfs_response)