import requests
from bot.management.commands.movies.movies_download.pyrogram_client import app, start_client, stop_client

async def upload_and_get_file_id(file_url):
    await start_client()

    # Faylni yuklab olish
    video_file = requests.get(file_url)
    video_path = "temp_movie.mp4"
    with open(video_path, "wb") as file:
        file.write(video_file.content)

    # Faylni Telegramga yuklash va `file_id` olish
    response = await app.send_video(
        chat_id="your_chat_id",  # Bu yerda haqiqiy chat_id kiritilishi kerak
        video=video_path
    )

    await stop_client()
    return response.video.file_id
