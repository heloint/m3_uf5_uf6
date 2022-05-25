'''
Utilities used by the "Anime searches" application.
'''
import re
import create_db as db

def get_headers(db_object: db.DB, keywords: str) -> list[str]:
    ''' Splits the search term into keywords and executes queries with each of them,
        then removes repetitions from the results, returning a list of headers.
    '''
    received_keywords: list[str] = re.split(r'[/\,;!]', keywords)
   
    headers: list[str] = []
    for keyword in received_keywords: 
        titles: list[str] = ["".join(list(title)) for title in db_object.get_query('title', keyword)]
        headers += titles 

    return headers


def get_content(db_object: db.DB, keywords: str) -> list[str]:
    ''' Splits the search term into keywords and executes queries with each of them,
        then removes repetitions from the results, returning a list of contents.
    '''
    
    received_keywords: list[str] = re.split(r'[/\,;!]', keywords)
   
    contents: list[str] = []
    for keyword in received_keywords: 
        data: list[str] = ["".join(list(title)) for title in db_object.get_query('desc', keyword)]
        contents += data

    return contents

def remove_duplicates(source_data: list[dict]) -> list[dict]:
    
    collector: list[str] = []
    data: dict = {}
    
    for key, value in source_data[0].items():
        if value not in collector:
            collector.append(value)
            data[key] = value

    return [data]
