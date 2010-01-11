from setuptools import setup, find_packages
 
setup(
    name='django-feedback',
    version=__import__('feedback').__version__,
    description='Basic Django Feedback',
    author='Luke Hutscal',
    author_email='luke@creaturecreative.com',
    url='http://github.com/girasquid/django-feedback/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)