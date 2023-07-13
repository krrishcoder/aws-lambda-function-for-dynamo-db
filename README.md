# aws-lambda-function-for-dynamo-db

client side code -->
---------------------------------------------------------------------------------
import pandas as pd
import requests as req
import json


URL = 'https://xy5w32z11f.execute-api.ap-south-1.amazonaws.com/class10'
PAYLOAD = {'roll_number':'10853' , 'marks':95670 , 'student_name' : 'ravi kumar'}

r = req.post(URL, params = PAYLOAD, timeout=5)
r = r.json()
print(r)

-----------------------------------------------------------------------------------
note that the above code can be used from anywhere to post the payload as  a http post
payload+http --> api --> lambda  --> dynamo db {a new instance of student is created }
a response is sent back from lambda to client 
