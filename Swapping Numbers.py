x = input("Enter value of x")
y = input("Enter value of y" )

x , y = y , x

print("Value of x is", x)
print("Value of y is", y)

#OR

x = input("Enter value of x")
y = input("Enter value of y" )

temp = x
x = y
y = temp

print("Value of x is", x)
print("Value of y is", y)

#OR

x = input("Enter value of x")
y = input("Enter value of y" )

x = x + y
y = x - y
x = x - y

print("Value of x is", x)
print("Value of y is", y)


