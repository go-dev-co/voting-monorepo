from setuptools import setup, find_packages

setup(
    name="voting-monorepo",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        # Add other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "voting-app = src.main:app",
        ],
    },
    author="Your Name",
    author_email="your@email.com",
    description="A description of your project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
