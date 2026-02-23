import urllib.request
import re
import csv

url = "https://msk.spravker.ru/avtoservisy-avtotehcentry"

html = urllib.request.urlopen(url).read().decode("utf-8")

pattern = r'(?:class="org-widget-header__title-link">)(?P<name>[^<]*)' \
          r'(?:</a>).*?' \
          r'(?:org-widget-header__meta--location">)(?P<address>[^<]*)' \
          r'(?:</span>).*?' \
          r'(?:Телефон</span></dt>\s*<dd class="spec__value">)(?P<phone>[^<]*)' \
          r'(?:</dd>).*?' \
          r'(?:Часы работы</span></dt>\s*<dd class="spec__value">)(?P<hours>[^<]*)'

matches = re.findall(pattern, html, re.S)

print("Найдено организаций:", len(matches))

with open("autoservices.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Название", "Адрес", "Телефон", "Часы работы"])
    for name, address, phone, hours in matches:
        writer.writerow([name.strip(), address.strip(), phone.strip(), hours.strip()])

print("Данные сохранены в autoservices.csv")