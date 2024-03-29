import discord
from discord.ext import commands
from ai import feel_ai

intents = discord.Intents.default() 
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def feel(ctx):
    await ctx.send("Добро пожаловать в FeelLab! Здесь вы можете получить рекомендации как улучшить себе настроение (если это понадобится)")
    await ctx.send("Для начала отправьте мне свое фото (на фото не должно быть никого, кроме вас)")
    attachment = ctx.message.attachments[0]
    print(ctx.message.attachments)
    if attachment.filename.endswith(('.png', '.jpeg', '.jpg')):
        await attachment.save(f"image_{ctx.message.author.id}.png")
    else:
        await ctx.message.channel.send("Это не изображение, попробуйте еще раз.")
        return

    result = feel_ai(f"image_{ctx.message.author.id}.png")
    await ctx.message.channel.send(result)

bot.run("MTE4ODg0ODc2MTU5MDUyNjAwMg.GPx_E3.WaIsxH1DqSgmlHmnfYAQAKPjiwtZ3VV_zlUmHQ")