# -*- coding: utf-8 -*-# 
# filename: handle.py

import hashlib
import reply
import receive
import web
import time
import random
import io
from random import randint

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

def random_film_a1g1():
    oldf = None
    try:
        oldf = io.open('/root/eline/funny-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a1g2():
    oldf = None
    try:
        oldf = io.open('/root/eline/love-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a1g3():
    oldf = None
    try:
        oldf = io.open('/root/eline/family-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a1g4():
    oldf = None
    try:
        oldf = io.open('/root/eline/fanzhui-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a2g1():
    oldf = None
    try:
        oldf = io.open('/root/eline/music-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a2g2():
    oldf = None
    try:
        oldf = io.open('/root/eline/hk-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a2g3():
    oldf = None
    try:
        oldf = io.open('/root/eline/guess-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a3g1():
    oldf = None
    try:
        oldf = io.open('/root/eline/top250-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a3g3():
    oldf = None
    try:
        oldf = io.open('/root/eline/hk-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a3g4():
    oldf = None
    try:
        oldf = io.open('/root/eline/nanae-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a4g1():
    oldf = None
    try:
        oldf = io.open('/root/eline/want-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a4g2():
    oldf = None
    try:
        oldf = io.open('/root/eline/top250-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a4g3():
    oldf = None
    try:
        oldf = io.open('/root/eline/star-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a4g4():
    oldf = None
    try:
        oldf = io.open('/root/eline/new-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a3g2g1():
    oldf = None
    try:
        oldf = io.open('/root/eline/ostar-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a3g2g2():
    oldf = None
    try:
        oldf = io.open('/root/eline/96s-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a3g2g3():
    oldf = None
    try:
        oldf = io.open('/root/eline/10s-表格 1.csv', 'r',encoding='UTF-8')
        lines = oldf.readlines()
        filelines=len(lines)
        ret_idx = random.sample(range(0, filelines), 1)[0]
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

CHAT_USR = {
    "oIiOM5cKpZgS_lAuHi50iTzb38o0": "jawardwu",
    "oQcgquAZLxops9dpqwQGxdJFjsoY": "nanaezheng",
    "oIiOM5cKpZgS_lAuHi50iTzb38o0": "elaine",
}

Q_A = {
    "以下哪句话最接近你的目的？": {
        "option": [
            "1. 纯粹为了放松",
            "2. 碎片时间消磨",
            "3. 享受电影乐趣",
            "4. 打卡完成任务",
        ],
        "answer": {
            "1": "描述一下你的状态？",
            "2": "现在是什么时间点？",
            "3": "再提一个要求吧？",
            "4": "我是否标记过？",
        }
    },
    "描述一下你的状态？": {
        "option": [
            "1. 感觉很累",
            "2. 日常愉快",
            "3. 有点郁闷",
            "4. 平平淡淡",
        ],
        "answer": {
            "1": random_film_a1g1,
            "2": random_film_a1g2,
            "3": random_film_a1g3,
            "4": random_film_a1g4,
        }
    },
    "现在是什么时间点？": {
        "option": [
            "1. 工作中的间隙",
            "2. 工作日下班后",
            "3. 愉快的周末",
        ],
        "answer": {
            "1": random_film_a2g1,
            "2": random_film_a2g2,
            "3": random_film_a2g3,
        }
    },
    "再提一个要求吧？": {
        "option": [
            "1. 豆瓣评分高",
            "2. 得奖的作品",
            "3. 高分华语片",
            "4. 和Nanae一起看",
        ],
        "answer": {
            "1": random_film_a3g1,
            "2": "关于电影年份？",
            "3": random_film_a3g3,
            "4": random_film_a3g4,
        }
    },
    "关于电影年份？": {
        "option": [
            "1. 只要经典就行",
            "2. 1996年以后的电影",
            "3. 最近十年的电影",
        ],
        "answer": {
            "1": random_film_a3g2g1,
            "2": random_film_a3g2g2,
            "3": random_film_a3g2g3,
        }
    },
    "我是否标记过？": {
        "option": [
            "1. 我标记过的",
            "2. 我没有标记过，分数要高",
            "3. 我没有标记过，只求看脸",
            "4. 我没有标记过，追求潮流",
        ],
        "answer": {
            "1": random_film_a4g1,
            "2": random_film_a4g2,
            "3": random_film_a4g3,
            "4": random_film_a4g4,
        }
    },
}

CONTENT_CACHE = {}


class Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"


class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{Content}]]></Content>
            </xml>
            """
        return XmlForm.format(**self.__dict)

class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[image]]></MsgType>
                <Image>
                <MediaId><![CDATA[{MediaId}]]></MediaId>
                </Image>
            </xml>
            """
        return XmlForm.format(**self.__dict)


def chatting(user, msg):
    # query user last context
    last_context = CONTENT_CACHE[user] if user in CONTENT_CACHE else ''

    # msg unknown
    if not last_context and '咚咚咚' not in msg:
        return '不是很明白你的意思呢(*╹▽╹*)'
    
    # first enter room and wanna chatting
    if not last_context and '咚咚咚' in msg:
        content = "以下哪句话最接近你的目的？"
        CONTENT_CACHE[user] = content
        content += '\n' + '\n'.join(Q_A[content]['option'])  
        return content

    # receive question
    if msg in Q_A:
        content = '\n'.join(Q_A[msg]['option'])
        CONTENT_CACHE[user] = content
        return content

    # receive answer
    if last_context in Q_A:
        content = Q_A[last_context]['answer'][msg]
        if not isinstance(content, str):
            content = content()
            del CONTENT_CACHE[user]
        elif content in Q_A:
            CONTENT_CACHE[user] = content
            content += '\n' + '\n'.join(Q_A[content]['option'])
        else:
            del CONTENT_CACHE[user]
        return content

    # msg not match
    return '不是很明白你的意思呢~(*╹▽╹*)'

class Handle(object):
    
    def POST(self):
        
        webData = web.data()
        recMsg = receive.parse_xml(webData)
        toUser = recMsg.FromUserName
        fromUser = recMsg.ToUserName
        formReceive = recMsg.Content

#        if toUser not in CHAT_USR:
#            replyMsg = reply.TextMsg(toUser, fromUser, '你不是心上人')
#            return replyMsg.send()

        content = chatting(toUser, formReceive)
        replyMsg = reply.TextMsg(toUser, fromUser, content)
            
        return replyMsg.send()
 
