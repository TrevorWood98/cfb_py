def whowhere(usr_input, cmd, cn):
        if  usr_input.split() == ['who', 'coaches', 'oklahoma']:
            query = f"SELECT * FROM whocoacheswho WHERE school = 'Oklahoma';"
            cmd.execute(query)
            rows = cmd.fetchall()
            print('\nOkay, this is what I found: ')
            for row in rows:
                for col in row:
                    print(col, end = ' ')
                print('\n')
            cn.close()

        elif usr_input.split() == ['who', 'coaches', 'michigan']:
            query = f"SELECT * FROM whocoacheswho WHERE school = 'Michigan';"
            cmd.execute(query)
            rows = cmd.fetchall()
            print('\nOkay, this is what I found: ')
            for row in rows:
                for col in row:
                    print(col, end = ' ')
                print('\n')
            cn.close()

        elif usr_input.split() == ['who', 'coaches', 'ohio', 'state']:
            query = f"SELECT * FROM whocoacheswho WHERE school = 'Ohio State';"
            cmd.execute(query)
            rows = cmd.fetchall()
            print('\nOkay, this is what I found: ')
            for row in rows:
                for col in row:
                    print(col, end = ' ')
                print('\n')
            cn.close()
        
        elif usr_input.split() == ['who', 'coaches', 'alabama']:
            query = f"SELECT * FROM whocoacheswho WHERE school = 'Alabama';"
            cmd.execute(query)
            rows = cmd.fetchall()
            print('\nOkay, this is what I found: ')
            for row in rows:
                for col in row:
                    print(col, end = ' ')
                print('\n')
            cn.close()

        elif usr_input.split() == ['who', 'coaches', 'tcu']:
            query = f"SELECT * FROM whocoacheswho WHERE school = 'TCU';"
            cmd.execute(query)
            rows = cmd.fetchall()
            print('\nOkay, this is what I found: ')
            for row in rows:
                for col in row:
                    print(col, end = ' ')
                print('\n')
            cn.close()

        elif usr_input.split() == ['who', 'coaches', 'georgia']:
            query = f"SELECT * FROM whocoacheswho WHERE school = 'TCU';"
            cmd.execute(query)
            rows = cmd.fetchall()
            print('\nOkay, this is what I found: ')
            for row in rows:
                for col in row:
                    print(col, end = ' ')
                print('\n')
            cn.close()

        elif usr_input.split() == ['who', 'coaches', 'oklahoma?']:
            query = f"SELECT * FROM whocoacheswho WHERE school = 'Oklahoma';"
            cmd.execute(query)
            rows = cmd.fetchall()
            print('\nOkay, this is what I found: ')
            for row in rows:
                for col in row:
                    print(col, end = ' ')
                print('\n')
            cn.close()

        elif usr_input.split() == ['who', 'coaches', 'michigan?']:
            query = f"SELECT * FROM whocoacheswho WHERE school = 'Michigan';"
            cmd.execute(query)
            rows = cmd.fetchall()
            print('\nOkay, this is what I found: ')
            for row in rows:
                for col in row:
                    print(col, end = ' ')
                print('\n')
            cn.close()

        elif usr_input.split() == ['who', 'coaches', 'ohio', 'state?']:
            query = f"SELECT * FROM whocoacheswho WHERE school = 'Ohio State';"
            cmd.execute(query)
            rows = cmd.fetchall()
            print('\nOkay, this is what I found: ')
            for row in rows:
                for col in row:
                    print(col, end = ' ')
                print('\n')
            cn.close()
        
        elif usr_input.split() == ['who', 'coaches', 'alabama?']:
            query = f"SELECT * FROM whocoacheswho WHERE school = 'Alabama';"
            cmd.execute(query)
            rows = cmd.fetchall()
            print('\nOkay, this is what I found: ')
            for row in rows:
                for col in row:
                    print(col, end = ' ')
                print('\n')
            cn.close()

        elif usr_input.split() == ['who', 'coaches', 'tcu?']:
            query = f"SELECT * FROM whocoacheswho WHERE school = 'TCU';"
            cmd.execute(query)
            rows = cmd.fetchall()
            print('\nOkay, this is what I found: ')
            for row in rows:
                for col in row:
                    print(col, end = ' ')
                print('\n')
            cn.close()

        elif usr_input.split() == ['who', 'coaches', 'georgia?']:
            query = f"SELECT * FROM whocoacheswho WHERE school = 'TCU';"
            cmd.execute(query)
            rows = cmd.fetchall()
            print('\nOkay, this is what I found: ')
            for row in rows:
                for col in row:
                    print(col, end = ' ')
                print('\n')
            cn.close()