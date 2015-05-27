====================
collective.cookielaw
====================

Add cookie notice to your Plone site to be compliant with EU cookie law.

It uses `https://github.com/silktide/cookieconsent2` to render the message.

Message
-------

The message stays in Plone document that you can add to each root of your site.

The package generates a default one on install with ID `cookie-law-msg-LANG`.

So that, if you have one language and not root language folders, you'll have

    /Plone/cookie-law-msg-en

if your site is in english.

If you have more languages you'll have:

    /Plone/cookie-law-msg-en
    /Plone/cookie-law-msg-fr
    /Plone/cookie-law-msg-es

and so on.

If you have root language folder (using LinguaPlone or PAM) you'll have:

    /Plone/en/cookie-law-msg-en
    /Plone/fr/cookie-law-msg-fr
    /Plone/es/cookie-law-msg-es


CookieConsent options
---------------------

You can tweak CookieConsent JSON options via registry with the key `collective.cookielaw.jsonoptions`.

You can also provide per-lang text for the dismiss button via the key `collective.cookielaw.confirm_button_text` that is a dictionary like:

    {'en': 'Ok!', 'it': 'Ho capito!'}


NOTE: the link that brings you to the policy page and its text are empty because you can handle them
in the text of the message.
