#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Python Doubanspider
"""
import urllib3,re

class DBSpr(object):
	def __init__(self):
		self.DB_url = 'https://movie.douban.com/top250?start={page}&filter='
		self.cur_page = 1
		self.data = []
		self._top_num = 1

	def get_page(self):
		http = urllib3.PoolManager()
		url = self.DB_url
		try:
			res = http.request('GET',url.format(page = (self.cur_page-1) * 25))
			res = res.data.decode('utf-8')
		except urllib3.exceptions.NewConnectionError:
			print('Connection failed.')
		return res

	def parse_page(self,res):
		temp_list = []
		res_list = []
		regExp = r'<span\s+class="title">(.*)</span>'
		m = re.findall(regExp,res)
		for item in m:
			clr_item = item.replace('&nbsp;','')
			temp_list.append(clr_item)
		for i in temp_list:
			if i[0] == '/':
				index = len(res_list)
				res_list[index-1] = res_list[index-1] + i
			else:
				res_list.append(i)
		print(res_list)


DB = DBSpr()
res = DB.get_page()
DB.parse_page(res)
