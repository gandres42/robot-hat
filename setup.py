import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="robot_hat",
    version="1.0",
    author="Gavin Andres",
    description="An version of robot-hat that sucks less",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gandres42/robot-hat",
    license="LICENSE.txt",
    packages=setuptools.find_packages()
)