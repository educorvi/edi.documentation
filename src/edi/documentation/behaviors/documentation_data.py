# -*- coding: utf-8 -*-
from edi.documentation import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
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
        fields=['product_owner', 'pl_on_invoice', 'ansprechpartner', 'externe_url', 'zope_admin', 'serveradressen', 
                'invoice_str_hnr', 'invoice_plz', 'invoice_ort']
    )

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

    invoice_str_hnr = schema.TextLine(title="Straße und Hausnummer für evtl. abweichende Rechnungsanschrift",
        required=False,
    )

    invoice_plz = schema.TextLine(title="Postleitzahl für evtl. abweichende Rechnungsanschrift",
        required=False,
    )

    invoice_ort = schema.TextLine(title="Ortsangabe für evtl. abweichende Rechnungsanschrift",
        required=False,
    )


@implementer(IDocumentationData)
@adapter(IDocumentationDataMarker)
class DocumentationData(object):
    def __init__(self, context):
        self.context = context

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
    def invoice_str_hnr(self):
        if hasattr(self.context, 'invoice_str_hnr'):
            return self.context.invoice_str_hnr
        return None

    @invoice_str_hnr.setter
    def invoice_str_hnr(self, value):
        self.context.invoice_str_hnr = value

    @property
    def invoice_plz(self):
        if hasattr(self.context, 'invoice_plz'):
            return self.context.invoice_plz
        return None

    @invoice_plz.setter
    def invoice_plz(self, value):
        self.context.invoice_plz = value

    @property
    def invoice_ort(self):
        if hasattr(self.context, 'invoice_ort'):
            return self.context.invoice_ort
        return None

    @invoice_ort.setter
    def invoice_ort(self, value):
        self.context.invoice_ort = value
