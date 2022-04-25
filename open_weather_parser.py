import os
import json
from asyncio import run

from aiohttp import ClientSession


token = os.getenv("TOKEN_OPEN_WEATHER")


async def request(url, params):
	async with ClientSession() as session:
		async with session.get(url=url, params=params) as response:
			return await response.json(encoding="UTF-8")


class OpenWeather:
    def __init__(self, token: str):
        self._token = token

    async def get(self, city: str):
        response = await request(
            "http://api.openweathermap.org/data/2.5/weather?", 
            params={"q": city, "lang": "en", "units": "celsius", "appid": self._token}
        )
        return response


weather = OpenWeather(token=token)


async def app():
    piter = await weather.get("Saint Petersburg")
    moscow = await weather.get("Moscow")
    ulan_ude = await weather.get("Ulan-Ude")

    dump = {
        "piter":piter,
        "moscow": moscow,
        "ulan_ude": ulan_ude,
    }

    with open("dump.json", "w") as f:
        json.dump(f, dump)
    
run(app())