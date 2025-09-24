import time

import fineio


def do_sync_work(name: str):
    time.sleep(1)
    return f"Hello, {name}"


async def main():
    message = do_sync_work(name="World")
    print(message)


fineio.run(main)
