from contextlib import contextmanager

import treact
from treact.core import NodeContext


@contextmanager
def ConsoleRenderer(buf=None):
    treact.__node_context__ = NodeContext()
    yield
    print(treact.__node_context__.root, file=buf)
