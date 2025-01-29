from bs4 import BeautifulSoup
import requests
from googletrans import Translator
import asyncio

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print("Произошла ошибка:", e)

async def translate_to_russian(text):
    translator = Translator()
    translation = await translator.translate(text, src='en', dest='ru')
    return translation.text

async def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        russian_word = await translate_to_russian(word)
        russian_definition = await translate_to_russian(word_definition)

        print(f"Значение слова: {russian_definition}")
        user = input("Какое слово загадано?")

        if user.strip().lower() == russian_word.strip().lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {russian_word}")

        play_again = input("Хотите продолжить игру? (да/нет) ")
        if play_again.lower() != "да":
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    asyncio.run(word_game())




