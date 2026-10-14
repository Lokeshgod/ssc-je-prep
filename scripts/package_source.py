from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
root=Path(__file__).resolve().parents[1]
target=root/'dist/materials/ssc-je-website-source.zip'
with ZipFile(target,'w',ZIP_DEFLATED) as z:
 for part in ['dist','scripts','.github']:
  for p in sorted((root/part).rglob('*')):
   if p.is_file() and p != target and '__pycache__' not in str(p):
    z.write(p,p.relative_to(root))
 z.write(root/'README.md','README.md')
 z.write(root/'.gitignore','.gitignore')
print(target.name,target.stat().st_size)
