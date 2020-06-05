from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = ''.join(f.readlines())

setup(
    name='dcso_converter',
    version='0.1.0',
    description='Tool for converting between JSON and DSCO maDMPs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Marek Suchánek',
    keywords='madmp dmp jinja2 conversion',
    license='MIT',
    url='https://github.com/MarekSuchanek/dcso-converter',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    zip_safe=False,
    python_requires='>=3.5, <4',
    install_requires=[
        'click',
        'jinja2',
        'rdflib',
    ],
    entry_points={
        'console_scripts': [
            'dcso_converter=dcso_converter:main',
        ],
    },
)