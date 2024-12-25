import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
import asyncio
import logging

# Ваши токены
TELEGRAM_TOKEN = ""
OPENWEATHER_API_KEY = ""
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

# Настроим логирование
logging.basicConfig(level=logging.INFO)

# Создаем экземпляры бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

async def fetch_weather(city: str):
    """Получает информацию о погоде для указанного города через API OpenWeather."""
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "ru",
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(OPENWEATHER_URL, params=params) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None


@dp.message(Command(commands=["start", "help"]))
async def send_welcome(message: Message):
    """Обрабатывает команды /start и /help."""
    await message.reply(
        "Привет! Я погодный бот. Напиши мне название города, и я расскажу тебе о погоде. ☁️\n\n"
        "Пример: Москва"
    )


@dp.message()
async def get_weather(message: Message):
    """Обрабатывает сообщения с названиями городов."""
    city = message.text.strip()
    await message.reply("⏳ Сейчас узнаю погоду, подождите...")

    weather_data = await fetch_weather(city)
    if weather_data:
        city_name = weather_data["name"]
        temp = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        description = weather_data["weather"][0]["description"].capitalize()

        response = (
            f"🌍 Город: {city_name}\n"
            f"🌡️ Температура: {temp}°C (ощущается как {feels_like}°C)\n"
            f"💧 Влажность: {humidity}%\n"
            f"💨 Ветер: {wind_speed} м/с\n"
            f"☁️ Описание: {description}"
        )
    else:
        response = "❌ Не удалось найти информацию о погоде для этого города. Проверьте правильность написания."

    await message.reply(response)


async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
