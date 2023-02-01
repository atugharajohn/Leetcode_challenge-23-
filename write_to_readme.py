import os
from urllib import parse

l = [n for n in os.listdir(".") if '.' not in n]
l = sorted(l,key = lambda x: os.path.getmtime('./'+x))

common_path = 'https://github.com/ThisIsSakshi/Leetcode-Solutions/blob/main/'
s='# Leetcode Solutions'
for month in l:
    s+='\n\n<details close> \n'
    s+='\t<summary style="font-size:18px;">'+month+':</summary>\n<ol>'

    all_questions = os.listdir('./'+month)
    all_questions = sorted(all_questions,key = lambda x: os.path.getmtime('./'+month+'/'+x)) 

    for question in all_questions:
        code_path = common_path+parse.quote(month+'/'+question)
        s+= '\n<li>\n\n['+question+']('+code_path+') \n\n</li>'
    s+='\n</ol>\n</details>'

file = open('README.md','w')
file.write(s)
file.close() 
