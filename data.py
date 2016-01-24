BASIC_SVG_STYLE = """
.Diagram line
{
    stroke: black;
    stroke-width:1px;
}
.Diagram rect
{
    fill: none;
    stroke: black;
    stroke-width:1px;
}
.Diagram text
{
    font-size: 7px;
}
"""

class Canvas:
    def __init__(self):
        """
        The Canvas which represents the diagram.
        :return: Canvas object
        """
        self.objects = []

    def add_participant(self, name):
        """
        Add a participant to the diagram
        :param name: String with the participant's name
        :return: None
        """
        pass
    def add_note(self, **kwargs):
        """
        Add a Note to the diagram
        :param kwargs: dict
            - message: str
            - pos: str ("left of" or "right of" or "over")
            - actor: str (a participant)
        :return: None
        """
        pass
    def set_title(self, title):
        """
        Set the diagram's title
        :param title: str
        :return: None
        """
        pass
    def add_link(self, **kwargs):
        """
        Add a link between two participants
        :param kwargs: dict
            - from: str (a participant)
            - to: str (a participant)
            - text: str
            - line-style: str ('-' or '--')
            - arrow-style: str ('>' or '>>')
        :return: None
        """
        pass
    def get_svg(self):
        """
        Get the canvas as SVG
        :return: str (The canvas as SVG)
        """
        svg = ""
        for o in self.objects:
            svg = ''.join([svg,o.get_svg(), '\n'])
        return "<style>{}</style>\n<svg class='Diagram'>\n{}</svg>".format(BASIC_SVG_STYLE, svg)

class Text:
    def __init__(self, **kwargs):
        """
        Representation of a text.
        :param kwargs: dict
            - text: str
            - pos: tuple of two numbers
        :return: Text object
        """
        self.text = kwargs.get('text', "")
        self.pos = kwargs.get('pos', (0,0))

    def get_svg(self):
        """
        Get your text as SVG.
        :return: str
        """
        return '<text x="{}" y="{}">{}</text>'.format(self.pos[0], self.pos[1], self.text)

class Line:
    def __init__(self, **kwargs):
        """
        Representation of a line.
        :param kwargs: dict
            - origin: tuple of two numbers
            - end : tuple of two numbers
            - end_arrow : str (">" or ">>") or None (default: None)
        :return: Line object
        """
        self.origin = kwargs.get('origin', (0,0))
        self.end = kwargs.get('end', (0,0))

    def get_svg(self):
        """
        Get your text as SVG.
        :return: str
        """
        return '<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(self.origin[0], self.origin[1], self.end[0], self.end[1])

class Rect:
    def __init__(self, **kwargs):
        """
        Representation of a rectangle.
        :param kwargs: dict
            - pos: tuple of two numbers
            - size: tuple of two numbers
        :return: Rect object
        """
        self.pos = kwargs.get('pos', (0,0))
        self.size = kwargs.get('size', (0,0))

    def get_svg(self):
        """
        Get your text as SVG.
        :return: str
        """
        return '<rect width="{}" height="{}" x="{}" y="{}"/>'.format(self.size[0],self.size[1], *self.pos)

class Element:
    def __init__(self, **kwargs):
        """
        An element of the canvas.
        :param kwargs: dict
            - pos: tuple of two numbers
        :return: Element object
        """
        pass
    def get_svg(self):
        """
        Get your text as SVG.
        :return: str
        """
        pass

class Note(Element):
    def __init__(self, **kwargs):
        """
        A note in the diagram.
        :param kwargs: dict
            - pos: tuple of two numbers
            - text: str
        :return: Note object.
        """
        pass

class Participant(Element):
    def __init__(self, **kwargs):
        """
        A participant in the diagram.
        :param kwargs: dict
            - pos: tuple of two numbers
            - text: str
        :return: Participant object.
        """
        pass

class Title(Element):
    def __init__(self, **kwargs):
        """
        The title the diagram.
        :param kwargs: dict
            - pos: tuple of two numbers
            - text: str
        :return: Title object.
        """
        pass

class Link(Element):
    def __init__(self, **kwargs):
        """
        A link in the diagram.
        :param kwargs: dict
            - origin: tuple of two numbers
            - end : tuple of two numbers
            - end_arrow : str (">" or ">>") or None (default: None)
            - text: str
        :return: Link object.
        """
        pass

if __name__ == '__main__':
    r = Rect(pos=(0,0), size=(50, 80))
    t = Text(pos=(2,5), text="Hello !")
    l = Line(origin=(10,10), end=(30,50))

    canvas = Canvas()
    canvas.objects = [r,t,l]
    print("<! DOCTYPE html>\n<html><body>")
    print(canvas.get_svg())
    print("</body></html>")