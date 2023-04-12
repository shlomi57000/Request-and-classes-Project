class MyUser :
    def __init__(self, id, email, username,name):
         self.id = id
         self.email = email
         self.username = username
         self.name = name

    def __str__(self):
         return f' The user details :\n id: {self.id}\n email : {self.email}\n username: {self.username}\n name: {self.name}  '

import requests

user2 = input('Enter your name : ')
while True :
    if isinstance(user2,str) and not user2.isdigit() and  user2 and all(char.isalpha() or char.isspace() for char in user2) :
        break
    else:
        user2 = input('Wrong input , Enter your name : ')

res = requests.get('https://jsonplaceholder.typicode.com/users')
users = res.json()
found = 0
for user in users :
    # לבקשת המשימה ליצור אובייקט לכל משתמש אשר נקרא מהאתר
    user = MyUser(user['id'],user['email'],user['username'],user['name'])
    if user.name == user2 :
        print(user)
        found = 1
if found == 0 :
    print('user not found')




