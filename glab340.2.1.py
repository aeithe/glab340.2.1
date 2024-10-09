a = 32 
b = 6

print('addition of two numbers: ' , a+b)
print('subtration of two numbers: ', a-b)
print('multiplication of two numbers: ', a*b)
print('division of two numbers: ', a/b)
print('remained of two numbers: ', a%b)
print('floor division of two numbers:', a//b)

MultipleOperators = 1 + 2 * 3 / 4.0

print('result of multipleoperators: ', MultipleOperators)

j = 10
print("j is : ", j)
j = 5 
k = j
print("j is : ", j)
print("k is : ", k)

k = j = 10; 

print("j is : ", j)
print("k is : ", k)

print('two numbers are equal or not: ', a == b)
print('two numbers are not equal or not: ', a!=b)
print('a is less than or equal to b: ', a <= b)
print('a is greater than or equal to b: ', a >= b)
print('a is less than b: ', a < b)
print('a is greater than b:', a > b)


a = 5 
print('is this statement true?: ', a > 3 and a < 5)
print('any one statement is true?: ', a > 3 or a < 5)
print('each statement is true then return false and vice-versa: ', (not(a > 3 and a < 5)))


a = ['Rose', 'Lotus']
b = ['Rose', 'Lotus']

c = a

print(a is c)
print(a is not c)
print(a is b)
print(a is not b)
print(a == b)
print(a != b)


x = ['Rose', 'Lotus']
print(' is this value present?: ', 'Rose' in x)
print(' is this value present?: ', 'Riya' not in x)

x = 'Hello world'
y = {1:'a', 2:'b'}

print('H' in x)
print('hello' not in x)
print(1 in y)
print('a' in y)
