# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


class ITodoTask(model.Schema):
    """ Marker interface and Dexterity Python Schema for TodoTask
    """

    title = schema.TextLine(title="ToDo (Was?)")

    description = schema.Text(title="Weitere Beschreibung zur ToDo Augabe")

    datetime = schema.Datetime(title="Wann?", required=False)

    responsible = schema.TextLine(title="Wer?" required = False)

    excludeFromDisplay = schema.Bool(title="ToDo Aufgabe von den normalen Ordneransichten ausschließen",
                                     default=True,)

@implementer(ITodoTask)
class TodoTask(Container):
    """
    """
