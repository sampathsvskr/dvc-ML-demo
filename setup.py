from setuptools import setup

with open("README.md","r",encoding='utf-8') as f:
    long_description=f.read()

setup(
    name="src",
    version="0.0.1",
    author="Sampath",
    description="DVC practice",
    long_description=long_description,
    long_description_type="text/markdown",
    url="https://github.com/sampathsvskr/dvc-ML-demo",
    author_email="sampathkumarreddysvskr@gmail.com",
    packages=['src'],    
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]


)