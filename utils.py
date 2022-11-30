# Модуль функций
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data\\")


def filter_query(param, data):
    return list(filter(lambda row: param in row, data))


def map_query(param, data):
    col_number = int(param)
    return list(map(lambda row: row.split(' ')[col_number], data))


def unique_query(param, data):
    result = []
    for row in data:
        if row not in result:
            result.append(row)
    return result


def sort_query(param, data):
    reverse = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param, data):
    limit = int(param)
    return data[:limit]


def check_param(param):
    """Функция проверки параметров и наличия файла"""
    valid_keys = ['file_name', 'cmd1', 'value1', 'cmd2', 'value2']
    for key in param.keys():
        if key not in valid_keys:
            return False

    valid_cmd_commands = ['filter', 'map', 'sort', 'unique', 'limit']
    if param['cmd1'] not in valid_cmd_commands or param['cmd2'] not in valid_cmd_commands:
        return False

    file_name = DATA_DIR + param.get('file_name')
    if not os.path.exists(file_name):
        return False

    return True


CMD_TO_FUNCTION = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query
}


def build_query(cmd, param, file_name, data=None):
    if not data:
        file_name = DATA_DIR + file_name
        with open(file_name) as file:
            data = list(map(lambda row: row.strip(' '), file))
    return CMD_TO_FUNCTION[cmd](param=param, data=data)
