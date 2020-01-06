# -*- coding: utf-8 -*-

from edi.documentation import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ToDoView(BrowserView):
    """Einzelansicht der ToDo-Aufgabe"""

    def get_contents(self):
        fc = self.context.getFolderContents()
        return fc

    def get_erledigung(self):
        erledigung = ''
        if self.context.erledigung:
            erledigung = self.context.erledigung.output
        return erledigung
