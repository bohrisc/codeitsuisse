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
        if k == "Ernesto Eno":
            result += temp[k]
            temp.remove("Ernesto Eno")
        if k == "Judi Jacquez":
            result += temp[k]
            temp.remove("Judi Jacquez")
    random.shuffle(temp)
    for i in range(len(temp)):
        result += temp[i]
        if i == len(temp)-1:
            pass
        else:
            result += ","
    return result