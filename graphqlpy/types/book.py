import strawberry

@strawberry.type
class Book:
    title: str
    description: str