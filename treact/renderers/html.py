from contextlib import contextmanager
from dataclasses import dataclass
from typing import Optional
from xml.dom.minidom import Document, Element

import treact
from treact.core import Node, NodeContext


@dataclass
class HtmlElement:
    tag: str
    attrs: dict[str, str]



def html_node(tag: str, attrs: dict[str, str] | None = None):
    if attrs is None:
        attrs = {}
    return Node(HtmlElement(tag, attrs))

def text_node(text: str):
    return Node(text)


def render_html(node: Optional[Node], document=Document()) -> Optional[Element]:
    if not node:
        return

    if isinstance(node.data, str):
        return document.createTextNode(node.data)
    
    tag_name = node.data.tag

    element = document.createElement(tag_name)
    for key, value in node.data.attrs.items():
        element.setAttribute(key, value)
    for child in node.children:
        element.appendChild(render_html(child, document))
    return element


@contextmanager
def HtmlRenderer(buf=None):
    treact.__node_context__ = NodeContext()
    yield
    print('<!DOCTYPE html>', file=buf)
    print(render_html(treact.__node_context__.root).toprettyxml(), file=buf)
