# -*- coding: utf-8 -*-
from plone import api
from plone.app.layout.viewlets import ViewletBase


class ToDoViewlet(ViewletBase):

    def get_entries(self):
        todos = api.content.find(context=self.context, portal_type="Todo Task", review_state=["todo", "in_progress"], sort_on="end")
        return todos

    def get_dones(self):
        todos = api.content.find(context=self.context, portal_type="Todo Task", review_state="done", sort_on="end", sort_order="reverse")
        return todos

    def done_view(self):
        return self.context.absolute_url() + '/done_view'

    def render(self):
        entries = self.context.listFolderContents(contentFilter={"portal_type" : "Todo Task"})
        if not entries:
            return ''
        return super(ToDoViewlet, self).render()
