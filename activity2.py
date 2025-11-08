class employee:
    def __init__(self):
        print ('employee created')
    def __del__(self):
        print ("destructor called")
def create_obj():
    print("Making obj")
    obj=employee()
    print("function end")
    return obj
print("Calling create_obj() function...")
obj=create_obj()
print("Program End...")