from contextlib import contextmanager

from rich import print
from rich.tree import Tree

import treact
from treact.core import NodeContext


def render_tree(node):
    if not node:
        return
    t = Tree(node.data)
    for child in node.children:
        r = render_tree(child)
        if r:
            t.add(r)
    return t


@contextmanager
def TreeRenderer(buf=None):
    treact.__node_context__ = NodeContext()
    yield
    print(render_tree(treact.__node_context__.root), file=buf)
