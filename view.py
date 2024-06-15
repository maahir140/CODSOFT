import asyncio
import aiofiles
import csv

async def add(i):
    async with aiofiles.open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(await file.__anext__())
        await asyncio.to_thread(writer.writerow, i)

async def view():
    data = []
    async with aiofiles.open('data.csv', 'r') as file:
        reader = csv.reader(await file.__anext__())
        async for row in reader:
            data.append(row)
    print(data)
    return data

async def remove(i):
    async def save(j):
        async with aiofiles.open('data.csv', 'w', newline='') as file:
            writer = csv.writer(await file.__anext__())
            await asyncio.to_thread(writer.writerows, j)

    new_list = []
    telephone = i

    async with aiofiles.open('data.csv', 'r') as file:
        reader = csv.reader(await file.__anext__())
        async for row in reader:
            new_list.append(row)
            for element in row:
                if element == telephone:
                    new_list.remove(row)
    await save(new_list)

async def update(i):
    async def update_newlist(j):
        async with aiofiles.open('data.csv', 'w', newline='') as file:
            writer = csv.writer(await file.__anext__())
            await asyncio.to_thread(writer.writerows, j)

    new_list = []
    telephone = i[0]

    async with aiofiles.open('data.csv', 'r') as file:
        reader = csv.reader(await file.__anext__())
        async for row in reader:
            new_list.append(row)
            for element in row:
                if element == telephone:
                    name = i[1]
                    gender = i[2]
                    telephone = i[3]
                    email = i[4]
                    
                    data = [name, gender, telephone, email]
                    index = new_list.index(row)
                    new_list[index] = data

    await update_newlist(new_list)

async def search(i):
    data = []
    telephone = i

    async with aiofiles.open('data.csv', 'r') as file:
        reader = csv.reader(await file.__anext__())
        async for row in reader:
            for element in row:
                if element == telephone:
                    data.append(row)
    print(data)
    return data
