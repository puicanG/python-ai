
var1 = 10
var1 = var1 + 30

var2 = 60
var3 = var2 + var1


print(var3)

# fundamentals data structures.

arr =[30,40,50,100,99,-1,"Harry Potter"]
print(arr[0])

var4 = {
    "name": "George",
    "age": 20,
}

print(arr)

def add(a,b):
    result = a + b
    return result

def multiply(a:int,b: int) -> int:
    return a * b

var5 = multiply(2,10)
print(var5)

# Tipuri de date:
# 0,1,-1,100 ----> int
# 0.5, 1.5, 3.1422323 ---> float/double
# True , False --> boolean
# "hell world" -> str
# [] --> list
# {} --> dict

# dynamically typed. --> python
# statically typed --> Uipath

offer_letter = True

if offer_letter == True:
    print("Yes all good!")
else:
    print("No")

age = 30
if age >= 25:
    print("Millenial")


# range --> iterator
for i in range(10):
    print(i)

for x in [10,20,33]:
    print(x)

# i = 0
# while i < 30:
#     print(i)
#     i = i + 1




