from time import perf_counter,process_time,sleep, time
from functools import wraps
import threading

def speedtest(func):
    @wraps(func) 
    def wrapper(*args,**kwargs):
        t0=perf_counter()
        function=func(*args,**kwargs)
        t1=perf_counter()
        print("The function",func.__name__," took ",t1-t0, "seconds")
        return function
    return wrapper

def speedtest_silent(func):
    @wraps(func) 
    func._times=[]
    def wrapper(*args,**kwargs):
        t0=perf_counter()
        function=func(*args,**kwargs)
        t1=perf_counter()
        func._times.append({time():t1-t0})        
        return function
    return wrapper 

def speedtest_minus_sleep(func):
    @wraps(func) 
    func._times=[]
    def wrapper(*args,**kwargs):
        t0=process_time()
        function=func(*args,**kwargs)
        t1=process_time()
        print("The function",func.__name__,"took",t1-t0, "seconds")
        return function
    return wrapper
    
def speedtest_minus_sleep(func):
    @wraps(func) 
    func._times=[]
    def wrapper(*args,**kwargs):
        t0=process_time()
        function=func(*args,**kwargs)
        t1=process_time()
        func._times.append({time():t1-t0})        
        return function
    return wrapper

def run_threaded(func):
    @wraps(func) 
    def wrap_and_run(*args,**kwargs):
        t = threading.Thread(target=func,args=args,kwargs=kwargs)
        t.start
        return t
    return wrap_and_run

@speedtest_minus_sleep
def test():
    print("Starting function")
    sleep(1)
    return 0

print(test())
