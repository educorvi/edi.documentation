# -*- coding: utf-8 -*-
from edi.documentation.behaviors.documentation_data import IDocumentationDataMarker
from edi.documentation.testing import EDI_DOCUMENTATION_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class DocumentationDataIntegrationTest(unittest.TestCase):

    layer = EDI_DOCUMENTATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_documentation_data(self):
        behavior = getUtility(IBehavior, 'edi.documentation.documentation_data')
        self.assertEqual(
            behavior.marker,
            IDocumentationDataMarker,
        )
