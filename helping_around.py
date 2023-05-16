
print("----------------------------------")
name = "helping around"
print (f"importing for: {name}")
import nextcord, os, os.path, random, time, pickle, datetime
print (f"imports done for: {name}, now working on intents")

# intents
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
# main file here

import settings

# user join the server
async def joining(member, client):   
	if member.guild.id == 1103066534978539624:
		# gives the data needed to make the server look nice 
		gifs = {"weclome": ["https://cdn.discordapp.com/attachments/976936075635327086/1092974087560757358/c1.gif", "https://cdn.discordapp.com/attachments/976936075635327086/1092972371146723399/c1.gif"],
				"goodbye": ["https://cdn.discordapp.com/attachments/976936075635327086/1092974720443486218/c1.gif", "https://cdn.discordapp.com/attachments/976936075635327086/1092973605748482200/c1.gif"]}
		channels = {798587674868973648: [798587674868973657],
					1103066534978539624: [1107833476989857912]}
		# selectes the correct channel based on the server
		channel = client.get_channel(channels[member.guild.id][0])

		# sends the message 
		await channel.send(f"welcome {member}, we hope you enjoy your stay at {member.guild.name}")
		await channel.send(f"{random.choice(gifs['weclome'])}")
  
# user leaves the server
async def leaving(member, client):
	if member.guild.id == 1103066534978539624:
		# gives the data needed to make the server look nice 
		gifs = {"weclome": ["https://cdn.discordapp.com/attachments/976936075635327086/1092974087560757358/c1.gif", "https://cdn.discordapp.com/attachments/976936075635327086/1092972371146723399/c1.gif"],
				"goodbye": ["https://cdn.discordapp.com/attachments/976936075635327086/1092974720443486218/c1.gif", "https://cdn.discordapp.com/attachments/976936075635327086/1092973605748482200/c1.gif"]}
		channels = {798587674868973648: [798587674868973657],
					1103066534978539624: [1107833476989857912]}
		# selectes the correct channel based on the server
		channel = client.get_channel(channels[member.guild.id][0])

		# sends the message 
		await channel.send(f"goodbye {member.mention} ||{member.name}||, we hope you had a good stay at {member.guild.name}")
		await channel.send(f"{random.choice(gifs['goodbye'])}")


		category = await client.fetch_channel(1107833476989857912)

		for channel in category.channels:
			print(channel.name)
			messages = await interaction.channel.history(limit=1, oldest_first=True).flatten()
			id = msg_brake(messages)[0]

			if id == member.id:
				await channel.delete()



async def help(client, message, prefix, a):


	#  build an embed 
	embed = nextcord.Embed(title="Help Guide",
						  url="https://example.com",
						  description=settings.help_desk(),
						  colour=0xeba937,
						  timestamp=datetime.datetime.now())

	embed.set_author(name="Huney YoGrrt <3#1375 and baby bee#8991")

	embed.add_field(name="***please note**",
					value="this bot is under development")

	embed.set_image(url="https://cdn.discordapp.com/attachments/976936075635327086/1092180422663880795/Huney_YoGrrt_3_Create_a_banner_image_for_Little_Bumbles_a_Disco_948292ee-ed23-4fec-8a74-59a17e44cf60.png")

	embed.set_thumbnail(url="")
	user = client.get_user(message.author.id)

	embed.set_footer(text=f"{message.author.mention} Enjoy!",
					 icon_url="\n\nhttps://slate.dan.onl/slate.png")


	

	if a == "user":
		await message.add_reaction("<a:pastel_bee:1080606804054122536>")

		if isinstance(message.channel, nextcord.DMChannel): # if the message is from a dm
			x = 1

		else: # if the message is not from dm
			channel = client.get_channel(798587675031371843)

			await channel.send(embed=embed)
			if message.channel.id != 798587675031371843:
				await message.channel.send(f"<@{message.author.id}> please use <#798587675031371843> for doing bot things\nthanks <:gold_star:1080321305821319228>")
	
	
	
	await message.author.send(embed=embed)




# main file ends here
print (f"file ready to go. {name} is a GO!\n----------------------------------")