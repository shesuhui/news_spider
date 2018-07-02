# -*- coding:utf-8 -*-

from elasticsearch_dsl import DocType,Nested,Date,Boolean,analyzer,Completion,Text,Keyword,Integer
from elasticsearch_dsl.connections import connections

# 新建连接
connections.create_connection(hosts="127.0.0.1")

class PoemType(DocType):
    id
    title = Text()
    url = Keyword()
    author = Keyword()
    content = Text()

    class Meta:
        # 数据库名称和表名称
        index = "poem"
        doc_type = "poem"

if __name__ == '__main__':
    PoemType.init()
    test=PoemType()
    test.title='长歌行'
    test.author='佘肃徽'
    test.content='测试内容！！！！'
    test.url='http://www.baidu.com'
    test.save()