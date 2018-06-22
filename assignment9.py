class Circle():
    def __init__(self,r):
        self.rad=r
    def getarea(self):
        g=3.14*self.rad*self.rad
        print(g)
    def getcircumfrance(self):
        h=2*3.14*self.rad
        print(h)
d=Circle(4)
d.getarea()
d.getcircumfrance()



class Student():
    def __init__(self, x,y):
        self.name=x
        self.rollno=y
    def display(self):
        print(self.name)
        print(self.rollno)
z=Student("isha",16)
z.display()





class Temperature():
    def __init__(self, t):
        self.temp=t
    def ctof(self):
        k=self.temp*2+30
        print(k)
    def ftoc(self):
        h=self.temp/2-15
        print(h)
s=Temperature(56)
s.ctof()
s.ftoc()



# q4


class Moviedetails():
    def __init__(self,a,b,c,d):
        self.moviename=a
        self.artistname=b
        self.yearofrelease=c
        self.ratings=d
    def display(self):
        print( self.moviename)
        print(self.artistname)
        print(self.yearofrelease)
        print(self.ratings)
f= Moviedetails('uig','fui',7989,8)
f.display()
g=Moviedetails('gui','gugu',7899,9)
g.display()




# q5



class Expenditure():
    def __init__(self,a,b):
        self.expenditure=a
        self.savings=b
    def display(self):
        print(self.expenditure)
        print(self.savings)
    def totalsalary(self):
        print( self.expenditure+ self.savings)
f=Expenditure(546,88)
f.display()
f.totalsalary()
