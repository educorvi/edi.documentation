# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from DateTime import DateTime
from plone.indexer import indexer


class ITodoTask(model.Schema):
    """ Marker interface and Dexterity Python Schema for TodoTask
    """

    title = schema.TextLine(title=u"ToDo (Was?)")

    description = schema.Text(title=u"Weitere Beschreibung der ToDo Aufgabe")

    datetime = schema.Datetime(title=u"Wann?", required=True)

    referenz = schema.URI(title=u"Referenz-URL zu dieser Aufgabe", description=u"z.B: URL auf Github", required=False)

    responsible = schema.TextLine(title=u"Wer?", required = False)

    erledigung = RichText(title=u"Dokumentation zur Erledigung der ToDo Aufgabe", required = False)

    excludeFromDisplay = schema.Bool(title=u"ToDo Aufgabe von den normalen Ordneransichten ausschließen",
                                     default=True,)

@implementer(ITodoTask)
class TodoTask(Container):
    """
    """

@indexer(ITodoTask)
def endIndexer(obj):
    if obj.datetime is None:
        return None
    return DateTime(obj.datetime)
