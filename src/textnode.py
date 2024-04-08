class TextNode():

    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def eq(self, node_1, node_2):
        match = True
        if (node_1.text != node_2.text):
            match = False
        if (node_1.text_type != node_2.text_type):
            match = False
        if (node_1.url != node_2.url):
            match = False
        return match


    def repr(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
