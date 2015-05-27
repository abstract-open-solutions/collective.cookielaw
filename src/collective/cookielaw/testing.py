# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import collective.cookielaw


class CollectiveCookielawLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            collective.cookielaw,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.cookielaw:default')


COLLECTIVE_COOKIELAW_FIXTURE = CollectiveCookielawLayer()


COLLECTIVE_COOKIELAW_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_COOKIELAW_FIXTURE,),
    name='CollectiveCookielawLayer:IntegrationTesting'
)


COLLECTIVE_COOKIELAW_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_COOKIELAW_FIXTURE,),
    name='CollectiveCookielawLayer:FunctionalTesting'
)


COLLECTIVE_COOKIELAW_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_COOKIELAW_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveCookielawLayer:AcceptanceTesting'
)
