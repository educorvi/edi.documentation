# -*- coding: utf-8 -*-
from edi.documentation.testing import EDI_DOCUMENTATION_FUNCTIONAL_TESTING
from edi.documentation.testing import EDI_DOCUMENTATION_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = EDI_DOCUMENTATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_all_tasks_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='all-tasks'
        )
        self.assertTrue(view.__name__ == 'all-tasks')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in all-tasks'
        # )

    def test_all_tasks_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='all-tasks'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = EDI_DOCUMENTATION_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
