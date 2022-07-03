class Post:
    def __init__(self, _id, title, author, text):
        self._id = _id
        self._title = title
        self._author = author
        self._text = text
        
        
    @property
    def post_id(self):
        return self._id
        
        
    @property
    def data(self):
        data = {
            'id': self._id,
            'title': self._title,
            'author': self._author,
            'text': self._text
        }
        return data
        
        
class Comment(Post):
    def __init__(self, _id, title, author, text, post_id):
        Post.__init__(self, _id, title, author, text)
        self._post_id = post_id
        
        
    @property
    def data(self):
        data = {
            'id': self._id,
            'post_id': self._post_id,
            'title': self._title,
            'author': self._author,
            'text': self._text
        }
        return data
    
    
if __name__ == '__main__':
    post = Post(1, 'Test post', 'admin', 'Hello!')
    
    comment1 = Comment(1, 'comment 1', 'user', 'Test comment!', post.post_id)
    comment2 = Comment(2, 'comment 2', 'user', 'Hello!', post.post_id)
    comment3 = Comment(3, 'comment 3', 'user', 'Another comment', post.post_id)
    
    print(post.data)
    print(comment1.data)
    print(comment2.data)
    print(comment3.data)