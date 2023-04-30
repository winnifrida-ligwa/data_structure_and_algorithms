def factorize(number):
    """Factorizes an input number into its prime factors."""
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    return factors

if __name__ == "__main__":
    number = 129
    factors = factorize(number)
    print(f"The prime factors of {number} are: {factors}")
