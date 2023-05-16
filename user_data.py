print("----------------------------------")
name = "user data"
print (f"importing for: {name}")
import nextcord, os, os.path, random, time, pickle
print (f"imports done for: {name}, now working on intents")

# intents
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

# main file here

async def log(message, client):
	user_id = message.author.id
	username = message.author.name
	username_hash = message.author.discriminator


	guild = client.get_guild(1103066534978539624)
	channels = guild.channels
	for channel in channels: 

		
		channels = guild.channels
		for channel in channels:
			if str(channel.name) == str(message.author.id):
				# print (f"oh shit {channel.name} is the one")

				messages = await channel.history(limit=1, oldest_first=True).flatten()
				fm = messages[0]
				cont = user_id
				# print (cont, fm.content)
				fm = str(fm.content).split(" ")
				# print (f"{fm[0]}, {fm[1]}, {fm[2]}")
				await client.get_channel(int(fm[0])).send(f"{message.id} | {message.channel.id} ~ content: {message.content}")
				await client.get_channel(int(fm[1])).send(f"{message}")


				return

			else:
				print (channel.name)




	channel = await guild.create_text_channel(name=user_id)
	cont = await channel.create_thread(name="content")
	prof = await channel.create_thread(name="profile")

	await channel.send(f"{channel.id} {cont.id} {prof.id}")
	await channel.send(f"{username}#{username_hash}")
# main file ends here
print (f"file ready to go. {name} is a GO!\n----------------------------------")