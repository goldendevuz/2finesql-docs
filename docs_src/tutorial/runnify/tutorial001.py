import fineio
import finesql


async def do_work(name: str):
    await fineio.sleep(1)
    return f"Hello, {name}"


async def main(name: str):
    result = await do_work(name=name)
    return result


result = finesql.runnify(main)(name="World")
print(result)
