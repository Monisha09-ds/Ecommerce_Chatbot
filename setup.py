
from setuptools import find_packages, setup

setup(
    name="Ecommercechatbot",
    version="0.0.1",
    author="Monisha",
    author_email="sabikunmonisha01@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-openai','datasets','pypdf','python-dotenv','flask']
)