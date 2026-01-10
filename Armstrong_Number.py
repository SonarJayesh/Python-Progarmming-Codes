n = 153
total = 0
temp = n

while temp >0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10

print(total == n)    