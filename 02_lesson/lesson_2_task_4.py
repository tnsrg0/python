def fizz_buzz(n):
    for f_b in range(1, n):
        if f_b % 3 == 0 and f_b % 5 == 0:
            print('FizzBuzz')
        elif f_b % 5 == 0:
            print('Buzz')
        elif f_b % 3 == 0:
            print('Fizz')
        else:
            print(f_b)


fizz_buzz(9)
