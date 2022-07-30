#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2019/5/19 21:22
# @Author: Junzhe_Zhang
import pandas
import numpy
import json
import os

# df = pandas.read_json('./Forum/dream.json', lines=True, encoding="utf8")

with open('./Forum/intel.json', 'r',encoding="utf8") as datafile:
    df = json.load(datafile)
di = pandas.DataFrame(df)

di.to_csv("./Forum/intel.csv")

