from setuptools import setup, find_packages

setup(
    name='clock-server',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'clock-server=server:app',
            'clock-client=client:main'
        ]
    },
    description='A REST API-based alarm server and command-line client.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/your-repo/clock-server',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
