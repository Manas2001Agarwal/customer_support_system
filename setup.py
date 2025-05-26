from setuptools import find_packages, setup

setup(name="flipkart-product-assistant",
      version='0.0.1',
      author = "Manas Agarwal",
      author_email="manasmrt10@gmail.com",
      packages=find_packages(),
      install_requires = ['langchain','langchain_astradb'])