# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from plone import api as ploneapi
import json


class ActiveTasks(BrowserView):
    def __call__(self):
        self.searchtasks = self.tasks()
        self.tasklist = self.format_tasks()
        return json.dumps(self.tasklist)

    def format_tasks(self):
        formatted = []
        searchtasks = self.searchtasks
        for element in searchtasks:
            singletask = {}
            singletask['id'] = element.UID
            singletask['title'] = element.Title
            singletask['note'] = False
            formatted.append(singletask)
        formatted = formatted + self.parents()    
        return formatted

    def tasks(self):
        tasks = []
        querydict = {}
        portal_catalog = ploneapi.portal.get_tool(name='portal_catalog')
        parents = []
        if self.context.tasksources:
            pathlist = []
            for i in self.context.tasksources:
                pathlist.append('/'.join(i.to_object.getPhysicalPath()))
            querydict["path"] = pathlist
        if querydict:
            querydict["review_state"] = ['todo', 'in_progress']
            querydict["portal_type"] = "Todo Task"
            tasks = portal_catalog.queryCatalog(querydict)
        else:
            tasks = ploneapi.content.find(portal_type="Todo Task", review_state=['todo', 'in_progress'])
        return tasks

    def parents(self):
        uids = []
        parents = []
        for task in self.searchtasks:
            obj = task.getObject()
            parent = obj.aq_parent
            if parent.UID() not in parents:
                uids.append(parent.UID())
                formtask = {}
                formtask['id'] = parent.UID()
                formtask['title'] = parent.title + ' (Sonstige Aufwendungen)'
                formtask['note'] = True
                parents.append(formtask)
        return parents
