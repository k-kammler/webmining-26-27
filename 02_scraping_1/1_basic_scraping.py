import requests

url = 'https://www.heise.de/news/Rundfunkreform-ARD-Radioprogramme-werden-von-70-auf-53-reduziert-9995463.html'

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

    # Irgendwie an den Hauptinhalt kommen ;-)
    main_content = html_content \
        .split('<button data-action="hide-en-pointer" class="notice-banner__hide-link">Don’t show this again</button>.')[1] \
        .split('<div class="ad ad--inread">')[0]
    
    print(main_content)

else:
    print(f"Fehler beim Abrufen der Seite: {response.status_code}")

