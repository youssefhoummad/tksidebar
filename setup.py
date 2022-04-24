import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tk_sidebare",
    version="0.1",
    author="youssef hoummad",
    author_email="youssefhoummad@outlook.com",
    description="Add nice sidebare to tkinter apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/youssefhoummad/tk_sidebare",
    project_urls={
        "Bug Tracker": "https://github.com/martinet101/win32mica/issues",
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