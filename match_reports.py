from transformers import pipeline
import requests
from bs4 import BeautifulSoup
summarizer = pipeline('summarization')

dublin_kerry_url = "https://www.rte.ie/sport/gaa/2019/0914/1075925-five-alive-o-dublin-dominate-kerry-to-make-gaa-history/"
tipp_kilkenny_url = "https://www.rte.ie/sport/gaa/2019/0818/1069488-all-ireland-hurling-final-2019-kilkenny-0-20-tipperary-3-25/"

for url in [dublin_kerry_url, tipp_kilkenny_url]:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    match_report = soup.findAll('p')
    match_report_text = ' '.join([paragraph.text for paragraph in match_report])

    match_summary = summarizer(match_report_text, min_length=100, max_length=500)

    print(match_summary[0]['summary_text'])
