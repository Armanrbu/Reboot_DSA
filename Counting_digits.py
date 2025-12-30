#Counting N no using loop
N = 123
count = 0

while(N > 0):
    last_dig = N % 10
    count += 1
    N = N // 10

print(count)


#Counting Using recursion function

def count_digit(N):
    c = 0
    if N == 0:
        return 0
    return 1 +count_digit(N // 10)


print(count_digit(1121))


