#Counting N no using loop
N = 123
count = 0

while(N > 0):
    last_dig = N % 10
    count += 1
    N = N // 10

print(count)


