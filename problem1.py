## Euler Project problem 1 :
## If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
## The sum of these multiples is 23.
## Find the sum of all the multiples of 3 and 5 below 1000.

def findMultiples(nbMax):
    res = 0
    for x in range(nbMax):
        if x % 3 == 0 or x % 5 == 0:
            res = res + x
    return res

def main():
    print("Start problem 1 : \n")
    res = findMultiples(1000)
    print(res)

if __name__ == "__main__":
    main()
