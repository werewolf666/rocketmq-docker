import time
import uuid
import json
from rocketmq.client import PushConsumer

# def callback(msg):
#     print(msg.id, msg.body)

# consumer = PushConsumer('CID_XXX')
# consumer.set_namesrv_addr('121.199.30.160:50047')
# consumer.subscribe('python-topic-1', callback)
# consumer.start()

# while True:
#     time.sleep(3600)

# consumer.shutdown()


class RocketmqPushConsumer():
    consumer = None
    def __init__(self,conf):
        pid = uuid.uuid1().hex
        self.consumer = PushConsumer(pid)
        self.consumer.set_namesrv_addr(conf)
    
    # 创建长连接
    def start(self):
        self.consumer.start()
    #关闭链接
    def close(self):
        self.consumer.shutdown()
    def callback(self,msg):
        print('self.callback')
        print(msg.body)
        return msg
    # 获取消息
    def getMessage(self,topic,callback=None):
        if not callback:
            callback = self.callback
        self.consumer.subscribe(topic,callback)
        self.start()

if __name__ == '__main__':
    namesrv_addr = '121.199.30.160:50047'
    topic='python-topic-1'
    consumer = RocketmqPushConsumer(namesrv_addr)
    def callback(msg):
        print('ouside.callback')
        print(msg.id,msg.body)
        return msg
    a = consumer.getMessage(topic,callback)

    
    while True:
        time.sleep(3600)





