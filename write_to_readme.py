import os
from urllib import parse

l = list(set(os.listdir("."))-set(['write_to_readme.py', 'README.md', '.git','.gitignore','.DS_Store']))
print(l)
common_path = 'https://github.com/ThisIsSakshi/Leetcode-Solutions/blob/main/'
s='# Leetcode Solutions'
for month in l:
    s+='\n\n<details close> \n'
    s+='\t<summary>'+month+':</summary>\n<ol>'
    for question in os.listdir('./'+month):
        code_path = common_path+parse.quote(+month+'/'+question)
        s+= '<li>\n\n['+question+']('+code_path+') \n</li>'
    s+='\n</ol></details>'

file = open('README.md','w')
file.write(s)
file.close() 
