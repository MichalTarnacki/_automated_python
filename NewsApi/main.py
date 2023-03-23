import requests

x = requests.get('https://newsapi.org/v2/everything?q="joe biden"&language=pl&from=2023-02-23&sortBy=publishedAt&apiKey=')
content = x.json()
for i in content['articles']:
    print(f"{i['title']}:\n {i['description']}\n")
