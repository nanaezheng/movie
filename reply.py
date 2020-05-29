# -*- coding:utf8 -*-  
import itchat
import time 

# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:
        # 发送一条提示给文件助手
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')
        # 回复给女神
	if msg['User']['NickName'].find('leeyan')>-1:
		return u'女神么么哒哟'
	

	# 关键字
	if msg['Text'].find('sb') >-1:
		return u'你才是SB'	
	if msg['Text'].find('SB')>-1:
		return u'你才是大写的SB'
	if msg['Text'].find(u'傻逼')>-1:
		return u'你才是傻逼'
        if msg['Text'].find(u'请客')>-1:
                return u'请个屁就知道吃'
        if msg['Text'].find(u'么么哒')>-1:
                return u'么么哒但是我心里有女神了'
        if msg['Text'].find(u'智障')>-1:
                return u'你才是智障'
        if msg['Text'].find(u'啪')>-1:
                return u'啪啪啪'
        if msg['Text'].find(u'约')>-1:
                return u'不约不约叔叔我们不约'
        if msg['Text'].find(u'辣鸡')>-1:
                return u'你才是辣鸡'
        if msg['Text'].find(u'垃圾')>-1:
                return u'你才是垃圾'
	if msg['Text'].find(u'郑旭')>-1:
                return u'叫你爸爸干嘛'

	# 普通回复
	return u'我非常认可你说的：%s\n' % (msg['Text'])

@itchat.msg_register(['Picture'])
def download_files(msg):
    	msg['Text'](msg['FileName'])
	return '@%s@%s'%({'Picture':'img','Video':'vid'}.get(msg['Type'],'fil'),msg['FileName'])

@itchat.msg_register(['Sharing'])
def text_reply(msg):
    itchat.send(u'你这篇文章我看过了,不就是: %s'%(msg['Text']),msg['FromUserName'])




if __name__ == '__main__':
    itchat.auto_login()

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()
