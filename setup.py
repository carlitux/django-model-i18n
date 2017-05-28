
from setuptools import setup, find_packages
 
setup(
    name='django-model-i18n',
    version='0.1',
    description='Model translation for Django using a registration-based approach and seperate translation tables.',
    author='Florian Ledermann',
    author_email='ledermann@ims.tuwien.ac.at',
    url='https://github.com/floledermann/django-model-i18n',
    license='BSD License',
    packages=find_packages(exclude=['test_project']),
    # include all data defined in MANIFEST.in
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
    ],
    zip_safe=False,
)
