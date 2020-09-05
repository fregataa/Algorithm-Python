import math
import re
from collections import Counter

# pattern = re.compile('\w*,*\w+')  this includes numbers
# pattern = re.compile('[a-zA-Z]+')
docs_path = ['./Docs/doc1.txt', './Docs/doc2.txt', './Docs/doc3.txt']

N = len(docs_path)
df = {}
tfs = []

for doc in docs_path:
    words = re.findall('[a-zA-Z]+', open(doc, 'r', encoding='utf8').read().lower())
    tf = Counter(words)
    tfs.append(tf)

for tfv in tfs:
    for ts in tfv:
        if ts not in df:
            df[ts] = 1
        else:
            df[ts] += 1

for idx, tf in enumerate(tfs):
    weight = []
    for term in tf:
        w = tf[term]*math.log10(N/df[term])
        weight.append((term, w))
    print("{0} Document TF-IDF".format(idx+1))
    for wgt in sorted(weight, key = lambda x: -x[1])[0:5]:
        print("{0}  {1:5f}".format(wgt[0], wgt[1]))
    print()



