# Examples

## Blog System

```python
from finesql import Database, Table, Column, ForeignKey

class User(Table):
    username = Column(str)
    email = Column(str)

class Post(Table):
    title = Column(str)
    content = Column(str)
    author = ForeignKey(User)

db = Database("blog.db")
db.create(User)
db.create(Post)

# Create user
user = User(username="alice", email="alice@blog.com")
db.save(user)

# Create post
post = Post(title="My First Post", content="Hello world!", author=user)
db.save(post)

# Query with relationships
post = db.get(Post, id=1)
print(f"'{post.title}' by {post.author.username}")
```

## Todo App

```python
from finesql import Database, Table, Column

class Todo(Table):
    title = Column(str)
    completed = Column(bool)
    priority = Column(int)

db = Database("todo.db")
db.create(Todo)

todo = Todo(title="Learn FineSQL", completed=False, priority=1)
db.save(todo)

# Mark as completed
todo.completed = True
todo = db.update(todo)
print(todo)
```
