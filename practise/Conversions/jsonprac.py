import json  
# print(dir(json))  

student  = {  
"Name" : "Peter",  
"Roll_no" : "0090014",  
"Grade" : "A",  
"Age": 20,  
    "Subject": ["Computer Graphics", "Discrete Mathematics", "Data Structure"]  
}  
  
# with open("data.json","w") as f:  
#     json.dump(student,f)  
    

# b = json.dumps(student)  

with open("data.json", "r") as read_file:  
    json.load(read_file)

# c = json.loads(b)  
