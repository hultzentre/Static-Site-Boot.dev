from textnode import TextNode


def main():
    result = TextNode('This is a string', "Bold", 'https://www.website.com')
    print(result.repr())

main()