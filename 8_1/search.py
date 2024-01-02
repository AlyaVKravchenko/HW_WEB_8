from mongoengine import connect
from models import Quote, Author
from mongoengine.connection import disconnect

def search_quotes(command):
    parts = command.split(':')
    if len(parts) != 2:
        print("Invalid command format")
        return

    field, value = parts[0].strip(), parts[1].strip()

    if field == 'name':
        author = Author.objects(fullname=value).first()
        if author:
            quotes = Quote.objects(author=author)
            for quote in quotes:
                print(quote.quote)
        else:
            print(f"No quotes found for author: {value}")
    elif field == 'tag':
        quotes = Quote.objects(tags=value)
        for quote in quotes:
            print(quote.quote)
    elif field == 'tags':
        tags = value.split(',')
        quotes = Quote.objects(tags__in=tags)
        for quote in quotes:
            print(quote.quote)
    elif field == 'exit':
        print("Exiting the script.")
        exit()
    else:
        print("Unknown command")

if __name__ == "__main__":
    disconnect(alias='default')
    connect('myhw8',
            host='mongodb+srv://alyavkravchenko:TryNewPass@cluster0.rxysigp.mongodb.net/myhw8?retryWrites=true&w=majority')

    while True:
        command = input("Enter command: ")
        if command.startswith('exit'):
            print("Exiting the script.")
            break
        search_quotes(command)