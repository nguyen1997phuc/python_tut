from requests import post

url = 'xxx'
user_name = 'xxx'
password = 'xxx'

response = post(url=url, auth=(user_name, password))
print(response)
