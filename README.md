# Web Mining und Datenvisualisierung – Codebeispiele

Codebeispiele zur Vorlesung **Web Mining und Datenvisualisierung** (JGU Mainz, Wintersemester 2026/27).
Die Ordner sind in der Reihenfolge nummeriert, in der die Themen in der Vorlesung behandelt werden.

| Ordner | Thema | Folien |
|---|---|---|
| [01_python_intro](01_python_intro) | Python-Einführung: Variablen, Schleifen, Listen, Funktionen, Dateien, Pandas | 59 |
| [02_scraping_1](02_scraping_1) | Web-Scraping I: HTML, Requests, CSS-Selektoren, Textextraktion (newspaper3k, boilerpy3) | 60–93 |
| [03_scraping_2](03_scraping_2) | Web-Scraping II: User Agent, Throttling, robots.txt, AJAX mit Selenium | 94–117 |
| [04_crawling_code](04_crawling_code) | Web-Crawling: Scrapy, NLTK (Tokens, N-Gramme) | 118–154 |
| [05_api_examples](05_api_examples) | APIs: JSON und XML lesen, REST-Service mit Flask, Requests | 155–195 |
| [06_llm_examples](06_llm_examples) | Große Sprachmodelle: KI-Chat der JGU über die API ansprechen | 253–294 |
| [07_plots_examples](07_plots_examples) | Datenvisualisierung: Balken-, Kreis-, Linien-, Streudiagramm, Boxplot, Heatmap, Netzwerk, Sankey, Treemap, Landkarte, Streamlit | 313–350 |

## Einrichtung

Virtual Environment anlegen und aktivieren:

```bash
# Windows
python -m venv mein_env
mein_env\Scripts\activate
# PowerShell meldet "Ausführung von Skripts ... deaktiviert"? Dann einmalig:
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
# (alternativ die Eingabeaufforderung/cmd verwenden)

# Mac / Linux
# Ubuntu/Debian: falls venv fehlt, vorher: sudo apt install python3-venv
python3 -m venv mein_env
source mein_env/bin/activate
```

Alle benötigten Pakete installieren:

```bash
pip install -r requirements.txt
```

Die Skripte am besten aus dem jeweiligen Ordner heraus starten, damit Dateien wie `gehalt.csv` oder `beispiel.txt` gefunden werden:

```bash
cd 01_python_intro
python 1_variablen.py
```

## Hinweise zu einzelnen Beispielen

- **01_python_intro/12_argv.py** erwartet zwei Zahlen als Argumente: `python 12_argv.py 3 9`
- **02_scraping_1/test.html** ist ein einfaches HTML-Grundgerüst (mit `<div>` und `<span>`) zum Öffnen im Browser bzw. in den DevTools.
- **02_scraping_1/7_extract_mac.py** ist eine Variante von `6_extract.py` für Macs, auf denen der SSL-Zertifikatsfehler auftritt.
- **03_scraping_2** (Selenium): Google Chrome muss installiert sein. Die NYT-Beispiele (`4_basic_nyt.py`, `5_ajax_nyt.py`) können vom Bot-Schutz der NYT blockiert werden (Status 403 bzw. Captcha im Browserfenster). Dann später erneut versuchen. `2_throttling.py` läuft ca. 2 Minuten (10 Anfragen mit 5–20 s Pause).
- **04_crawling_code**: Die Scrapy-Spider werden mit `scrapy runspider example_crawler_1.py -O quotes.json` gestartet (großes `-O` überschreibt die Datei; mit kleinem `-o` wird angehängt und die JSON-Datei ist ab dem zweiten Lauf ungültig). `scrapy crawl quotes` funktioniert nur in einem mit `scrapy startproject` angelegten Projekt. Für `nlp_example.py` beim ersten Start die beiden `nltk.download(...)`-Zeilen einkommentieren.
- **05_api_examples**: Zuerst `python flask_example.py` starten (läuft auf `http://127.0.0.1:5000`, beenden mit Strg+C), dann in einem zweiten Terminal (dort ebenfalls das venv aktivieren) `python requests_example.py` ausführen. Neu angelegte Studierende liegen nur im Speicher und sind nach einem Neustart weg. Zum Testen mit curl: `curl -H "Accept: application/json" http://127.0.0.1:5000/students/1`. In der Windows-PowerShell `curl.exe` statt `curl` schreiben: `curl` ist dort ein Alias für `Invoke-WebRequest`, das keinen Accept-Header sendet (Antwort 406 Not Acceptable); alternativ `Invoke-RestMethod -Headers @{Accept="application/json"} http://127.0.0.1:5000/students/1`.
- **06_llm_examples**: Einen API-Key unter [ki-chat.uni-mainz.de](https://ki-chat.uni-mainz.de) erzeugen und im Hauptordner des Repos eine Datei `.env` mit der Zeile `KI_CHAT_API_KEY=...` anlegen (mit einem Texteditor, z.B. VS Code, nicht mit `echo ... > .env` in der Windows-PowerShell, die speichert UTF-16). Die Datei wird von `python-dotenv` gelesen und ist per `.gitignore` vom Commit ausgeschlossen. Den eigenen Key bitte nie committen. Die verfügbaren Modell-IDs zeigt `python llm_models_example.py`.
- **07_plots_examples** unter Linux (Ubuntu/Debian): Damit `plt.show()` ein Fenster öffnet, einmalig `sudo apt install python3-tk` installieren. Ohne Tkinter wird nur die PNG-Datei gespeichert.
- **07_plots_examples/map.py** lädt die Erdbebendaten aus dem Internet. Für `fig.write_image(...)` braucht kaleido einen installierten Chrome (oder Chromium/Edge). Falls keiner vorhanden ist, einmalig `plotly_get_chrome` im aktivierten Environment ausführen.
- **07_plots_examples/gui_example.py** wird mit `streamlit run gui_example.py` gestartet. Beim allerersten Start fragt Streamlit im Terminal nach einer E-Mail-Adresse – das Feld leer lassen und Enter drücken. Danach öffnet sich die App im Browser (http://localhost:8501); beenden mit Strg+C.
