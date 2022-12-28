def prime_check(n):

    n=11

    for i in range(2,n):
        if n%i==0:
            print('Not a prime!')

            break

    else:
        print('Prime num')