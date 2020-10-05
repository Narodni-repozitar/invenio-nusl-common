# -*- coding: utf-8 -*-


'''NR common data types'''

import os

from setuptools import find_packages, setup

readme = open('README.md').read()

tests_require = [
    'pytest',
    'pytest-cov',
    'oarepo[tests]'
]

extras_require = {
    'docs': [
        'Sphinx>=1.5.1',
    ],
    'tests': tests_require,
    'all': []
}

for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

setup_requires = [
    'pytest-runner>=2.6.2',
]

install_requires = [
    'pycountry>=19.0.0',
    'arrow',
    'isbnlib>=3.10.3,<4.0.0',
    'python-stdnum>=1.14, <2.0',
    'IDUtils>=1.1.8, <2.0.0',
    'oarepo-invenio-model>=2.0.0, <3.0.0',
    'oarepo-multilingual>=2.0.0, <3.0.0',
    'oarepo-taxonomies>=2.5.0, <3.0.0',
    'oarepo-mapping-includes==1.2.0',  # TODO: fixnout bug a rozvolnit závislost
    'pytest-invenio==1.3.4'
]

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('nr_common', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='nr-common',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='Nationa Repository common model Invenio',
    license='MIT',
    author='Daniel Kopecký',
    author_email='Daniel.Kopecky@techlib.cz',
    url='',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_jsonschemas.schemas': [
            'nr_common = nr_common.jsonschemas'
        ],
        'invenio_pidstore.minters': [
            'nr = nr_common.minters:nr_id_minter',
        ],
        'invenio_pidstore.fetchers': [
            'nr = nr_common.fetchers:nr_id_fetcher',
        ],
        'invenio_db.alembic': [
            'nr = nr_common:alembic',
        ],
        'oarepo_mapping_includes': [
            'nr_common = nr_common.mapping_includes'
        ],
        'invenio_search.mappings': [
            'nr_common = nr_common.mappings'
        ]
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 3 - Planning',
    ],
)
