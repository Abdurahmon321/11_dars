import asyncio
import time
from colours import colored_print, free_space
import aiohttp


api = "ce49db589f7362fba4b2f1babc7ffb26"


async def weather(city):
    parametrs = {
        "q": city,
        "appid": api,
        "units": "metric"
    }

    url = "https://api.openweathermap.org/data/2.5/weather?"
    try:
        async with (aiohttp.ClientSession() as session):
            async with session.get(url, params=parametrs) as response:
                res = await response.json()
                city_name = res["name"]
                temp = res["main"]["temp"]
                description = res["weather"][0]["description"]
                weather_info = colored_print(f"{city_name} shaxrida hozir havo harorati {temp},", color="blue",
                                             ) + f" Havo: {description} "
                print(weather_info)
    except:
        print(colored_print("bunday shahar yo'q", color="yellow"))


async def main():
    while True:
        free_space()
        city = input(colored_print("Shahar nomini kiriting: ", color="green"))
        if city == "stop":
            print(colored_print("Dastur to'xtatildi", color="red"))
            break
        await weather(city)

start = time.time()

asyncio.run(main())

end = time.time()

print(colored_print(f"Dastur ishlashi uchun ketgan vaqt {round(end-start, 5)}", color="red"))
free_space()

# 2 usul ---------------------------------------------------------------------------------------------

#
# cities = []
#
# while True:
#     city = input("Shahar nomini kiriting: ")
#     if city == "stop":
#         break
#     cities.append(city)
#
#
# async def main(cities):
#     tasks = []
#     for city in cities:
#         task = asyncio.create_task(weather(city))
#         tasks.append(task)
#
#     for task in tasks:
#         await task
#
# asyncio.run(main(cities))
