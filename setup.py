try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'NLP Notebooks',
    'author': 'Alexis K.',
    'url': '',
    'download_url': '',
    'author_email': '',
    'version': '0.1',
    'install_requires': ['nose', 'nltk'],
    'packages': [],
    'scripts': [],
    'name': 'nlp-notebooks'
}

setup(**config)
