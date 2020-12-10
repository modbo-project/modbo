import setuptools

setuptools.setup(
    name="pytg",
    version="0.0.1",
    author="aegroto",
    author_email="aegroto@protonmail.com",
    description="PyTG boilerplate",
    long_description="PyTG boilerplate",
    long_description_content_type="text/markdown",
    url="https://github.com/pytg/pytg",
    packages=["pytg", "pytg.components", "pytg.commands", "pytg.remote", "pytg.testing"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)