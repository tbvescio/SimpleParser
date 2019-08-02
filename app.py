from bs4 import BeautifulSoup
import requests, smtplib,time, config

def check_price():
    resp = requests.get('https://compragamer.com/producto/joystick_redragon_saturn_g807_pc_ps3_7365?redir=1&nro_max=50')
    soup = BeautifulSoup(resp.text,features="html.parser")
    #elemento html que parsea
    price= soup.find('div', {'class':'precioEspecial col-sm-3 col-xs-5'}).get_text()
    return price

def send_email():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(config.username, config.password_mail)
    server.sendmail("pythonscript640@gmail.com", 
                    config.mail, #dirrecion a la que manda
                    "THE PRICE IS LOWER!\n")
    server.quit()
    return True
def main():
    aux  =""
    while True:
        
        if check_price() != aux:
            send_email()
        aux = check_price()
        time.sleep(7200) #espera dos horas

if __name__ == "__main__":
    main()
