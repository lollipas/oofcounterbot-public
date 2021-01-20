
import discord
import json


client = discord.Client()
d = {}
with open('ooflist.json') as f:
    data = json.load(f)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='Counting your oofs 😳 🐒'))

@client.event
async def on_message(message):   
    
    username = message.author.name
    userid = message.author.id
    bot_id = 'id'
    
    message.content = message.content.lower().replace(' ', '')
    if str(userid) != str(bot_id):
        if ('oof') in message.content:        
            members = message.guild.members
            for member in members: 
                data[member.name] = data[member.name]
                
            data[username] = data[username] + 1
            with open('ooflist.json', "w")  as f:   
                json.dump(data,f,indent=2)
            
    if message.content.startswith('!count'):
        await message.channel.send(f"{username} has said oof {data[username]} times.")
    
    if message.content.startswith('!lb'):
        embed = discord.Embed(title='Current OOF leaderboard', description='I am sentient now 😳')
        
        
        sorted_values = []
        for key, value in data.items():
            keys = []
            values = []
            keys.append(key)
            values.append(value)
            sorted_values.append(value)
            embed.add_field(name=keys[0], value=f"{values[0]} oofs", inline=False)   
        await message.channel.send(content = None,embed = embed)
        
        
client.run('your token here')


