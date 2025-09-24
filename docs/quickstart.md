# Quick Start

## Installation

FineSQL requires only standard Python libraries and can be installed easily.

=== "pip"

    ```bash
    pip install finesql
    ```

=== "uv"

    ```bash
    uv add finesql
    ```

## Full Example

Here's the complete example code in one file:

```python
from finesql import Database, Table, Column, ForeignKey

class User(Table):
    username = Column(str)
    age = Column(int)

class Post(Table):
    title = Column(str)
    body = Column(str)
    author = ForeignKey(User)

db = Database("app.db")

db.create(User)
db.create(Post)

# Create users
alice = User(username="Alice Johnson", age=25)
db.save(alice)

robert = User(username="Robert Smith", age=30)
db.save(robert)

# Create a post
post = Post(title="Hello World", body="This is my first post", author=robert)
db.save(post)

# Get all users
users = db.all(User)
print(users)

# Get by id
user1 = db.get(User, id=1)
print(user1)

# Filter by username (reuse first name)
alice = db.get_by_field(User, field_name="username", value="Alice Johnson")
print(alice)

robert = db.get_by_field(User, field_name="username", value="Robert Smith")
print(robert)

alice = db.get(User, id=1)
alice.age = 26
db.update(alice)
print(alice)

db.delete(User, id=1)
users = db.all(User)
print(users)

post = db.get(Post, id=1)
print(post.author)
```
