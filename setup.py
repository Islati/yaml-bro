from setuptools import setup

setup(
    name='yamlbro',
    version='0.0.1',
    packages=[
        'yamlbro',
    ],
    package_dir={'yamlbro': 'yamlbro'},
    include_package_data=True,
    url='',
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
    ]
)
