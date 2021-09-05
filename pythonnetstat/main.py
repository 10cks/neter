# -*- coding: utf-8 -*-
import os
import re
from posixpath import join, split
import psutil
from prettytable import PrettyTable

def pid_list_generate():
    dict_pid={}
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        dict_pid[pid]=p.name()
    return dict_pid

def port_search_list(port):
    command = os.popen("netstat -ano|findstr %d"%(port))
    b = command.read()
    b = re.sub(' +', ' ', b).split(' ')  # 先去重复空格，变成列表
    b = ' '.join(b)  # 再用单空格连接成字符串
    b = b.split("\n")  # 再用换行分割成列表
    b.pop() #列表删除最后一个元素,用del(list[-1])也可以    
    return b

def insert_program(d={},e=[]):
    
    x = PrettyTable()
    x.field_names = ['protocol','local_ip:port','remote_ip:port','status','PID','program_name']
    final_list = []

    for i in range(len(e)):
        c=e[i].split(' ')
        for key in d:
            if c[-1] == str(key):
                c.append(d[key])
            else:pass
        c.pop(0)
        for i in range(6):
            if len(c) != 6:
                c.append(' ')
            else:
                break
        x.add_row(c)
        # final_list.append(' '.join(c))
    print(x)
    # for i in final_list:
    #     x.add_row(i)
    # print(x)


if __name__ == "__main__":
    #insert_program(pid_list_generate(),port_search_list())
    print("WELCOME NETER.\n")
    #PID PORT REFRESH KILL
    #PID NAME PORT STATUS
    while True:
        print("INPUT:[list port][kill PID]")
        user_input = input(">>")
        first_number=second_number=1
        try:
            number = re.findall(r"\d+\.?\d*",user_input)
            first_number = int(number[0])
            second_number  = int(number[1])
        except:
            pass
        # if user_input == "port "
        if "clear" == user_input:os.system("cls")   
        elif "exit" == user_input:break
        elif user_input.find("list") == 0:
            if isinstance(first_number,int):
                insert_program(pid_list_generate(),port_search_list(first_number))
            else:
                os.system("netstat -ano")
        elif user_input.find("kill") == 0:
            os.system("taskkill /F /PID %d"%(first_number))