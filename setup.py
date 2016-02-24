from setuptools import setup

setup(
    name='yamlbro',
    version='0.0.1',
    packages=[
        'yamlbro',
    ],
    url='https://github.com/TechnicalBro/yaml-bro',
    license='',
    author='Brandon Curtis',
    author_email='bcurtis@artectis.com',
    description="""
    Easy PyYaml wrapper and utilities that give a plethora of features.
        """,
    install_requires=[
        'PyYaml'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
        'Topic :: Text Processing',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
