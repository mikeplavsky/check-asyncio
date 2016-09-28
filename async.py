import asyncio

async def check1(l):
    print("Done 1")

    await asyncio.sleep(2,loop=l)

async def check(l):

    print("Done")
    await asyncio.sleep(2,loop=l)

    await check1(l)


def call():
    yield 12
    yield 14

def run_check():

    loop = asyncio.new_event_loop()
    loop.run_until_complete(check(loop))

    loop.close()
