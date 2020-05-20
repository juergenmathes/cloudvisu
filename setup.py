import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cloudvisu",
    version="0.0.1",
    author="Juergen Mathes",
    description="A package to visualize point clouds and boxes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juergenmathes/cloudvisu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
