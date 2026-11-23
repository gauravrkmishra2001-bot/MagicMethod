#__mul__

class Test:
    def __init__(self,num):
        self.num=num

    def __mul__(self,sn):
        temp=Test(0)
        temp.num=self.num*sn.num
        return temp
        
    def __str__(self):
        return f"{self.num}"

obj1=Test(2)
obj2=Test(5)
obj3=obj1*obj2
print(obj3)
