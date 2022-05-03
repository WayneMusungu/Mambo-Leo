
class Category:
    '''
    Class that instantiates objects of the news categories objects of the news sources
    '''
    
    def __init__(self, author, title, description, url, publishedAt, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt = publishedAt
        self.content = content