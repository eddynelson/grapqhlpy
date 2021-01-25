from graphqlpy.types import Book

def get_books():
    return [
        Book(
            title='The Great Gatsby',
            description='The better book of the world!!',
        ),
    ]
