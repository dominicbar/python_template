from chalice import Blueprint
from chalice import Response
import os
from chalice.app import APIGateway
import psycopg2
import json
import datetime
from datetime import timezone
import random
import requests

helperFunctions = Blueprint(__name__)

ENV_NAME = os.environ["ENV_NAME"]
DEBUG_ENABLE = False

responseMessage = {}
responseSubMessage = {}

if ENV_NAME == 'dev':
    connection = psycopg2.connect(user="mobile_diagnostics_role",
                                  password="mobilediagnostics123",
                                  host="all-test-dev.c6f7bs1lumk2.ap-south-1.rds.amazonaws.com",
                                  port="5432",
                                  database="mobile_diagnostics_dev")
elif ENV_NAME == 'test':
    connection = psycopg2.connect(user="mobile_diagnostics_role",
                                  password="mobilediagnostics123",
                                  host="all-test-dev.c6f7bs1lumk2.ap-south-1.rds.amazonaws.com",
                                  port="5432",
                                  database="mobile_diagnostics_test")
elif ENV_NAME == 'sandbox':
    connection = psycopg2.connect(user="mobile_diagnostics_role",
                                  password="mobilediagnostics123",
                                  host="all-test-dev.c6f7bs1lumk2.ap-south-1.rds.amazonaws.com",
                                  port="5432",
                                  database="mobile_diagnostics_sandbox")
elif ENV_NAME == 'prod':
    connection = psycopg2.connect(user="mobile_diagnostics_role",
                                  password="mobilediagnostics123",
                                  host="misc-prod.c6f7bs1lumk2.ap-south-1.rds.amazonaws.com",
                                  port="5432",
                                  database="mobile_diagnostics_prod")
else:
    connection = psycopg2.connect(user="mobile_diagnostics_role",
                                  password="mobilediagnostics123",
                                  host="all-test-dev.c6f7bs1lumk2.ap-south-1.rds.amazonaws.com",
                                  port="5432",
                                  database="mobile_diagnostics_dev")
    
def openDataBaseConnection():
    try:
        cursor = connection.cursor()
        print("Database connection opened!")
        return cursor

    except  Exception   as  e:
        responseSubMessage['errorCode'] = 500
        responseSubMessage['errorMessage'] = 'Internal Server Error'
        responseMessage['type'] = 'error'
        responseMessage['message'] = responseSubMessage
        print(responseMessage)
        return Response(body=responseMessage, status_code=401, headers={'Content-Type': 'application/json'})

@helperFunctions.route('/mobileDiagnosticsService/v1/mobile/{mobileId}/accessorId', methods=['GET'],api_key_required=True)
def getAccessorId(mobileId):
    try:
        cursor=openDataBaseConnection()
        cursor.execute('''SELECT "accessorId"  FROM accessors_mobiles where "mobileId" = {}'''.format(mobileId))
        accessorId=cursor.fetchone()
        
        if accessorId != None:
            for item in accessorId:
                accessorId=item
            response={
                "type":"success",
                "message":{
                "accessorId":accessorId
                }
                
            }
            response=json.dumps(response)
            return Response(body=response, status_code=200, headers={'Content-Type': 'application/json'})
        elif accessorId==None:
            responseSubMessage['errorCode'] = 2001
            responseSubMessage['errorMessage'] = 'accessorId not found for particular mobileId'
            responseMessage['type'] = 'error'
            responseMessage['message'] = responseSubMessage
            return Response(body=responseMessage,headers={'Content-Type': 'application/json'})

        
    except Exception as e:
        responseSubMessage['errorCode'] = 500
        responseSubMessage['errorMessage'] = e
        responseMessage['type'] = 'error'
        responseMessage['message'] = responseSubMessage
        return Response(body=responseMessage, status_code=500, headers={'Content-Type': 'application/json'})