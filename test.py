class Akash:
    name = "akash"
    age = 20
    college = "DDU"
    def cal(self,x,y):
        self.x=x
        self.y= y
        c=x+y
        return c

detail = Akash()
print(detail.name,detail.cal(10,20))


