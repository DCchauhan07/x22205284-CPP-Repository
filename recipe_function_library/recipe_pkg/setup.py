import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="food-calorie-tracker",
    version="0.0.1",
    author="Adminuser07",
    author_email="x22205284@student.ncirl.ie",
    description="A simple food calorie tracker package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DCchauhan07/CPP-Final-Project.git",
    packages=setuptools.find_packages(),
    install_requires=[],  
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
