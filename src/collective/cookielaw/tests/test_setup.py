# -*- coding: utf-8 -*-
"""Setup tests for this package."""

from collective.cookielaw.interfaces import CONTENT_ID_KEY
from collective.cookielaw.interfaces import JSON_OPTIONS_KEY
from collective.cookielaw.interfaces import CONFIRM_BUTTON_KEY
from collective.cookielaw.setuphandlers import create_default_content
from collective.cookielaw.testing import COLLECTIVE_COOKIELAW_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.cookielaw is properly installed."""

    layer = COLLECTIVE_COOKIELAW_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def as_manager(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_product_installed(self):
        """Test if collective.cookielaw is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.cookielaw'))

    def test_uninstall(self):
        """Test if collective.cookielaw is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.cookielaw'])
        self.assertFalse(self.installer.isProductInstalled('collective.cookielaw'))

    def test_browserlayer(self):
        """Test that ILayer is registered."""
        from collective.cookielaw.interfaces import ILayer
        from plone.browserlayer import utils
        self.assertIn(ILayer, utils.registered_layers())

    def test_registry(self):
        registry = api.portal.get_tool('portal_registry')
        self.assertTrue(CONTENT_ID_KEY in registry)
        self.assertTrue(JSON_OPTIONS_KEY in registry)
        self.assertTrue(CONFIRM_BUTTON_KEY in registry)
        self.assertTrue(isinstance(registry[CONFIRM_BUTTON_KEY], dict))

    def test_default_content(self):
        registry = api.portal.get_tool('portal_registry')
        content_id_prefix = registry[CONTENT_ID_KEY] + '-' + self.portal.Language()
        self.assertTrue(content_id_prefix in self.portal.objectIds())

    def test_default_content_multilang(self):
        self.as_manager()
        registry = api.portal.get_tool('portal_registry')
        content_id_prefix = registry[CONTENT_ID_KEY]

        # add some languages and their root folders
        language_tool = api.portal.get_tool('portal_languages')
        language_tool.addSupportedLanguage('ca')
        language_tool.addSupportedLanguage('es')
        for lang in language_tool.getSupportedLanguages():
            api.content.create(
                container=self.portal,
                type='Folder',
                id=lang,
                title=lang.upper(),
            )
        create_default_content(self.portal)
        for lang in language_tool.getSupportedLanguages():
            folder = self.portal[lang]
            self.assertTrue(content_id_prefix + '-' + lang in folder.objectIds())
