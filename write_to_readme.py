import os
import re
from urllib import parse

l = [n for n in os.listdir(".") if '.' not in n]
l = sorted(l,key = lambda x: os.path.getmtime('./'+x))
month_bullet= {'Jan Challenge':'💝','Feb Challenge':'🧡','Mar Challenge':'💚' ,'Apr Challenge':'💙', 'May Challenge':'💛', 'Jun Challenge':'💜','Jul Challenge':'🤎','Aug Challenge':'🖤','Sep Challenge':'🤍','Oct Challenge':'💕','Nov Challenge':'💖','Dec Challenge':'❤️‍🩹'}

common_path = 'https://github.com/ThisIsSakshi/Leetcode-Solutions/blob/main/'
s='# Leetcode Solutions'
for month in l:
    sno=1
    s+='\n\n<details close> \n'
    s+='\t<summary style="font-size:25px;">'+month+':</summary>'

    all_questions = os.listdir('./'+month)
    all_questions = sorted(all_questions,key = lambda x: os.path.getmtime('./'+month+'/'+x)) 

    for question in all_questions:
        file_path=os.getcwd()+'/'+month+'/'
        num=re.findall(r'^(\d{1,2}): ',question)
        new_question_name = question
        if num==[]: 
            new_question_name = str(sno)+': '+question
            os.rename(file_path+question,file_path+new_question_name)
        code_path = common_path+parse.quote(month+'/'+new_question_name)
        s+= '\n\n'+month_bullet[month]+' ['+new_question_name+']('+code_path+') \n'
        sno+=1
    s+='\n</details>'

file = open('README.md','w')
file.write(s)
file.close() 
