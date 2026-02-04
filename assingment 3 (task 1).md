def factorial(num):
    if num==0 or num ==1:
        return 1
    else:
        return num * factorial(num -1) # recursive call

user_num = int(input("Enter a number to get factorail"))
print(factorial(user_num))