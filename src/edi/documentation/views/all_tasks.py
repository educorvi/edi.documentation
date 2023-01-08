# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from plone import api as ploneapi
import json


class AllTasks(BrowserView):
    def __call__(self):
        self.tasklist = self.format_tasks()
        return json.dumps(self.tasklist)

    def format_tasks(self):
        formatted = []
        searchtasks = self.tasks()
        for element in searchtasks:
            singletask = {}
            singletask['id'] = element.UID
            singletask['title'] = element.Title
            singletask['state'] = element.review_state
            formatted.append(singletask)
        return formatted

    def tasks(self):
        tasks = []
        querydict = {}
        portal_catalog = ploneapi.portal.get_tool(name='portal_catalog')
        if self.context.tasksources:
            pathlist = []
            for i in self.context.tasksources:
                pathlist.append('/'.join(i.to_object.getPhysicalPath()))
            querydict["path"] = pathlist
        if querydict:
            querydict["review_state"] = ['todo', 'in_progress', 'done']
            querydict["portal_type"] = "Todo Task"
            tasks = portal_catalog.queryCatalog(querydict)
        else:
            tasks = ploneapi.content.find(portal_type="Todo Task", 
                                          review_state=['todo', 'in_progress','done'])
        return tasks
