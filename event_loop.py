import asyncio

async def tarea1():
    print("Tarea 1 iniciada")
    await asyncio.sleep(2)
    print("Tarea 1 completada")

async def tarea2():
    print("Tarea 2 iniciada")
    await asyncio.sleep(1)
    print("Tarea 2 completada")

async def main():
    loop = asyncio.get_event_loop()

    # Crear tareas y registrarlas en el event loop
    task1 = loop.create_task(tarea1())
    task2 = loop.create_task(tarea2())

    # Esperar a que todas las tareas finalicen
    await asyncio.gather(task1, task2)

# Crear y ejecutar el event loop manualmente
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()