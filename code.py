import json
import boto3

ROUTE_KEY = 'GET /class10'
ROUTE_KEY_POST  = 'POST /class10'

def lambda_handler(event, context):
    dct = {'Greetings':'hello bro'}
    
    
    if event['routeKey'] == ROUTE_KEY :
       
        #getting roll number from payload
        roll_of_student = event['queryStringParameters']['student_roll']
        
        #now test it for numeric
        
        if not roll_of_student.isnumeric() :
            dct['statusCode'] = 'failed due to wrong roll number'
            return json.dumps(dct)
          
        #now search the roll number in dynamo db table    
        
        dct['statusCode'] = 'success also by dynamo db'
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('student_table_class_10')
    
        try:
            response = table.get_item(Key={'roll_number':roll_of_student })
            specific_student_data = response['Item']
        except :
            dct['statusCode'] = 'DATA NOT FOUND'
            return json.dumps(dct)
        
        #adding response to result
        dct['STUDENT NAME'] =specific_student_data['student_name']
        return   json.dumps(dct)
        
    if event['routeKey'] ==ROUTE_KEY_POST :
        dct['statusCode'] = 'post done'
       
        dct['statusCode'] = 'success also by dynamo db'
        dynamodb = boto3.resource('dynamodb')
        
        table = dynamodb.Table('student_table_class_10')
        
        payload_rec = event['queryStringParameters']
        
        try:
            if int(payload_rec['marks']) > 100 :
                dct['insertion'] = 'FALSE'
                dct['error message'] = 'Marks is above 100'
                return json.dumps(dct)
                
            response = table.put_item(
                Item={
                    'roll_number' : payload_rec['roll_number'],
                    'student_name' : payload_rec['student_name'],
                    'marks' : int(payload_rec['marks']),
                    }
            )
            
            dct['insertion'] = 'TRUE'
        except :
            dct['statusCode'] = 'ERROR IN INSERTION'
        
        
        return json.dumps(dct)
    
 
   
