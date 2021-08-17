#print ( "Howdy cow")
import re
data=open('regex_sum_1334540.txt')

sum =0
x=list()
for line in data:
    num=re.findall('[0-9]+',line)
    x=x+num

for i in x:
    sum=sum+int(i)
print(sum)
