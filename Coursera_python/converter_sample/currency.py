from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get(f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}")  # Использовать переданный requests
    soup = BeautifulSoup(response.content, 'xml')

    if cur_from != 'RUR':
        val_1 = soup.find('CharCode', text=cur_from).find_next_sibling('Value').string
        nominal_1 = soup.find('CharCode', text=cur_from).find_next_sibling('Nominal').string
        val_1 = val_1.replace(',', '.')

    if cur_to != 'RUR':
        val_2 = soup.find('CharCode', text=cur_to).find_next_sibling('Value').string
        nominal_2 = soup.find('CharCode', text=cur_to).find_next_sibling('Nominal').string
        val_2 = val_2.replace(',', '.')

    if cur_from == 'RUR':
        result = Decimal(amount) / Decimal(val_2) * Decimal(nominal_2)
    elif cur_to == 'RUR':
        result = Decimal(amount) * Decimal(val_1) / Decimal(nominal_1)
    else:
        result = (Decimal(amount) * Decimal(val_1) / Decimal(nominal_1)) / Decimal(val_2) * Decimal(nominal_2)

    return result.quantize(Decimal("1.0000"))  # не забыть про округление до 4х знаков после запятой
