import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
# chrome_options.add_argument('--headless')
# Selenium lädt den passenden chromedriver automatisch. Falls das nicht klappt, chromedriver manuell laden: https://googlechromelabs.github.io/chrome-for-testing/
#service = Service('chromedriver.exe')   # Mac/Linux: Service('chromedriver')
#driver = webdriver.Chrome(service=service, options=chrome_options)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.nytimes.com/search?dropmab=false&endDate=2024-11-01&lang=en&query=&sort=best&startDate=2024-10-01')

time.sleep(10)

# Cookie-Overlay entfernen (falls vorhanden)
for overlay in driver.find_elements(By.CSS_SELECTOR, 'div#fides-overlay'):
    driver.execute_script("arguments[0].style.display='none';", overlay)

# Scroll-Sperre aufheben
driver.execute_script("document.body.classList.remove('fides-no-scroll');")

time.sleep(15)

# Mehr anzeigen-Button klicken
for _ in range(5):
    try:
        more_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="search-show-more-button"]')
        more_button.click()
        time.sleep(3)
    except:
        pass 

time.sleep(2)

# Headlines auslesen und ausgeben
# data-testid/data-tpl-Attribute sind stabiler als automatisch erzeugte CSS-Klassen
headlines = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="search-bodega-result"] div[data-tpl="h"]')
print(len(headlines), 'Headlines gefunden')   # 0: Captcha/Bot-Schutz im Browserfenster? Oder Selektor veraltet?
for headline in headlines:
    print(headline.text)

driver.quit()