from chalice import Blueprint
from chalice import Response
import os
import psycopg2
import json
import datetime
from datetime import timezone
import random
import requests

helperFunctions = Blueprint(__name__)

ENV_NAME = os.environ["ENV_NAME"]
DEBUG_ENABLE = False

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

@helperFunctions.route('/mobileDiagnosticsService/v1/hello/{name}', methods=['GET'], cors=True)
def getHello(name):

    responseMessage = {}
    responseSubMessage = {}

    responseSubMessage = 'hi from {}' .format(name)

    responseMessage['type'] = 'success'
    responseMessage['message'] = responseSubMessage

    return Response(body=responseMessage, status_code=200, headers={'Content-Type': 'application/json'})