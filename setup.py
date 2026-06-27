# Code on local package installation

from setuptools import setup, find_packages

# Package metadata
__version__ = "0.0.1"
REPO_NAME = "E2E-ML-Project-with-mlflow"
AUTHOR_USER_NAME = "mbdev1993"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "developer_mb1993@outlook.com"

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name=SRC_REPO,                          # Package name
    version=__version__,                   # Package version
    author=AUTHOR_USER_NAME,               # Author name
    author_email=AUTHOR_EMAIL,             # Author email
    description="End-to-End ML Project with MLflow",
    long_description=long_description,     # Detailed project description
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        "Source Code": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    },
    package_dir={"": "mlProject"},               # Source code location
    packages=find_packages(where="mlProject"),   # Find packages inside src/
    include_package_data=True,
    install_requires=[
        # Add package dependencies here
        # Example:
        # "numpy",
        # "pandas",
        # "scikit-learn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)