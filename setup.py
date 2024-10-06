from setuptools import setup, find_packages

setup(
    name='FlexLang',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pygame',
    ],
    entry_points={
        'console_scripts': [
            'flexengine=flexengine.engine:main',
            'flexlang-ide=flexlang_ide.flexlang_ide:main',
        ],
    },
    description='FlexLang Game Development Library',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/FlexLang',  # Update with your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
