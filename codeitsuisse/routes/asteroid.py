import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def asteroid(request):


@app.route('/asteroid', methods=['POST'])
def evaluateasteroid():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")
    result = 1
    logging.info("My result :{}".format(result))
    return json.dumps(result)



def main():
    for i in range(len(input_list)):
        for j in range(input_list[i]):
            

            input_list[]

