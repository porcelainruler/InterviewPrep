print(2|7)

def comparator(a, b): 
    ab = str(a) + str(b) 
    ba = str(b) + str(a) 
    return ((int(ba) > int(ab)) - (int(ba) < int(ab))) >= 0

def myCompare(mycmp):
    class K(object):
        def __init__(self, obj):
            super().__init__()
            self.obj = obj
        
        def __lt__(self, value):
            return mycmp(self.obj, value.obj) < 0
        
        def __gt__(self, value):
            return mycmp(self.obj, value.obj) > 0

        def __eq__(self, value):
            return mycmp(self.obj, value.obj) == 0
        
        def __ge__(self, value):
            return mycmp(self.obj, value.obj) >= 0
        
        def __le__(self, value):
            return mycmp(self.obj, value.obj) <= 0




arr = ['1', '52', '90', '6', '62']
# arr = [(1, 2), (3, 4), (4, 1), (2, 3)]

# ar = sorted(arr, key=lambda x: x[0])
ar = sorted(arr, key=myCompare(comparator))
print(ar)