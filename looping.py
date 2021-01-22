import sys

#
# ============== FOR LOOP =================
#
# Example #1
for letter in 'Python':
    print('Current Letter : ', letter)

# Example #2
fruits = ['Apple', 'Mango', 'Orange']
for fruit in fruits:
    print(fruit)

# Example #3 - Using Indexes
fruits = ['Apple', 'Mango', 'Orange']
for index in range(len(fruits)):
    print('Fruit is : ', fruits[index])

#
# ============== WHILE LOOP =================
#

# Example #1
count = 0
while count < 5:
    print('The count is:', count)
    count = count + 1

#
# =========== Tree Triangle Exaple ==========
#

for i in range(0, 5):
    for j in range(0, 5 - i):
        print('*', end='')
    print()

# ============== Loop Control ============
#
#
# var1 = ""
# while (var1 != "exit"):
#     try:
#         var1 = input("Please enter an integer (type exit to exit): ")
#         print(int(var1))
#     except:
#         print("Unexpected error:", sys.exc_info()[0])
#         pass

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break

# Another Example

# List Comprehension #!
numbers = [1, 2, 3, 4]
squares = []
for n in numbers:
    squares.append(n ** 2)
print(squares)

# List Comp #2
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]
print("List Comp #2 : ", squares)

# List Comp #3 - Find Two Match ONLY In Two Different List
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = []
for a in list_a:
    for b in list_b:
        if a == b:
            common_num.append(a)

print(common_num)   # Output [2, 3, 4]

# Syntax above canbe simplify by
# Contoh4 Implementasi dengan list comprehension
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]
print("It Works :", common_num)  # Output: [2, 3, 4]


# Example of list comprehension
list_upper = ['Hello', 'WORLD', 'Some', 'USER']
list_lower = [kata.lower() for kata in list_upper]
print(list_lower)


# Another Example
list_a = range(1, 10, 2)
x = [[a ** 2, a ** 3] for a in list_a]
print(x)

list_a = range(1, 10, 2)
x = [[a ** 2, a ** 3] for a in list_a]
print(x)