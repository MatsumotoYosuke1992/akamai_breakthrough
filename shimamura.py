# install python and selenium and chorom https://prog-8.com/docs/python-env , https://note.com/yuu________/n/n48b3530b0fe6
# open private browser in chorm https://watlab-blog.com/2019/08/16/selenium-chrome-secretmode/
# To prevent akamai from being judged as a bot system https://www.mussyu1204.com/hp/articles/0114_selenium-akamai, https://qiita.com/yagrush/items/ff069b2741d0f09a6d7f
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --profile-directory="Default"
# confirm http://localhost:9222/json
import time                                 # スリープを使うために必要
from selenium import webdriver              # Webブラウザを自動操作する（python -m pip install selenium)
import chromedriver_binary                  # パスを通すためのコード
from selenium.webdriver.chrome.options import Options # オプションを使うために必要


def main(username, password):
#def main():
    options = Options()                          # オプションを用意
    options.add_argument('--incognito')          # シークレットモードの設定を付与
    options.add_experimental_option('excludeSwitches', ["enable-automation"])
    options.add_argument('–user-agent=' + 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36')
    options.add_argument('--remote-debugging-port=9222')

    driver = webdriver.Chrome(options = options)   # Chromeを準備(optionでシークレットモードにしている）

    # WebサイトのURLを指定
    url = 'https://auth.shop-shimamura.com/login'
    driver.get(url)       # Googleを開く


    time.sleep(2)

    elem_username  = driver.find_element_by_name('username')
    elem_username.send_keys(username)
    time.sleep(2)

    elem_password = driver.find_element_by_name('password')
    elem_password.send_keys(password)

    time.sleep(2)

    driver.find_element_by_class_name('send-btn').click()

    driver.get('https://www.member.shop-shimamura.com/mypage?brand=avail')
    time.sleep(1)
    driver.get('https://www.member.shop-shimamura.com/mypage?brand=chambre')
    time.sleep(1000)
    driver.get('https://www.member.shop-shimamura.com/mypage?brand=birthday')


username_password_list = [
    ['XXXXXXXXXX@yahoo.co.jp','Passs']
]

for username_password in username_password_list:
    main(username_password[0],username_password[1])


