no = 600851475143
no2 = 13195
def largest_pf(n):
    i  = 2
    res = 1
    while (i <= n ):
        if (n % i == 0):
            n = n / i
            res = i
        else:
            i += 1
    return res

print(largest_pf(no))