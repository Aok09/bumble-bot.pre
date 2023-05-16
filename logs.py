print("----------------------------------")
name = "logs"
print (f"importing for: {name}")
import nextcord, os, os.path, random, time, pickle, asyncio
print (f"imports done for: {name}, now working on intents")

# intents
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

# main file here
import buttons 

async def save(message, client):
	logging = client.get_guild(1103840675763597435)
	has_log = True

	for channel in logging.channels:
		print(channel.name)

	if has_log == False:
		
		channel = await logging.create_text_channel(name=message.author.id)
		data = await channel.create_thread(name="userdata")
		profile = await channel.create_thread(name="profile")
		messages = await channel.create_thread(name="message log")
		full = await channel.create_thread(name="full msg log")


		await channel.send(f"{data.id} {profile.id} {messages.id} {full.id} .")
		user = await client.fetch_user(message.author.id)

		await message.channel.trigger_typing()
		await asyncio.sleep(3)
		await user.send(f"hay {user.name} iv seen that i dont have a log file for you")
		await message.channel.trigger_typing()
		await asyncio.sleep(4)
		await user.send(f"i have a created a log for your account and ill drop a link in a sec just let me grab one")
		await message.channel.trigger_typing()
		await asyncio.sleep(5)
		await user.send(f"https://discord.gg/nJ4vMmKfA9")
		await message.channel.trigger_typing()
		await asyncio.sleep(3)
		await user.send(f"there you go i hope you dont mind if we log :)")

async def edit(before, after, client):

	print(f"Message edited in {before.channel.name} by {before.author.name}.")
	print(f"Original message: {before.content}")
	print(f"Edited message: {after.content}")

async def deleted(message, client):
	print(f"A message with content '{message.content}' was deleted in channel {message.channel.name}")

# main file ends here
print (f"file ready to go. {name} is a GO!\n----------------------------------")