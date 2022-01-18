from bs4 import BeautifulSoup
import requests
import schedule

<<<<<<< HEAD
from constantes import BTC
#TOKEN 
=======
TOKEN #Agregamos el Token
>>>>>>> 427f2ff62394bb19bbc5d0ec25bb03ff5cf3689e
chatId = '1442996092'

#<td class="wbreak_word align-middle coin_price">$60,832.60</td>

def btc_scrapping():
    url_bitcoin = 'https://awebanalysis.com/es/coin-details/bitcoin/'
    url = requests.get(url_bitcoin)
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class' : 'coin_price'})
    format_result = result.text
    #print(format_result)

    return format_result

#https://api.telegram.org/bot2071545023:AAHdU-bdQ285L4YYU4HpZ6NvUJhZ3Q908gA/getUpdates

def bot_send_text(bot_message):
    send_text = 'https://api.telegram.org/bot' + BTC + '/sendMessage?chat_id=' + chatId + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    return response

#test_bot = bot_send_text('/start')
#print(test_bot)

def report():
    btc_price = f'El precio del Bitcoin es de {btc_scrapping()}'
    bot_send_text(btc_price)

if __name__ == '__main__':

    schedule.every().day.at("18:22").do(report)

    while True:
<<<<<<< HEAD

        schedule.run_pending()
=======
        
        schedule.run_pending()
>>>>>>> 427f2ff62394bb19bbc5d0ec25bb03ff5cf3689e
