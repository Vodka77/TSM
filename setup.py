import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Check-X",
    version="0.0.1",
    author="ruks",
    author_email="author@example.com",
    description="By : Vodka_Tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vodka77/TSM",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
