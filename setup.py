from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1.0',
      description='Clean Folder',
      author='Logush Ruslan',
      author_email='phenix@bigmir.net',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder=clean_folder.clean:start']}
)