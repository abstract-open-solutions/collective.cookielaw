# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger('[collective.cookielaw.setup]')
from plone import api
# from plone.app.textfield import RichTextValue

from collective.cookielaw.interfaces import CONTENT_ID_KEY
from collective.cookielaw.interfaces import DEFAULT_MSG


def isNotCurrentProfile(context): # noqa
    return context.readDataFile('collectivecookielaw_marker.txt') is None


def post_install(context):
    """Post install script"""
    if isNotCurrentProfile(context):
        return
    # Do something during the installation of this package
    create_default_content(context.getSite())


def create_default_content(site):
    registry = api.portal.get_tool('portal_registry')
    content_id_prefix = registry[CONTENT_ID_KEY]
    pl = api.portal.get_tool('portal_languages')
    supported_languages = pl.getSupportedLanguages()
    roots = []
    # be nice w/ multilingual sites
    for lang in supported_languages:
        if lang in site.objectIds():
            roots.append((lang, site[lang]))
    if not roots:
        roots = [(site.Language(), site), ]
    for lang, root in roots:
        new_id = content_id_prefix + '-' + lang
        if new_id not in root.objectIds():
            page = api.content.create(
                container=root,
                type='Document',
                id=new_id,
                title='Cookie law - message %s' % lang,
            )
            page.setText(DEFAULT_MSG)
            page.setExcludeFromNav(True)
            # TODO: handle dexterity types
            # page.text = RichTextValue(
            #     raw=u"Cookie message: update this text as you like!",
            #     mimeType='text/plain',
            #     encoding='utf-8'
            # )
            # page.exclude_from_nav = True
            page.reindexObject()
            logger.info('created %s' % page.absolute_url_path())
