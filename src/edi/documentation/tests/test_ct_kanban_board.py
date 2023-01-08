# -*- coding: utf-8 -*-
from edi.documentation.content.kanban_board import IKanbanBoard  # NOQA E501
from edi.documentation.testing import EDI_DOCUMENTATION_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class KanbanBoardIntegrationTest(unittest.TestCase):

    layer = EDI_DOCUMENTATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_kanban_board_schema(self):
        fti = queryUtility(IDexterityFTI, name='Kanban Board')
        schema = fti.lookupSchema()
        self.assertEqual(IKanbanBoard, schema)

    def test_ct_kanban_board_fti(self):
        fti = queryUtility(IDexterityFTI, name='Kanban Board')
        self.assertTrue(fti)

    def test_ct_kanban_board_factory(self):
        fti = queryUtility(IDexterityFTI, name='Kanban Board')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IKanbanBoard.providedBy(obj),
            u'IKanbanBoard not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_kanban_board_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Kanban Board',
            id='kanban_board',
        )

        self.assertTrue(
            IKanbanBoard.providedBy(obj),
            u'IKanbanBoard not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('kanban_board', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('kanban_board', parent.objectIds())

    def test_ct_kanban_board_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Kanban Board')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_kanban_board_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Kanban Board')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'kanban_board_id',
            title='Kanban Board container',
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
