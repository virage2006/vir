num = 123
count = 0

while num != 1:
    if num % 2 == 1:
       num *= 3
       num += 1
       num //= 2
    count += 1


print(count)
