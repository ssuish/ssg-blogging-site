from textnode import TextNode, TextType

def main():
    text = TextNode(
        "This is some anchor text", TextType.LINK, "https://example.com"
    )
    print(text)

if __name__ == "__main__":
    main()
