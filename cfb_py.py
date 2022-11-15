import pymysql as ps
import tenwin
import whocoaches
import cfbhistory
import sys
import maskpass as mp

print('Enter database password before we begin: \n')
pwd = mp.askpass(mask="")


while True:
    print('********************************************************************')
    print('Hello! I am the football guru! Ask me anything & tap done to exit: ')
    print('********************************************************************')
    usr_input = input().lower()
    try:
        cn = ps.connect(host='localhost', port=3306,
                        user='root', password=pwd, db='cfb_statrec')
        cmd = cn.cursor()

        # Ten wins since 2010 questions
        tenwin.tenwin(usr_input, cmd, cn)

        # Who coaches what teams
        whocoaches.whowhere(usr_input, cmd, cn)

        # History of teams
        cfbhistory.hist(usr_input, cmd, cn)

        if usr_input == 'done':
            sys.exit()

    except Exception as e:
        print(e)
        sys.exit()
