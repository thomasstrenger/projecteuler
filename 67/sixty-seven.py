#https://projecteuler.net/problem=67

rows = []
pyramid = open('p067_triangle.txt').read().split('\n')
for row in pyramid:
    if row != '':
       rows.append([int(i) for i in row.split(' ')])

for i in range(len(rows)-2,-1,-1):
    rows[i] = [r+max(rows[i+1][n:n+2]) for n,r in enumerate(rows[i])]

print rows[0]
#solution 7273
