#functional scope or local scope

def fullName():
        global fName
        fName = "Tendu"
        lName = "Thulasi"
fullName()
print(fName)
print(lName)

#global variable

def fullName():
        global fName
        lName = "Tendu"
        fName = "Thulasi"
fullName()
print(fName)
print(lName)

#block scope

class fibseries:
        def fibex(self):
                n=10
                a=1
                b=0
                i=1
                lst=[]
        while i<=n:
                c=10
                lst.append(b)
                a=a+b
                b=a-b
                i+=1
        print(lst)
        fib=fibseries()
        fib.fibex()