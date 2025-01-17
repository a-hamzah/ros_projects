from setuptools import find_packages, setup
import os # add this line
from glob import glob # add this line

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))) # add this line
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jammy',
    maintainer_email='Spellbreaker907@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = my_package.my_node:main',
            'test = my_package.test:main'
        ],
    },
)

