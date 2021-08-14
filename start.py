from datetime import date
from dateutil import relativedelta

p = input("Enter Amount :")
t1 = input("Enter Starting Date in Format DD/MM/YYYY :")
t2 = input("Enter Final Date in Format DD/MM/YYYY :")
#09-03-2002
d1 = date(int(t1[6:10]), int(t1[3:5]), int(t1[0:2]))
d2 = date(int(t2[6:10]), int(t2[3:5]), int(t2[0:2]))
number = d2-d1
dur = relativedelta.relativedelta(d2, d1)
r = input("Enter Rate of Interest :")
p = int(p)
t = number.days
r = float(r)
i1 = 0
while(t>365):
    i = p*r*365/3000
    i1 = i1+i
    p = p + i
    t = t - 365
i = p*r*t/3000
i1 = i1 + i
print('{} Years'.format(dur.years))
print('{} Months'.format(dur.months))
print('{} Days'.format(dur.days))
print(i1)
A = p + i
print(A)