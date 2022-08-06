from setuptools import setup

with open("requirements.txt") as fh:
    install_requires = fh.read()

setup(
    name='happyfunc',
    version='0.2.13',
    url='https://github.com/inerfire/happyfunc',
    author='inerfire',
    author_email='happy@email.com',
    packages=["happyfunc"],
    install_requires=install_requires,
    zip_safe=True,
)
