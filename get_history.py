import aiohttp
import asyncio
import calendar
import json
import pathlib


async def fetch_json(url:str)->dict:
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url=url)
        session.close
        if resp.status == 200:
            return await resp.json()
            
        else:
            raise Exception("response not 200")
async def main():
    # Specify the year
    year = 2024
    # Get the number of days in May for the specified year
    days_in_may = calendar.monthrange(year, 5)[1]
    base_path = pathlib.Path(__file__).parent.resolve()

    for i in range(1,days_in_may):
        date = f"202405{i:02}"
        result = await fetch_json(url=f"https://zkillboard.com/api/history/{date}.json")
        # Specify the filename
        filename = f'{base_path}/2024/05/{date}.json'
        # Write JSON data to file
        with open(filename, 'w') as file:
            json.dump(result, file, indent=4)
    

    

asyncio.run(main())