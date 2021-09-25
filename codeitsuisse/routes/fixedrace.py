import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def fixedrace():
    data = request.get_data(as_text=True)
    logging.info("data sent for evaluation {}".format(data))
    temp = data.split(",")
    result = ""
    if "Lamont Lasch" in temp == True:
        result += "Lamont Lasch," 
        temp.remove("Lamont Lasch")
    if "Annamarie Ahern" in temp == True:
        result += "Annamarie Ahern," 
        temp.remove("Annamarie Ahern")
    if "Regenia Rathburn" in temp == True:
        result += "Regenia Rathburn,"
        temp.remove("Regenia Rathburn")
    random.shuffle(temp)
    for i in range(len(temp)):
        result += temp[i]
        if i == len(temp)-1:
            pass
        else:
            result += ","
    return result