
count = 0
for number in range(2,1000):
    prime, divisor = True, 2

    while prime and divisor ** 2 <= number:
        if number % divisor == 0:
            prime = False
        divisor += 1

    if (prime):
        count +=1
        print(number)


print(f"Prime count is : {count}")



import time
start_time = time.time()
random_prime(1000)
elapsed_time = time.time() - start_time
print(elapsed_time)

n = 923923
s=0
for k in range(1, n):
    if gcd(k,n) == 1:
        s += 1

print(s)