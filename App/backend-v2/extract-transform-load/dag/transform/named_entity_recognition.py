import requests
import logging
from airflow.models import TaskInstance


NER_MODEL_API_URL = 'http://host.docker.internal:5051/extract-entities'


def apply_ner(ti: TaskInstance, file_basename:str) -> None:
    # Pull (file) data from XCom
    data = ti.xcom_pull(key=f'{file_basename}_json_extract_articles')

    articles_entities = post_request(data)

    logging.info(f"Articles entities {articles_entities}")
    logging.info(f"pushing into {file_basename}_articles_entities")

    ti.xcom_push(key=f'{file_basename}_articles_entities', value=articles_entities)

def post_request(data): # TODO specify the data type and return type
    """
    Request to NER model API.
    """
    articles_entities = []

    for article in data:
        article_content = article['content']
        
        try:
            response = requests.post(NER_MODEL_API_URL, json={'content': article_content})
            response.raise_for_status()

            entities = response.json()['entities']
            articles_entities.append(entities)
        except Exception as e:
            logging.error(f"Failed post request to NER model. Error: {str(e)}")
            raise

    return articles_entities