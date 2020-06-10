import discord
import random
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

@client.event
async def on_message(message):
    if message.content == "수아 도움말":
        embed = discord.Embed(title="수아에요!", description="", color=0xFF007F)  # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="명령어", value="수아야/수아야 졸려/수아야 사랑해/씨발/수아는 착하구나/니애미/뀨/자러간다/"
                                          "헤이 수아/수아펀치/귀여워 수아야/수아야 주사위굴려줘", inline=True)
        embed.set_footer(text="")  # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed)  # embed를 포함 한 채로 메시지를 전송합니다.


    if message.content == "수아야":
        await message.channel.send('네!수아에요!')


    if message.content == "수아야 졸려":
            await message.channel.send("어머나..졸린 모습도 귀여우셔라...")

    if message.content == "수아야 사랑해":
        await message.channel.send("수아앗!")

    if message.content == "씨발":
            await message.channel.send("그런말은 쓰지마세요 도련님!")

    if message.content == "수아는 착하구나":
        await message.channel.send("그런말하지마세요 부끄러워요!! 도련님!!")

    if message.content == "니애미":
            await message.channel.send("당신 어머니가 그런말은 가르쳐 주셨나요?")

    if message.content == "뀨":
            await message.channel.send("귀여우셔라...")

    if message.content == "자러간다":
            await message.channel.send(file=discord.File("ㅇㅇ.jpg"))
            await message.channel.send("안녕히 주무세요 도련님")

    if message.content == "헤이 수아":
            await message.channel.send("예스 아임 수아!!")

    if message.content == "수아펀치":
           await message.channel.send("수아~~~펀!!!치!!!!")


    if message.content == "귀여워 수아야":

        await message.channel.send(file=discord.File("보여줘.jpg"))
        await message.channel.send('수아아아앗!')

    if message.content == "수아야 주사위굴려줘":
        a=random.choice(['1이 나왔어요 도련님', '2가 나왔어요 도련님', '3이 나왔어요 도련님', '4가 나왔어요 도련님', '5가 나왔어요 도련님', '6이 나왔어요 도련님'])
        await message.channel.send(a)










access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
