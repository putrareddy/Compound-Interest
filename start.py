from datetime import date

p = input("Enter Amount :")
t1 = input("Enter Starting Date in Format DD/MM/YYYY :")
t2 = input("Enter Final Date :")
#09-03-2002
d1 = date(int(t1[6:10]), int(t1[3:5]), int(t1[0:2]))
d2 = date(int(t2[6:10]), int(t2[3:5]), int(t2[0:2]))
number = d2-d1
r = input("Enter Rate of Interest :")
p = int(p)
t = number.days
r = float(r)
while(t>365):
    i = p*r*365/3000
    p = p + i
    t = t - 365
i = p*r*t/3000
A = p + i
print(A)