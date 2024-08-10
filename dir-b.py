#!/usr/bin/python3
import requests , socket , sys 

T = input("Enter your address : ")

def check_path(path):
    try :
        u = "https://" + T + "/" + path
        print(f"\n Test for {u}")
        r = requests.get(u).status_code
    except Exception :
        print("\n Can not reach this url ")
        sys.exit(1)
    if r == 200 :
        print(f"\n [+ Valid url {u}]")


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try :
    print ("\n Check Host ...........")
    status = s.connect_ex((T,80))
    s.close()

    if status == 0 :
        print("host done")
        pass
    else :
        print("filed")
        sys.exit()

    print ("\n Check List")
    with open ("dlist.txt",'r') as myfile :
        check_list = myfile.read().strip().split('\n')
        print("list done")
        print("\n total path : %s " %str (len(check_list)))


    print("start test ")
    for i in range(len(check_list)):
        check_path(check_list[i])

    print("end test ")
except IOError:
    print("\n file error")
except socket.error:
    print("\n socket error")

except IOError:
    print("\n user interup")