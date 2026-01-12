import json 

# it converts python data into json data

py_data = {'x':True , "y":False , '''z''':None}

json_data = json.dumps(py_data)
print(json_data)
print(type(json_data))
