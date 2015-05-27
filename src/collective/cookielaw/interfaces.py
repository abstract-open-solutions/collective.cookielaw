# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

# from collective.cookielaw import _
# from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ILayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


CONTENT_ID_KEY = 'collective.cookielaw.content_id_prefix'
JSON_OPTIONS_KEY = 'collective.cookielaw.jsonoptions'
CONFIRM_BUTTON_KEY = 'collective.cookielaw.confirm_button_text'

DEFAULT_MSG = """
<p><b>Cookie message:</b> update this text as you like!</p>
<p><a href="#">View policy</a></p>
"""
