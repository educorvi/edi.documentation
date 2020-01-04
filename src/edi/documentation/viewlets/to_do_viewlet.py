# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class ToDoViewlet(ViewletBase):

    def get_entries(self):
        todos = self.context.listFolderContents(contentFilter={"portal_type" : "ToDo Task"})
        todos.sort(key=lambda x: x.datetime, reverse=False)
        return todos

    def render(self):
        entries = self.context.listFolderContents(contentFilter={"portal_type" : "ToDo Task"})
        if not entries:
            return ''
        return super(ToDoViewlet, self).render()
