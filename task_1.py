result = 0
time_lst = '1h 45m,360s,25m,30m 120s,2h 60s'.split(',')

for interval in time_lst:
    for i in interval.split(' '):
        time_unit = i[len(i)-1]
        if time_unit == 'm':
            result += int(i.replace('m',''))
        elif time_unit == 'h':
            result += int(i.replace('h','')) * 60
        else:
            result += int(i.replace('s','')) % 60

print(result)