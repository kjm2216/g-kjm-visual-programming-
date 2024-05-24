class human:
    def __init__(self,n):
        self.name = n
        print('id=',id(self))
        
a = human('jeong-min Kim')

class human:
    def __init__(self,n):
        self.name = n
    def print_name(self):
        print(self.name)
        return self.name
    
a = human('jeongmin')
print(a.name)
a.print_name()

current_name = a.print_name()
print(current_name)

new_name=human.print_name(a)
print(new_name)

b=human('xxxx')
c=human('xxxx')
print(b==c)

a=int(7)
b=int(7)
print(a==b)

print(a is b)

b=int(798472323)
a=int(798472323)
print(a is b)
print(a==b)

class Student(human):
    def __init__(self):
        super().__init__('not defined')
        
b=Student()
b.print_name()

class Teacher(human):
    def __init__(self,n):
        super().__init__(n)
    def print_name(self):
        print("teacher:",self.name)
        
a=human('jeongmin')
b=Teacher('jeongmin')

a.print_name()
b.print_name()

        