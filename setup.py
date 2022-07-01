import setuptools
setuptools.setup(
    name='mkfol',
    version='0.1',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    entry_points={
        'console_scripts': ['mkfol=src.mkfol:mkfol']
    },
    author='Sulthan Abiyyu Hakim',
    author_email="sabiyyuhakim@student.ub.ac.id",
    description='Folder maker based on template',
    install_requires=[
        'setuptools',
    ],
    python_requires='>=3.5',
)
