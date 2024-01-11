import discord
from discord.ext import commands
from imageclass import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Minecraft"))


@bot.event
async def on_ready():
       await bot.change_presence(status=discord.Status.online, activity=discord.Game('Minecraft'))
       print(f'{bot.user} Ok Ok I am here! :) ')


@bot.command()
async def check(ctx):

    if ctx.message.attachments:

        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            img_path = f"img/{file_name}"    
            await attachment.save(img_path)

        class_name, score = get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=img_path)
        await ctx.send(f"Bu bir {class_name.strip()}. Bundan {score}% eminim.")

    

    else: 
        await ctx.send("resim göndermediniz")




bot.run("your token")
