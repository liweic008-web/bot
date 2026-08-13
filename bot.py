import os
import random
from datetime import datetime
import discord
from discord.ext import commands
import pytz

# 🚨 貼上你想讓法師開示的頻道 ID
CHANNEL_ID = 1537423958696132649  

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# 📜 星雲法師智慧金句庫（可以自由新增修改！）
AORISMS = [
    "存好心，說好話，做好事。",
    "慈悲無敵，智慧無量。",
    "給人信心，給人希望，給人歡喜，給人方便。",
    "心甘情願面對現實，隨緣隨份度過人生。",
    "忍耐不是懦弱，而是懂得包容與化解的勇氣。",
    "做好事是為自己積德，說好話是為自己結緣。",
    "心胸寬廣，天地皆寬；心狹量小，處處碰壁。",
    "人生的財富不一定在於銀行裡的數字，而是在於內心的滿足。",
    "放下不是放棄，而是看破執著後的從容。",
    "心如蓮花不著水，又如日月不拘空。"
]

def get_buddhist_quote():
    # 🎲 隨機抽出一句金句
    quote = random.choice(AORISMS)
    
    tw_tz = pytz.timezone('Asia/Taipei')
    now = datetime.now(tw_tz)

    # 📿 組裝佛系開示排版
    report = f" ═══ 【星雲法師．雲端晨間開示】 ═══ \n"
    report += f" 雲端曆法：{now.strftime('%Y/%m/%d %H:%M')}\n\n"
    report += f"✨ 『 {quote} 』 ✨\n\n"
    report += f"願各位太空居士，今日心無罣礙，事事順心。"
    return report

@bot.event
async def on_ready():
    print(f"【雲端法師】{bot.user} 已上線開光。")
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print(f"【錯誤】找不到頻道 ID：{CHANNEL_ID}")
        await bot.close()
        return

    # 抽籤並發送
    report = get_buddhist_quote()
    await channel.send(report)
    print("【成功】智慧金句已播播，功德圓滿，準備關機。")
    await bot.close()

bot.run(DISCORD_TOKEN)
