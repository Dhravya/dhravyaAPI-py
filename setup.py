from distutils.core import setup



setup(
  name = 'dhravyaAPI',         # How you named your package folder (MyLib)
  packages = ['dhravyaAPI'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This is an API that I made while learning and it does a lot of cool things like OCR and QR code generation',   # Give a short description about your library
  author = 'Dhravya Shah',                   # Type in your name
  author_email = 'dhravyashah@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/dhravya',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Dhravya/dhravyaAPI/archive/refs/tags/v0.2.tar.gz',    # I explain this later on
  keywords = ['API wrapper', 'qrcode', 'ocr', 'dhravya'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'aiohttp'
      ],
  long_description="Check https://github.com/dhravya/dhravyaapi for more information",
  long_description_content_type='text/markdown',
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)