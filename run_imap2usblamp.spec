# -*- mode: python -*-

from os import path
pwd = path.abspath(path.curdir)

block_cipher = None

libusb = [
    ('pyusblamp\\libusb', 'pyusblamp\\libusb'),
]

a = Analysis(['run_imap2usblamp.py'],
             pathex=[pwd],
             binaries=libusb,
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='imap2usblamp',
          debug=False,
          strip=False,
          upx=True,
          console=False )
