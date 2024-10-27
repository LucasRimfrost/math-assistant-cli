from setuptools import setup, find_packages
from math_assistant.version import __version__

setup(
    name="math-assistant-cli",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "anthropic>=0.5.0",
        "Pillow>=9.0.0",
        "rich>=10.0.0",
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "math-assist=math_assistant.cli:main",
        ],
    },
    python_requires=">=3.8",
    author="Lucas Rimfrost",
    author_email="lucas.rimfrost@gmail.com",
    description="AI-powered math problem solver and tutor",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LucasRimfrost/math-assistant-cli",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="mathematics education ai tutor claude anthropic",
)
