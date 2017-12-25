import datetime

start = '2017-11-20'
end = '2017-12-24'

datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
dateend = datetime.datetime.strptime(end, '%Y-%m-%d')
sum = 0

while datestart < dateend:
    datestart += datetime.timedelta(days=1)
    print(datestart.strftime('%Y-%m-%d'))
    sum += 1

print(sum)
