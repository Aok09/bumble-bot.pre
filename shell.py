print ("main\nimporting")
import nextcord, time, pickle, importlib, asyncio, pytz, cammands, main
from nextcord import File
from datetime import datetime
print ("finding files")
import helping_around, verifying, user_data
print ("all files found moving to prelanch")

# sets who can use the bot

testers = [519240996987600900, 975016627747840020]



#intents
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

#creates clint object
client = nextcord.Client(intents=intents)

#getting bot info
print ("grabbing bot info")
with open('main/bot.pkl', 'rb') as file:
	bot_info = pickle.load(file)
	file.close()

# bot is ready 
@client.event
async def on_ready():
	print (f"bot started\n" + bot_info["INVITE"])


# on message
@client.event
async def on_message(message):

	importlib.reload(main)

	await main.message(message, client, testers)



@client.event
async def on_member_join(member):

	importlib.reload(helping_around)
	importlib.reload(verifying)

	await helping_around.joining(member, client)
	await verifying.verify(member.id, member.guild.id, client)


@client.event
async def on_member_remove(member):
	
	importlib.reload(helping_around)

	await helping_around.leaving(member, client)


async def send_message():
	await client.wait_until_ready()
	channel = client.get_channel(1061414516438614037) # Replace channel_id with the ID of the channel you want to send the message in
	while not client.is_closed():
		print("loop")
		now = datetime.now(pytz.timezone('US/Eastern'))
		if now.hour == 6 or now.hour == 20:
			message = f"""it is {now.hour} and has Casey<3 had their' meds been "*administered*"?\n|| <@519240996987600900> <@975016627747840020>||"""
			await channel.send(message)
		await asyncio.sleep(120) # checks every 2 min




print ("token running")
client.run(bot_info["TOKEN"])