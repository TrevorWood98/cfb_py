import pymysql as ps

def hist(usr_input, cmd, cn):
    if usr_input == 'history of oklahoma football':
        query = "SELECT * FROM history WHERE school = 'Oklahoma' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()
    
    elif usr_input == 'oklahoma football history':
        query = "SELECT * FROM history WHERE school = 'Oklahoma' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()

    elif usr_input == 'oklahoma  history':
        query = "SELECT * FROM history WHERE school = 'Oklahoma' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()

    elif usr_input == 'ohio state  history':
        query = "SELECT * FROM history WHERE school = 'Ohio State' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()
    
    elif usr_input == 'history of ohio state':
        query = "SELECT * FROM history WHERE school = 'Ohio State' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()

    elif usr_input == 'history of ohio state football':
        query = "SELECT * FROM history WHERE school = 'Ohio State' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()

    
    #Michigan
    elif usr_input == 'history of michigan football':
        query = "SELECT * FROM history WHERE school = 'Michigan' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()

    elif usr_input == 'michigan football history':
        query = "SELECT * FROM history WHERE school = 'Michigan' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()

    elif usr_input == 'history of michigan':
        query = "SELECT * FROM history WHERE school = 'Michigan' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()

    #Alabama
    elif usr_input == 'history of alabama football':
        query = "SELECT * FROM history WHERE school = 'Alabama' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()

    elif usr_input == 'alabama football history':
        query = "SELECT * FROM history WHERE school = 'Alabama' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()
    
    elif usr_input == 'history of alabama':
        query = "SELECT * FROM history WHERE school = 'Alabama' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()

    #georgia
    elif usr_input == 'georgia football history':
        query = "SELECT * FROM history WHERE school = 'Georgia' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()

    elif usr_input == 'history of georgia football':
        query = "SELECT * FROM history WHERE school = 'Georgia' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()

    elif usr_input == 'history of georgia':
        query = "SELECT * FROM history WHERE school = 'Georgia' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()

    #TCU
    elif usr_input == 'tcu football history':
        query = "SELECT * FROM history WHERE school = 'TCU' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()

    elif usr_input == 'history of tcu football':
        query = "SELECT * FROM history WHERE school = 'TCU' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()

    elif usr_input == 'history of tcu':
        query = "SELECT * FROM history WHERE school = 'TCU' ORDER BY year DESC;"
        cmd.execute(query)
        rows = cmd.fetchall()
        print('\nOkay, this is what I found: ')
        for row in rows:
            for col in row:
                print(col, end = ' ')
            print()
        cn.close()