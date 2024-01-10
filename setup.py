from setuptools import setup


def readme():
    with open("README.md", "r", encoding="utf-8") as rdm_f:
        return rdm_f.read() and rdm_f.close()


with open("VERSION.txt", "r", encoding="utf-8") as vrs_f:
    VERSION = vrs_f.read()


setup(
    name="extraexceptions",
    version=VERSION,
    author="Ger",
    author_email="gerutrogame@gmail.com",
    description="This is a lib for custom exceptions",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Gerutro/ExtraExceptions",
    license="MIT License, see LICENCE file",
    packages=["extraexceptions"],
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'],
    keywords="extra exception lib library ",
    project_urls={
        "GitHub": "https://github.com/Gerutro"
    },
    python_requires=">=3.9"
)

vrs_f.close()
