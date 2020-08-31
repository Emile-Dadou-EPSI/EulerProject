# Project Euler problem 3 : Largest prime factor
# What is the largest prime factor of the number 600851475143


def largestPrimeFactor(n):
    largest_prime = None

    for i in range(2, n):
        while n % i == 0:
            largest_prime = i
            n //= i
        
        if n == 1:
            return largest_prime
        
    if n > 1:
        return n

def main():
    print(">> Problem 3 started :")
    lpf = largestPrimeFactor(600851475143)
    print(lpf)

if __name__ == "__main__":
    main()

