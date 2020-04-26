import time
import uuid
import json
from rocketmq.client import Producer, Message

class RocketProducer():
	produce = None
	message = None
	# 初始化配置文件
	def __init__(self,conf):
		pid = uuid.uuid1().hex
		self.produce = Producer("pid")
		self.produce.set_namesrv_addr(conf)
	# 开始链接
	def start(self):
		return self.produce.start()
	# 发送同步消息
	def sendSync(self,topic,msg,group='',keys='',tags=''):
		if not topic or not msg:
			print('消息topic或msg不能为空')
			return
		msg = bytes(json.dumps(msg),encoding="utf8")
		if not self.message:
			self.getMessageInstance(topic)
		if keys:
			self.setkeys(keys)
		if tags:
			self.setTags(tags)
		self.message.set_body(msg)
		print('sending')
		response = self.produce.send_sync(self.message)
		return response	
	# 发送延时消息 level 为延时等级，总共12级 最大2h
	def sendDelay(self,topic,msg,group='',keys='',tags='',level=None):
		pass
	# 获取消息队列实例
	def getMessageInstance(self,topic):
		self.message = Message(topic)
	# 设置消息体
	def setkeys(self,keys):
		if keys:
			return self.message.set_keys(keys)
	# 设置标签
	def setTags(self,tags):
		if tags:
			return self.message.set_tags(tags)
	# 关闭链接
	def close(self):
		self.produce.shutdown()                                                                                 

if __name__ == '__main__':
	namesrv_addr = '121.199.30.160:50047'
	topic = 'python-topic-1'
	msg = {
		'name':"python-client",
		'type':'normal message',
		'content':'这是一条普通消息',
		'order':0
	}                                                                                  
	produce = RocketProducer(namesrv_addr)
	produce.start()
	while True:
		a = produce.sendSync(topic,msg)
		time.sleep(5)
	
	# a = produce.sendSync(topic,'msg')
	print(a)

