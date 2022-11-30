# Домашка 23
from flask import Flask, request, jsonify

from utils import check_param, build_query

app = Flask(__name__)


@app.route("/perform_query", methods=['POST'])
def perform_query():
    param = request.json
    if not check_param(param):
        return "Ошибка в параметрах запроса или нет файла", '400'

    cmd1 = param.get('cmd1')
    value1 = param.get('value1')
    cmd2 = param.get('cmd2')
    value2 = param.get('value2')
    file_name = param.get('file_name')

    result = None
    result = build_query(cmd1, value1, file_name, result)
    result = build_query(cmd2, value2, file_name, result)

    return jsonify(result), '200'


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
