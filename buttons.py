print("----------------------------------")
name = "buttons"
print (f"importing for: {name}")
import nextcord, os, os.path, random, time, pickle
print (f"imports done for: {name}, now working on intents")

# intents
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
client = nextcord.Client(intents=intents)
# main file here
def msg_brake(messages):
	idi = int(str(messages[0].content).split(" ")[0][2:-1])

	idi = [idi]
	return idi

async def button_one_test(self, interaction: nextcord.Interaction):
	await interaction.response.send_message(f"head please")


async def verify_finished(self, interaction: nextcord.Interaction, button, client):

	messages = await interaction.channel.history(limit=1, oldest_first=True).flatten()
	id = msg_brake(messages)[0]
	verifiable = 0
	intro = 0
	async for message in interaction.channel.history(limit=None):
		if int(message.author.id) == id:
			verifiable = 1
			break

	if verifiable == 0:
		await interaction.response.send_message("oops! it looks like you may have pressed the button to early thats ok. you got this!👍")
		return 

	intros = client.get_channel(1104444464581320795)

	async for message in intros.history(limit=None):
		if int(message.author.id) == id:
			intro = 1
			break

	if intro == 0:
		await interaction.response.send_message("oops! looks like you havent made an introduntion, please head over to <#798625729502904400> and cheked the pinned message")
		return 

	nex = intro + verifiable
	print (f"intro?{intro} + verifiable?{verifiable} = {nex}")
	if nex == 2:
		if str(interaction.user.id) != str(id):
			temp = await interaction.response.send_message(f"ayyy thats for the person verifying to press")
			return 
		
		if str(interaction.user.id) == str(id):
			await client.get_channel(interaction.channel.id).send("Good job! a staff member will be with you as soon as posible, hold tight!")
			await interaction.channel.edit(name=f"🖐️{interaction.user.name}")
			button.disabled = True
			await interaction.response.edit_message(view=self)
			return

		else:
			await interaction.response.send_message("hold on somethings not right here <@1103489418360275059> please help!")
			return





async def verify_close(self, interaction: nextcord.Interaction, button, client):

	class check(nextcord.ui.View):
		def __init__(self):
			super().__init__()

			self.add_item(nextcord.ui.Button(label="sure?", style=nextcord.ButtonStyle.danger))
			self.children[0].callback = self.sure


		async def sure(self, interaction: nextcord.Interaction):
			await client.get_channel(interaction.channel.id).delete()
			

	await interaction.response.send_message("are you sure?", view=check())
# main file ends here
print (f"file ready to go. {name} is a GO!\n----------------------------------")