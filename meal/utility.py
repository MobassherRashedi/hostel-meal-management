class MyDictionary(dict):
# __init__ function
    def __init__(self, *args, **kwargs):
        self = dict()
# Function to add key:value
    def add(self,key,value):
        self[key] = value
    