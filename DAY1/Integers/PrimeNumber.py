var = int(input("Enter a number"))
prime = [True]
def is_prime(var):
    var1 = range(2, var-1, 1)
    for i in var1:
        if var % i == 0 and var - i != 0:
            prime[0] = False
            break
        continue

is_prime(var)

if prime[0]:
    print("The number is prime")
else:                               
    print("The number is not prime")



