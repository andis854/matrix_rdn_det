from distutils.core import setup
setup(
  name = 'matrix_rdn_det',        
  packages = ['matrix_rdn_det'], 
  version = '0.1',    
  license='MIT',     
  description = 'Randomize a matrix with the determinant value as parameter.E',   
  author = 'Anders Israelsson',                
  author_email = 'anders.israelsson@math.uu.se',     
  url = 'https://github.com/andis854/matrix_rdn_det',   
  download_url = 'https://github.com/andis854/matrix_rdn_det/archive/refs/tags/v_0.1.tar.gz',   
  keywords = ['linear algebra', 'matrix', 'random', 'determinant'],   
  install_requires=[            # I get to this in a second
          'numpy',
          'sys',
          'argparse',
          'matrix_rdn_det'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.10',
  ],
)
