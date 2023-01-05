# -*- coding: utf-8 -*-
from plone import api
from edi.documentation import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ToDoDone(BrowserView):
    """List the todos done in current folder"""

    def get_dones(self):
        todos = api.content.find(context=self.context, portal_type="Todo Task", review_state="erledigt", sort_on="end", sort_order="reverse")
        return todos    

    def backlink(self):
        return self.context.absolute_url()
