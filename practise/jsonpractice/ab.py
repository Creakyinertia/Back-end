import json
class ab:
    def __init__(self,id,name,age,company):
        self.id=id
        self.name=name
        self.age=age
        self.company=company      
    
    
           
    def display(self):
        with open('abc.json','w')as ad:
            json.dump(obj1,ad)
    
obj=ab('1','darshu','23','estuate')
obj1=dict(id=obj.id,name=obj.name,age=obj.age,company=obj.company)
