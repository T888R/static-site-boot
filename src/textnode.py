from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value) -> bool:
        return (
            self.text_type == value.text_type
            and self.text == value.text
            and self.url == value.url
        )
    
    def __repr__(self) -> str:
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'        
        
