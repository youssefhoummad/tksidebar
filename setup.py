import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tksidebar",
    version="0.3.0",
    author="youssef hoummad",
    author_email="youssefhoummad@outlook.com",
    description="Add nice sidebar to tkinter apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/youssefhoummad/tksidebar",
    project_urls={
        "Bug Tracker": "https://github.com/youssefhoummad/tksidebar/issues",
    },
    classifiers=[
          'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
