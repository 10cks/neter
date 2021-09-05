from os import system
import re
print("WELCOME NETSTAT\n")
#PID PORT REFRESH KILL
#PID NAME PORT STATUS

while True:
    print("INPUT:[list port] [ ]")
    user_input = input(">>")
    port=pid=1
    try:
        number = re.findall(r"\d+\.?\d*",user_input)
        port = int(number[0])
        pid  = int(number[1])
    except:
        pass
    # if user_input == "port "
    if "clear" == user_input:system("cls")   
    elif "exit" == user_input:break
    elif user_input.find("list") is 0:
        if isinstance(port,int):
            system("netstat -ano|findstr %d"%(port))
        else:
            system("netstat -ano")
        
