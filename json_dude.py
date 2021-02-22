import json

file_url = 'static/data'
data = {
	'name': 'phuc',
	'age': 24,
	'occupation': 'dev',
}

with open(file_url, 'w') as f:
	json.dump(data, f)

with open(file_url, 'r') as _f:
	res = _f.readline()

s = '{"wonderland": [1, 2, 3], "foo": "bar", "alice": 1}'
print(json.loads(s))
