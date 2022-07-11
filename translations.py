from config import ASSISTANT_NAME
from helpers.bot_utils import BOT_NAME, USERNAME


START_TEXT = f"👋🏻 **Hello**, \n\nThis is **{BOT_NAME}** \nTôi có thể phát trực tuyến cuộc sống, radio, video YouTube & tệp âm thanh / video Telegram trên trò chuyện thoại của nhóm Telegram.  Hãy cùng bạn bè thưởng thức chế độ xem điện ảnh của trình phát video nhóm với bạn bè của bạn  \n\n**Made With ❤️ By @Shabox!** 👑"
HELP_TEXT = f"""
🛠-- **Setting Up Bot**:--

\u2022 Bắt đầu trò chuyện thoại trong nhóm của bạn!!
\u2022 Thêm (@{USERNAME}) & My Assistant (@{ASSISTANT_NAME}) vào nhóm của bạn!
\u2022 Cấp quyền admin (@{USERNAME}) & My Assistant (@{ASSISTANT_NAME}) trong nhóm của bạn!

⚔️-- **Available Commands**:--

\u2022 `/play` - Stream An Audio
\u2022 `/stream` - Stream An Video
\u2022 `/pause` - Pause Current Stream
\u2022 `/resume` - Resume Paused Stream
\u2022 `/endstream` - End Stream & Left VC
\u2022 `/restart` - Restart Bot (Sudo Only)
"""
ABOUT_TEXT = f"💡-- **Information**:-- \n\nThis bot is created for streaming videos in telegram group video chats using several methods from WebRTC. Powered by pytgcalls the async client API for the Telegram Group Calls and Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users and Bots. \n\n**This bot licensed under GNU-GPL 3.0 License!**"
