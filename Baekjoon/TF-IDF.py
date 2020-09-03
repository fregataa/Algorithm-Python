import math
import re

# pattern = re.compile('\w*,*\w+')  this includes numbers
pattern = re.compile('[a-zA-Z]+')
docs_path = ['./Docs/doc1.txt', './Docs/doc2.txt', './Docs/doc3.txt']

N = len(docs_path)
df = {}
tfs = []

for doc in docs_path:
    with open(doc, 'r', encoding='utf8') as inFile:
        lines = inFile.readlines()
    tf = {}
    for line in lines:
        words = pattern.findall(line.lower())
        for word in words:
            if word in tf:
                tf[word] += 1
            else:
                tf[word] = 1
    for tfv in tf:
        if tfv in df:
            df[tfv] += 1
        else:
            df[tfv] = 1
    tfs.append(tf)

for idx, tf in enumerate(tfs):
    weight = []
    for term in tf:
        w = tf[term]*math.log10(N/df[term])
        weight.append((term, w))
    print("{0} Document TF-IDF".format(idx+1))
    for wgt in sorted(weight, key = lambda x: -x[1])[0:5]:
        print("{0}  {1:5f}".format(wgt[0], wgt[1]))
    print()