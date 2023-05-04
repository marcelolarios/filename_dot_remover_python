'''
cd /filespath/
python3 tiraponto.py
'''
import glob
import os

def filename_replacer(filename):
  fname, fext = os.path.splitext(filename)
  return fname.replace(".", " ") + fext
  
print('\nFiles found:')
for name in glob.glob('*.*.*'): #dots in filename
	troca = filename_replacer(name)
	print(name)
	os.rename(name, troca)

print('\nDone!')