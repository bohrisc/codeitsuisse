import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def fixedrace():
    data = request.get_data(as_text=True)
    logging.info("data sent for evaluation {}".format(data))
    result = ""
    return result