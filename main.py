import aiohttp
import asyncio
import time

start_time = time.time()


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name']


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            # Permite ejecutar una corrutina en backbround
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        # Esperar a que todas las tareas finalicen y devuelva un iterable
        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))