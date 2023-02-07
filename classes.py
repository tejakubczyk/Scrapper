def get_list(title, content):
    return [title, content]


class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def return_list(self, title, content):
        return [title, content]




