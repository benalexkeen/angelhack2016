from setuptools import setup, find_packages

data = dict(
    name="algorithms",
    version="0.1",
    install_requires=[],
    data_files=[],
    packages=find_packages(),
)

if __name__ == '__main__':
    setup(**data)