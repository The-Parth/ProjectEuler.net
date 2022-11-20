ft = 1 ; st = 2
sum = 0
while (st < 4000000):
    if st%2==0:
        sum = sum + st
    temp = ft
    ft = st
    st = temp + st

print(sum)