from django import db
from flask import request, jsonify, Blueprint
from datetime import datetime
from http import HTTPStatus
import json

from resources import bigquery


v = Blueprint('routes', __name__)

@v.route('/ejercicio', methods=['GET','OPTIONS'])
def ejercicio():

    headers = {'content-type': 'application/json'}
    
    if request.method == 'OPTIONS':
        return ('', HTTPStatus.NO_CONTENT)

    if request.method == 'GET':
        response, http_code = bigquery.ejercicio_Bigquery()
        http_code= HTTPStatus.OK   
        return (response, http_code,headers)


