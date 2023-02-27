def print_n_times(value: str, n: int = 10):
    for _ in range(n):
        print(value)


if __name__ == "__main__":
    print_n_times("Hello")
    print_n_times("World", n=2)
