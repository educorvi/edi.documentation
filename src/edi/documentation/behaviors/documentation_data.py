# -*- coding: utf-8 -*-
from edi.documentation import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IDocumentationDataMarker(Interface):
    pass

@provider(IFormFieldProvider)
class IDocumentationData(model.Schema):
    """
    """

    model.fieldset(
        'projectdata',
        label=_(u"Projektdaten"),
        fields=['ansprechpartner', 'externe_url', 'zope_admin', 'serveradressen']
    )

    ansprechpartner = schema.List(title=u"Ansprechpartner im Projekt", 
        value_type=schema.TextLine(),
        required=False,
    )

    externe_url = schema.URI(title=u"Externe URL für das Projekt",
        required=False,
    )

    zope_admin = schema.TextLine(title=u"Webserver-Admin (z.B: Zope-Admin)",
        required=False,
    )

    serveradressen = schema.List(title=u"Serveradressen / Shell-Zugriff",
        value_type=schema.TextLine(),
        required=False,
    )


@implementer(IDocumentationData)
@adapter(IDocumentationDataMarker)
class DocumentationData(object):
    def __init__(self, context):
        self.context = context

    @property
    def ansprechpartner(self):
        if hasattr(self.context, 'ansprechpartner'):
            return self.context.ansprechpartner
        return None

    @ansprechpartner.setter
    def ansprechpartner(self, value):
        self.context.ansprechpartner = value

    @property
    def externe_url(self):
        if hasattr(self.context, 'externe_url'):
            return self.context.externe_url
        return None

    @externe_url.setter
    def externe_url(self, value):
        self.context.externe_url = value

    @property
    def zope_admin(self):
        if hasattr(self.context, 'zope_admin'):
            return self.context.zope_admin
        return None

    @zope_admin.setter
    def zope_admin(self, value):
        self.context.zope_admin = value

    @property
    def serveradressen(self):
        if hasattr(self.context, 'serveradressen'):
            return self.context.serveradressen
        return None

    @serveradressen.setter
    def serveradressen(self, value):
        self.context.serveradressen = value
