import asyncio
import io


async def request_manager(n: int) -> str:
    # noinspection PyUnresolvedReferences
    tasks = [asyncio.create_task(send_request()) for _ in range(n)]
    res = io.StringIO()
    for task in tasks:
        res.write(await task)
    return res.getvalue()
