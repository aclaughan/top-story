import requests as requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO, filename="app.log")


def main():
    response = requests.get("https://news.ycombinator.com/news").text
    soup = BeautifulSoup(response, "html.parser")

    # logging.debug(soup)

    tags = [tag.getText() for tag in
            soup.find_all(name="a", class_="storylink")]
    hrefs = [tag.get('href') for tag in
             soup.find_all(name="a", class_="storylink")]
    scores = [int(score.getText().replace(' points', '')) for score in
              soup.find_all(name="span", class_="score")]

    max_score = max(scores)
    x = scores.index(max_score)
    print(f"{tags[x]} ({scores[x]})\n{hrefs[x]}")


if __name__ == '__main__':
    main()
