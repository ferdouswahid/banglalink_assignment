import datetime, sys, os
import json
from flask import Flask, jsonify, Response


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


app = Flask(__name__)

@app.route('/')
def hello_world():
    outputList = []
    datetimeList = []
    with open('input.txt', 'r') as f:
        testCase = f.readline().strip()
        lines = f.readlines()
        if not testCase.isdigit():
            print('Please input the number of test cases in integer.')
            f.close()
            return Response(json.dumps({'message': 'Please input the number of test cases in integer.'}), status=200, mimetype='application/json')
        elif (int(testCase)*2) != len(lines):
            print('Number of test cases and number of dates not match.')
            f.close()
            return Response(json.dumps({'message': 'Number of test cases and number of dates not match.'}), status=200, mimetype='application/json')
        else:
            #lines = f.readlines()
            for line in lines:
                datetimeList.append(line.strip())

    for i in range(0, len(datetimeList), 2):
        dt1 = get_datetime(datetimeList[i])
        dt2 = get_datetime(datetimeList[i + 1])

        if dt1 != '' and dt2 != '':
            elapsedTime = (dt1 - dt2)
            print(int(elapsedTime.total_seconds()))
            outputList.append(str(int(elapsedTime.total_seconds())))
    return Response(json.dumps(outputList), status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)