import requests

def animal():
    answer = input("**What animal would you like to see?\n1: Dog\n2: Cat\n3: Panda\n4: Koala\n5: Foxy\n6: Bird\n7: Duck**")

    try:
        if answer == "1":
                request = await session.get(
                    'https://some-random-api.ml/img/dog')
                dogjson = await request.json()
                embed = discord.Embed(
                    title="Doggo!",
                    description=
                    "A random cute doggy to make your day, how adorable <3")
                embed.set_image(url=dogjson['link'])
                await ctx.send(embed=embed)
                return

        if reaction.emoji == "2⃣":
            async with aiohttp.ClientSession() as session:
                request = await session.get(
                    'https://some-random-api.ml/img/cat')
                dogjson = await request.json()
                embed = discord.Embed(
                    title="Kitty!",
                    description=
                    "A random cute kitty to make your day, how adorable <3")
                embed.set_image(url=dogjson['link'])
                await ctx.send(embed=embed)
                return

        if reaction.emoji == "3⃣":
          embed = discord.Embed(title="**What type of panda would you like to see?**")
          embed.add_field(name="Choices:", value="1: Normal Panda\n2: Red Panda")
          msg = await ctx.channel.send(embed=embed)
          await msg.add_reaction("1⃣")
          await msg.add_reaction("2⃣")

          try:
            reaction, user = await bot.wait_for(
            "reaction_add",
            check=lambda reaction, user: user == ctx.author and reaction.emoji
            in ["1⃣", "2⃣"],
            timeout=30.0)

          except asyncio.TimeoutError:
            await ctx.send("Timed out")
            return

          else:
            if reaction.emoji == "1⃣":
              async with aiohttp.ClientSession() as session:
                request = await session.get(
                    'https://some-random-api.ml/img/panda')
                dogjson = await request.json()
                embed = discord.Embed(
                    title="Pandy!",
                    description=
                    "A random cute panda to make your day, how adorable <3")
                embed.set_image(url=dogjson['link'])
                await ctx.send(embed=embed)
                return

            else:
              async with aiohttp.ClientSession() as session:
                request = await session.get(
                    'https://some-random-api.ml/img/red_panda')
                dogjson = await request.json()
                embed = discord.Embed(
                    title="Red Pandy!",
                    description=
                    "A random cute red panda to make your day, how adorable <3")
                embed.set_image(url=dogjson['link'])
                await ctx.send(embed=embed)
                return

        if reaction.emoji == "4️⃣":
            async with aiohttp.ClientSession() as session:
                request = await session.get(
                    'https://some-random-api.ml/img/koala')
                dogjson = await request.json()
                embed = discord.Embed(
                    title="Koala!",
                    description=
                    "A random cute koala to make your day, how adorable <3")
                embed.set_image(url=dogjson['link'])
                await ctx.send(embed=embed)
                return

        if reaction.emoji == "5️⃣":
            async with aiohttp.ClientSession() as session:
                request = await session.get(
                    'https://some-random-api.ml/img/fox')
                dogjson = await request.json()
                embed = discord.Embed(
                    title="Foxy!",
                    description=
                    "A random cute lil fox to make your day, how adorable <3")
                embed.set_image(url=dogjson['link'])
                await ctx.send(embed=embed)
                return

        else:
            async with aiohttp.ClientSession() as session:
                request = await session.get(
                    'https://some-random-api.ml/img/bird')
                dogjson = await request.json()
                embed = discord.Embed(
                    title="Birdy!",
                    description=
                    "A random cute bird to make your day, how adorable <3")
                embed.set_image(url=dogjson['link'])
                await ctx.send(embed=embed)
                return
            
    except asyncio.TimeoutError:
        await ctx.send("Timed out")
        return