from distutils.core import setup
import os

root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

data_files = []
for dirpath, dirnames, filenames in os.walk('ajax_filtered_fields'):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        continue
    elif filenames:
        for f in filenames:
            data_files.append(os.path.join(dirpath[21:], f))
        
version = "%s.%s" % __import__('ajax_filtered_fields').VERSION[:2]

setup(name='django-ajax-filtered-fields',
      version=version,
      description='Django fields for many to many and foreign key ajax filtered relations',
      author='Francesco Banconi',
      author_email='francesco.banconi@gmail.com',
      url='http://code.google.com/p/django-ajax-filtered-fields/',
      package_dir={'ajax_filtered_fields': 'ajax_filtered_fields'},
      packages=['ajax_filtered_fields', 'ajax_filtered_fields.forms'],
      package_data={'ajax_filtered_fields': data_files},
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
