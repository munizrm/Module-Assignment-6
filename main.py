import sys

from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

def main():
    dt = datetime.now()
    utc = datetime.utc.now()
    time_string = dt.striftme("%X")
    """https://strftime.org"""

    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) == 6:
            data = date, time. store, item, cost, payment
        print("{dt}\t{time_string}\t{store}\t{item}\t{cost}\t{payment}")

print (datetime.now() + timedelta (days=1))
print (datetime.now() - timedelta (seconds=60))
print (datetime.now() + timedelta (days=730))

d = timedelta(microseconds=-1)
print(d.days,d.seconds,d.microseconds)

s = timedelta(days=100, seconds=36000, microseconds=7800000000)
print(s.days,s.seconds,s.microseconds)

datetime_object = datetime.now()
def heightandtime(x,y,z):
    print('The height is ',x,' feet and ',y,' inches.')
    print(z)
x=input('Input Feet:')
y=input('Input Inches: ')
heightandtime(x,y,datetime_object)