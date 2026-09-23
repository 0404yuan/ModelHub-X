from setuptools import find_packages, setup

setup(
    name="accelerate",
    version="0.0.1",
    description="A simple way to train and use PyTorch models with multi-GPU, TPU, mixed-precision.",
    long_description="Accelerate: a simple way to launch, train, and use PyTorch models on almost any device and distributed configuration.",
    packages=find_packages(exclude=["tests", "examples"]),
    install_requires=[
        "numpy>=1.17",
        "packaging>=20.0",
        "psutil",
        "pyyaml",
        "torch>=1.10.0",
        "safetensors>=0.3.1",
    ],
    python_requires=">=3.8.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
)
