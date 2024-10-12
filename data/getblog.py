def decodeblog(blog) -> dict:
    return {
        '_id': str(blog['_id']),
        'title': blog['title'],
        'content': blog['content'],
        'author': blog['author'],
        'tags': blog['tags'],
        'date': blog['date']
    }
def decode_all(blogs) -> dict:
    return {
        'message': 'OK',
        'data': [decodeblog(blog) for blog in blogs]
    }