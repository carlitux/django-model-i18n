"""
Functions on this module are added to every manager on each multilingual model.
"""
from model_i18n.query import TransQuerySet
from model_i18n.conf import MULTIDB_SUPPORT

from django.utils.translation import get_language

def get_query_set(self):
    """ Adds TransQuerySet support """
    qs = self.get_query_set_orig()
    kwargs = {'query': qs.query}
    # Pass DB attribute if multi-db support is present.
    if MULTIDB_SUPPORT:
        kwargs['using'] = qs._db
    # return the global language set for user, to change the language use set_language function
    return TransQuerySet(self.model, **kwargs).set_language(get_language()[:2])

def set_language(self, language_code):
    """ Sets the current language """
    qs = self.get_query_set_orig()
    kwargs = {'query': qs.query}
    # Pass DB attribute if multi-db support is present.
    if MULTIDB_SUPPORT:
        kwargs['using'] = qs._db
    return TransQuerySet(self.model, **kwargs).set_language(language_code)

