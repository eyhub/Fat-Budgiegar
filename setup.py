from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.01",
    description="math quiz game package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="eyhub",
    author_email="ozgurakbulut2@gmail.com",
    url="https://github.com/eyhub/Fat-Budgiegar",
    packages=find_packages(),
    install_requires=[
        # No external dependencies in this example
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)