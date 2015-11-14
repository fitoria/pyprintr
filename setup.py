from setuptools import setup


setup(
    name="pyprintr",
    version="1.1",
    author="Eugenia Bahit",
    author_email="ebahit@member.fsf.org",
    packages=["printr"],
    url="http://www.python-printr.org/",
    license="GPL v3.0",
    description="Module that allows to emulate the print_r() PHP function",
    long_description=open('README.md').read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
