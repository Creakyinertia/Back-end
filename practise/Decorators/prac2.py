from mod_decorators import do_twice   
 
@do_twice    
def say_hello(x,y):    
    print(x+y)    
say_hello(5,3)   