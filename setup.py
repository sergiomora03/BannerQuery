from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'BannerQuery',         # How you named your package folder (MyLib)
  packages = ['BannerQuery'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Query from Banner by Ellucian made easy to solve problems and decision making!',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Sergio A. Mora Pardo',                   # Type in your name
  author_email = 'sergiomora823@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/sergiomora03/BannerQuery',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/sergiomora03/BannerQuery/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Banner', 'Query', 'Ellucian', 'Poli', 'SQL', 'Python'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'cx_Oracle',
          'math',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)