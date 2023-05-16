print("----------------------------------")
name = "verifying "
print (f"importing for: {name}")
import nextcord, os, os.path, random, time, pickle, asyncio, importlib
from nextcord.ui import button
print (f"imports done for: {name}, now working on intents")

# intents
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

# main file here
import settings, buttons 

# grabs the first message at gets the user id from it
def msg_brake(messages):
	idi = int(str(messages[0].content).split(" ")[0][2:-1])

	idi = [idi]
	return idi







async def verify(id, guild, client):

	class nubnigus(nextcord.ui.View):
		@nextcord.ui.button(label="Ready!", style=nextcord.ButtonStyle.primary)
		async def first_button_callback(self, button, interaction):
			importlib.reload(buttons)
			await buttons.verify_finished(self, interaction, button, client)


		@nextcord.ui.button(label="close", style=nextcord.ButtonStyle.danger)
		async def second_button_callback(self, button, interaction):
			importlib.reload(buttons)
			await buttons.verify_close(self, interaction, button, client)








	name = await client.fetch_user(id)
	print (name)

	guild = client.get_guild(guild)

    
	overwrites = {
		guild.default_role: nextcord.PermissionOverwrite(read_messages=False),
		guild.get_role(798587674868973654): nextcord.PermissionOverwrite(read_messages=True), # Queen Bee
		guild.get_role(799619598835122236): nextcord.PermissionOverwrite(read_messages=True), # worker bees
		guild.get_role(798587674868973651): nextcord.PermissionOverwrite(read_messages=True), # bots
		guild.get_role(801464683650744330): nextcord.PermissionOverwrite(read_messages=True), # helper bees
		guild.get_role(801823713988444182): nextcord.PermissionOverwrite(read_messages=True), # Trial Bees
		guild.get_role(798592176854007878): nextcord.PermissionOverwrite(read_messages=True), # New Bees
		guild.get_role(798587674868973652): nextcord.PermissionOverwrite(read_messages=True), # Admin Bees
		guild.get_member(id): nextcord.PermissionOverwrite(read_messages=True)
	}

	channel = await client.get_channel(1079901631572885544).create_text_channel(name=f"verify ~ {name}", overwrites=overwrites)

	# mark = (str(int(time.time() * 1000000000)) + str(random.randint(0, 99999999999999)).zfill(24 - len(str(time.time))))

	
    #await client.get_channel(1103841374618525817).send(f"{id} {mark} ")
	await channel.send(f"<@{id}>") #" {mark}")  




	 
	await channel.send(f"{settings.intro('intro')}\n{settings.intro('fill_me')}")



	await channel.send(f"When you feel happy with your answers, please use press the button (if you press the button early thats ok just carry on) \nthankyou", view=nubnigus())








# main file ends here
print (f"file ready to go. {name} is a GO!\n----------------------------------")