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
async def get_download_link(client, message):
    terabox_url = message.text.strip()

    try:
        # Step 1: Access the initial page and fetch redirection URL
        response = requests.get(terabox_url, allow_redirects=False)
        if "Location" in response.headers:
            redirect_url = response.headers["Location"]
            
            # Step 2: Follow the redirect to get the final video URL
            final_response = requests.get(redirect_url, allow_redirects=True)
            
            # Log or inspect the content
            print("Final URL:", final_response.url)
            
            if final_response.ok and "filename" in final_response.url:
                await message.reply(f"Here is your download link:\n{final_response.url}")
            else:
                await message.reply("Failed to extract the download link. Please check the URL.")
        else:
            await message.reply("Unable to fetch redirection link. Please ensure the URL is valid.")
    except Exception as e:
        await message.reply(f"An error occurred: {e}")

if __name__ == "__main__":
    app.run()