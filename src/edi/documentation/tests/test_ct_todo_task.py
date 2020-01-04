# -*- coding: utf-8 -*-
from edi.documentation.content.todo_task import ITodoTask  # NOQA E501
from edi.documentation.testing import EDI_DOCUMENTATION_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class TodoTaskIntegrationTest(unittest.TestCase):

    layer = EDI_DOCUMENTATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_todo_task_schema(self):
        fti = queryUtility(IDexterityFTI, name='Todo Task')
        schema = fti.lookupSchema()
        self.assertEqual(ITodoTask, schema)

    def test_ct_todo_task_fti(self):
        fti = queryUtility(IDexterityFTI, name='Todo Task')
        self.assertTrue(fti)

    def test_ct_todo_task_factory(self):
        fti = queryUtility(IDexterityFTI, name='Todo Task')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ITodoTask.providedBy(obj),
            u'ITodoTask not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_todo_task_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Todo Task',
            id='todo_task',
        )

        self.assertTrue(
            ITodoTask.providedBy(obj),
            u'ITodoTask not provided by {0}!'.format(
                obj.id,
            ),
        )

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertIn('todo_task', self.parent.objectIds())

    def test_ct_todo_task_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Todo Task')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_todo_task_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Todo Task')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'todo_task_id',
            title='Todo Task container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
