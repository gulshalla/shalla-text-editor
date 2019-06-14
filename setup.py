import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shalla-editor",
    version="0.0.1",
    author="Omar Shalla",
    description="A text editor built using Python3",
    url="https://github.com/gulshalla/shalla-editor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)