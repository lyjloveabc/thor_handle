import datetime

start = '2017-11-20'
end = '2017-12-24'

sum = ''

datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
dateend = datetime.datetime.strptime(end, '%Y-%m-%d')
while datestart < dateend:
    date_str = datestart.strftime('%Y%m%d')
    sum += ('"' + date_str + '",')
    datestart += datetime.timedelta(days=1)

print(sum)