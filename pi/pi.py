def calculatar_pi(n: int) -> float:
    signo: int = 1
    denominador: float = 1
    numerador: float = 4
    pi: float = 0

    for _ in range(n):
        pi += signo * (numerador / denominador)
        denominador += 2
        signo *= -1
    return pi

if __name__ == "__main__":
    print(calculatar_pi(100000000))