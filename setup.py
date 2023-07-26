from setuptools import find_packages, setup

long_description = ""

setup(
    name="rfc_calculator",
    version="0.0.1",
    description="Python RFC calculator.",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/altscore/rfc-calculator-python",
    author="AltScore",
    author_email="developers@altscore.ai",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.80",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pydantic",
    ],
    extras_require={
        "dev": ["pytest>=7.0"],
    },
    python_requires=">=3.8",
)
