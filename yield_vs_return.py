# Use of yield
def printresult(String) : 
    for i in String: 
        if i == "e": 
            yield i
            
def return_print():
    a = "Return part"
    return a

def yield_print():
    a = "Yield part"
    yield a
    

r = return_print()
y = yield_print()
print(r)
print(y)
print(next(y))
 