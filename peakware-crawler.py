# -*- coding: utf-8 -*-

from pyquery import PyQuery as pq
import json
import sys

RANGE = [int(i) for i in sys.argv[1:]]
FILENAME = 'mountains%i-%i.json' % (RANGE[0], RANGE[1])


with open(FILENAME, 'w') as file:
  file.write('[')
  for i in range(*RANGE):
    print("crawling %i" % i)
    q = pq(url='https://www.peakware.com/peaks.php?pk=%i' % (i))
    mountain = {'id': i}
    trs = q('#overview table tr')
    if len(trs):

      for tr in trs:
        try:
          key = pq(tr)('th').text().replace(' \n ', ' ').replace('\n', '').replace(':', '').strip()
          value = pq(tr)('td').text().replace(' \n ', ' ').replace('\n', '')
          mountain[key] = value
        except UnicodeDecodeError:
          print('error unicode on mountain %i %s' % (i, key))
      try:
        mountain['name'] = q('h1').text()
      except UnicodeDecodeError:
        print('error unicode on mountain %i NAME' % i)
      try:
        mountain['description'] = q('#peakDescription').text()
      except UnicodeDecodeError:
        print('error unicode on mountain %i DESCRIPTION' % i)

      file.write(json.dumps(mountain))
      if i + 1 != RANGE[1]:
        file.write(',')
  file.write(']')
