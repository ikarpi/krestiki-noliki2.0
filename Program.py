from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
    service = Service('path/to/chromedriver')  # Укажите путь к вашему chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def search_wikipedia(query):
    driver.get(f"https://ru.wikipedia.org/wiki/{query}")
    time.sleep(2)  # Ждем загрузки страницы
    return driver


def list_paragraphs():
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')
    for i, paragraph in enumerate(paragraphs):
        print(f"Параграф {i + 1}: {paragraph.text}\n")


def get_links():
    links = driver.find_elements(By.XPATH, '//a[@href and not(contains(@href, ":"))]')
    return links


def main():
    global driver
    driver = init_driver()

    initial_query = input("Введите первоначальный запрос для поиска в Википедии: ")
    search_wikipedia(initial_query)

    while True:
        print("\nЧто вы хотите сделать?")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Выберите действие (1, 2, 3): ")

        if choice == '1':
            list_paragraphs()
        elif choice == '2':
            links = get_links()
            print("Выберите номер статьи для перехода:")
            for i, link in enumerate(links[:5]):  # Ограничиваем до первых 5 ссылок
                print(f"{i + 1}. {link.text} - {link.get_attribute('href')}")
                link_choice = int(input("Введите номер статьи для перехода: ")) - 1

                if 0 <= link_choice < len(links):
                    driver.get(links[link_choice].get_attribute('href'))
                    time.sleep(2)  # Ждем загрузки страницы
                else:
                    print("Неверный выбор.")

            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

        driver.quit()

        if __name__ == "__main__":
            main()