# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from edi.documentation.testing import EDI_DOCUMENTATION_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that edi.documentation is properly installed."""

    layer = EDI_DOCUMENTATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if edi.documentation is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'edi.documentation'))

    def test_browserlayer(self):
        """Test that IEdiDocumentationLayer is registered."""
        from edi.documentation.interfaces import IEdiDocumentationLayer
        from plone.browserlayer import utils
        self.assertIn(
            IEdiDocumentationLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EDI_DOCUMENTATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['edi.documentation'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if edi.documentation is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'edi.documentation'))

    def test_browserlayer_removed(self):
        """Test that IEdiDocumentationLayer is removed."""
        from edi.documentation.interfaces import IEdiDocumentationLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IEdiDocumentationLayer,
            utils.registered_layers())
