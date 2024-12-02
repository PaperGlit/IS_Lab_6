from primes import Primes


class Console:
    def __init__(self):
        self.main()

    @staticmethod
    def main():
        while True:
            prompt = input("1 - Generate a big prime number\n"
                           "2 - Find all primes in range\n"
                           "3 - Find first 100 primitive roots of a prime\n"
                           "Your choice: ")
            match prompt:
                case "1":
                    try:
                        n = int(input("Enter the amount of bits (n): "))
                        t = int(input("Enter the amount of Rabin-Miller cycles (t): "))
                        prime, iterations, execution_time = Primes.generate_large_prime(n, t)
                        print(f"Found prime: {prime}\n"
                              f"Iterations: {iterations}\n"
                              f"Execution time: {execution_time:.4f} seconds\n")
                    except ValueError:
                        print("Please enter a valid number.")
                case "2":
                    try:
                        start = int(input("Enter the range's start: "))
                        end = int(input("Enter the range's end: "))
                        primes, execution_time = Primes.find_primes_in_range(start, end)
                        print(f"Found primes in range [{start}, {end}]: {primes}\n"
                              f"Execution time: {execution_time:.4f} seconds\n")
                    except ValueError:
                        print("Please enter a valid number.")
                case "3":
                    try:
                        n = int(input("Enter the prime number: "))
                        primitive_roots, execution_time = Primes.find_primitive_roots(n)
                        print(f"Found primitive roots for {n}: {primitive_roots}\n"
                              f"Execution time: {execution_time:.4f} seconds\n")
                    except ValueError:
                        print("Please enter a valid number.")
                case _:
                    return
