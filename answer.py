# -*- coding = 'uft-8' -*-

import re
from fractions import Fraction
from suffix_expression import suffix_to_value,to_suffix

def expression_result(exp_list):
    """
    求表达式的结果
    :param exp_list: 表达式列表
    :return: None
    """
    for i, exp in enumerate(exp_list):
        order_str = str(i+1)
        s = str(suffix_to_value(to_suffix(exp)))
        exp_value = change_fraction(s) + '\n'
        result = order_str + ': '+ exp_value
        with open('Answer.txt','a+', encoding='utf-8') as f:
            f.write(result)

def check_answer(exercisefile, answerfile):
    """
    校对答案
    :param 
        exercisefile: 练习题文件
        answerfile: 答案文件
    :return: None
    """
    wrong_num = 0
    correct_num = 0
    exercise_answer = [] 
    correct_list = [] # 正确题目序号
    wrong_list = [] # 错误题目序号

    try:
        with open(exercisefile, 'r', encoding = 'utf-8') as f:
            for line in f:
                #匹配出正则表达式
                exp_str = re.findall(r'\d+: (.*) = \n',line)
                if exp_str:
                    exp = exp_str[0]
                else:
                    continue
                temp = str(suffix_to_value(to_suffix(exp)))
                exp_value = change_fraction(temp)
                exercise_answer.append(exp_value)
    except IOError:
        print('please check if the path is correct')
    
    #判断表达式列表是否为空
    try:
        with open(answerfile, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                ans_str = re.findall(r'\d+: (.*)\n', line)
                #容错
                if ans_str:
                    ans = ans_str[0]
                else:
                    continue
                #判断是否正确
                if ans == exercise_answer[i]:
                    correct_num += 1
                    correct_list.append(i+1)
                else:
                    wrong_num += 1
                    wrong_list.append(i+1)
        with open('Grade.txt', 'w+', encoding='utf-8') as f:
            correct_str = 'Correct: ' + str(correct_num) + ' '+ str(correct_list) + '\n' 
            wrong_str = 'Wrong: ' + str(wrong_num) + ' '+ str(wrong_list)
            f.write(correct_str)
            f.write(wrong_str)
    except IOError:
        print('please check if the path is correct')

def change_fraction(s):
    """
    把分数转换为带分数
    ：param s:原分数
    :return :带分数
    """
    fra = Fraction(s)
    if fra.numerator % fra.denominator == 0:
        fra = int(fra.numerator / fra.denominator)
        return str(fra)
    elif fra.numerator > fra.denominator:
        integer = fra.numerator // fra.denominator
        fra = fra - integer
        return "'".join([str(integer), str(fra)])
    else:
        return s