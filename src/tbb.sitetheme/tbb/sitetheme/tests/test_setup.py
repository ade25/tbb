# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from tbb.sitetheme.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of tbb.sitetheme into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if tbb.sitetheme is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('tbb.sitetheme'))

    def test_uninstall(self):
        """Test if tbb.sitetheme is cleanly uninstalled."""
        self.installer.uninstallProducts(['tbb.sitetheme'])
        self.assertFalse(self.installer.isProductInstalled('tbb.sitetheme'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ITbbSitethemeLayer is registered."""
        from tbb.sitetheme.interfaces import ITbbSitethemeLayer
        from plone.browserlayer import utils
        self.failUnless(ITbbSitethemeLayer in utils.registered_layers())
