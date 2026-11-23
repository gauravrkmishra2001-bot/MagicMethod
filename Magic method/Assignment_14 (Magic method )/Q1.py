# __init__

class Test:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def __str__(self):
        return str(self.id)+" "+self.name

obj=Test(1089,"Kartik")
print(obj)