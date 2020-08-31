# Project Euler Problem 4 : Largest palindrom product
# Find the largest palindrom made from the product of two 3-digit numbers.

def getLargestPalindrom():
    n = 0
    for i in range(100, 1000):
        for y in range(100, 1000):
            x = i * y
            if x > n:
                s = str(i * y)
                if s == s[::-1]:
                    n = i * y
    return n

def main():
    print(">> Problem 4 started :")
    res = getLargestPalindrom()
    print(res)

if __name__ == "__main__":
    main()