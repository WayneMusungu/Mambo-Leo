from app import app
import urllib.request,json
from .models import sources

Source = sources.Source

#Getting API Key
api_key = app.config['NEWS_API_KEY']


#Getting the News source url
source_url= app.config['NEWS_API_SOURCE_URL']

def get_source():
    '''
    Function that gets the json response to url request
    '''
    get_source_url= source_url.format(api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    function to that process news results and transform them to a list of objects
    Args:
        source_list:A list of dictionaries that contain movie details
    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        
        if id:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)

    return source_results 
