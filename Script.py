class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝑴𝒀 𝑵𝑨𝑴𝑬 , <a href='https://t.me/{temp.U_NAME}'>ELSA</a>, 𝑰𝒕'𝒔 𝑽𝒆𝒓𝒓𝒚 𝑬𝒂𝒔𝒚. 𝑱𝒖𝒂𝒕 𝑨𝒅𝒅 𝑴𝒆 𝑻𝒐 𝒀𝒐𝒖𝒓 𝑮𝒓𝒐𝒖𝒑 𝑨𝒏𝒅 𝑴𝒂𝒌𝒆 𝑴𝒆 𝑨𝒅𝒎𝒊𝒏, 𝑻𝒉𝒂𝒕𝒔 𝑨𝒍𝒍, 𝑰'𝑳𝑳 𝑷𝒓𝒐𝒗𝒊𝒅𝒆 𝑴𝑶𝑽𝑰𝑬𝑺 𝑻𝒉𝒆𝒓𝒆 🤓
𝑯𝑬𝒀,𝑨𝒅𝒅 𝑴𝒆 𝑻𝒐 𝒀𝒐𝒖𝒓 𝑮𝒓𝒐𝒖𝒑 𝑨𝒏𝒅 𝑴𝒂𝒌𝒆 𝑴𝒆 𝑨𝒏 𝑨𝒅𝒎𝒊𝒏 𝑻𝒉𝒆𝒓𝒆 😉
➖➖➖➖➖➖➖➖➖➖➖➖➖
©️MᴀɪɴᴛᴀɪɴᴇD Bʏ: <a href="https://t.me/Unni0240"> AMAL NATH </a>"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝘏𝘦𝘳𝘦 𝘐𝘴 𝘛𝘩𝘦 𝘏𝘦𝘭𝘱 𝘍𝘰𝘳 𝘔𝘺 𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴."""
    ABOUT_TXT = """
✪ 𝓜𝔂𝓷𝓪𝓶𝓮: <a href="https://t.me/{temp.U_NAME"> ELSA </a>
✪ 𝓒𝓻𝓮𝓪𝓽𝓸𝓻: <a href="https://t.me/unni0240"> AMAL NATH </a>
✪ 𝓛𝓲𝓫𝓻𝓮𝓪𝓻𝓻𝔂: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✪ 𝓛𝓪𝓷𝓰𝓾𝓪𝓰𝓮: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✪ 𝓓𝓪𝓽𝓪 𝓑𝓪𝓼𝓮: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✪ 𝓑𝓸𝓽 𝓼𝓮𝓻𝓿𝓮𝓻: 𝙷𝙴𝚁𝙾𝙺𝚄
✪ 𝓑𝓾𝓲𝓵𝓭 𝓢𝓽𝓪𝓽𝓾𝓼: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- 𝑰 𝒂𝒎 𝒏𝒐𝒕 𝒂 𝒐𝒑𝒆𝒏 𝒔𝒐𝒖𝒓𝒄𝒆 𝒑𝒓𝒐𝒋𝒆𝒄𝒕. 
- 𝑷𝒍𝒆𝒂𝒔𝒆 𝒄𝒐𝒏𝒕𝒂𝒄𝒕𝒔 𝒎𝒚 𝒎𝒂𝒔𝒕𝒆𝒓 𝒇𝒊𝒓 𝒎𝒚 𝒅𝒐𝒖𝒃𝒕𝒔 𝒂𝒏𝒅 𝒄𝒐𝒎𝒑𝒍𝒂𝒏𝒕𝒆𝒔

𝗠𝗔𝗦𝗧𝗘𝗥:
<a href="https://t.me/Unni0240"> Amal </a>  """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1.*This bot* 𝒔𝒉𝒐𝒖𝒍𝒅 𝒉𝒂𝒗𝒆 𝒂𝒅𝒎𝒊𝒏 𝒑𝒓𝒊𝒗𝒊𝒍𝒍𝒂𝒈𝒆.
2. 𝑶𝒏𝒍𝒚 𝒂𝒅𝒎𝒊𝒏𝒔 𝒄𝒂𝒏 𝒂𝒅𝒅 𝒇𝒊𝒍𝒕𝒆𝒓𝒔 𝒊𝒏 𝒂 𝒄𝒉𝒂𝒕.
3. 𝑨𝒍𝒆𝒓𝒕 𝒃𝒖𝒕𝒕𝒐𝒏𝒔 𝒉𝒂𝒗𝒆 𝒂 𝒍𝒊𝒎𝒊𝒕 𝒐𝒇 64 𝒄𝒉𝒂𝒓𝒆𝒄𝒕𝒆𝒓𝒔.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- This bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Elsa supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/ElsaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of elsa

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """✪ 𝑻𝒐𝒕𝒂𝒍 𝒇𝒊𝒍𝒆𝒔: <code>{}</code>
✪ 𝑻𝒐𝒕𝒂𝒍 𝑼𝒔𝒆𝒓𝒔: <code>{}</code>
✪ 𝑻𝒐𝒕𝒂𝒍 𝑪𝒉𝒂𝒕𝒔: <code>{}</code>
✪ 𝑼𝒔𝒆𝒅 𝑺𝒕𝒐𝒓𝒂𝒈𝒆: <code>{}</code> 𝙼𝚒𝙱
✪ 𝑭𝒓𝒆𝒆 𝑺𝒕𝒐𝒓𝒂𝒈𝒆: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
