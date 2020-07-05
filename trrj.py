from seleniumrequests import Firefox
import base64
from PIL import Image
from captcha2upload import CaptchaUpload



captcha_fn = "captcha.png"
driver = Firefox()
#driver.set_page_load_timeout(5);
response = driver.get("http://www4.tjrj.jus.br/consultaProcessoWebV2/consultaProc.do?v=2&FLAGNOME=&back=1&tipoConsulta=publica&numProcesso=2020.002.017258-3")


def get_captcha():
    element = driver.find_element_by_id("imgCaptcha") # element name containing the catcha image
    location = element.location
    size = element.size
    driver.save_screenshot("temp.png")

    x = location['x']
    y = location['y']
    w = size['width']
    h = size['height']
    width = x + w
    height = y + h
    im = Image.open('temp.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(captcha_fn)
    
get_captcha()

captcha = CaptchaUpload("hvxrw69kkdcpfzjt38jtm2bxyzr7ypvn")
captcha_resolved = captcha.solve(captcha_fn)


driver.find_element_by_id("captcha").send_keys(captcha_resolved)
driver.find_element_by_xpath('//*[@id="container_captcha"]/fieldset/table/tbody/tr[2]/td[2]/input').click()




