
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