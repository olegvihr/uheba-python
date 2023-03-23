import time


if __name__ == '__main__':

    # start_time = time.time()
    start_time = time.monotonic()
    time.sleep(7)
    print(f"Прошло {time.monotonic() - start_time}")
