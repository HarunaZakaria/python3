#!/usr/bin/env python3
# 1-asy.py.py

import time

def count():
    print("Dauda")
    time.sleep(1)
    print("Soalihu")

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
