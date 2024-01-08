from setuptools import setup, find_packages

setup(
    name='Cal',  # Replace with your package's name
    version='0.1',  # Your package's version
    author='Your Name',  # Your name
    author_email='your.email@example.com',  # Your email
    description='A short description of your package',  # A short description # Long description read from the readme file # Type of the long description, usually markdown or plain text
    url='http://example.com',  # Your package's website or repository
    packages=find_packages(),  # Automatically find your package
    install_requires=[
        # List of dependencies, for example:
        # 'numpy>=1.18.1',
        # 'pandas>=1.0.3',
    ],
    classifiers=[
        # Trove classifiers (https://pypi.org/classifiers/)
        # Examples:
        # 'Development Status :: 4 - Beta',
        # 'Intended Audience :: Developers',
        # 'License :: OSI Approved :: MIT License',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.8',
    ],
)
