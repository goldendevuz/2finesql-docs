import fineio
import finesql


async def do_work(name: str):
    await fineio.sleep(1)
    print(f"Hello, {name}")


async def get_data():
    async with finesql.create_task_group() as task_group:
        task_group.soonify(do_work)(name="Yury")
        task_group.soonify(do_work)(name="Nathaniel")
        task_group.soonify(do_work)(name="Alex")


async def main():
    await get_data()


fineio.run(main)
