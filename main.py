import discord
import random
from discord.ext import commands
bot = commands.Bot(intents=discord.Intents.all(), command_prefix="/")



@bot.command("info")
async def command_info(ctx:commands.Context):
    await ctx.send("Я БОТ, который скидывает информацию о природе. Пока я в ранней версией, но буду улучшаться! Команда /help покажит что я умею")




@bot.command("naturprob")
async def command_naturprob(ctx:commands.Context):
    natur = ["К основным экологическим проблемам относятся сокращение озонового слоя", "агрязнение атмосферы не обошло стороной ни одну страну", "Загрязнение почвы происходит регулярно путем утилизации в земле отходов"]
    prob = random.choice(natur)
    await ctx.send(prob)





@bot.command("natur")
async def command_mem(ctx:commands.Context):
    images = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]
    image_names = random.choice(images)
    with open("images/"+image_names, "rb") as file:
        image = discord.File(file)
    await ctx.send("Рандомная картинка о положение земли в будущем )", file=image)
