with open('cro.txt', 'r') as f:
    for row in f.readlines():
        line = row.replace('\n', '')

        print('"' + line + '",')
