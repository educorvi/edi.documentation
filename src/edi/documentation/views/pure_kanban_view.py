# -*- coding: utf-8 -*-
from edi.documentation import _
from plone import api as ploneapi
from Products.Five.browser import BrowserView


class PureKanbanView(BrowserView):

    def __call__(self):
        return self.index()

    def tasks(self):
        tasks = []
        querydict = {}
        portal_catalog = ploneapi.portal.get_tool(name='portal_catalog')
        if self.context.workflows:
            querydict["review_state"] = self.context.workflows
        if self.context.tasksources:
            pathlist = []
            for i in self.context.tasksources:
                pathlist.append('/'.join(i.to_object.getPhysicalPath()))
            querydict["path"] = pathlist
        if querydict:
            querydict["portal_type"] = "Todo Task"
            tasks = portal_catalog.queryCatalog(querydict)
        else:
            tasks = ploneapi.content.find(portal_type="Todo Task")
        return tasks

    def get_user(self, userid):
        user = ploneapi.user.get(username=userid)
        return user.getProperty('fullname')
