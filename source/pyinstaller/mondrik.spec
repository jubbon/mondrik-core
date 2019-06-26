# -*- mode: python -*-

import os
import six
import xml
import ansible

block_cipher = None


a = Analysis(['/usr/src/app/__main__.py'],
             pathex=['/usr/src/dist'],
             binaries=[('/usr/local/lib/python3.7/site-packages/ansible/config/', 'ansible/config/')],
             datas=[
                (six.__file__, '.'),
                (os.path.dirname(xml.__file__), 'xml'),
                (os.path.dirname(ansible.__file__), 'ansible')
             ],
             hiddenimports=['configparser', 'smtplib', 'csv', 'logging.handlers', 'distutils.version', 'distutils.spawn', 'pty'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)


pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=block_cipher)


exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='mondrik',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
