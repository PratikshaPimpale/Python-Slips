'''A) Write a python class to accept a string and number n from user and display n 
repetition of strings by overloading * operator. '''

class Demo:
    def accept(self):
        self.s=input("Enter string:")
        self.n=int(input("Enter number"))
    def __mul__(self,obj):
        print("String=",obj.s*obj.n)
ob=Demo()
ob1=Demo()
ob1.accept()
ob*ob1
