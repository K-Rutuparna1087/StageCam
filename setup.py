from setuptools import setup, find_packages

setup(
    name='stagecam',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'mediapipe',
        'numpy',
    ],
    author='K Rutuparna',
    description='A Python library for face-aware frame tracking like Apple Center Stage',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/K-Rutuparna1087/StageCam.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
