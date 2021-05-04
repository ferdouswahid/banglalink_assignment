import datetime

datetimeList = []
with open('input.txt', 'r') as f:
    testCase = f.readline().strip()
    lines = f.readlines()
    if not testCase.isdigit():
        print('Please input the number of test cases in integer.')
        f.close()
    elif (int(testCase)*2) != len(lines):
        print('Number of test cases and number of dates not match')
        f.close()
    else:
        #lines = f.readlines()
        for line in lines:
            datetimeList.append(line.strip())

def get_datetime(val):
    try:
        fmt = '%a %d %b %Y %H:%M:%S %z'
        dt = datetime.datetime.strptime(val, fmt)
        if dt.year <= 3000:
            return dt
        else:
            return ''
    except:
        return ''


for i in range(0, len(datetimeList), 2):
    dt1 = get_datetime(datetimeList[i])
    dt2 = get_datetime(datetimeList[i + 1])

    if dt1 != '' and dt2 != '':
        elapsedTime = (dt1 - dt2)
        print(int(elapsedTime.total_seconds()))
