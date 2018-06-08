with open('hahha.txt', 'r') as f:
    for line in f.readlines():
        print('UPDATE users SET passwd = "670b14728ad9902aecba32e22fa4f6bd" WHERE mobile = "{mobile}";'.format(mobile=line[:-1]))
