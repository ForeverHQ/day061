import os

import yaml


def ReadLoginData(filename):
    filename = os.getcwd() + os.sep + filename
    with open(filename, "r", encoding="utf-8") as f:
        datas = yaml.load(f)
    arrs = list
    for data in datas.values():
        arrs.append((data.get("username"), data.get("pwd")))
    return arrs
