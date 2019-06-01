#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BaseService(object):
    '''
    处理用户请求的service基类
    '''
    def handle_request(self, json_obj, client):
        '''
        处理用户请求
        :param json_obj: json数据
        :param client: socket客户端
        :return:
        '''
        pass