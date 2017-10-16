#!/usr/local/bin/python3.5

import json
import sys

'''
read met file and save in json format

'''

arrMet = []

for line in sys.stdin:
  row = line.strip('\n').split('\t')[1:]
  arrMet.append([ round(float(x) * 100, 2) for x in row ])

print(arrMet)

def getMWC(matchScore, gamesWon, gamesOppWon, isPostCrawford=False):

  away1 = matchScore - gamesWon
  away2 = matchScore - gamesOppWon

  print("{0}-away, {1}-away".format(away1, away2));

  mwc = None

  if isPostCrawford:
    if away1 == 1:
      mwc = arrMet[0][away2]
    elif away2 == 1:
      mwc = arrMet[away1][0]
  else:
    mwc = arrMet[away1][away2]

  return mwc

###

print("MWC:",  getMWC(11, 9, 9))

print("MWC:",  getMWC(11, 10, 9, True))

print("MWC:",  getMWC(11, 10, 8, True))

print("MWC:",  getMWC(11, 10, 7, True))

print("MWC:",  getMWC(11, 2, 10, True))

print("MWC:",  getMWC(11, 3, 10, True))

### save MET in JSON format ###

fh = open("met.json", "w")

json.dump(arrMet, fh, indent=1)

fh.close()

print(
  json.dumps(arrMet, indent=4)
)

