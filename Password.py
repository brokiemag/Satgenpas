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
account_sid="#acc_sid"
auth_token="#auth_token"
client = Client(account_sid, auth_token)
message = client.messages.create(
        body="Your Satellite Generated Password is: "+str(password),
        from_='#phno',
        to="#urphno"
    )
with open('pass.txt') as file:
    contents = file.read()
    pass_verification = input("Please Verify Your Satellite Generated Password:- ")
    if pass_verification in contents:
        print ('Satellite Generated Password Found')
        sleep(1)
        print ('Redirecting to Authorized page...')
        os.startfile("#path")
    else:
        print ('Satellite Generated Password Error')
