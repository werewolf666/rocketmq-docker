# -*- coding: utf-8 -*-

# rocketmq产生消息类，通过指定消息类型生产消息

from rocketmq.client import Message
import json

def get_msg_instance(topic,body,keys='',tags='',property=None,delay_time_level=0):
    msg = Message(topic)
    if keys:
        msg.set_keys(keys)
    if tags:
        msg.set_tags(tags)
    if property:
        msg.set_property(property[0], property[1])
    if delay_time_level:
        msg.set_delay_time_level(delay_time_level)
    body = str(body)
    # body = bytes(json.dumps(body),encoding="utf8")
    msg.set_body(body)
    return msg

# class RmqMessage():
#
#     # 消息实例
#     msg = None
#     '''
#     topic:消息主题 string
#     body:消息内容, bytes类型,字典元组等要转换成bytes
#     keys:消息二级keys string
#     tags:消息标签 string
#     property:消息属性，传入数组['property','test']
#     delay_time_level:延时消息时间 number
#     '''
#     def __init__(self,topic,body,keys='',tags='',property=None,delay_time_level=0):
#         self.msg = Message(topic)
#         if keys:
#             self.msg.set_keys(keys)
#         if tags:
#             self.msg.set_tags(tags)
#         if property:
#             self.msg.set_property(property[0],property[1])
#         if delay_time_level:
#             self.msg.set_delay_time_level(delay_time_level)
#         self.msg.set_body(body)
#     # 获取消息体
#     def get_instance(self):
#         return self.msg
