from collections import Counter, defaultdict, deque
from functools import reduce

import heapq as hq
import json
import time

response = '''[
 {
    "TxId": "dd6d392f350e74a027fed8fdf68e88802dea590ec6db33990ca7e423ba594c51",
    "Timestamp": {
        "seconds": { "low": 1600792773, "high": 0, "unsigned": "false" },
        "nanos": 449000000
    },
    "Value": {
        "doctorNumber": "0",
        "enrollNumber": 179,
        "patientHash": "trainer 3",
        "rawImgCID": "QmYChDgEyM8J2hJbUaEsGhzr89ns7VJZ54yEsdHbLee9VZ",
        "resultImgCID": "QmRLCxPh8Kmaj24AUSaexFcHPorSbDe5Mi4xZAhWJC2VxK"
    }
  },
  {
    "Timestamp": {
        "seconds": { "low": 1600792890, "high": 0, "unsigned": "false" },
        "nanos": 449000000
    },
    "Value": {
      "doctorID": "doctor",
      "enrollNumber": 2,
      "patientHash": "patientHash1",
      "rawImgCID": "QmYdsKciEobSYvJXpmJUCnyF7s1otEBUQs8E97oHq8WJfw",
      "resultImgCID": "QmbdqCVPxFqjxDtCBUhrfEQU11VQkrnatobedVFfHqKEgd"
    }
  },
  {
    "Timestamp": {
        "seconds": { "low": 1608799999, "high": 0, "unsigned": "false" },
        "nanos": 449000000
    },
    "Value": {
      "patientHash": "patientHash1",
      "enrollNumber": 1,
      "doctorID": "doctor",
      "rawImgCID": "QmVWn1q82hNNJSttYgNAhhHE6iMdcTHS2VF6C2zTTbKg6o",
      "resultImgCID": "QmeSSVxj2qozvTQAQWhnCcsq6J8HAUmTV14LvWrdRps8Wn"
    }
  }
]
'''

data_list = []
res = sorted(json.loads(response), key=lambda x: -(x['Timestamp']['seconds']['low']))
for each_data in res:
    tm = time.localtime(each_data['Timestamp']['seconds']['low'])
    # time_data = {'year': tm.tm_year, 'month': tm.tm_mon, 'day': tm.tm_mday, 'hour': tm.tm_hour, 'minute': tm.tm_min}
    time_data = str(tm.tm_year) + '.' + str(tm.tm_mon) + '.' + str(tm.tm_mday) + ' / ' + str(tm.tm_hour) + ':' + str(tm.tm_min)
    data = {'time': time_data, 'rawImgCID': each_data['Value']['rawImgCID'], 'resultImgCID': each_data['Value']['resultImgCID']}
    data_list.append(data)

print(data_list)

# print(json.load(response))




# l = [[1,2,3], [4,5,6], [7,8,9]]

# lr = list(zip(*l[::-1]))
# lr = list(zip(*l))[::-1]
