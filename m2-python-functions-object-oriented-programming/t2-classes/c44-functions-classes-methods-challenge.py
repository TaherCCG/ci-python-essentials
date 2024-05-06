# Classes - Functions + Classes: Methods Challenge



class BlogPost:
    """Creates an instance of BlogPost"""

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def get_overview(self):
        return f"{self.title} by {self.author}"

    def full_info(self):
        return f"Blog post: {self.title}. Content: {self.content}. Author: {self.author}"


post = BlogPost("Python Classes", "Python is known as an object-oriented language...", "Code Institute")

print(post.get_overview())

print(post.full_info())

