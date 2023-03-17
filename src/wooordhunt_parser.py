import requests
from bs4 import BeautifulSoup


def take_word(word):
    url = requests.get(f"https://wooordhunt.ru/word/{word}")
    resp_check = url.text
    soup = BeautifulSoup(resp_check, "html.parser")
    try:
        translate = soup.find("div", class_="t_inline_en").text
        transcript = soup.find(
            "span",
            class_="transcription",
            title=f"британская транскрипция слова {word}",
        ).text
        return f"{word}{transcript} {translate}"
    except:
        return word


file = open("./words.txt", "r")
words = [i.strip() for i in file.readlines()]
file.close()

file = open("./readywords.txt", "w")
file.close()

file = open("./readywords.txt", "a")
count = 1
notfound = []
for word in words:
    word_info = take_word(word)
    if word_info == word:
        notfound.append(str(count))
    file.write(f"{word_info}\n")
    print(f"{count}. {word_info}")
    count += 1
file.write("\nСледующие номера слов не были найдены:\n")
file.write("\n".join(notfound))
file.close()
