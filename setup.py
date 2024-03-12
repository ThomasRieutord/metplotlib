import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metplotlib",
    version="0.1.0",
    author="Thomas Rieutord",
    author_email="thomas.rieutord@met.ie",
    description="""Meteorological plotting utilities""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThomasRieutord/metplotlib",
    packages=setuptools.find_packages(),
    classifiers=(
        "Environment :: Console" "Programming Language :: Python :: 3",
        "Operating System :: Linux",
        "Development Status :: 2 - Pre-Alpha",
    ),
)
