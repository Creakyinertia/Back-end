# import json
# class employee:
#     def __init__(self, id, details):
#       self.id = id
#       self.details = details
#     # global json_file
#     # json_file=[]
#     # def add_user(self):
#     #     user = {
#     #     "id":self.id,
#     #     "details":self.details
#     #     }
#     #     with open("users.json","w") as file:
#     #         # data = json.load(file)
#     #         # print(data,type(data))
#     #         json_file.append(user)
#     #         json.dump(json_file,file,indent=4)
    
#     def addnew(self):
#         user = {
#         self.id:self.details
#         }
        
#         with open("users.json","r") as file:
#             data = list(json.load(file))
#             print(data,type(data))
        
#         data.append(user)
        
#         with open("users.json","w") as file:
#             json.dump(data,file,indent=4)
        
#     def delete(self,id):
#         with open("users.json","r") as file:
#             data = list(json.load(file))
        
#         dict1={}
        
#         for x in range(len(data)):
#                 dict1.update(data[x])   
        
#         dict1.pop(str(id))
#         print(dict1)
#         x3=list(dict1.items())
#         print(x3)
#         l4={}
        
#         for x7 in x3:
#             l4[x7[0]]=x7[1]    
        
#         l3=[l4]
#         print(l3)
#         with open("users.json","w") as file:
#             json.dump(l3,file,indent=4)
        
#     def display(self):
#         print(self.id , self.details)
        
        
# e1 = employee(2,{"name":"rakshi","age":1})
# # e1.display()
# # e1.addnew()
# e3 = employee(6,{"name":"rakshitha","age":6})
# # e2.addnew()
# # e2.display()
# e3.delete('3')

# hel={
# 	'first':'element',
# 	'two':2,
# 	'three':3,
# 	'four':2
# }
# print("The original dictionary is : " + str(hel))
# res = {}
# for key, val in hel.items():
#     res.setdefault(val, key)
# print("The dictionary after values removal : " +
#       str(dict((v, k) for k, v in res.items())))


# test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
# print("The original dictionary is : " + str(test_dict))
# unique_values = set(test_dict.values())
# res = {}
# for val in unique_values:
# 	for key in test_dict.keys():
# 		if test_dict[key] == val:
# 			res[key] = val
# 			break
# print("The dictionary after values removal : " + str(res))

# dict = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# def remove_dict(d,v):
#     f=[]
#     for i in range(len(d)):
#         if(d[i]['id'] == v):
#             print(d[i]['id'])
            
#     return d
# print(remove_dict(dict,"#800000"))









