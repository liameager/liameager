print('Hello World!')

# this is a comment

'''
this is a miltiline comment
so is this
'''

# Variables:

X = 10
print(X)

# Math functions:


# if statements:

x = -1
y = 1
if x < 0:
    x = 1
    x += 10
    print("x was negative")

'''
if x > 0 and y < 1

if x > 0 or y > 1
'''

# loops
nums = [10, 20, 30, 40, 50]
for i in range(5):
    print(i)

for i in range(2,5):
    print(i)

for i in range(len(nums)):
    print(nums[i])

for peak in nums:
    peak += 5
    print(peak)

for i, val in enumerate(nums):
    print('i is', i,'and val is', val)

dogs = ['maisy', 'harper', 'hank']

for name in range(len(dogs)):
    print(dogs[name])

for i in dogs:
    print('the dogs name is', i)

numb = [3, 6, 9, 12]
sum_nums = 0
for num in numb:
    sum_nums += num
print('the sum of nums is', sum_nums)
print(f'the sum of the nums is {sum_nums}')

# functions

def hello(name="Liam"):
    print("hello",name)

hello("bob")
hello()

# Strings

fname = 'Liam'
lname = "Eager"

print('he said "Hi" to his friend.')
print("she's a great dancer.")
print(fname, lname)

sentance = 'My first name is ' + fname + ' and my last name is ' + lname + '.'
print(sentance)

print('The first letter of my name is', fname[0])
print('The last letter of my name is ', fname[-1])

title = 'Rephactor Python'
print(len(title))

print(title * 3)

name_3 = fname * 3
print(name_3)

if fname == 'Liam':
    print("thats my guy")

if fname != 'Liam':
    print("wheres Liam? thats my guy")

uname = 'liam'
uppername = uname.upper()
print(uppername)

fullname = "Liam Eager"
first = fullname[0:4]
last = fullname[5:10]
print(first, last)
# dont have to use the start or last index, it auto assumes
platform_computing = "platform.computing"
platform = platform_computing[0:8]
computing = platform_computing[9:18]
print(platform, computing)

nums = [0, 3, 8, 5, 4]
print(nums)
temp = nums[2]
nums[2] = nums[4]
nums[4] = temp
print(nums)





