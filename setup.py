from setuptools import setup, find_packages

setup(
    name="topsis-102266001",
    version="1.0.1",
    author="Sonal Kasana",
    author_email="skasana_be22@thapar.edu",
    description="TOPSIS assignment",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/snlkasana/topsis-snl",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
