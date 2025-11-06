name = str(input('Enter your name:'))
while True:
    try:
        age = int(input('Enter your age:'))
        break   
    except ValueError:
        print("Enter a valid age!")

hobbies = (input('Enter 3 hobbies:').split(','))

user_dict = {'name': name,
             'age':age,
             'hobbies':hobbies}
print(user_dict)

