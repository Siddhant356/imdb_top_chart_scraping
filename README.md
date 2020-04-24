# imdb_top_chart_scraping
[Clone or download]() project. Then create a virtual environment in the same location.
To create vitual environment open CMD 
```bash
python -m venv environment_name
environment_name\Scripts\activate
```
install scrapy
```bash
pip install scrapy
```
To run spider
```bash
scrapy crawl imdb -o topchart.csv
```
or
```bash
scrapy crawl imdb -o topchart.json
```
