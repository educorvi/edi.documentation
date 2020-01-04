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

    ansprechpartner = schema.List(title="Ansprechpartner im Projekt", 
        value_type=schema.TextLine(),
        required=False,
    )

    externe_url = schema.URI(title="Externe URL für das Projekt",
        required=False,
    )

    zope_admin = schema.TextLine(title="Webserver-Admin (z.B: Zope-Admin)",
        required=False,
    )

    serveradressen = schema.URI(title="Serveradressen / Shell-Zugriff",
        required=False,
    )


@implementer(IDocumentationData)
@adapter(IDocumentationDataMarker)
class DocumentationData(object):
    def __init__(self, context):
        self.context = context

    @property
    def project(self):
        if hasattr(self.context, 'project'):
            return self.context.project
        return None

    @project.setter
    def project(self, value):
        self.context.project = value
