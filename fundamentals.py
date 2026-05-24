print("Start small. Ship something.")
name = "sm"
age = 32
print("hello, i am {}, and i am {}".format(name, age))
print("hello, i am", name )

#if conditions 
score = 80 

if score >= 90:
    print("Grade :A")
elif score <= 80:
    print("Grade: B ")
else:
    print("Grade: C")
    
x = 10 
y = 5

#logical operators 
if x > 5 and y < 2:
    x +=2
elif x ==10 or y == 5:
    x += 5
else:
    x+=10
    
print(x )

#loops 
for i in range(1,4):
    print("loop number: ", i)

print("\n")

count = 1
while count <= 3:
    print("Count is: ", count )
    count+=1
    
#loop controls
for num in range (1,6):
    if num == 3:
        break
    print (num)
    
print("\n")

for num in range (1, 6 ):
    if num == 3:
        continue
    print(num)

print("\n")

for i in range ( 1, 6):
    if i == 4:
        break
    print ( i, end=" ")
    
#functions
def new():
    print("\n")

new()
print("hellow world")

#argument and parameters
def greetings (name) :
    print("hello, {}".format(name))

greetings("Ramil")

new()
#return 
def addNumber (x, y):
    return x + y
    
total = addNumber(5, 10)
print("result is",total)

new()
def calculate(val1, val2):
    if val1 > val2:
        return val1 - val2
    else:
        return val1 + val2
    print("calculation is done")

ans = calculate(2, 5)
print ( "calculated",  ans )

new()
#object & memory management
print(type(ans))
x = " hello"
print(type(x))

new()
#variable scobe: loca vs global
#Local Variables: Variables created inside a function. They only exist while that function is running. Once the function finishes, they are completely wiped from memory.
#Global Variables: Variables created outside of all functions (at the root level of your file). Any function inside that file can read them.

num = 10

def changeNum ():
    num = 20 
    return num
changeNum()
print(num)

new()
#Recursion 
def factorial(n):
    #base case
    if n == 1:
        return 1
    else: 
        return n * factorial( n -1)
        
print(factorial(3))

new()
#lists 
fruits = ["Apple", "Banana" ,"Cherry"]
print(fruits[0])
print(fruits[-1])

new()
#lists are mutable
numbers = [3, 1, 4, ]
numbers.append(2)
numbers.sort()
print(numbers)

new()
#2d lists
grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(grid[1][2])

new()
#ex
metrics = [
    [10, 20],
    [30, 40]
    ]

total = metrics[0][1] + metrics[1][0]
print(total)


