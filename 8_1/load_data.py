import json
from models import Author, Quote
from mongoengine.connection import disconnect
from connect import connect

def load_authors(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        authors_data = json.load(file)

    for author_data in authors_data:
        Author(**author_data).save()

def load_quotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        quotes_data = json.load(file)

    for quote_data in quotes_data:
        author = Author.objects(fullname=quote_data['author']).first()
        if author:
            quote_data['author'] = author
            Quote(**quote_data).save()

if __name__ == "__main__":
    disconnect(alias='default')
    connect('myhw8', host='mongodb+srv://alyavkravchenko:TryNewPass@cluster0.rxysigp.mongodb.net/myhw8?retryWrites=true&w=majority')

    load_authors('authors.json')
    load_quotes('quotes.json')