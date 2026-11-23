#__add__

class Test:
    def __init__(self,km,mtr):
        self.km=km
        self.mtr=mtr

    def __add__(self,sd):
        temp=Test(0,0)
        temp.km=self.km+sd.km
        temp.mtr=self.mtr+sd.mtr
        if temp.mtr >=1000:
            temp.km+=1
            temp.mtr-=1000
        return temp
        
    def __str__(self):
        return f"{self.km} km {self.mtr} meter"

obj1=Test(23,500)
obj2=Test(1,500)
obj3=obj1+obj2
print(obj3)
