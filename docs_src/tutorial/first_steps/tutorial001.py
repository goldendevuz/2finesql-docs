import fineio


async def do_work(name: str):
    await fineio.sleep(1)
    return f"Hello, {name}"


async def main():
    message = await do_work(name="World")
    return message


result = fineio.run(main)
print(result)
