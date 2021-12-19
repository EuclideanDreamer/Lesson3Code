#this is an inline comment the processor will ignore me

"""This is
    a multiline comment
        this will also be ignored by the computer

        notice also that blank lines are 
"""

#printing hello 
print("hello 1")

#using a function to print hello
def hello():
    print("hello 2")
    return

#passing a print function the string we pass it
def printStr(str):
    print(str)
    return


#getting a string from the user
s = input("please say hello: ")


#using the two functions above
hello()
printStr(s)


#lets make a function to output 1-10 to the console
def oneToTen():
    i=1
    for i in range(1,11):
        print(i)
    return

#lets make a power fnction using a range based loop
def power(n, e):
    e = e -1
    v = n
    for i in range(e):
        n = n * v
    return n


#now we deploy our functions together
printStr(power(3,3))


#now we use the python library to do the same thing
print(pow(3,3))

oneToTen()
