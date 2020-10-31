from GoogleNews import GoogleNews

class News:
    def search_news(self,query):
        news = GoogleNews(lang='en')
        news.search(query)
        news.getpage(1)
        return(news.result())



