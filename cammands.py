print("----------------------------------")
name = "cammands"
print (f"importing for: {name}")
import nextcord, os, os.path, random, time, pickle, importlib, asyncio
from nextcord.ui import TextInput
from io import BytesIO
from nextcord.ui import Button 

print (f"imports done for: {name}, now working on intents")

# intents
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

# main file here
print (f"{name} is grabbing needed py files")
import helping_around, verifying, user_data
print ("files grabbed")

async def cammands(message, client, testers, prefix):

	cammand = f"{prefix}verify"
	if message.content.startswith(cammand):
		
		importlib.reload(verifying)


		print ("verifying")
		id = message.content[3 + len(f"{prefix}verify"):][:-1] # cuts off the len of command + 3 for: " <@" and the ">" at the end

		if id == "": # checks if the user was pining someone to open a ticket for 
			id = message.author.id

		else:
			roles = [role.id for role in message.author.roles] # creates a list of rile ids the euser has
			if 1107434078766116975 in roles: # checks the user has the correct role
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



# main file ends here
print (f"file ready to go. {name} is a GO!\n----------------------------------")



