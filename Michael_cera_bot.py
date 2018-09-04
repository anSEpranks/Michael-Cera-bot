import discord

client = discord.Client()

fight_me = ['fight me', 'fight mE', 'fight Me', 'fight ME', 'fighT me', 'fighT mE', 'fighT Me', 'fighT ME', 'figHt me', 'figHt mE', 'figHt Me', 'figHt ME', 'figHT me', 'figHT mE', 'figHT Me', 'figHT ME', 'fiGht me', 'fiGht mE', 'fiGht Me', 'fiGht ME', 'fiGhT me', 'fiGhT mE', 'fiGhT Me', 'fiGhT ME', 'fiGHt me', 'fiGHt mE', 'fiGHt Me', 'fiGHt ME', 'fiGHT me', 'fiGHT mE', 'fiGHT Me', 'fiGHT ME', 'fIght me', 'fIght mE', 'fIght Me', 'fIght ME', 'fIghT me', 'fIghT mE', 'fIghT Me', 'fIghT ME', 'fIgHt me', 'fIgHt mE', 'fIgHt Me', 'fIgHt ME', 'fIgHT me', 'fIgHT mE', 'fIgHT Me', 'fIgHT ME', 'fIGht me', 'fIGht mE', 'fIGht Me', 'fIGht ME', 'fIGhT me', 'fIGhT mE', 'fIGhT Me', 'fIGhT ME', 'fIGHt me', 'fIGHt mE', 'fIGHt Me', 'fIGHt ME', 'fIGHT me', 'fIGHT mE', 'fIGHT Me', 'fIGHT ME', 'Fight me', 'Fight mE', 'Fight Me', 'Fight ME', 'FighT me', 'FighT mE', 'FighT Me', 'FighT ME', 'FigHt me', 'FigHt mE', 'FigHt Me', 'FigHt ME', 'FigHT me', 'FigHT mE', 'FigHT Me', 'FigHT ME', 'FiGht me', 'FiGht mE', 'FiGht Me', 'FiGht ME', 'FiGhT me', 'FiGhT mE', 'FiGhT Me', 'FiGhT ME', 'FiGHt me', 'FiGHt mE', 'FiGHt Me', 'FiGHt ME', 'FiGHT me', 'FiGHT mE', 'FiGHT Me', 'FiGHT ME', 'FIght me', 'FIght mE', 'FIght Me', 'FIght ME', 'FIghT me', 'FIghT mE', 'FIghT Me', 'FIghT ME', 'FIgHt me', 'FIgHt mE', 'FIgHt Me', 'FIgHt ME', 'FIgHT me', 'FIgHT mE', 'FIgHT Me', 'FIgHT ME', 'FIGht me', 'FIGht mE', 'FIGht Me', 'FIGht ME', 'FIGhT me', 'FIGhT mE', 'FIGhT Me', 'FIGhT ME', 'FIGHt me', 'FIGHt mE', 'FIGHt Me', 'FIGHt ME', 'FIGHT me', 'FIGHT mE', 'FIGHT Me', 'FIGHT ME']

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    for text in fight_me:
	    	if message.content.startswith(text):
	        	msg = 'MichaelCera.png'
	        	await client.send_file(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDg2MzgxODQwOTMyOTI5NTM2.Dm-z1A.zCBGUkYR3_uIHz9UJqDB34K5FDU')	