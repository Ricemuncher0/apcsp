
1.5 part a
def hello_world():
    print("Hello, World!")
hello_world()
print("Hello!\n")
hello_world()

1.5 part b

def hello_user(ssss):
    print("Hello, " + ssss + "!")
name = input("What is your name?")
hello_user(name)
print("Top of the morning to you!\n")

1.5 part c

def repeat_string(string, times):
    print(string * times)
repeat_string(6, 12)
repeat_string(8, 14)
repeat_string(10, 16)

1.5.1 part a
def double(num):
    return(num * 2)
userNum = int(input('Give me a number: '))
double(userNum)

1.5.1 part b
def double(num):
    return(num * 2)
userNum = int(input('Give me a number: '))
double(userNum)
print('Double your number is ' + userNum)
userNum = double(userNum)
print('Double your number is ' + double(userNum))
print('Double your number is ' + userNum)

1.5.2
first = int(input('Give me number'))
second = int(input('Give me a number again'))
if first > second:
        print('First digit is bigger than the Second')
elif first < second:
        print('First digit is smaller than the Second')
else:
        print('First digit equals to the Second')
    
