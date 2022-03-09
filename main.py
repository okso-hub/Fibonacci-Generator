def main():

    fibonacci = [0, 1, 1]
    n = int(input("Length of Fibonacci sequence: "))

    for i in range(3, n):
        fibonacci.append(fibonacci[i - 2] + fibonacci[i-1])
    
    print(fibonacci)


if __name__ == "__main__":
    main()
