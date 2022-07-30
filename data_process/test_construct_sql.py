#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2019/5/19 15:35
# @Author: Junzhe_Zhang
import json
a='''
{"item_url": "/products/product/37403/", 
"item_title": "Fritz Springmeier - The Illuminati Formula Used to", 
"item_description": " Fritz Springmeier - The Illuminati Formula Used to Create an Undetectable Total Mind When the mind and emotions are put under extreme stress they break and create a new mental-emotional state. It is within these mental states - born of trauma - that the mind can be conditioned. That someone would do this intentionally is unthinkable yet it has been done and tested to the degree of a science. \\"Trauma Based Mind Control\\" has been used by criminal organizations to maintain secrecy and ensure every order is followed to the letter. Through this process you get the Undetectable Total Mind Controlled Slave. Trauma Based Mind Control creates separate personalities within the individual that will carry out their duty with robotic exactness and then sleep so that the individual has no memory of their actions. These people are used as messengers, drug mules, sexual blackmail slaves and are placed in positions close to the worlds most powerful people. In short, they are used to manipulate and control the lives of the world elite.",
 "vendor_name": "HappyEyes", "vendor_url": "/users/profile/47/", "shiping_details": "Worldwide *to* Worldwide", "item_sold": 2, "CVE": [], "category": "Fraud", "transaction_details": [1530547200, 1505145600], "release_time": 1505145600}
'''

m=json.loads(a)
for key in m:
    print(m[key])
m={'key1':'1','key2':'3','key3':3}
cmd='insert into darkweb ('
for key in m:
    cmd+="'"+key+"',"
cmd=cmd[:-1]
cmd+=') values ('
for key in m:
    cmd += json.dumps(m[key]) + ","
cmd = cmd[:-1]
cmd+=');'
print(cmd)