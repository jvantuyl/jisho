import asyncio
from pprint import pprint
from jisho import Jisho

async def main():
    pprint(await Jisho().search('かんぱい'))

if __name__ == '__main__':
    asyncio.run(main())
