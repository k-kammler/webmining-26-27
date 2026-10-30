# Web Mining und Datenvisualisierung – Codebeispiele

Codebeispiele zur Vorlesung **Web Mining und Datenvisualisierung** (JGU Mainz, Wintersemester 2026/27).
Die Ordner sind in der Reihenfolge nummeriert, in der die Themen in der Vorlesung behandelt werden.

| Ordner | Thema | Folien |
|---|---|---|
| [01_python_intro](01_python_intro) | Python-Einführung: Variablen, Schleifen, Listen, Funktionen, Dateien, Pandas | 59 |
| [02_scraping_1](02_scraping_1) | Web-Scraping I: Requests, CSS-Selektoren, Textextraktion (newspaper3k, boilerpy3) | 76–93 |
| [03_scraping_2](03_scraping_2) | Web-Scraping II: User Agent, Throttling, robots.txt, AJAX mit Selenium | 94–117 |
| [04_crawling_code](04_crawling_code) | Web-Crawling: Scrapy, NLTK (Tokens, N-Gramme) | 118–154 |
| [05_api_examples](05_api_examples) | APIs: JSON und XML lesen, REST-Service mit Flask, Requests | 155–195 |
| [06_llm_examples](06_llm_examples) | Große Sprachmodelle: KI-Chat der JGU über die API ansprechen | 253–294 |
| [07_plots_examples](07_plots_examples) | Datenvisualisierung: Balken-, Kreis-, Linien-, Streudiagramm, Boxplot, Heatmap, Netzwerk, Sankey, Treemap, Landkarte, Streamlit | 313–350 |

## Einrichtung

Virtual Environment anlegen und aktivieren (siehe Folie 56):

```bash
# Windows
python -m venv mein_env
mein_env\Scripts\activate

# Mac / Linux
python3 -m venv mein_env
source mein_env/bin/activate
```

Alle benötigten Pakete installieren:

```bash
pip install -r requirements.txt
```

Die Skripte am besten aus dem jeweiligen Ordner heraus starten, damit Dateien wie `gehalt.csv` oder `test.html` gefunden werden:

```bash
cd 01_python_intro
python 1_variablen.py
```

## Hinweise zu einzelnen Beispielen

- **01_python_intro/12_argv.py** erwartet zwei Zahlen als Argumente: `python 12_argv.py 3 9`
- **02_scraping_1/7_extract_mac.py** ist eine Variante von `6_extract.py` für Macs, auf denen der SSL-Zertifikatsfehler auftritt.
- **03_scraping_2** (Selenium): Google Chrome muss installiert sein.
- **04_crawling_code**: Die Scrapy-Spider werden mit `scrapy runspider example_crawler_1.py -o quotes.json` gestartet. Für `nlp_example.py` beim ersten Start die beiden `nltk.download(...)`-Zeilen einkommentieren.
- **05_api_examples**: Zuerst `python flask_example.py` starten (läuft auf `http://127.0.0.1:5000`), dann in einem zweiten Terminal `python requests_example.py` ausführen.
- **06_llm_examples**: Einen API-Key unter [ki-chat.uni-mainz.de](https://ki-chat.uni-mainz.de) erzeugen und statt `YOUR_API_KEY_HERE` eintragen. Den eigenen Key bitte nie committen.
- **07_plots_examples/gui_example.py** wird mit `streamlit run gui_example.py` gestartet.
