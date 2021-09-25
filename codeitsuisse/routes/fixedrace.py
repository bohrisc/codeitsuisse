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
    for k in range(len(temp)):
        if temp[k] == "Lamont Lasch":
            result = result + temp[k] +"," 
            temp.remove(temp[k])
        if temp[k] == "Annamarie Ahern":
            result + result + temp[k] +"," 
            temp.remove(temp[k])
        if temp[k] == "Regenia Rathburn":
            result + result + temp[k] +"," 
            temp.remove(temp[k])
    random.shuffle(temp)
    for i in range(len(temp)):
        result += temp[i]
        if i == len(temp)-1:
            pass
        else:
            result += ","
    return result