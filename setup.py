from setuptools import setup
from sys import version_info

setup(name='smd',
      version='0.3.8',
      description='Script Markdown',
      url='https://github.com/kenlowrie/smd',
      author='Ken Lowrie',
      author_email='ken@kenlowrie.com',
      license='Apache',
      packages=['smd', 'smd.core'],
      install_requires=['kenl380.pylib'],
      entry_points = {
        'console_scripts': ['smd=smd.smd:smd_parse_file',
                            'livesmd=smd.livesmd:livesmd',
                            'ismd=smd.ismd:ismd',
                            'smdparse=smd.smdparse:parse'
        ],
      },
      include_package_data=True,
      zip_safe=False)
