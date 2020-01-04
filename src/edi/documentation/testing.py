# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import edi.documentation


class EdiDocumentationLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=edi.documentation)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edi.documentation:default')


EDI_DOCUMENTATION_FIXTURE = EdiDocumentationLayer()


EDI_DOCUMENTATION_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDI_DOCUMENTATION_FIXTURE,),
    name='EdiDocumentationLayer:IntegrationTesting',
)


EDI_DOCUMENTATION_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDI_DOCUMENTATION_FIXTURE,),
    name='EdiDocumentationLayer:FunctionalTesting',
)


EDI_DOCUMENTATION_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EDI_DOCUMENTATION_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EdiDocumentationLayer:AcceptanceTesting',
)
