'''B) Create a class circles having members radius. Use operator overloading to add the 
radius of two circle objects. Also display the area of circle.  '''

class Circle:
    def __init__(self):
        self.r=float(input("Enter radius:"))
    def __add__(self,obj):
        print("Addition of radius of two circles=",self.r+obj.r)
    def area(self):
        a=3.14*self.r*self.r
        print("Area of circle=",a)
ob=Circle()
ob1=Circle()
ob+ob1
ob1.area()
    
