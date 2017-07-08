with open('allRoleCodes', 'r') as f:
    for row in f.readlines():
        aaa = row[:-1]
        # print('{a}("{b}", "{c}"),'.format(a=aaa, b=aaa, c=aaa))
        print('- {a}'.format(a=aaa))
