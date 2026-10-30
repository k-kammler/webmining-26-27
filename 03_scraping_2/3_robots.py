import urllib.robotparser

robotParse = urllib.robotparser.RobotFileParser()

robotParse.set_url('https://www.zdf.de/robots.txt')
robotParse.read()

print(robotParse.can_fetch('*','https://www.zdf.de/filme'))
print(robotParse.can_fetch('*','https://www.zdf.de/mainzelmaennchen'))
print(robotParse.can_fetch('*','https://www.zdf.de/service-und-hilfe/zuschauerservice/impressum-zdf-100.html'))
print(robotParse.can_fetch('GPTBot','https://www.zdf.de/sport/bundesliga/union-berlin-eintracht-frankfurt-highlights-zusammenfassung-saison-2024-25-100.html'))