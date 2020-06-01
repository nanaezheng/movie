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
MOVIE_QA_STORE = {}

MSG_TPL = '电影标题：{movie_name}\n获取链接：<a href="{rs_link}">点我</a>\n提取码：{keyword}'
MSG_QA_TPL = 'Nanae为你精心推荐\n--------------------------\n电影标题：「{uu}」\n豆瓣评分：{uu_rating}\n获取链接：<a href="{uu_link}">点我</a>\n提取码：{uu_keyword}\n--------------------------\n重新选择请回复：T'

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
        return True, 'Nanae帮你找到\n--------------------------\n' + MSG_TPL.format(movie_name=movie_name, rs_link=rs_link, keyword=keyword) + '\n--------------------------\n资源有误，请→<a href="https://nanae.jaward.cn/wechat.html">疯狂戳我</a>'

    fuzzy_buff = []
    for store_name, info in MOVIE_STORE.items():
        if movie_name not in store_name:
            continue
        rs_link, keyword = info
        fuzzy_buff.append(MSG_TPL.format(movie_name=store_name, rs_link=rs_link, keyword=keyword))

    if fuzzy_buff:
        return True, 'Nanae帮你找到\n--------------------------\n' + '\n\n'.join(fuzzy_buff) + '\n--------------------------\n资源有误，请→<a href="https://nanae.jaward.cn/wechat.html">疯狂戳我</a>'

    return False, '请息怒，你寻找的影片没有找到，请检查片名是否输入准确，有无错别字，或微信联系：nanaezheng'


def random_film(filepath):
    oldf = None
    try:
        if filepath.startswith('file:'):
            filepath = filepath.replace('file:', '')
        oldf = io.open(filepath, 'r',encoding='UTF-8')
        lines = oldf.readlines()
        random_idx = random.sample(range(1, len(lines)), 1)[0]
        line = str(lines[random_idx])

        content = line.strip().split(',')

        uu = content[0].strip()
        uu_rating = content[1].strip()
        uu_link = content[2].strip()
        uu_keyword = content[3].strip()

        return MSG_QA_TPL.format(uu=uu, uu_rating=uu_rating, uu_link=uu_link, uu_keyword=uu_keyword)
        
    except Exception as e:
        return "系统繁忙嘻嘻嘻"
    finally:
        if oldf:
            oldf.close()


Q_A = {
    "我如何帮到你~【请回复数字】": {
        "option": [
            "1. 推荐【某类型】电影",
            "2. 【个性化】推荐电影",
            "3. 【电影名】寻找资源",
        ],
        "answer": {
            "1": "根据什么标准筛选？",
            "2": "跟谁一起看电影？",
            "3": "告诉我电影名字吧",
            "4": "Elaine跟谁看呀？",
        }
    },
    "Elaine跟谁看呀？": {
        "option": [
            "1. 自己看",
            "2. 跟Nanae看",
            "3. 跟朋友看",
        ],
        "answer": {
            "1": "file:/root/eline/for_elaine-表格 1.csv",
            "2": "file:/root/eline/with_nanae-表格 1.csv",
            "3": "file:/root/eline/with_friend-表格 1.csv",
        }
    },
    "跟谁一起看电影？": {
        "option": [
            "1. 自己一个人看",
            "2. 跟对象一起看",
            "3. 跟朋友一起看",
            "4. 跟家人一起看",
        ],
        "answer": {
            "1": "描述一下你的状态？",
            "2": "在一起多久了？",
            "3": "现在是什么时间点？",
            "4": "有没有小朋友或长辈？",
        }
    },
    "描述一下你的状态？": {
        "option": [
            "1. 精力充沛",
            "2. 略微疲倦",
            "3. 有些压抑",
        ],
        "answer": {
            "1": "file:/root/eline/random_film_happy-表格 1.csv",
            "2": "file:/root/eline/random_film_tired-表格 1.csv",
            "3": "file:/root/eline/random_film_sad-表格 1.csv",
        }
    },
    "在一起多久了？": {
        "option": [
            "1. 1年内",
            "2. 1到3年",
            "3. 3年以上",
        ],
        "answer": {
            "1": "file:/root/eline/random_film_under1year-表格 1.csv",
            "2": "file:/root/eline/random_film_1years-表格 1.csv",
            "3": "file:/root/eline/random_film_3years-表格 1.csv",
        }
    },
    "现在是什么时间点？": {
        "option": [
            "1. 工作中的间隙",
            "2. 工作日下班后",
            "3. 愉快的周末",
        ],
        "answer": {
            "1": "file:/root/eline/random_film_work-表格 1.csv",
            "2": "file:/root/eline/random_film_relax-表格 1.csv",
            "3": "file:/root/eline/random_film_weekend-表格 1.csv",
        }
    },
    "有没有小朋友或长辈？": {
        "option": [
            "1. 都没有",
            "2. 有长辈",
            "3. 有小朋友",
            "4. 都有",
        ],
        "answer": {
            "1": "file:/root/eline/random_film_brother-表格 1.csv",
            "2": "file:/root/eline/random_film_parents-表格 1.csv",
            "3": "file:/root/eline/random_film_kid-表格 1.csv",
            "4": "file:/root/eline/random_film_family-表格 1.csv",
        }
    },
    "根据什么标准筛选？": {
        "option": [
            "1. 上映「年份」",
            "2. 所用「语言」",
            "3. 具体「类型」",
        ],
        "answer": {
            "1": "你希望的电影年份是？",
            "2": "你希望的电影语言是？",
            "3": "你希望的电影类型是？",
        }
    },
    "你希望的电影年份是？": {
        "option": [
            "1. 半年内新片",
            "2. 最近两年的电影",
            "3. 2010年后的电影",
            "4. 2000年后的电影",
        ],
        "answer": {
            "1": "file:/root/eline/random_film_year_2020s-表格 1.csv",
            "2": "file:/root/eline/random_film_year_2015s-表格 1.csv",
            "3": "file:/root/eline/random_film_year_2010s-表格 1.csv",
            "4": "file:/root/eline/random_film_year_2000s-表格 1.csv",
        }
    },
    "你希望的电影语言是？": {
        "option": [
            "1. 华语电影",
            "2. 英语电影",
            "3. 小语种电影",
            "4. 日语/韩语电影",
        ],
        "answer": {
            "1": "file:/root/eline/random_film_language_Chinese-表格 1.csv",
            "2": "file:/root/eline/random_film_language_English-表格 1.csv",
            "3": "file:/root/eline/random_film_language_Small-表格 1.csv",
            "4": "file:/root/eline/random_film_year_Japanese-表格 1.csv",
        }
    },
    "你希望的电影类型是？": {
        "option": [
            "1. 剧情",
            "2. 悬疑",
            "3. 爱情",
            "4. 动作",
            "5. 犯罪",
            "6. 喜剧",
            "7. 恐怖",
            "8. 科幻",
        ],
        "answer": {
            "1": "file:/root/eline/random_film_story-表格 1.csv",
            "2": "file:/root/eline/random_film_suspense-表格 1.csv",
            "3": "file:/root/eline/random_film_love-表格 1.csv",
            "4": "file:/root/eline/random_film_action-表格 1.csv",
            "5": "file:/root/eline/random_film_crime-表格 1.csv",
            "6": "file:/root/eline/random_film_comedy-表格 1.csv",
            "7": "file:/root/eline/random_film_scary-表格 1.csv",
            "8": "file:/root/eline/random_film_science-表格 1.csv",
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

    if msg == "T":
        content = "我如何帮到你~【请回复数字】"
        CONTENT_CACHE[user] = content
        content += '\n' + '\n'.join(Q_A[content]['option'])  
        return content

    # msg unknown
    if not last_context and '咚咚咚' not in msg:
        return '不是很明白你的意思呢(*╹▽╹*)'
    
    # first enter room and wanna chatting
    if not last_context and '咚咚咚' in msg:
        content = "我如何帮到你~【请回复数字】"
        CONTENT_CACHE[user] = content
        content += '\n' + '\n'.join(Q_A[content]['option'])  
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
        elif content.startswith('file:'):
            content = random_film(content)
            del CONTENT_CACHE[user]
        else:
            CONTENT_CACHE[user] = content
        return content
    elif last_context == "告诉我电影名字吧":
        is_find, content = find_movie(msg)
        if is_find:
            del CONTENT_CACHE[user]
        return content

    # msg not match
    return '不是很明白你的意思呢(*╹▽╹*)'

class Handle(object):
    
    def POST(self):
        
        webData = web.data()
        recMsg = receive.parse_xml(webData)
        toUser = recMsg.FromUserName
        fromUser = recMsg.ToUserName
        formReceive = recMsg.Content
        last_context = CONTENT_CACHE[toUser] if toUser in CONTENT_CACHE else ''
        content = chatting(toUser, formReceive)
        replyMsg = reply.TextMsg(toUser, fromUser, content)
            
        return replyMsg.send()
