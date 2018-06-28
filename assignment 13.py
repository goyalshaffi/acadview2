'''
# q1
a=3
if a<4:
    a=a/(a-3)
    print(a)
#ZeroDivisionError

# q2

l=[1,2,3]
print(l[3])

# IndexError: list index out of range


# q3


try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")

# ans=an exception


# q4


def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)



# q5

try:
    import isha
    a=[1,2,3]
    b=(3-a)/a[3]
except ImportError:
    print("libaray isha does nt exist")
except ValueError:
    print("when a is 3")
except IndexError:
    print("a[3] does nt exist")
finally:
    print("final stmt")


'''
# q6


class AgeError(Exception):
    pass
try:
    count=0
    while (count < 18):
        a=int(input("enter age"))
        if(a<18):
            raise AgeError
        count=count+1

except ValueError:
    print("value error")
except AgeError:
    print("age is too small")
else:
    print("no exception")



