Forced Fun
#1.5 part a
def hello_world():
    print("Hello, World!")
hello_world()
print("Hello!\n")
hello_world()

#1.5 part b

def hello_user(ssss):
    print("Hello, " + ssss + "!")
name = input("What is your name?")
hello_user(name)
print("Top of the morning to you!\n")

#1.5 part c

def repeat_string(string, times):
    print(string * times)
repeat_string(6, 12)
repeat_string(8, 14)
repeat_string(10, 16)

#1.5.1 part a
def double(num):
    return(num * 2)
userNum = int(input('Give me a number: '))
double(userNum)

#1.5.1 part b
def double(num):
    return(num * 2)
userNum = int(input('Give me a number: '))
double(userNum)
print('Double your number is ' + userNum)
userNum = double(userNum)
print('Double your number is ' + double(userNum))
print('Double your number is ' + userNum)

#1.5.2
first = int(input('Give me number'))
second = int(input('Give me a number again'))
if first > second:
        print('First digit is bigger than the Second')
elif first < second:
        print('First digit is smaller than the Second')
else:
        print('First digit equals to the Second')

#EXCERCISES
#1.5.0.1
blank_lines = ('\n'*5)
print(blank_lines)

#1.5.0.2
def print_square():
    number = input("give me an integer")
    print(number**2)
#1.5.0.3
def get_bill_total():
    bill = input("Please enter restaurant total\n")
    print("18 %%: %.2f" %round((float(bill)*.18),2))
    print("20 %%: %.2f" %round((float(bill)*.20),2))
    print("22 %%: %.2f" %round((float(bill)*.22),2))
get_bill_total()
#1.5.0.4
def nthPower():
    base = int(input("Give me a base number"))
    exp = int(input("Give me a exponent"))
    Result = pow(base, exp)
    print(Result)
nthPower()

#1.5.1.1
def greater(num1, num2): #() is a parameter, its an arguement when you call it
    if num1 > num2:
        return num1
    else:
        return num2
greater(26, 79)

#Part B
def lesser(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2
lesser(29, 95)
#1.5.1.2
num0 = int(input("Give me an number "))
num1 = int(input("Give me another number "))
num2 = int(input("Give me another number "))
num3 = int(input("Give me another numeber "))

big = greater(num0, num1)
bigger = greater(big, num2)
biggest = greater(bigger, num3)
print(f"The biggest number is {biggest}")

#Part B
num0 = int(input("Give me an number "))
num1 = int(input("Give me another number "))
num2 = int(input("Give me another number "))
num3 = int(input("Give me another numeber "))

small = lesser(num0, num1)
smaller = lesser(small, num2)
smallest = lesser(smaller, num3)
print(f"The least number is {smallest}")

#1.5.2
def isDivisible(num, divisor):
    if num%divisor == 0:
        print(f"{num} is divisible by {divisor}")
        return True
    else:
        print(f"{num} is not divisible by {divisor}")
        return False
isDivisible(8, 3)
#1.5.3
Import math
def hypotenuse(leg0, leg1):
    hyp = math.sqrt(leg0**2 + leg1**2)
    return hyp
hypotenuse(3, 4)
#1.5.4
#NAE article is Fresh water

def cleanwater():
    count = 0
    loop = True
    while loop:
        rain()
        river()
        ocean()
        cloud()
        count += 1
        if count == 1000:
            loop = False
        
def rain():
    print("Now it rains")
def river():
    print("The water falls into the river")
def ocean():
    print("The water flows to the ocean")
def cloud():
    print("The water evaporates into the cloud")
cleanwater()



#Forced Fun   
#1.6.0 A
emptyList = []
littleSquares = [1, 4, 9, 16]
composites = [1, 4, 6, 8, 9, 10, 12, 14, 15]

#Part b
emptyList = []
littleSquares = [1, 4, 9, 16]
composites = [1, 4, 6, 8, 9, 10, 12, 14, 15]
composites = composites + [18]
composites += [20]

#Part C
emptyList = []
littleSquares = [1, 4, 9, 16]
composites = [1, 4, 6, 8, 10, 12, 14, 15]
composites = composites + [18]
composites += [20]

#Part D
friends = ["Arnav", "Jeff", "Ethan"]
friends.remove("Ethan")
        #sorry Ethan
#friends.append("Sathkrith")
friends.insert(1, "Theo")

#Part E
friends = ["Arnav", "Jeff", "Ethan"]
friends.remove("Ethan")
        #sorry Ethan
friends.append("Sathkrith")
friends.insert(1, "Theo")
#its in second, because python likes 0 more
friends2 = ["Pratul", "Yahir", "Tim"]
friends.append(friends2)

#Part F
friends = ["Arnav", "Jeff", "Ethan"]
friends.remove("Ethan")
        #sorry Ethan
friends.append("Sathkrith")
friends.insert(1, "Theo")
#its in second, because python likes 0 more
friends.append("Pratul")
friends.append("Yahir")
friends.append("Tim")

3Part g
friends = ["Arnav", "Jeff", "Ethan"]
friends.remove("Ethan")
        #sorry Ethan
friends.append("Sathkrith")
friends.insert(1, "Theo")
#its in second, because python likes 0 more
friends2 = ["Pratul", "Yahir", "Tim"]
friends.append(friends2)
exFriend = friends.pop()
print(exFriend)

#Part H
friends = ["Arnav", "Jeff", "Ethan"]
friends.remove("Ethan")
        #sorry Ethan
friends.append("Sathkrith")
friends.insert(1, "Theo")
#its in second, because python likes 0 more
friends2 = ["Pratul", "Yahir", "Tim"]
friends.append(friends2)
exFriend = friends.pop(1)
print(exFriend)
#basically, Theo is now removed, because he was the seconds (which in python is 1)

#First, we have list in [], then .remove removes the name from the list
#then append adds another variable into the list.
#Insert works by adding a variable into the list, at a specific place
#friends2 inserts more list into the pre existing friends list
#pop removes the friends from the first list, leaving only friends2
#pop 1 removes the 2 second name in the friends+friends2 list
           
#EXERCISES
#1.6.1
numberList = []
for i in range(4):
    number = input("give me a integers")
    numberList.append(int(number))
numberList.append(numberList.pop(0))
print(numberList)
#1.6.2
numberList = []
for i in range(6):
    number = input("give me a integers")
    numberList.append(int(number))
print(numberList)

#Part b
print(numberList[4])

#Part c
print(numberList[-3: -1])

#Part d
print(numberList[-3:])

#part e
numberList.reverse()

#Part f
sum(numberList)

#Part g
if 0 in numberList:
    index = numberList.index(0)
    print(index)
else:
    print("There is no 0 in your list")

#Part H
numberList.pop()
print(numberList)

#Part I
numberList.insert(-1, int(4301))
print(numberList)

#Part j
numberList.append(-228)
print(numberList)

#1.6.3
sportsList = ["Football", "Soccer"]
randomList = input("What sport do you like?")
sportsList.append(randomList)
print(sportsList)

#1.6.4
tvList = ["Top Gear", "The Grand Tour", "The Mandalorian", "Kitchen Nightmare"]
tvList.insert(int(input("Where do you want to put it")),input("What Tv show do you like"))

print(*tvList,sep='\n')

#1.6.5
unList = ["0. No poverty", "1. No hunger", "2. Good health and well being", "3. quality education", 
          "4. Gender equality", "5. Clean water and sanitation", "6. Clean energy", "7. Decent work and economic growth", "8. industry, renovation, and infrastructure", "9. Reduced inequalites", "10. sustainable cities", "11. Responsible consuption and production", "12. Climate action", "13. Life below water", "14. Life on land", "15. peace, justice and strong insitiutions", "16. partnerships for the goals"]
var0 = "0"
var1 = "1"
var2 = "2"
var3 = "3"
var4 = "4"
var5 = "5"
var6 = "6"
var7 = "7"
var8 = "8"
var9 = "9"
var10 = "10"
var11 = "11"
var12 = "12"
var13 = "13"
var14 = "14"
var15 = "15"
var16 = "16"
print(unList)

loop = True
while loop:
    userInput = input("Which topic do you wanna learn about(0-16 to select, else to quit)? ")
    
    if userInput == var0:
        print("More than 700 million people, or 10 per cent of the world population, still live in extreme poverty today, struggling to fulfil the most basic needs like health, education, and access to water and sanitation, to name a few. The majority of people living on less than $1.90 a day live in sub-Saharan Africa. Worldwide, the poverty rate in rural areas is 17.2 per cent—more than three times higher than in urban areas")
    elif userInput == var1:
        print("After decades of steady decline, the number of people who suffer from hunger – as measured by the prevalence of undernourishment – began to slowly increase again in 2015. Current estimates show that nearly 690 million people are hungry, or 8.9 percent of the world population – up by 10 million people in one year and by nearly 60 million in five years.")
    elif userInput == var2:
        print("Before the pandemic, major progress was made in improving the health of millions of people. Significant strides were made in increasing life expectancy and reducing some of the common killers associated with child and maternal mortality. But more efforts are needed to fully eradicate a wide range of diseases and address many different persistent and emerging health issues. By focusing on providing more efficient funding of health systems, improved sanitation and hygiene, and increased access to physicians, significant progress can be made in helping to save the lives of millions.")
    elif userInput == var3:
        print("Education enables upward socioeconomic mobility and is a key to escaping poverty. Over the past decade, major progress was made towards increasing access to education and school enrollment rates at all levels, particularly for girls. Nevertheless, about 260 million children were still out of school in 2018 — nearly one fifth of the global population in that age group. And more than half of all children and adolescents worldwide are not meeting minimum proficiency standards in reading and mathematics. ")
    elif userInput == var4:
        print("Gender equality is not only a fundamental human right, but a necessary foundation for a peaceful, prosperous and sustainable world. There has been progress over the last decades: More girls are going to school, fewer girls are forced into early marriage, more women are serving in parliament and positions of leadership, and laws are being reformed to advance gender equality")    
    elif userInput == var5:
        print("While substantial progress has been made in increasing access to clean drinking water and sanitation, billions of people—mostly in rural areas—still lack these basic services. Worldwide, one in three people do not have access to safe drinking water, two out of five people do not have a basic hand-washing facility with soap and water, and more than 673 million people still practice open defecation.")  
    elif userInput == var6:
        print("The world is making progress towards Goal 7, with encouraging signs that energy is becoming more sustainable and widely available. Access to electricity in poorer countries has begun to accelerate, energy efficiency continues to improve, and renewable energy is making impressive gains in the electricity sector. ")  
    elif userInput == var7:
        print("Sustained and inclusive economic growth can drive progress, create decent jobs for all and improve living standards. ")  
    elif userInput == var8:
        print("Inclusive and sustainable industrialization, together with innovation and infrastructure, can unleash dynamic and competitive economic forces that generate employment and income. They play a key role in introducing and promoting new technologies, facilitating international trade and enabling the efficient use of resources. ")  
    elif userInput == var9:
        print("Reducing inequalities and ensuring no one is left behind are integral to achieving the Sustainable Development Goals. Inequality within and among countries is a persistent cause for concern. Despite some positive signs toward reducing inequality in some dimensions, such as reducing relative income inequality in some countries and preferential trade status benefiting lower-income countries, inequality still persists.")  
    elif userInput == var10:
        print("The world is becoming increasingly urbanized. Since 2007, more than half the world’s population has been living in cities, and that share is projected to rise to 60 per cent by 2030. Cities and metropolitan areas are powerhouses of economic growth—contributing about 60 per cent of global GDP. However, they also account for about 70 per cent of global carbon emissions and over 60 per cent of resource use. Rapid urbanization is resulting in a growing number of slum dwellers, inadequate and overburdened infrastructure and services (such as waste collection and water and sanitation systems, roads and transport), worsening air pollution and unplanned urban sprawl. ")  
    elif userInput == var11:
        print("Worldwide consumption and production — a driving force of the global economy — rest on the use of the natural environment and resources in a way that continues to have destructive impacts on the planet. Economic and social progress over the last century has been accompanied by environmental degradation that is endangering the very systems on which our future development — indeed, our very survival — depends. ")  
    elif userInput == var12:
        print("Carbon dioxide (CO2) levels and other greenhouse gases in the atmosphere rose to new records in 2019, and 2019 was the second warmest year on record. The Paris Agreement, adopted in 2015, aims to strengthen the global response to the threat of climate change by keeping a global temperature rise this century well below 2 degrees Celsius above pre-industrial levels. The agreement also aims to strengthen the ability of countries to deal with the impacts of climate change, through appropriate financial flows, a new technology framework and an enhanced capacity building framework.")  
    elif userInput == var13:
        print("The ocean drives global systems that make the Earth habitable for humankind. Our rainwater, drinking water, weather, climate, coastlines, much of our food, and even the oxygen in the air we breathe, are all ultimately provided and regulated by the sea. Careful management of this essential global resource is a key feature of a sustainable future. However, at the current time, there is a continuous deterioration of coastal waters owing to pollution, and ocean acidification is having an adversarial effect on the functioning of ecosystems and biodiversity. This is also negatively impacting small scale fisheries. ")  
    elif userInput == var14:
        print("Nature is critical to our survival: nature provides us with our oxygen, regulates our weather patterns, pollinates our crops, produces our food, feed and fibre. But it is under increasing stress. Human activity has altered almost 75 per cent of the earth’s surface, squeezing wildlife and nature into an ever-smaller corner of the planet.")  
    elif userInput == var15:
        print("Conflict, insecurity, weak institutions and limited access to justice remain a great threat to sustainable development. The number of people fleeing war, persecution and conflict exceeded 70 million in 2018, the highest level recorded by the UN refugee agency (UNHCR) in almost 70 years. ")  
    elif userInput == var16:
        print("The SDGs can only be realized with strong global partnerships and cooperation. A successful development agenda requires inclusive partnerships — at the global, regional, national and local levels — built upon principles and values, and upon a shared vision and shared goals placing people and the planet at the centre. Many countries require Official Development Assistance to encourage growth and trade. Yet, aid levels are falling and donor countries have not lived up to their pledge to ramp up development finance.")  
    else:
        print("Good Bye!")
        loop = False

#1.6.6
loop = True
print('Hello, what is your name?')
name = input()
while loop:
    print(name, 'Would you like to take this quiz? Please type yes or no')
    choice = input()
    
    if choice == 'no':
        loop = False
        print("bye")
    elif choice == 'yes' :
        print('Great, Here are the questions!')
        score = 0
        answer = input("When was the 'Paris Agreement' signed? ")
        if answer == "2015": 
            print("Correct!")
            score += 1
        else:
            print(f"The answer is '2015', not {answer}")
            score += 0
        answer1 = input("Worldwide, one in three people do not have access to safe drinking water, ___ out of five people do not have a basic hand-washing facility with soap and water")
        if answer1 == "two":
            print("Correct!")
            score += 1
        else:
            print(f"The answer is two, not {answer1}")
            score += 0
        
        answer2 = input("2019 was so hot, it was recorded as the _____ hottest year on record")
        if answer2 == "second":
            print("Correct!")
            score += 1
        else:
            print(f"The answer is 'second', not {answer2}")
            score += 0
    
        answer3 = input("How many people were estimated in 2015 to be hungry?")
        if answer3 == "690 million":
            print("Correct!")
            score += 1
        else:
            print(f"The answer is '690 million', not {answer3}")
            score += 0
    
        answer4 = input("How much proverty per cent decreased from 1990 to 2015?")
        if answer4 == "26 cents":
            print("Correct!")
            score += 1
        else:
            print(f"The answer is '26 cents', not {answer4}")
            score += 0
        print(str(score)+ " " + "out of 5")
        loop = False

#1.7 parts a
for i in range(5):
    print(i)
for num in range(10):
    print(num, 'tripledis', 3*num)
for biden in range(50):
    print(biden, 'squared is', biden**2)

#1.7 part b

for i in range(2,5):
    print(i)
for num in range(5, 10):
    print(3*num)
for biden in range(12, 50):
    print(biden**2)
#part c

for i in range(19, 441):
    print(i)

#part d

for i in range(16, 998, 2):
    print(i)
for num in range(1, 100, 2):
    print(num)
for biden in range(4, 1250, 4):
    print(biden)
for through in range(1250, 1310):
    print(through)

#part e
for i in range(167, -190, -2):
    print(i)
for i in range(30, 0, -1):
    print(i)
print('Blast off!')

#1.7.1 part a
murder = [1, 2, 3, 4, 5, 6, 7, 8,]
count = 0
for crow in murder:
    count += 1
print(count)

#Part b
for i in ["Duenas", "Schafer", "Fort", "Schaeffer"]:
    print("Good morning, Ms. " + i)

#Part c
phrase = "love is the seventh wave"
count = 0
for letter in phrase:
    count +=1
print(count)

#Part D
friendsList = ["Jeff", "Ethan"]
inList = False
for BFF in friendsList:
    if(BFF == "Alex"):
        inList = True
        print("Alex is in the list too")

#1.7.2

#def repeatString(str, num):
    
num = ["I have 6", "I have no"]
str = ["bowls of rice"]

for i in range(5):
    
    for x in num:
        for y in str:
            print(x,y)
#1.7.3 part a
count = 0
for num in range(1,101):
    if ((num**0.5) == int(num**0.5)):
        count += 1
print(count)

#1.7.3 part b
word = "mississipi"
count = 0
for letter_s in word:
    if letter_s == "s":
        count += 1

print(word)

#1.7.4 part a
sum = 0 
for num in range(1, 1012):
    if (num % 7 == 0):
        sum += 1
print(sum)
#part b
sum = 0 
for num in range(1, 11112):
    if (num % 11 == 0):
        sum += 1
print(sum)
#part c
sum = 0 
for num in range(1313, 131314):
    if (num % 13 == 0):
        sum += 1
print(sum)

#1.7.5 part a
import math
product = 1
for num in range(1, 11):
    product *= num
print(product)

#part b
import math
product = 1
for num in range(1, 21):
    product *= num
print(product)

#part c
import math
product = 1
userInput = int(input("Give a number "))
for num in range(1, userInput):
    product *= num
print(product)

#1.7.6 part a
countdown = 20
while (countdown > 1):
    countdown = countdown - 1
    print(countdown)
print("Blast Off!")
#part b
name = ""
num = 0
while not (name.isalpha()):
    name = input("Enter your name(Letter only): ")
while not ((num >= 0) and (num <= 1001)):
    num = int(input("Enter a number from 1 to 1000."))
print(str(num) + " is lucky for a kid named " + name)

#1.7.0.1
userInput = input("Enter a word")
print(f"{userInput} \n" *30)

#1.7.0.2
for num in range(3, 104, 4):
    print(num)

# 1.7.0.3
for num in range(30, 0, -1):
    print(num)
    
# 1.7.0.4
letter1 = "A"
letter2 = "B"
for i in letter1:
    for j in letter2:
        print(i *30 + j *40)

# 1.7.1.1
from functools import partial
from random import randint


def randints(count, *randint_args):
    num = partial(randint, *randint_args)
    return [num() for _ in range(count)]


print(randints(10, 1, 100))

#1.7.1.3
from functools import partial
from random import randint


def Original(count, *randint_args):
    num = partial(randint, *randint_args)
    return [num() for _ in range(count)]

numberList = Original(50, 1, 10000)
print(numberList)


count = 0    
for num in numberList:
    if num % 2 == 0:
        count += 1
print(f"You have {count} even numbers")
(min(numberList))

#1.7.2.1
def divisible(start, end):
    for i in range(start, end):
        if i % 3 == 0 and i % 7 == 0: #much more strict
            continue
        #i is the list, meaning that it always changes
        if i % 3 == 0 or i % 7 == 0: #much more lose
            print(i)
        
divisible(1, 101)        

# 1.7.2.2
for i in range(1, 201):
    if i % 10 == 8:
        continue
    print(i)

# 1.7.3.1
def is_upper(input):
    for i in input:
        if i >= "a" and i <= "z":
            return False
    return True
is_upper("AP CSP")

#Part B
userinput = input("Give me a word in Upper case: ")
loop = True
while loop:
    if is_upper(userinput):
        print("Thank you")
        loop = False
    else:
        print("Try again ")
        userinput = input("Enter a word again: ")

# 1.7.3.3
count = 0
nameinput = input("What is your name: ")
vowel = {"a", "A", "e", "E", "I", "i", "O", "o", "U", "u"}
for i in nameinput:
    if i in vowel:
        count += 1
print(f"You have {count} vowels")

# 1.7.3.5
userInput = input("Enter a name: ")
for y in userInput:
    print(y)

#part B
userinput = input("Enter a name: ")
n = int(input("Enter a number: "))
for x in range(n):
    for y in userinput:
        print(y)

1.7.4.1

questions = [
"If angle a is 65 degrees, and angle b is 46. What does angle c equal?\n(a) 560\n(b) 69\n(c) 180\n(d) 68.8.96346\n",
"\nSolve 6=2(y+2)\n",
"\nThe triangle on the right has 5 cm in base, and 3cm in height. The other triangle has 15cm in base, and x in height. Find the length of x(answer with units)\n"
]
answers= [
"b", "1", "9cm"
 ]


score = 0
for i in range(3):
    question = questions[i]
    
    answer = answers[i]
    useranswer = input(question)
    if useranswer == answer:
        print("Correct")
        score += 1
    else:
        print("incorrect")
print(f"Your total score is: {score} out of 3")         

#1.7.4.2
import random
teamNames = ["A", "B", "C", "D", "E", "F", "G", "H"]
def teams(names):
    teams1 = []
    teams2 = []
    for name in names:
        dice = random.randint(0, 1)
        if dice == 0:
            teams1.append(name)
        else:
            teams2.append(name)
    print(f"Team1 contains {teams1}")
    print(f"Team2 contains {teams2}")
teams(teamNames)

#1.7.4.4
import random
score = 0.0
for i in range(12):
    a = random.randint(20, 100)
    b = random.randint(20, 100)
    c = random.randint(20, 100)
    total = a + b + c
    guess = int(input("Guess the number "))
    if guess == total:
        print("Right")
        score += 1
    elif abs(guess - total) < 3:
        print("Close")
        score += 0.5
    else:
        print("Incorrect")
print(f"Youre final score is {score} out of 12")

#1.7.5.1
def add_up_range(start, end, step):
    total = start
    loop = True
    while loop:
        start += step
        if start >= end:
            loop = False
        else:
            total += start
    print(f"The sum is {total}")        





add_up_range(3, 14, 2)
#the number is starting number, ending, and a step

#1.7.5.2
import math
def isprime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def find_prime(num):
    start = 2
    count = 0
    while True:
        if isprime(start):
            count += 1
        if count == num:
            return start
        start += 1
print("The 100th prime number is " + str(find_prime(100)))
print("The 255th prime number is " + str(find_prime(255)))
print("The 10001th prime number is " + str(find_prime(10001)))

#1.7.5.3
import math
def isprime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def find_primes(maxNum):
    total = 0
    start = 2
    while True:
        if start >= maxNum:
            return total
        if isprime(start):
            total += start 
        start += 1
print("The sum of all prime number less than 1000 is " + str(find_primes(1000)))
print("The sum of all prime number less than 18888 is " + str(find_primes(18888)))
print("The sum of all prime number less then 5,000,000 " + str(find_primes(5000000)))

#1.7.5.4
def solveX(C3, C2, C1, C0):
    bestX = 0
    minval = C0
    for i in range(1, 100000000):
        val = C3 * i **3 + C2 * i **2 + C1 * i + C0
        if abs(val) < abs(minval):
            minval = val
            bestX = i
    return bestX

print("The solution for 21x^2-x^3+21904=0 is " + str(solveX(-1, 21, 0 ,21904)))
print("The solution for x^3-6x^2+11x-6=0 is " + str(solveX(1, -6, 11, -6)))
print("The solution for 403x^3-131x^2-11204x-902264858=0 is " + str(solveX(403, -131, -11204, -902264858)))

#1.7.8
hundreds = ["", "ciento", "dosciento", "tresciento", "cuatrociento", "quinientos", "seiscientos", "setescientos", "ochocientos", "novecientos"]
tens = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setena", "ochenta", "noventa"]
ones = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve"]
userInput = int(input("enter a number "))
original = userInput
if userInput >= 11 and userInput <= 19:
    print(f"{original} in Spanish is " + ones[userInput])
else:
    words = []
    num = userInput % 10
    if ones[num]:
        words.append(ones[num])
    userInput = int(userInput/10)
    num = userInput % 10
    if tens[num]:    
        words.insert(0, tens[num])
    userInput = int(userInput / 10)
    num = userInput
    if hundreds[num]:
        words.insert(0, hundreds[num])
    print(f"{original} in Spanish is " + " y ".join(words))
    

    
    

