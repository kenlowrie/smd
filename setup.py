from setuptools import setup
from sys import version_info

setup(name='livesmd',
      version='0.3.8',
      description='Live Script Markdown',
      url='https://github.com/kenlowrie/smd',
      author='Ken Lowrie',
      author_email='ken@kenlowrie.com',
      license='Apache',
      packages=['livesmd', 'livesmd.smd'],
      install_requires=['kenl380.pylib'],
      entry_points = {
        'console_scripts': ['livesmd=livesmd.livesmd:smd_parse_file',
                            'mklivesmd=livesmd.mklivesmd:mklivesmd',
        ],
      },
      include_package_data=True,
      zip_safe=False)
