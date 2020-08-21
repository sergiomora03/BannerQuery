import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BannerQuery", # Replace with your own username
    version="0.0.1",
    author="Sergio A. Mora Pardo",
    author_email="sergiomora823@gmail.com",
    description="Easy tool to do query from Banner by Ellucian to solve problems and decision making!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sergiomora03/BannerQuery",
    packages=setuptools.find_packages(),
    classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
  ],
    python_requires='>=3.6',
)
