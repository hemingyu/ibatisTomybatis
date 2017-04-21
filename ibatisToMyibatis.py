#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os , re, sys

#replacefile转换ibatis为myibatis,针对mapper文件
def replacefile(refile,fileName):
	print refile
	if not refile.strip():
		print 'refile is null'
	print '正在操作'+fileName+'文件'

	f=open(refile,'r+')
	all_lines=f.readlines()
	f.seek(0)
	f.truncate()
	for line in all_lines:
		#匹配ibatis头
		p_1='<!DOCTYPE sqlMap.*?>'
		data_1=re.findall(p_1,line)
		#匹配sqlMap
		p_2='sqlMap'
		data_2=re.findall(p_2,line)
		#匹配class
		p_3='class'
		data_3=re.findall(p_3,line)
		#匹配XXXClass
		p_4='Class'
		data_4=re.findall(p_4,line)
		#匹配isNotEmpty,isNotNull,isEqual
		p_5_1='<isNotEmpty.*?prepend=\".*?\".?property=\".*?\"?>'
		data_5_1=re.findall(p_5_1,line)
		p_5_2='<isNotEmpty.*?prepend=\"(.*?)\".?property=\"(.*?)\"?>'
		data_5_2=re.findall(p_5_2,line)
		
		p_6_1='<isNotEmpty.*?property=\".*?\".?prepend=\".*?\"?>'
		data_6_1=re.findall(p_6_1,line)
		p_6_2='<isNotEmpty.*?property=\"(.*?)\".?prepend=\"(.*?)\"?>'
		data_6_2=re.findall(p_6_2,line)
		
		p_7_1='<isNotEmpty.*?property=\".*?\"'
		data_7_1=re.findall(p_7_1,line)	
		p_7_2='<isNotEmpty.*?property=\"(.*?)\"'
		data_7_2=re.findall(p_7_2,line)
		
		p_8='<isNotEmpty  prepend="and".*?>'
		data_8=re.findall(p_8,line)
		#匹配</isNotEmpty结尾
		p_9='</isNotEmpty.*?>'
		data_9=re.findall(p_9,line)
		#匹配<dynamic prepend="WHERE"?>
		p_10='<dynamic prepend="WHERE"?>'
		data_10=re.findall(p_10,line)
		#匹配<dynamic>
		p_11='<dynamic>'
		data_11=re.findall(p_11,line)
		#匹配</dynamic?>结尾
		p_12='</dynamic?>'
		data_12=re.findall(p_12,line)
		#匹配#value#需要改成:#{value}
		p_13_1='#.*?#'
		data_13_1=re.findall(p_13_1,line)
		p_13_2='#(.*?)#'
		data_13_2=re.findall(p_13_2,line)
		#print data_13_1,data_13_2
		#匹配$value$需要改成:${value}
		p_14_1='\$.*?\$'
		data_14_1=re.findall(p_14_1,line)
		p_14_2='\$(.*?)\$'
		data_14_2=re.findall(p_14_2,line)
		#print data_14_1,data_14_2
		if data_1:
			for i in range(len(data_1)):
				line.replace(data_1[i],'<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.i//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">')
		if data_2:
			for i in range(len(data_2)):
				line=line.replace(data_2[i],'mapper')
		if data_3:
			for i in range(len(data_3)):
				line=line.replace(data_3[i],'type')
		if data_4:
			for i in range(len(data_4)):
				line=line.replace(data_4[i],'Type')
		if data_5_1:
			for i in range(len(data_5_1)):
				line=line.replace(data_5_1[i],'<if test="'+data_5_2[i][1]+' != null and '+data_5_2[i][1]+' != \'\' ">\n	'+data_5_2[i][0]+'')
		if data_6_1:
			for i in range(len(data_6_1)):
				line=line.replace(data_6_1[i],'<if test="'+data_6_2[i][0]+' != null and '+data_6_2[i][0]+' != \'\' ">\n	'+data_6_2[i][1]+'')
		if data_7_1:
			for i in range(len(data_7_1)):
				line=line.replace(data_7_1[i],'<if test="'+data_7_2[i][0]+' != null and '+data_7_2[i][0]+' != \'\' "')
		if data_8:
			for i in range(len(data_8)):
				line=line.replace(data_8[i],'and')
		if data_9:
			for i in range(len(data_9)):
				line=line.replace(data_9[i],'</if>')
		if data_10:
			for i in range(len(data_10)):
				line=line.replace(data_1i[i],'where 1=1')
		if data_11:
			for i in range(len(data_11)):
				line=line.replace(data_11[i],'')
		if data_12:
			for i in range(len(data_12)):
				line=line.replace(data_12[i],'')
		if data_13_1:
			for i in range(len(data_13_1)):
				line=line.replace(data_13_1[i],'#{'+data_13_2[i]+'}')
		if data_14_1:
			for i in range(len(data_14_1)):
				line=line.replace(data_14_1[i],'${'+data_14_2[i]+'}')
		f.write(line)
	f.close()

def preimport(path):
				'''
				打印一个目录下的所有文件夹和文件 
				'''
				Xfile=[]
				for root, dirs, files in os.walk(path):
					for file in files:
						if os.path.splitext(file)[1] == '.xml':
							#Xfile.append(os.path.join(root, file))
							replacefile(os.path.join(root, file),file)
				#for refile in Xfile:
					#replacefile(refile)
if   __name__ == "__main__":
    print sys.argv[1]
    preimport(sys.argv[1])
	