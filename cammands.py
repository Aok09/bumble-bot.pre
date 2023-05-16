print("----------------------------------")
name = "cammands"
print (f"importing for: {name}")
import nextcord, os, os.path, random, time, pickle, importlib, asyncio
from nextcord.ui import TextInput
from io import BytesIO
from nextcord.ui import Button 
from nextcord import ui

print (f"imports done for: {name}, now working on intents")

# intents
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

# main file here
print (f"{name} is grabbing needed py files")
import helping_around, verifying, user_data, buttons
print ("files grabbed")

async def cammands(message, client, testers, prefix):

	cammand = f"{prefix}joining"
	if message.content.startswith(cammand):
		importlib.reload(helping_around)
		helping_around.joining(member, client)

	cammand = f"{prefix}leaving"
	if message.content.startswith(cammand):
		print ("we be leaving")
		async def simulate_member_join_leave(self):
			importlib.reload(helping_around)
			helping_around.leaving(member, client)


	cammand = f"{prefix}verify"
	if message.content.startswith(cammand):
		
		importlib.reload(verifying)


		print ("verifying")
		id = message.content[3 + len(f"{prefix}verify"):][:-1] # cuts off the len of command + 3 for: " <@" and the ">" at the end

		if id == "": # checks if the user was pining someone to open a ticket for 
			id = message.author.id

		else:
			roles = [role.id for role in message.author.roles] # creates a list of rile ids the euser has
			if 1103652510264197130 in roles: # checks the user has the correct role
				id = int(id)

			else: # if the user dosnt have the correct role
				await message.channel.trigger_typing()
				await asyncio.sleep(.5)
				await message.channel.send("sorry you dont have permsion to open a ticket for someone else")
				await message.channel.trigger_typing()
				await asyncio.sleep(2)
				await message.channel.send("if you think this was a mistake then please content a staff member")
				return


		await verifying.verify(id, message.guild.id, client) # the passed id is depned on the input 


	cammand = f"{prefix}vtc"
	if message.content.startswith(cammand):

		roles = [role.id for role in message.author.roles]
		if 1103652510264197130 in roles:
			importlib.reload(verifying)

			hold = str(message.content)[len(cammand):]
			hold = int(str(hold)[3:-1])
			hold = f"{round(float(str(hold*2/5)[:6]), 6)}"



			messages = await message.channel.history(limit=1, oldest_first=True).flatten() # gets cheks
			fallback = verifying.idi(messages) # converts them into something usable
			passby = f"{round(float(str(fallback[0]*2/5)[:6]), 6)}" # reacreates the users number

			print (hold, passby)
			if hold == passby:
				print ("ingus")
			

	if message.content == "<@1103489418360275059>":
		await message.channel.send("<@975016627747840020> loves <@519240996987600900> btw")




	if message.content.startswith(f"{prefix}help"):

		importlib.reload(helping_around)

		a = "user"
		await helping_around.help(client,message, prefix, a)




	cammand = f"{prefix}b"
	if message.content.startswith(cammand):
		class MyButton1(nextcord.ui.View):



			@nextcord.ui.button(label="Button 1", style=nextcord.ButtonStyle.primary)
			async def first_button_callback(self, button, interaction):
				button.disabled = True

				await client.get_channel(interaction.channel.id).send("You pressed me!")
				await interaction.response.edit_message(content="You took too long! Disabled all the components.", view=self)
				

			@nextcord.ui.button(label="Button 2", style=nextcord.ButtonStyle.primary)
			async def second_button_callback(self, button, interaction):
				await interaction.response.send_message("You pressed me!")




		message = await message.channel.send("Click the button!", view=MyButton1())








	cammand = f"{prefix}vom_gather"
	if message.content.startswith(cammand):  # checks if the message starts with ".gather"
		await message.delete()  # deletes the message that triggered the command

			
		members = client.get_guild(message.guild.id).members  # gets all members from the guild where the message was sent
		
		await client.get_channel(1092846715859644416).send(f"------------------------------\nfrom server:{message.guild.name}")  # sends a message to a specific channel
		
		count = 0  

		for member in members:  # loops through all the members
			
			count += 1 
			print(count)  


			await message.send(f"{bradcast}{member.name}#{member.discriminator} ~ {count}") # logs all the users and saves eachone on a new line


		await client.get_channel(1092846715859644416).send(f"member count:{count}")  # sends a message to a specific channel with the member count
		

	cammand = f"{prefix}vom_roles"
	if message.content.startswith(cammand):
		await message.delete()
		guild = client.guilds[0]  # get the first guild the bot is a member of
		roles = guild.roles
		for role in roles:
			print(f"{role.name} ~ {role.id}")

	cammand = f"{prefix}ddm"
	if message.content.startswith(cammand):

		class ddm(nextcord.ui.View):
			options = [
				nextcord.SelectOption(label="1a", description="1b", value="1c"),
				nextcord.SelectOption(label="2a", description="2b", value="2c"),
				nextcord.SelectOption(label="3a", description="3b", value="3c"),
				nextcord.SelectOption(label="4a", description="4b", value="4c"),
			]

			def __init__(self):
				super().__init__(timeout=600)
				self.dropdown = nextcord.ui.Select(placeholder='placeholder1', options=self.options)

			@nextcord.ui.select(placeholder="placeholder2", options=options)
			async def dropdown_callback(self, select, interaction):
				selected_option = select.values[0]
				selected_label = None
				for option in self.options:
					if option.value == selected_option:
						selected_label = option.label
						break
				await interaction.response.send_message(f"You selected: {selected_label}")




		view = ddm()
		embed = nextcord.Embed(title="title", description='embed description')
		message = await message.channel.send(embed=embed, view=view)



	cammand = f"{prefix}intro"
	if message.content.startswith(cammand):
		print ("sent")
		import settings
		channel = message.channel.id
		await channel.send(f"{settings.intro}")

	cammand = f"{prefix}old"
	if message.content.startswith(cammand):
		channel = client.get_channel(message.channel.id)
		messages = await channel.history(limit=1, oldest_first=True).flatten()
		first_message = messages[0]
		await message.channel.send(first_message.content[2:-1])


	cammand = f"{prefix}max"
	if message.content.startswith(cammand):
		number = 0
		
		for channel in message.guild.channels:
			start_time = time.monotonic()

			if isinstance(channel, nextcord.TextChannel):
				async for message in channel.history(limit=None):
					print (f"{message.author.name}#{message.author.discriminator} ~~ {message.author.id}\n{message.content}")
					number += 1
					await user_data.log(message, client)

		
			elapsed_time = time.monotonic() - start_time
			if elapsed_time < 0.5:
				time.sleep(0.5 - elapsed_time)
				print (elapsed_time)

			start_time = time.monotonic()
			print (number)



	cammand = f"{prefix}first"
	if message.content.startswith(cammand):
		here = client.get_guild(1103066534978539624)
		for channel in here.channels:
			if isinstance(channel, nextcord.TextChannel):

				async for message in channel.history(limit=1):
					print(f"Content of the first message in {channel.name}: {message.content}")


	cammand = f"{prefix}del"
	if message.content.startswith(cammand):
		server = client.get_guild(message.guild.id)

		channels = server.text_channels
		probing = []
		for channel in channels:
			chan = await channel.send("this is a test")

			if chan.channel.id == 1107767901370462208:
				print ("not this one")
				await chan.delete()
				if message.channel.id == 1107767901370462208:
					await message.delete()

			else:
				probing.append(chan.channel.id)
				print (chan.channel.id)

		print (probing)

		for id in probing:


			if id == 1107767901370462208:
				print ("not this one")
				
			else:
				await client.get_channel(id).delete()
				print (f"channel: {id} is gone")

		await server.create_text_channel(name="oggers")
		await server.create_text_channel(name="rpg-tests")




	cammand = f"{prefix}bung"
	if message.content.startswith(cammand):


		# Check roles of the message author
		roles = [role.id for role in message.author.roles]
		if 1103652510264197130 in roles:
			print ("YAY!")



	cammand =f"{prefix}dbme"
	if message.content.startswith(cammand):
		print ("oop")

	cammand = f"{prefix}type"
	if message.content.startswith(cammand):
		await message.channel.trigger_typing()



	# this for the clean channal thingy add any channal id to keep it clean
	kept_clean = [1107767901370462208]
	if message.channel.id in kept_clean:
		await message.delete()
		await message.author.send("bro no")
# main file ends here
print (f"file ready to go. {name} is a GO!\n----------------------------------")



