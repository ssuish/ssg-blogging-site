from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node doesn't have a tag")

        if self.children is None:
            raise ValueError("Parent node doesn't have a children")

        props_str = self.props_to_html()

        children_html = "".join(child.to_html() for child in self.children)

        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"

    def __repr__(self) -> str:
        print("tag: ", self.tag)
        print("children: ", self.children)
        print("props: ", self.props)
