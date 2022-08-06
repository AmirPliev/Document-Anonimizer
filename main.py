import spacy
nlp = spacy.load("nl_core_news_lg")

from document_handler import MyDocuments

LOAD_DIRECTORY="files_to_anonimize"
documents = MyDocuments(LOAD_DIRECTORY)
documents.show_all_documents()
documents.anonimize_all_documents()
