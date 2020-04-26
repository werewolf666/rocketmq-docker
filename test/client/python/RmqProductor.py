# -*- coding: utf-8 -*-

# rocketmq生产者类，发送不同的消息

from rocketmq.client import Producer
import RmqMessage
import time

class RmqProductor():
    # 生产者实例
    producer = None

    '''
    传入配置文件，链接namesrv
    conf:namesrv配置文件
    group_id:消费组id
    orderly:是否是顺序消息
    timeout:超时
    compress_level:消息压缩水平 number
    max_message_size:消息大小限制
    '''
    def __init__(self,conf,group_id,orderly=False, timeout=None, compress_level=None, max_message_size=None):
        self.producer = Producer(group_id,orderly, timeout, compress_level)
        self.producer.set_namesrv_addr(conf)
        self.producer.start()

    # 发送普通消息
    def send_message_sync(self,topic,body,keys='',tags='',property=None,delay_time_level=0):
        msg = RmqMessage.get_msg_instance(topic,body,keys,tags)
        ret = self.producer.send_sync(msg)
        print('send message status: ' + str(ret.status) + ' msgId: ' + ret.msg_id)
        return ret

    def send_orderly_with_sharding_key(self,topic,body,order_id,keys='',tags='',property=None,delay_time_level=0):
        msg = RmqMessage.get_msg_instance(topic, body, keys, tags, property, delay_time_level)
        ret = self.producer.send_orderly_with_sharding_key(msg, order_id)
        print('send message status: ' + str(ret.status) + ' msgId: ' + ret.msg_id)
        print('send sync order message done')
        return ret
    def shutdown(self):
        self.producer.shutdown()

if __name__ == '__main__':
    namesrv_addr = '127.0.0.1:50047'
    topic = 'python-topic-2'
    msg = {
        'name': "python-client",
        'tpoic':'python-topic-2',
        'type': 'normal message',
        'content': '这是一条普通消息',
        'order': 0
    }
    keys = 'keys_' + topic
    tags = 'tags_' + topic
    group_id = 'python-topic-2'
    produce = RmqProductor(namesrv_addr,group_id)
    a = produce.send_message_sync(topic, msg,keys,tags)
    print(a)
    # produce.shutdown()
        

