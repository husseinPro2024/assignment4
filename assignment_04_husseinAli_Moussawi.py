#HomeWork4
#Ex.1
def sumtuple(tup1,tup2):#choice 1
    tup3=()
    for i in range(len(tup1)):
        sum=tup1[i]+tup2[i]
        tup3=tup3+(sum,)
    return tup3

def felldictionary(dictionary):#choice 2
    for key in dictionary.keys():
        dictionary[key] = input(f"Enter value for {key}: ")
    return dictionary
def dict_to_json_manual(dictionary, filename):#choice 2 
    def dict_to_json_str(dictionary):
        json_str = "{\n"
        for i, (key, value) in enumerate(dictionary.items()):
            json_key = f'"{key}"'  
            if isinstance(value, str):
                json_value = f'"{value}"' 
            elif isinstance(value, bool):
                json_value = "true" if value else "false"
            elif value is None:
                json_value = "null"  
            elif isinstance(value, dict):
                json_value = dict_to_json_str(value) 
            elif isinstance(value, list):
                json_value = "[" + ", ".join([dict_to_json_str(v) if isinstance(v, dict) else f'"{v}"' if isinstance(v, str) else str(v) for v in value]) + "]"
            else:
                json_value = str(value)  
            json_str += f'  {json_key}: {json_value}'
            if i < len(dictionary) - 1:
                json_str += ","
            json_str += "\n"
        json_str += "}"
        return json_str
    with open(filename, 'w') as file:
        json_str = dict_to_json_str(dictionary)
        file.write(json_str)

#choice 3
def convert_json_to_dicts(file_name):
    # Open the file and read its content
    with open(file_name, 'r') as file:
        json_content = file.read()
    
    # We'll use a simple parser for JSON-like structure
    json_objects = []
    current_obj = {}
    key = ''
    value = ''
    in_key = False
    in_value = False
    is_string = False
    is_number = False
    is_object = False
    
    # Traverse the content of the file
    for char in json_content:
        if char == '{':
            if not is_object:
                current_obj = {}
                is_object = True
        elif char == '}':
            if is_object:
                json_objects.append(current_obj)
                current_obj = {}
                is_object = False
        elif char == '"':
            if not is_string:
                in_key = True if not in_key and not in_value else False
                is_string = True
            else:
                is_string = False
                if in_key:
                    key = key.strip()
                    in_key = False
                elif in_value:
                    value = value.strip()
                    current_obj[key] = value
                    key = ''
                    value = ''
                    in_value = False
        elif char == ':':
            in_value = True
        elif char == ',':
            if in_value and not is_string:
                current_obj[key] = value.strip()
                key = ''
                value = ''
                in_value = False
        else:
            if in_key:
                key += char
            elif in_value:
                value += char
    
    return json_objects
while True :
    print("1. Sum Tuples")
    print("2. Export JSON")
    print("3. Import JSON")
    print("4. Exit")
    print("- - - - - - - - - - - - - - -")
    Input=int(input("Enter a choice:"))
    if Input==1:
       length=int(input("Enter length of tuples:"))
       tup1=()
       tup2=()
       while True :
            for i in range (length):
                 Input1=int(input(f"Enter Elements of tup1(Enter only {length} numbers ):"))
                 tup1=tup1+(Input1,)
            for i in range (length):
                 Input2=int(input(f"Enter Elements of tup2(Enter only {length} numbers ):"))
                 tup2=tup2+(Input2,)
            if len(tup1)==len(tup2):
                 tup3=sumtuple(tup1,tup2)
                 print("OutPut:",tup3)
                 break
            else:
                 print("not equal elements plz enter elements agian (be careful)")
    elif Input==2:
        i=0
        while True :
            i+=1
            fileName=input("Plz enter file name: ")
            dec=fileName+str(i)
            dec={
                "id":"",
                "name":"",
                "salary":"",
                "position":""
                }
            
            dic=felldictionary(dec)
            dict_to_json_manual(dic,fileName+".json")
            complete=input("do you want to compelete?/yes (if you dont want enter no)")
            if complete=="no":
                break
            elif complete=="yes":
                print("ok")
                print("-------------------------")
            else:
                 print("Invalid input")

            
    elif Input==3:
        file_name = input("Enter the name of the JSON file: ")
        converted_list = convert_json_to_dicts(file_name)
        print(converted_list)   
    elif Input==4:
        break
    else:
        print("not valid input")
#homework 2
"""
a-N^3
b-N^3
c-N!
d-NlogN
e-N
f-N^2
g-N^2
h-N!
N!>N2>NlogN>N>logN>1


"""