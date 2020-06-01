# -*- coding: utf-8 -*-# 
# filename: handle.py
import hashlib
import reply
import receive
import web
import time
import random
import io
import csv
from random import randint

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')


MOVIE_STORE = {}

MSG_TPL = '电影名：{movie_name}\n获取地址：<a href="{rs_link}">点我</a>\n提取码：{keyword}'

CSV_FILEPATH = '/root/mo.csv'


def load_csv():
    with open(CSV_FILEPATH, 'r') as fp:
        for line in fp.readlines():
            content = line.strip().split(',')
            title = content[0].strip()
            if title == '标题':
                continue

            rs_link = content[1].strip()
            keyword = content[2].strip()
            MOVIE_STORE[title] = (rs_link, keyword)
    fp.close()


def find_movie(movie_name):
    if not MOVIE_STORE:
        load_csv()

    if movie_name in MOVIE_STORE:
        rs_link, keyword = MOVIE_STORE[movie_name]
        return MSG_TPL.format(movie_name=movie_name, rs_link=rs_link, keyword=keyword)

    fuzzy_buff = []
    for store_name, info in MOVIE_STORE.items():
        if movie_name not in store_name:
            continue
        rs_link, keyword = info
        fuzzy_buff.append(MSG_TPL.format(movie_name=store_name, rs_link=rs_link, keyword=keyword))

    if fuzzy_buff:
        return '\n\n'.join(fuzzy_buff)

    return '暂时没有这个电影，请微信联系:nanaezheng'


def random_film_a1g1():
    oldf = None
    try:
        oldf = io.open('/root/eline/funny-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 54), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a1g2():
    oldf = None
    try:
        oldf = io.open('/root/eline/love-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 92), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a1g3():
    oldf = None
    try:
        oldf = io.open('/root/eline/family-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 32), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a1g4():
    oldf = None
    try:
        oldf = io.open('/root/eline/fanzhui-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 25), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a2g1():
    oldf = None
    try:
        oldf = io.open('/root/eline/music-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 6), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a2g2():
    oldf = None
    try:
        oldf = io.open('/root/eline/hk-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 29), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a2g3():
    oldf = None
    try:
        oldf = io.open('/root/eline/guess-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 120), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a3g1():
    oldf = None
    try:
        oldf = io.open('/root/eline/top250-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 207), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a3g3():
    oldf = None
    try:
        oldf = io.open('/root/eline/hk-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 23), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a3g4():
    oldf = None
    try:
        oldf = io.open('/root/eline/nanae-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 23), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a4g1():
    oldf = None
    try:
        oldf = io.open('/root/eline/want-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 37), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a4g2():
    oldf = None
    try:
        oldf = io.open('/root/eline/top250-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 207), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a4g3():
    oldf = None
    try:
        oldf = io.open('/root/eline/star-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 60), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a4g4():
    oldf = None
    try:
        oldf = io.open('/root/eline/new-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 8), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a3g2g1():
    oldf = None
    try:
        oldf = io.open('/root/eline/ostar-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 59), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a3g2g2():
    oldf = None
    try:
        oldf = io.open('/root/eline/96s-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0, 14), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

def random_film_a3g2g3():
    oldf = None
    try:
        oldf = io.open('/root/eline/10s-表格 1.csv', 'r',encoding='UTF-8')
        ret_idx = random.sample(range(0,14), 1)[0]
        lines = oldf.readlines()
        return str(lines[ret_idx]).replace(',', '\n')
    finally:
        if oldf:
            oldf.close()

Q_A = {
    "开门~找我干什么呀？": {
        "option": [
            "1. 推荐电影",
            "2. 找资源",

        ],
        "answer": {
            "1": "描述一下你的状态？",
            "2": "告诉我电影名字吧~",
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
            "2": "我是否标记过？",
            "3": random_film_a1g3,
            "4": "关于电影年份？",
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
    # movie
    if last_context == '告诉我电影名字吧~':
        content = find_movie(msg)
        del CONTENT_CACHE[user]
        return content

    # msg unknown

    if not last_context and '咚咚咚' not in msg:
        return find_movie(msg)
    
    # first enter room and wanna chatting
    if not last_context and '咚咚咚' in msg:
        content = "开门~找我干什么呀？"
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
    return find_movie(msg)


class Handle(object):
    
    def POST(self):
        
        webData = web.data()
        recMsg = receive.parse_xml(webData)
        toUser = recMsg.FromUserName
        fromUser = recMsg.ToUserName
        formReceive = recMsg.Content

        content = chatting(toUser, formReceive)
        replyMsg = reply.TextMsg(toUser, fromUser, content)
            
        return replyMsg.send()
 
