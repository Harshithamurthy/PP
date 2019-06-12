def swapThree(a, b, c):
    # Store sum of all in a
    a = a + b + c  # (a = 60)

    # After this, b has value of a
    b = a - (b + c)  # (b = 60 – (20+30) =10)

    # After this, c has value of b
    c = a - (b + c)  # (c = 60 – (10 + 30) = 20)

    # After this, a has value of c
    a = a - (b + c)  # (a = 60 – (10 + 20) = 30)

    print("After swapping a =", a, ", b =", b, ", c =", c)


# Driver code
if __name__ == '__main__':
    a = 20
    b = 40
    c = 70

    print("Before swapping a =", a, ", b =", b, ", c =", c)

    swapThree(a, b, c)

#OR

a = input("Enter the value of a")
b = input("Enter the value of b")
c = input("Enter the value of c")


temp = a
a = b
b = c
c = temp

print("The value of a is ", a)
print("The value of b is ", b)
print("The value of c is ", c)