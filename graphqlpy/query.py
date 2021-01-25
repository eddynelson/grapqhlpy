import typing

import strawberry
from graphqlpy.types import Book
from graphqlpy.resolvers import get_books

@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)