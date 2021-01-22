# feeling = input('How are you?')
# if feeling.lower() == 'great':
#     print('I feel great too.')
# else:
#     print('I hope the rest of your day is good.')
#
#
# # Check String is num
# test = "08293829"
# print(test.isalnum())

# while True:
#     print('Enter your age:')
#     age = input()
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age.')
# while True:
#     print('Select a new password (letters and numbers only):')
#     password = input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers.')


# ljust and rjust
#
# hello = 'Hello'.center(15, '-')
# print(hello)

# Remove White Space

spam = '    Hello World     '
print(spam.strip())
spam = '    Hello World     '
print(spam.lstrip())
spam = '    Hello World     '
print(spam.rstrip())

# Or even Remove some character
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

# Replace String
string = "geeks for geeks geeks geeks geeks"
print(string.replace("geeks", "Geeks"))
