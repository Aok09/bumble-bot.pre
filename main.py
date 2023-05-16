print("----------------------------------")
name = "main"
print (f"importing for: {name}")
import nextcord, time, pickle, importlib, asyncio, pytz, cammands, main
print (f"imports done for: {name}, now working on intents")

# intents
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

# main file here
import cammands, user_data

async def message(message, client, testers):
	if message.author.bot == 0:




		importlib.reload(cammands)
		importlib.reload(user_data)

		await cammands.cammands(message, client, testers, ".")
		# await user_data.log(message, client)


	print("done")





# main file ends here
print (f"file ready to go. {name} is a GO!\n----------------------------------")