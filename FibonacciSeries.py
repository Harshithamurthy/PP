# Number = int(input("Enter the Number"))     # 0 1 1 2 3 5 8 13 21 34......
# i = 0
# firstvalue = 0
# secondvalue = 1
# while i < Number:
#     if i <= 1:
#         next = i
#     else:
#         next = firstvalue + secondvalue
#         firstvalue = secondvalue
#         secondvalue = next
#     print(next)
#     i = i + 1

#OR

def fibonacci(num):
    if num == 0:
        print("Enter valid number")
    elif num == 1:
        print(0)
    elif num == 2:
        print(1)
    else:
        return(fibonacci(num - 1) + fibonacci(num - 2))

i = 0
num = 10
while i < num:
    print(fibonacci(num))
    i = i + 1

