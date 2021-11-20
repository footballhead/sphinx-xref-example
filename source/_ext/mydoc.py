"""
Sphinx extension which demonstrates how to use xrefs. Provides:

* ``mydoc``: A custom role that works like Sphinx doc
* ``mytoctree``: A custom direction that works like Sphinx toctree
"""

from docutils import nodes
from docutils.parsers import rst
from docutils.parsers.rst import states
from sphinx import addnodes, application
from typing import Any, Dict, List, Tuple


def mydoc(
    name: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: states.Inliner,
    options: dict = {},
    content: List[str] = [],
) -> Tuple[List[nodes.Node], List[Any]]:
    """
    This role tries to emulate the doc role to show how pending_xref works.

    A custom role is a callable, e.g. a function or a class that defines __call__.

    For what all the parameters do, see the official docs:
    https://docutils.sourceforge.io/docs/howto/rst-roles.html

    Sphinx knows mydoc exists because it is registered in setup() with add_role.

    TODO: What is type of "A list of system messages"? I'm using Any right now
    """

    # pending_xref is where all the magic happens.
    xref = addnodes.pending_xref(
        # reftarget is the name of the document to which to link
        reftarget=text,
        # refdomain for docs must be 'std'
        refdomain="std",
        # reftype for document xrefs must be 'doc'
        reftype="doc",
        # refexplicit: wrap the child or replace with reftarget title
        refexplicit=False,
        # refwarn if True will warn when reftarget doesn't exist
        refwarn=True,
    )

    # For inline roles, a parent is not necessary. This will be important in
    # the mytoctree example though!

    # pending_xref must have a child! This will be overwritten when refexplicit
    # is False so in this example we don't care what the child actually
    # contains.
    xref += nodes.inline(text=text)

    # The return is 2 lists: a list of nodes (the xref), and a list I don't care about
    return [xref], []


class MyTocTree(rst.Directive):
    """
    A directive that generates a table of contents, similar to toctree.

    Sphinx knows mytoctree exists because it is registered in setup() with
    add_directive.
    """

    # All table of contents names are provided in directive content
    has_content: bool = True

    def run(self) -> List[nodes.Node]:
        """
        Construct a bulleted list. Each content line is turned into a link and added
        to the bullet list.
        """

        # Since names are provided by content, fail if we have no content
        self.assert_has_content()

        # A bullet_list translates into <ul>
        bullet_list = nodes.bullet_list()

        # Each line of the content is a new link
        for content_line in self.content:
            # A bullet_list contains list_items
            list_item = nodes.list_item()
            bullet_list += list_item

            # list_items contain paragraphs
            xref_container = nodes.paragraph()
            list_item += xref_container

            # pending_xref is where all the magic happens.
            xref = addnodes.pending_xref(
                # reftarget is the name of the document to which to link
                reftarget=content_line,
                # refdomain for docs must be 'std'
                refdomain="std",
                # reftype for document xrefs must be 'doc'
                reftype="doc",
                # refexplicit: use a user title (the child) or reftarget title
                refexplicit=False,
                # refwarn if True will warn when a reftarget doesn't exist
                refwarn=True,
            )

            # For roles, it's assumed we're already in a paragraph. For
            # directives this doesn't hold true. So we have to ensure we have
            # a proper parent for the xref
            xref_container += xref

            # pending_xref must have a child! This will be overwritten when
            # refexplicit is False so in this example we don't care what the
            # child actually contains.
            #
            # (If refexplicit is True then the given text is turned into a link)
            xref += nodes.inline(text=content_line)

        return [bullet_list]


def setup(app: application.Sphinx) -> Dict[str, Any]:
    """
    Main extension entry point.

    Registers the custom directive and role so that Sphinx knows how to parse
    them.
    """

    app.add_role("mydoc", mydoc)
    app.add_directive("mytoctree", MyTocTree)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_sage": True,
    }
