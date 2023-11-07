def do_twice(func):      # here, we are creating a function and passing the parameter  
    def wrapper_do_twice(*args,**kwargs):       
     # here, we are creating a function and passing the parameter  
        func(*args,**kwargs)    
        func(*args,**kwargs)    
    return wrapper_do_twice  