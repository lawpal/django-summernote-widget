from setuptools import find_packages, setup


setup(
    name = 'django-summernote-widget',
    version = '0.1.1',
    description = "A Summernote textarea widget for Django",
    long_description = open('README.md').read(),
    author = 'Jamie Connolly',
    author_email = 'jamie@lawpal.com',
    url = 'https://github.com/lawpal/django-summernote-widget/',
    license = 'MIT',
    packages = find_packages(exclude=('tests', 'docs')),
    include_package_data = True,
    install_requires = ['Django>=1.2'],
    zip_safe = False,
    test_suite = 'tests'
)
