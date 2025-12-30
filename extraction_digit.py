N = 192

# a = N % 10
# print("last digit",a)                 Divide by 10 then Print the remainder to find the last digit

# b = N // 10
# print("Remaining digit",b)            Using floor division Divide it by 10


#   --- Function for Extraction of last digit of any N number one by one ---


# Normal way 
def extraction(N):
    if N == 0:
        return
    last_digit = N % 10
    print(last_digit)
    # N = N // 10            #Remaining digit
    extraction(N // 10)

extraction(1278)




#   --- Using loop to do the same --- 

#Normal way
N = int(input("Enter your lucky no :)"))

while(N > 0):
    last_digit = N % 10
    N = Remaining_digit = N // 10
    print(f"Last digit : {last_digit}")


#   ---- Best way for large N inputs ----
"loading...."




#           *******************************************-X-X-X-X-X-X-X-X-*******************************************