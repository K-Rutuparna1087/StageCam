from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='stagecam',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'mediapipe',
        'numpy',
    ],
    python_requires='>=3.7',
    author='K Rutuparna',
    description='A Python library for face-aware frame tracking like Apple Center Stage',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/K-Rutuparna1087/StageCam',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
