import time

import fineio
from finesql import sqlify, syncify


async def do_async_work(name: str):
    await fineio.sleep(1)
    return f"Hello, {name}"


def do_sync_work(name: str):
    time.sleep(1)
    message = syncify(do_async_work)(name=name)
    return message


async def main():
    message = await sqlify(do_sync_work)(name="World")
    print(message)


fineio.run(main)
