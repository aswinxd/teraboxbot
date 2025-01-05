from pyrogram import Client, filters
import requests

# Replace with your credentials
API_ID = 27589257  # Your Telegram API ID
API_HASH = "0af78b04b48361bc117fa4e06d6d2292"  # Your Telegram API Hash
BOT_TOKEN = "7880005347:AAERpFnNOdD6t2T3Eneytec1ZFtV2Q0kgyc"

# Create a Pyrogram Client
app = Client(
    "terabox_downloader",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

TERABOX_API_URL = "https://teradownloader.com/api/download"

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Welcome to Terabox Downloader Bot! Send a Terabox link to download.")

@app.on_message(filters.text)
async def download_file(client, message):
    terabox_link = message.text

    try:
        # Interact with TeraDownloader or Terabox
        response = requests.post(TERABOX_API_URL, json={"url": terabox_link})
        response.raise_for_status()
        data = response.json()

        if "downloadLink" in data:
            download_link = data["downloadLink"]
            await message.reply(f"Here is your download link:\n{download_link}")
        else:
            await message.reply("Failed to retrieve the download link. Please check the URL.")
    except Exception as e:
        await message.reply(f"An error occurred: {e}")

if __name__ == "__main__":
    app.run()

