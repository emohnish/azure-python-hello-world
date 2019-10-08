#imports
from flask import Flask
from flask import request
from flask import make_response
from flask import render_template

# for the api
import json

import logging

app = Flask(__name__)

# Just that we have a start page for the web application
@app.route("/")
def hello():
    
    # https://www.tutorialspoint.com/flask/flask_templates.htm
    app.logger.info("hello called")

    return render_template("hello.html"),200

# The api method. Expects a parameter named "input"
@app.route("/api", methods=["GET"])
def api():

    retdict ={} 

    try:
        input_string = request.args.get("input","[you forgot to feed in input]")
        app.logger.info("FAKE API CALL, input = "+input_string)

        response = {
            'input':input_string,
            'my_api_output':"hello api "+input_string
        } 
        
        retdict['response']=response

    except Exception as e:
        msg = "Bad Request (400): "+str(e)
        app.logger.info(msg)
        # print(msg)
        return msg,400
    
    retJson = json.dumps(retdict)
    app.logger.info("retjson :"+retJson)

    resp = make_response(retJson)
    resp.headers['content-type']="application/json"
    resp.headers['Access-Control-Allow-Origin']="*"

    # http://www.flaskapi.org/api-guide/status-codes/#successful-2xx
    return resp, 200
