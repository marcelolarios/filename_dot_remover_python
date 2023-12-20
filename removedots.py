'''
cd /filespath/
python3 removedots.py

'''
import os
import glob

def filename_replacer(filename):
	fname, fext = os.path.splitext(filename)
	return fname.replace(".", " ") + fext
  
print('\nFiles found:')

for root, _, files in os.walk(os.getcwd()):
	os.chdir(os.path.join(root))
	for name in glob.glob('*.*.*'): #dots in filename
		troca = filename_replacer(name)
		print(name)
		os.rename(name, troca)

print('\nDone!')