# ========================================================
# مقرر: ذكاء اصطناعي (عملي)
# التكليف: سحب واستخراج البيانات من المواقع الإلكترونية (Web Scraping)
# إعداد الطالب: عبدالرحمن علي احمد فرحان
# ========================================================

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://webscraper.io/test-sites/e-commerce/static/phones/touch'

print("جاري الاتصال بالموقع وسحب البيانات...")
client = urlopen(url)
html = client.read()
client.close()

soup = bs(html, 'html.parser')
containers = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
print(f"تم العثور على {len(containers)} منتجات.")

filename = "scraped_phones_data.csv"
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Price", "Description", "Reviews"])
    
    for item in containers:
        name_val = item.find_all("a", itemprop="name")[0].text.strip()
        price_val = item.find_all("span", itemprop="price")[0].text.strip()
        desc_val = item.find_all("p", itemprop="description")[0].text.strip()
        reviews_val = item.find_all("p", class_="review-count float-end")[0].text.strip()
        
        writer.writerow([name_val, price_val, desc_val, reviews_val])
        print(f"- {name_val} | {price_val} | {desc_val} | {reviews_val}")

print(f"\n✅ تم حفظ البيانات المسحوبة بنجاح في: {filename}")

df = pd.read_csv(filename)
print("\n--- معاينة البيانات عبر Pandas ---")
print(df.head())