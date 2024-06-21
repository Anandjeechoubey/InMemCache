from setuptools import setup, find_packages

setup(
    name='InMemCache',
    version='0.1.0',
    description='A Python library for in-memory caching with multiple eviction policies',
    author='Anand Jee Choubey',
    author_email='anandjechoubey@gmail.com',
    url='https://github.com/Anandjeechoubey/InMemCache',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
