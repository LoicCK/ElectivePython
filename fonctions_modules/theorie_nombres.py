from controle_execution.controle_premiers import premier

def fermat(n: int) -> int:
    fn = 2**(2**n) + 1
    return fn

def first_non_prime_fermat() -> int:
    n = 1
    while True:
        f_n_non_premier = not premier(fermat(n))[0]
        if f_n_non_premier:
            return n
        n+=1

def next_prime(n: int) -> int:
    if n%2==0:
        n+=1
    else:
        n+=2
    while True:
        n_premier = premier(n)[0]
        if n_premier:
            return n
        n+=2

def couple_prime_after(n: int) -> int:
    while True:
        n = next_prime(n)
        next_n_premier = premier(n+2)[0]
        if next_n_premier:
            return n

def germain_prime_after(n: int) -> int:
    while True:
        n = next_prime(n)
        n_s_g = premier(2 * n + 1)[0]
        if n_s_g:
            return n


def main():
    print(fermat(5))
    print(first_non_prime_fermat())
    print(next_prime(100000))
    print(couple_prime_after(100000))
    print(germain_prime_after(100000))


if __name__ == "__main__":
    main()