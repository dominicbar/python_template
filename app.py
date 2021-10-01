import os
from chalice import Chalice
from chalicelib.helperFunctions import helperFunctions

ENV_NAME = os.getenv('ENV_NAME')
app = Chalice(app_name='MiscMobileDiagnosticsService-{}'.format(ENV_NAME))
app.register_blueprint(helperFunctions)