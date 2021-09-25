import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def fixedrace():
    data = request.get_data()
    logging.info("data sent for evaluation {}".format(data))
    temp = data.split(",")
    result = ""
    for i in range(len(temp)):
        result = result + temp[i]
        if i = len(temp)-1:
            result += ","
    return result