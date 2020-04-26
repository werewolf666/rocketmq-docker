# -*- coding: utf-8 -*-

# rocketmq消费者类
from rocketmq.client import PushConsumer
import time

class RmqConsumer():
    consumer = None

    def __init__(self, conf, group_id, orderly=False,):
        self.consumer = PushConsumer(group_id, orderly)
        self.consumer.set_namesrv_addr(conf)
    # 接受消息
    def start_consume_message(self,topic,callback):
        self.consumer.subscribe(topic, callback)
        print('start consume message')
        self.consumer.start()

    def start_consume_orderly_message(self,topic,callback,ak, sk, channel):
        # 发送顺序消息必须初始化顺序消息的 Producer，确保第二个参数为 True
        self.consumer.set_session_credentials(ak, sk, channel)
        self.consumer.subscribe(topic, callback)
        # ********************************************
        # 1. 确保订阅关系的设置在启动之前完成
        # 2. 确保相同 GID 下面的消费者的订阅关系一致
        # 3. 确保此处设置的 Topic 一定是控制台上申请的顺序类型
        # *********************************************
        print('start orderly consume message')
        self.consumer.start()


if __name__ == '__main__':
    namesrv_addr = '127.0.0.1:50047'
    topic = 'python-topic-2'
    group_id = 'python-topic-2'
    consumer = RmqConsumer(namesrv_addr,group_id)
    def callback(msg):
        print('ouside.callback')
        print(msg.id, msg.body)
    consumer.start_consume_message(topic, callback)

    while True:
        time.sleep(3600)