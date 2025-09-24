import time

import fineio
from finesql import sqlify


def do_sync_work(name: str):
    time.sleep(1)
    return f"Hello, {name}"


async def main():
    message = await sqlify(do_sync_work)(name="World")
    print(message)


fineio.run(main)
