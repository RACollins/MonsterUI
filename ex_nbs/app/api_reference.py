"""Reference to all FrankenUI Components"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../API Reference.ipynb.

# %% auto 0
__all__ = ['docs_button', 'docs_heading', 'enum_to_html_table', 'create_doc_section']

# %% ../API Reference.ipynb
from fasthtml.common import *
from fh_frankenui.core import *
from nbdev.showdoc import *

from enum import EnumType
from collections.abc import Callable

# %% ../API Reference.ipynb
def enum_to_html_table(enum_class):
    headers = ["Option", "Value"]
    rows = [[name, value.value] for name, value in enum_class.__members__.items()]
    return Div(
        Hr(cls='uk-divider-icon my-4'),
        H3(enum_class.__name__,cls='my-4'),
        P(I(enum_class.__doc__)),
        TableFromLists(headers, rows, cls=(TableT.hover, 'uk-table-small')),)

# %% ../API Reference.ipynb
def create_doc_section(*content, title, md_content=None):
    res = []
    for c in content:
        if isinstance(c, str):        res.append(render_md(c))
        elif isinstance(c, EnumType): res.append(enum_to_html_table(c))
        elif isinstance(c, FT):       res.append(c)
        elif isinstance(c, Callable): 
            _html = str(show_doc(c, renderer=AdvHtmlRenderer))
            res.append(NotStr(apply_classes(_html, class_map_mods={"table":'uk-table uk-table-hover uk-table-small'})))
        else: res.append(c)
    return Section(H1(title,cls='mb-10'), *res)

# %% ../API Reference.ipynb
docs_button = create_doc_section(Button, 
                       ButtonT, 
                       enum_to_html_table(ButtonT),
                       title="Buttons")

docs_heading = create_doc_section(H1, H2, H3, H4, 
                       Card(H1("Level 1 Heading (H1)"), 
                            H2("Level 2 Heading (H2)"), 
                            H3("Level 3 Heading (H3)"), 
                            H4("Level 4 Heading (H4)"),
                           cls='mt-8'),
                        title="Headings")
