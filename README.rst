=================
django-model-i18n 
=================

django-model-i18n is a django application that tries to make multilingual data in models less painful.

The main features/goals are:

* Easy installation and integration. No data or schema migration pain.
* Each multilingual model stores it's translations in a separate table, which from django is just a new model dynamically created, we call this model the translation model.
* You can add (or even drop) i18n support for a model at any time and you won't need to migrate any data or affect the original model (we call this the master model) table definition. This allows you to develop your apps without thinking in the i18n part (you even can load data for the main language and you won't need to migrate it) and when you are comfortable with it register the multilingual options and start working with the content translations.
* 3rd party apps friendly. You can add i18n support to the existing models without modifying their definition at all (think in apps you can't modify directly for example djago.contrib.flatpages).
 
Installation
===========

* cloning repository
 
Configuration
=============

In module settings::

    MODEL_I18N_CONF = 'project.i18n_conf'

also add 'django.middleware.locale.LocaleMiddleware' into MIDDLEWARE_CLASSES::

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        ## IF CACHE MIDDLEWARE IS SETTING PUT HERE
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    ) 

Notes
=====

If you will translate models that are registered into django-admin such as django-flatpages
do this::

    from model_i18n import loaders
    from model_i18n import translator

    admin.autodiscover()
    loaders.autodiscover()
  
    class ModelTranslation(translator.ModelTranslation):
        fields = ('title', 'content')
        
    translator.register(Model, ModelTranslation) # Model class should be imported from your django-app
  
into MODEL_I18N_CONF file
 
Changes
=======
* now translation model returns user language and keeps set_language method logical:

  * get_query_set -> method return actual i18n translation if there is one else return master language, value used from django.utils.translation.get_language(). This modified to avoid change external source code like flatpages middleware.
  * set_language -> method return model for language sent as parameters used from django.utils.translation.get_language()    
                  
* changing " for ' into sql queries it is understand as table field for postgresql

* setup_admin changed to load "related_name" manager


