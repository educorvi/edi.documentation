# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


class ITodoTask(model.Schema):
    """ Marker interface and Dexterity Python Schema for TodoTask
    """

    title = schema.TextLine(title=u"ToDo (Was?)")

    description = schema.Text(title=u"Weitere Beschreibung zur ToDo Augabe")

    datetime = schema.Datetime(title=u"Wann?", required=False)

    responsible = schema.TextLine(title=u"Wer?", required = False)

    excludeFromDisplay = schema.Bool(title=u"ToDo Aufgabe von den normalen Ordneransichten ausschließen",
                                     default=True,)

@implementer(ITodoTask)
class TodoTask(Container):
    """
    """
