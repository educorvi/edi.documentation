# -*- coding: utf-8 -*-
from DateTime import DateTime
from plone import api as ploneapi
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.indexer import indexer
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from zope.interface import provider
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@provider(IContextSourceBinder)
def get_users(context):

    terms = []
    users = ploneapi.user.get_users()
    for user in users:
        userid = user.getId()
        email = user.getProperty('email')
        fullname = user.getProperty('fullname')
        terms.append(SimpleTerm(value=userid, token=email, title=fullname))
    return SimpleVocabulary(terms)


class ITodoTask(model.Schema):
    """ Marker interface and Dexterity Python Schema for TodoTask
    """

    title = schema.TextLine(title=u"ToDo (Was?)")

    description = schema.Text(title=u"Weitere Beschreibung der ToDo Aufgabe")

    datetime = schema.Datetime(title=u"Wann?", required=True)

    referenz = schema.URI(title=u"Referenz-URL zu dieser Aufgabe", description=u"z.B: URL auf Github", required=False)

    responsible = schema.Choice(title=u"Wer?", source = get_users, required = False)

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

@indexer(ITodoTask)
def parentTitleIndexer(obj):
    return obj.aq_parent.title
