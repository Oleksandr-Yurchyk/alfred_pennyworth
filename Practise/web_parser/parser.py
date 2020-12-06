from bs4 import BeautifulSoup
from Practise.web_parser.raw_html import html


def _normalize_title(title: str):
    title = title.replace(',', '.')
    return title


def _normalize_price(price: str):
    normal_price = ''
    for character in price:
        if character.isdecimal():
            normal_price += character
        elif character == ',':
            normal_price += '.'
    normal_price += ' грн'
    return normal_price


def parse_html(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    html_results = soup.select('.results-wrapper')

    if html_results:
        html_results = html_results[0]
    else:
        print("Results not found")
        exit(0)

    # delete analogues for the medicament
    for analogue in html_results.select('tbody.analogue'):
        analogue.decompose()

    return tuple(
        (_normalize_title(title.text), _normalize_price(price.text)) for title, price in zip(
            html_results.select('td.col1 .item-title'),
            html_results.select('td.col4 .item-price')
        )
    )


if __name__ == '__main__':
    parse_html(html)
