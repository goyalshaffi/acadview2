# q1

class Animal():
    def animal_attribute(self):

        return("this is a class of animal")
class Tiger(Animal):
    def tiger(self):
        return("tigers are also animals")
Cheetah=Tiger()
print(Cheetah.animal_attribute())
print(Cheetah.tiger())



# q2
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
print(a.g(),b.g())



# q3


class Cop():
    def __init__(self,a,b,c,d,e):
        self.name=a
        self.age = b
        self.work = c
        self.experience = d
        self.desigination = e
    def display(self):
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.experience)
        print(self.desigination)
    def add(self):
        pass
    def update(self):
        self.name = 'daman'
        self.age = 34
        self.work = 'teacher'
        self.experience = '1 yr'
        self.desigination = 'teaching'
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.experience)
        print(self.desigination)
class Mission(Cop):
    def add_mission_details(self):
        print("the details")
s=Mission('tina',19,'student','no','doctor')
s.add()
s.display()
s.update()



# q4

class Shape():
    def __init__(self,l,b):
        l=self.length
        b=self.breath
    def area(self):
        a=self.length*self.breath
        print(a)
    def sarea(self):
        c=self.length*4
        print(c)
d=Shape(2,2)
d.area()
d.sarea()

