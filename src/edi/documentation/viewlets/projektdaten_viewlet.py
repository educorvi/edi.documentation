# -*- coding: utf-8 -*-
from edi.documentation.behaviors.documentation_data import IDocumentationData
from plone.app.layout.viewlets import ViewletBase


class ProjektdatenViewlet(ViewletBase):

    def render(self):
        if hasattr(self.context, 'ansprechpartner') and self.context.portal_type in ['Folder',]:
            return super(ProjektdatenViewlet, self).render()
        else:
            return ''
