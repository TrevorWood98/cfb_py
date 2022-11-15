import pymysql as ps


def tenwin(usr_input, cmd, cn):
    # If user asks about 10 win seasons since 2010
    if usr_input == 'who has 10 win seasons since 2010?':
        query = "SELECT school, TenWin FROM tenwinseason_post2010;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end=' ')
            print()
        cn.close()

    elif usr_input == 'who has 10 win seasons since 2010?':
        query = "SELECT school, TenWin FROM tenwinseason_post2010;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end=' ')
            print()
        cn.close()

    elif usr_input == 'who has 10 win seasons since 2010':
        query = "SELECT school, TenWin FROM tenwinseason_post2010;;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end=' ')
            print('\n')
        cn.close()

    elif usr_input == '10 win seasons since 2010?':
        query = "SELECT school, TenWin FROM tenwinseason_post2010;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end=' ')
            print('\n')
        cn.close()

    elif usr_input == '10 win seasons since 2010':
        query = "SELECT school, TenWin FROM tenwinseason_post2010;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found:')
        for row in rows:
            for col in row:
                print(col, end=' ')
            print('\n')
        cn.close()
