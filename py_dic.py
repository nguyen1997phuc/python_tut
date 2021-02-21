# python dictionary
dict_1 = {
	'one': 1,
	'two': 2
}

# print(dict_1)
# print(type(dict_1))


dict_2 = dict(id=123, name='jone')
# print(dict_2)

python_dict = {
	'name': 'python',
	'version': '3.8',
	'description': 'high level programing language',
	'level': 'beginner',
}

name_present_python_dict = 'name' in python_dict
name_not_present_python_dict = 'name' not in python_dict
# print(name_present_python_dict)
# print(name_not_present_python_dict)

py_name = python_dict['name']
# print(py_name)
python_dict['name'] = 'pyt'
# print(python_dict)
del python_dict['name']
# print(python_dict)
# print(len(python_dict))
# print(python_dict.keys())
# print(python_dict.values())
# print(python_dict.get('duration', 'not found'))
print(python_dict.pop('level'))
print(python_dict)
