from fasthtml.common import *

app, rt = fast_app()


#
# Black formatting on save with...
# . typing trailing commas everywhere ! ! !
# . maybe only if more than 1 param ! ! !
#
@rt("/")
def get():
    return Titled(
        "Hello FastHTML World !!!",
        hx_get="/change",
    )


@rt("/change")
def get():
    return Titled("Goodbye FastHTML World : - O")


serve()
