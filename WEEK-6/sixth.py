string = input("Enter any String :")

uppercase = 0
lowercase = 0 
alphabets = 0
digit = 0

for i in string:

    if i.isupper():
        uppercase += 1

    if i.islower():
        lowercase += 1

    if i.isalpha():
        alphabets += 1

    if i.isdigit():
        digit += 1

print(f"Number of Uppercase Characters : {uppercase}")
print(f"Number of Lowercase Characters : {lowercase}")
print(f"Number of Alphabets : {alphabets}")
print(f"Number of Digits : {digit}")