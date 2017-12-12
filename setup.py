from setuptools import setup, find_packages

README = open('README.txt').read()

setup(
    name = "django-weekday-field",
    version = "2.0.0",
    description = "Weekday field for django models",
    url = "https://github.com/Idona-has/django-weekday-field",
    author = "Rob Kent (Idona)",
    author_email = "info@idona.co.uk",
    packages = find_packages(),
    package_data = {
        '': ['static/*/*/*'],
    },
    classifiers = [
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
    install_requires=["Django"],
    tests_require=["Django"],
    test_suite="runtests.runtests",
    )
