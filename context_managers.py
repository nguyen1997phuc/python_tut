# import requests
#
# payload = dict(
# 	key1='value1',
# 	key2='value1',
# )
#
# r = requests.post('https://httpbin.org/post', data=payload)
# print(r.text)


user1 = dict(name='user1', age=21)
user2 = dict(name='user2', ages=22)
user3 = dict(name='user3', age=23)
user4 = dict(names='user4', age=24)

users = [user1, user2, user3, user4]

for user in users:
	print(user.get('name', 'n/a'))

for user in users:
	print(user.get('age', 'n/a'))

for user in users:
	user['young'] = True if (user.get('age') or 30) < 24 else False

for user in users:
	print(user)
