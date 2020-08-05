# 直接建立一個新的txt在你目前的工作目錄下
fo = open('myfile.txt', 'w')

fo.write('This is a test')

fo = open('myfile.txt','r')

fo = open('myfile.txt', 'a')
fo.write(' and I love you')
fo.close()

import os.path

if os.path.isfile('myfile.txt'):
		print('档案存在')
else:
		print('档案不存在')