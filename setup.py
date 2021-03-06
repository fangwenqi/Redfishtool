from setuptools import setup

setup(name='redfishtool',
      version='1.0.0',
      description='Redfishtool package and command-line client',
      author='DMTF',
      author_email='dmtf@dmtf.org',
      license='BSD 3-clause "New" or "Revised License"',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3.4',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Communications'
      ],
      keywords='Redfish',
      url='https://github.com/DMTF/Redfishtool',
      download_url='https://github.com/DMTF/Redfishtool/archive/1.0.0.tar.gz',
      packages=['redfishtool'],
      scripts=['redfishtool.py'],
      install_requires=['requests']
      )
