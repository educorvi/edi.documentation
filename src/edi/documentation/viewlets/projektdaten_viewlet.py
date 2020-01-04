# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class ProjektdatenViewlet(ViewletBase):

    def render(self):
        if IDocumentationData.providedBy(self.context):
            return super(ProjektdatenViewlet, self).render()
        else:
            return ''
