#! usr/bin/python #coding=utf-8 /
import time
from itertools import groupby,count

#打印神的一个名字
def printGodsName(words):
	
	godsName = ""
	#神没有带有三个连续字母的名字
	if max(len(list(g)) for k, g in groupby(words) )>=3:
		return
	for singleWord in words[::-1]:
		godsName+=chr(65+singleWord) 
	print godsName

#26进制
def twentySixDecimal(words,i=0):
	if words[i]==26:
		words[i] = 0
		if i == len(words)-1:
			words.append(0)
		else:
			words[i+1]+=1
		i+=1
		twentySixDecimal(words,i)
	return words

#启动V型电脑
def RunMarkV(bitCount):
	words = [-1]
	for i in count():
		if i==(26**bitCount+26*(1-26**(bitCount-1))/(-25)):
			break					
		words[0] += 1
		words = twentySixDecimal(words)
		printGodsName(words)

	#如果运行到这里世界还没有毁灭的话.....呼一口气，乘坐DC-3离开
	time.sleep(1)
	print u"神是脆弱的东西，他们闻点儿科学的气味或者喝点常识的药水都会死掉"

def main():
	bitCount = 9
	RunMarkV(bitCount)
if __name__ == '__main__':
	main()
