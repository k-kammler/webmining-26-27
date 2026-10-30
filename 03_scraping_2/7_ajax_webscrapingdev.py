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

# Übungsseite zum Scraping-Lernen: die Bewertungen stehen nicht im HTML, sie werden per AJAX nachgeladen
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://web-scraping.dev/reviews')

time.sleep(5)

# Sanftes Scrollen abschalten, sonst klickt Selenium, während die Seite noch zum Button scrollt
driver.execute_script("document.documentElement.style.scrollBehavior = 'auto';")

# Mehr anzeigen-Button klicken
for _ in range(5):
    try:
        more_button = driver.find_element(By.CSS_SELECTOR, 'button#page-load-more')
        more_button.click()
        time.sleep(3)
    except:
        pass   # sind alle Bewertungen geladen, verschwindet der Button

time.sleep(2)

# Bewertungen auslesen und ausgeben
# data-testid-Attribute sind stabiler als automatisch erzeugte CSS-Klassen
reviews = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="review"] p[data-testid="review-text"]')
print(len(reviews), 'Bewertungen gefunden')   # nur 20: Klicks abgefangen? Oder Selektor veraltet?
for review in reviews:
    print(review.text)

driver.quit()
