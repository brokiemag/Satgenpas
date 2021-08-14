from random import seed
from random import random
from twilio.rest import Client
import random , string
import csv
import string
from time import sleep
import os
password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
Write_Output = open("pass.txt", 'w')
Write_Output.write(password)
Write_Output.close()
account_sid="AC28de424e67e90e4ed9d39f76cd13b5c8"
auth_token="e98f2ccf8c97e1e5f77b60fc8d9db748"
client = Client(account_sid, auth_token)
message = client.messages.create(
        body="Your Satellite Generated Password is: "+str(password),
        from_='+17607481310',
        to="+917416801085"
    )
with open('pass.txt') as file:
    contents = file.read()
    pass_verification = input("Please Verify Your Satellite Generated Password:- ")
    if pass_verification in contents:
        print ('Satellite Generated Password Found')
        sleep(1)
        print ('Redirecting to Authorized page...')
        os.startfile("C:\\Windows\\addins\\Private")
    else:
        print ('Satellite Generated Password Error')



# if query in open('pass.csv').read():
#     print("True")
# else:
#     print("False")
# # import random
# import string

# # printing lowercase
# letters = string.ascii_lowercase
# print ( ''.join(random.choice(letters) for i in range(10)) )
# input("enter the password:- ")
# query = input

# if letters in query:
#     print("Hello World")
# else:
#     print("Password incorrect")
