class Canvas:
    def __init__(self):
        pass
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
        pass

class Text:
    def __init__(self, **kwargs):
        """
        Representation of a text.
        :param kwargs: dict
            - text: str
            - pos: tuple of two numbers
        :return: Text object
        """
        pass
    def get_svg(self):
        """
        Get your text as SVG.
        :return: str
        """
        pass

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
        pass
    def get_svg(self):
        """
        Get your text as SVG.
        :return: str
        """
        pass

class Rect:
    def __init__(self, **kwargs):
        """
        Representation of a rectangle.
        :param kwargs: dict
            - pos: tuple of two numbers
            - size: tuple of two numbers
        :return: Rect object
        """
        pass
    def get_svg(self):
        """
        Get your text as SVG.
        :return: str
        """
        pass

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