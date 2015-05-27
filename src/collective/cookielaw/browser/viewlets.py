# -*- coding: utf-8 -*-

import json
import logging
logger = logging.getLogger('[collective.cookielaw.viewlet]')

from plone.app.layout.viewlets import common
from plone.memoize import view
from plone import api
from Products.CMFPlone.utils import base_hasattr

from collective.cookielaw.interfaces import CONTENT_ID_KEY
from collective.cookielaw.interfaces import JSON_OPTIONS_KEY
from collective.cookielaw.interfaces import CONFIRM_BUTTON_KEY
from collective.cookielaw.interfaces import DEFAULT_MSG


class CookieMessageViewlet(common.ViewletBase):

    @property
    def ps(self):
        return self.context.restrictedTraverse('@@plone_portal_state')

    def available(self):
        return self.ps.anonymous()

    def get_page(self):
        registry = api.portal.get_tool('portal_registry')
        root = self.ps.navigation_root()
        page = None
        # TODO: handle
        try:
            page_id = registry[CONTENT_ID_KEY]
        except KeyError:
            page_id = ''
        if not page_id:
            return None
        # we handle also the case where you have multilingual site,
        # but w/out root folders, so that you could have
        # page_id-en, page_id-fr, etc all in the same root.
        for k in (page_id, page_id + '-' + self.ps.language()):
            if base_hasattr(root, k):
                page = getattr(root, k)
                break
        return page

    @view.memoize
    def get_message(self):
        content = DEFAULT_MSG
        page = self.get_page()
        if page:
            content = page.getText()
        return content

    @property
    def settings(self):
        registry = api.portal.get_tool('portal_registry')
        try:
            settings = registry[JSON_OPTIONS_KEY]
        except KeyError:
            logger.error("key {} missing in registry".format(JSON_OPTIONS_KEY))
            settings = ''
        try:
            settings = json.loads(settings)
        except Exception as e:
            logger.error("JSON config contains errors: {}".format(str(e)))
            settings = {}
        # get button text
        try:
            button_settings = registry[CONFIRM_BUTTON_KEY]
        except KeyError:
            logger.error("key {} missing in registry".format(CONFIRM_BUTTON_KEY)) # noqa
            button_settings = {}
        lang = self.ps.language()
        settings['dismiss'] = button_settings.get(lang)
        settings['message'] = self.get_message()
        return settings

    @property
    @view.memoize
    def json_settings(self):
        return json.dumps(self.settings)
