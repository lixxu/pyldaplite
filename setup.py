"""
pyldaplite
----------------

Simple python-ldap handy wrapper
"""
from setuptools import setup

setup(
    name='pyldaplite',
    version='0.1.3',
    url='https://github.com/lixxu/pyldaplite',
    license='BSD',
    author='Lix Xu',
    author_email='xuzenglin@gmail.com',
    description='Simple package for LDAP',
    long_description=__doc__,
    packages=['pyldaplite'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'python-ldap',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
