from setuptools import setup

setup(name='pipelines',
      version='0.0.1',
      description='Sample PySpark Application for use with Databricks Connect',
      author='Guanjie Shen',
      packages=['pipelines', 'pipelines.utils', 'pipelines.jobs'],
      zip_safe=False)