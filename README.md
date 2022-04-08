<center><img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=TY BOT&fontSize=80&fontAlignY=35&animation=twinkling&fontColor=gradient" /></center>

# 🧩| FEATURES
- [x] moderation
- [x] avatar
- [x] github information
- [x] leveling
- [x] Fun games like tictaktoe
- [x] wikipedia
- [x] google search
- [x] anime
- [x] tag system
- [x] welcoming system
- [x] trolling

# ⚙️| SETUP
### SELF HOSTING
First of all fill all the details in `config/botconfig.json`

```json
{
    "token" : "Your_BOT_token_goes_here",
    "prefix" : "Enter anything here bcz bot only run slash command",
    "database_url" : "POSTGRES database URL get it from HEROKU",
    "welcomeWebhookUrl" : "Welcoming welcomeWebhookUrl"
}
```
Then fill the details in `config/guilds.json`
```json
{
    "guilds":
        [
            Your_guild_id_here
        ],
    "modRole":"Role ID of MOD here of your server",
    "mutedRole":"Muted Role ID here"

    
}
```
Then Run `main.py`

### NOTE
make sure to install the following packages also using `pip install <package_name>` 
<br>e.g. - `pip install py-cord==2.0.0b5`
```txt
py-cord==2.0.0b5
easy-pil==0.0.9
asyncpg
flask
urllib3
wikipedia
```
### REPL.IT
The support for repl.it is also there for the BOT. Just go on repl and while creating the repl do `import from github` and paste this link there 
```
https://github.com/typhonshambo/TY-BOT-v3
```

make sure to fill up the BOT configs in `config/botconfig.json` and `config/guilds.json`

### Heroku 
A saperate branch for has been made for heroku [click here](https://github.com/typhonshambo/TY-BOT-v3/tree/heroku) to go there. Just download the code and push it in heroku all the dependencies are already setup.

`Config Vars`
```
token=Discord Bot token
database_url=PostGres Database url
welcomeWebhookUrl=Webhook URL for Welcoming
prefix=Put any value you want
```
<img src="https://i.imgur.com/UivSvkf.png" width=500>

# ❓| HAVE ANY QUESTION?
join our discord server and ping me in chat, i will be happy to help you out :D

[![Support Server](https://discord.com/api/guilds/556197206147727391/widget.png?style=banner2)](https://discord.gg/m5mSyTV7RR)

# 🙌| SUPPORT
- [x] Follow my github profile
- [x] Join our discord Server
- [x] Star this Repository