#!/usr/bin/env python3
#0-asy.py

import asyncio

async def count():
    print("Haruna")
    await asyncio.sleep(1)
    print("Zakaria")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed  in {elapsed:02f} seconds.")
