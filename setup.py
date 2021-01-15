from setuptools import setup, find_packages

setup(
    name='NIFTANALYSER',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='ISC',
    author='Manu Bhat',
    author_email='manugbhat@gmail.com',
    description='Nifty 50 stocks VWAP Analysis',
    include_package_data=True,
    install_requires=[
        "nsepy", "PyQt5"
    ],
    entry_points={"console_scripts": ["NIFTYANALYSER.py"]},
)
