print("----------------------------------")
name = "template"
print (f"importing for: {name}")
import nextcord, os, os.path, random, time, pickle
print (f"imports done for: {name}, now working on intents")

# intents
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

# main file here

async def reading(message):
	print ("reading faild")





# main file ends here
print (f"file ready to go. {name} is a GO!\n----------------------------------")