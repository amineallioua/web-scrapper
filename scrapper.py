from flask import Flask, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    # Send request to the BBC Arabic page
    bbc = requests.get("https://www.bbc.com/arabic/topics/cv2xyrnr8dnt")
    
    # Create a BeautifulSoup object
    soup = BeautifulSoup(bbc.content, 'html.parser')

    # Find the <ul> with the specific class
    news = soup.find('ul', class_='bbc-k6wdzo')

    # Get all <li> elements inside the <ul>
    news_titles = news.find_all('li')

    # Get the text of each <li> element
    titles = [item.get_text() for item in news_titles] if news_titles else ["No news titles found."]

    # Render HTML template
    html = '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BBC News Scraper</title>
    </head>
    <body>
        <h1>BBC News Titles</h1>
        <ul>
            {% for title in titles %}
                <li>{{ title }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    '''

    return render_template_string(html, titles=titles)

if __name__ == '__main__':
    app.run(debug=True)
