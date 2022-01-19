import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openweathermap",
    version="0.1.1",
    author="Ali Shekari",
    author_email="alishekari1991@outlook.com",
    description="openweathermap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alishekari/openweathermap",
    packages=setuptools.find_packages(),
    install_requires=['django', 'requests'],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
