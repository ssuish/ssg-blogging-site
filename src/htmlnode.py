class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag  # html tags (<h1>,<p>,etc.,)
        self.value = value  # value of html tags (<h1>Value</h1>)
        self.children = children  # HTMLNode objects children
        self.props = props or {}  # html atttributes

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        return "".join(f' {k}="{v}"' for k, v in self.props.items())

    def __repr__(self) -> str:
        print("tag: ", self.tag)
        print("value: ", self.value)
        print("children: ", self.children)
        print("props: ", self.props)
