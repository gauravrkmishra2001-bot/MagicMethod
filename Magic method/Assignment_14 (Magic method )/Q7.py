# __mod__

class Test:
    def __init__(self,num):
        self.num=num

    def __mod__(self,sn):
        temp=Test(0)
        if sn.num!=0:
            temp.num=self.num%sn.num
            return temp
        else:
            return "Invalid opreands"
        
    def __str__(self):
        return f"{self.num}"

obj1=Test(10)
obj2=Test(2)
obj3=obj1%obj2
print(obj3)
