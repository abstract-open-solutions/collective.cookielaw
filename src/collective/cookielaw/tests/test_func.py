# -*- coding: utf-8 -*-
"""Setup tests for this package."""

from collective.cookielaw.browser.viewlets import CookieMessageViewlet
from collective.cookielaw.interfaces import DEFAULT_MSG
from collective.cookielaw.testing import COLLECTIVE_COOKIELAW_FUNCTIONAL_TESTING  # noqa
# from plone.app.testing import setRoles
# from plone.app.testing import TEST_USER_ID

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.cookielaw is properly installed."""

    layer = COLLECTIVE_COOKIELAW_FUNCTIONAL_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def test_viewlet(self):
        viewlet = CookieMessageViewlet(self.portal, self.request, None, None)
        viewlet.update()
        self.assertEqual(viewlet.get_page().getId(), 'cookie-law-msg-en')
        settings = viewlet.settings
        self.assertEqual(settings['message'], DEFAULT_MSG)
        self.assertEqual(settings['dismiss'], 'Ok!')
