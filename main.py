# -*- coding = 'utf-8 -*-

import argparse

from exp_generate import Config,Generator
from answer import expression_result,check_answer

def main():
    """
    主函数
    """
    parser = argparse.ArgumentParser(description="***** 自动生成小学四则运算题目 *****")
    parser.add_argument("-n", metavar = "--题目个数", dest = "expnum_arg", help = "控制生成题目的个数" )
    parser.add_argument("-r", metavar = "--数值范围", dest = "range_arg", help = "控制题目中数值（自然数、真分数和真分数分母）的范围")
    parser.add_argument("-e", metavar = "--题目文件", dest = "exercise_arg", help = "提供题目文件")
    parser.add_argument("-a", metavar = "--答案文件", dest = "answer_arg", help = "提供答案文件")
    args = parser.parse_args()
    
    #判断生成的表达式的数目
    if args.expnum_arg:
        #表达式的范围
        if args.range_arg:
            config = Config(exp_num=int(args.expnum_arg),num_range=int(args.range_arg))
        else:
            config = Config(exp_num=int(args.expnum_arg))
        print('***** 正在生成 *****')
        generator = Generator()
        res_list = generator.generate(config)
        generator.normalize_exp(res_list)
        expression_result(res_list)
        print('***** 生成完成 *****')
    
    #练习题答案的文件判断
    if args.exercise_arg:
        if args.answer_arg:
            check_answer(args.exercise_arg, args.answer_arg)
        else:
            print('please give an answer files')
            exit(0)

if __name__ == '__main__':
    main()