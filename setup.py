from setuptools import setup, find_packages

setup(
    name="math-assistant",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "anthropic>=0.5.0",
        "Pillow>=9.0.0",
    ],
    python_requires=">=3.8",
    author="Lucas Rimfrost",
    author_email="lucas.rimfrost@gmail.com",
    description="A Math Assistant using Claude API for help with mathematics problems",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/math-assistant",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
)
