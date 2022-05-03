# from pickle import TRUE


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_SOURCE_URL=' https://newsapi.org/v2/sources?apiKey={}'
    CAT_API_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
    
   

class ProdConfig(Config):
    '''
    Production  configuration child class
    '''
    pass

class DevConfig(Config):
    '''
     Development  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True 
