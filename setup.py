from setuptools import setup, find_packages

setup(
    name='pyqt-show-long-text-as-tooltip-list-widget',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QListWidget which shows text as tooltip longer than widget\'s size',
    url='https://github.com/yjg30737/pyqt-show-long-text-as-tooltip-list-widget.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)