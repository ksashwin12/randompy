def prime_or_not(n):
    number_of_divisors = 0
    for i in range(1,n+1):
        if n%i == 0:
            number_of_divisors+=1
    if number_of_divisors == 2:
        return "Prime"
    else:
        return "Not Prime"
print(prime_or_not(5))