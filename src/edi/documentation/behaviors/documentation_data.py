# -*- coding: utf-8 -*-
from plone.app.multilingual.browser.interfaces import make_relation_root_path
from edi.documentation import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from plone.autoform import directives
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider
from z3c.relationfield.schema import RelationChoice
from plone.app.z3cform.widget import RelatedItemsFieldWidget

class IDocumentationDataMarker(Interface):
    pass

@provider(IFormFieldProvider)
class IDocumentationData(model.Schema):
    """
    """

    model.fieldset(
        'projectdata',
        label=_(u"Projektdaten"),
        fields=['product_owner', 'pl_on_invoice', 'ansprechpartner', 'externe_url', 'zope_admin', 'serveradressen', 
                'customer', 'auftragsnummer']
    )
    project_folder = schema.Bool(title="Bei diesem Ordner handelt es sich um Projektordner eines aktiven Projekts.", required=False)

    product_owner = schema.TextLine(title="Projektleiter:in oder Product-Owner",
        required=False,)

    pl_on_invoice = schema.Bool(title="Soll der/die Projektleiter:in oder Product-Owner auf der Rechnung erscheinen?",
        required=False)

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


    customer = RelationChoice(
        title='Verweis auf den Kunden (eventuell abweichend zum Ordner)',
        vocabulary='plone.app.vocabularies.Catalog',
        required=False,
    )

    directives.widget(
        'customer',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['Customer'],
            'basePath': make_relation_root_path,
        },
    )

    auftragsnummer = schema.TextLine(title="Auftrags- oder Vergabenummer beim Kunden",
        required=False,
    )


@implementer(IDocumentationData)
@adapter(IDocumentationDataMarker)
class DocumentationData(object):
    def __init__(self, context):
        self.context = context

    @property
    def project_folder(self):
        if hasattr(self.context, 'project_folder'):
            return self.context.project_folder
        return None

    @project_folder.setter
    def project_folder(self, value):
        self.context.project_folder = value

    @property
    def product_owner(self):
        if hasattr(self.context, 'product_owner'):
            return self.context.product_owner
        return None

    @product_owner.setter
    def product_owner(self, value):
        self.context.product_owner = value

    @property
    def pl_on_invoice(self):
        if hasattr(self.context, 'pl_on_invoice'):
            return self.context.pl_on_invoice
        return None

    @pl_on_invoice.setter
    def pl_on_invoice(self, value):
        self.context.pl_on_invoice = value

    @property
    def ansprechpartner(self):
        if hasattr(self.context, 'ansprechpartner'):
            return self.context.ansprechpartner
        return None

    @ansprechpartner.setter
    def ansprechpartner(self, value):
        self.context.ansprechpartner = value


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

    @property
    def customer(self):
        if hasattr(self.context, 'customer'):
            return self.context.customer
        return None

    @customer.setter
    def customer(self, value):
        self.context.customer = value

    @property
    def auftragsnummer(self):
        if hasattr(self.context, 'auftragsnummer'):
            return self.context.auftragsnummer
        return None

    @auftragsnummer.setter
    def auftragsnummer(self, value):
        self.context.auftragsnummer = value

