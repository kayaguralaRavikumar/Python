import requests

api1 = 'http://127.0.0.1:8080/json'
api2 = 'http://127.0.0.1:8080/api2'
api3 = 'http://127.0.0.1:8080/api3'

api1_response = requests.get(api1)
api1_response = api1_response.json()
print('api_reso = ', api1_response)


api3_response = requests.post(api3 , params={'moviename' : 'ABC Movie'})
api3_response = api3_response.json()
print('api3_reso = ', api3_response)
