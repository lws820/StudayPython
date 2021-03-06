# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/7/10 10:54
# @describe : 验证xmltodict库xml转json功能

import xmltodict
import json

xml = """<ROOT>
	<RETURN_CODE type="long">0</RETURN_CODE>
	<RETURN_MSG type="string">ok!</RETURN_MSG>
	<DETAIL_MSG type="string">OK!</DETAIL_MSG>
	<PROMPT_MSG type="string"></PROMPT_MSG>
	<OUT_DATA>
		<CUST_NAME type="string">＊＊文</CUST_NAME>
		<BRAND_NAME type="string">全球通</BRAND_NAME>
		<BRAND_ID type="string">001</BRAND_ID>
		<ID_NO type="long">18170000922816</ID_NO>
		<CUST_ID type="long">18072601894224</CUST_ID>
		<SILLATTR type="int">1</SILLATTR>
		<CNT_INIT_SCORE type="long">15896</CNT_INIT_SCORE>
		<CUR_SCORE type="long">10296</CUR_SCORE>
		<INIT_SCORE type="long">26346</INIT_SCORE>
		<ADJ_SCORE type="long">11543</ADJ_SCORE>
		<USE_SCORE type="long">27593</USE_SCORE>
	</OUT_DATA>
	<USER_MSG type="string">处理成功!</USER_MSG>
</ROOT>"""

xmldict = xmltodict.parse(xml)    # 入参xml字符串，出参dict对象
# print xmldict['ROOT']['RETURN_CODE']['#text']
json_str = json.dumps(xmldict, indent=1)  # 将字典转换成json
date = {'page': {'title': 'King Crimson', 'ns': 0, 'revision': {'id': 547909091}}}
xml1 = xmltodict.unparse(date)   # 入参json字符串，出参xml报文
print xml1
