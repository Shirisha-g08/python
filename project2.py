import random
letters=[]
for i in range(ord('A'),ord('Z')+1):
    letters.append(chr(i))
for i in range(ord('a'),ord('z')+1):
    letters.append(chr(i))
print(letters)
numbers=[]
for i in range(10):
    numbers.append(i)
    numbers[i]=str(numbers[i])
print(numbers)
symbols=['!','@','#','$','%','^','&','*','(',')','_','-','+']
print("WELCOME TO THE PASSWORD GENERATOR")
password_list=[]
n_letters=int(input(("enter how many letters would you want in your password?")))
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_list+=char
n_numbers=int(input("enter how many numbers you want in your password?"))
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password_list+=char
n_symbols=int(input("enter how many symbols you want in your password?"))
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_list+=char
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for i in password_list:
    password+=i
print(password)