from setuptools import find_packages, setup

long_description = """Atlas MicroPython Robotics Programming Framework."""

setup(
    name="Atlas",
    packages=[package for package in find_packages()
              if package.startswith("Atlas")],
    install_requires=["pyserial",],
    author="Matthew McCann",
    url="https://github.com/MattCodes03/Atlas",
    description="Atlas MicroPython Robotics Programming Framework",
    long_description=long_description,
    keywords="serial hardware uart pico raspberry micropython",
    license="MIT",
    version="0.1",
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe=False,
)
