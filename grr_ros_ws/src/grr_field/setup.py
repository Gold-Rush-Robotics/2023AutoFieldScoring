from setuptools import setup

package_name = 'grr_field'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='grr',
    maintainer_email='philip@randomsmiths.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'field = grr_field.field:main',
            'viewer = grr_field.testImage:main',
            'cubes = grr_field.countCubes:main',
        ],
    },
)
