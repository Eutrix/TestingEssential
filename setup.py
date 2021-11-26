# DONE settings.gradle rootProject.name
# DONE README.md
# DONE build.gradle archivesBaseName
# DONE /src/main/resources/mcmod.info
# DONE /src/main/kotlin/dev/eutrix/BadForgeTemplate/
# DONE .../BadForgeTemplate/BadForgeTemplate.kt
# ..... package
# ..... @Mod()
# ..... object BadForgeTemplate()

# Change this to True if you want to change the name 'eutrix' in the project to your own name
changeAuthor = False

newName = input('What will the name of the mod be?\n> ')

import os, pathlib
workingdir = input(f'Use {os.getcwd()} [Y/Enter] or another dir [/path/to/dir]?\n> ')
if workingdir in {'Y', 'y', ''}:
	workingdir = os.getcwd() 
workingdir = pathlib.Path(workingdir)
# I haven't tested using another working dir, will do later if I remember to do it

if changeAuthor:
	newAuthor = input('What is your name?\n> ')

newModID = input('What will the modid be?\n> ')
newDesc = input('Enter a short description for your mod\n> ')

print('\n=============================================================\n')

# I'll only explain the first one, as they are mostly the same
# build.gradle
buildFile = workingdir / 'build.gradle'
if buildFile.exists():
	with buildFile.open(mode = 'r+', encoding = 'UTF-8') as f:
		# Read the file and change the name
		newText = f.read().replace('BadForgeTemplate', newName) 
		if changeAuthor:
			newText = newText.replace('eutrix', newAuthor)
		
		# Go to the beginning of the file
		f.seek(0)
		# overwrite everything
		f.write(newText)
		# remove any stuff after the current position in case the new text is shorter than the old one
		f.truncate()
		print('Finished writing build.gradle')
else:
	print('No build.gradle, skipping')

# README.md
readme = workingdir / 'README.md'
if readme.exists():
	with readme.open(mode = 'w', encoding = 'UTF-8') as f:
		f.write(f'# {newName}\n\n{newDesc}')
		print('Finished writing README.md')
else:
	print('No README.md, skipping')


# settings.gradle
settingsFile = workingdir / 'settings.gradle'
if settingsFile.exists():
	with settingsFile.open(mode = 'r+', encoding = 'UTF-8') as f:
		newText = f.read().replace('BadForgeTemplate', newName)
		f.seek(0)
		f.write(newText)
		f.truncate()
		print('Finished writing settings.gradle')
else:
	print('No settings.gradle, skipping')

# mcmod.info
mcmodFile = workingdir / 'src/main/resources/mcmod.info'
if mcmodFile.exists():
	with mcmodFile.open(mode = 'r+', encoding = 'UTF-8') as f:
		newText = f.read().replace('BadForgeTemplate', newName)
		if changeAuthor:
			newText = newText.replace('eutrix', newAuthor)
		newText = newText.replace('badforgemodid', newModID)
		newText = newText.replace('BadDescription', newDesc)
		f.seek(0)
		f.write(newText)
		f.truncate()
		print('Finished writing mcmod.info')
else:
	print('No mcmod.info, skipping')

# src/main/kotlin/dev/<author>/
nameFolder = workingdir / 'src/main/kotlin/dev/eutrix/'
if changeAuthor and nameFolder.exists():
	os.rename(nameFolder, workingdir / f'src/main/kotlin/dev/{newAuthor}')
	print('Renamed /src/main/kotlin/dev/eutrix/')

if changeAuthor:
	nameFolder = workingdir / f'src/main/kotlin/dev/{newAuthor}'

# src/main/kotlin/dev/<author>/<newName>/
otherFolder = nameFolder / 'BadForgeTemplate'
if otherFolder.exists():
	os.rename(otherFolder, nameFolder / newName)
	print(f'Renamed {otherFolder}')
	otherFolder = nameFolder / newName

# <newName>.kt
baseFile = otherFolder / 'BadForgeTemplate.kt'
if baseFile.exists():
	os.rename(baseFile, otherFolder / f'{newName}.kt')
	print(f'Renamed {baseFile}')
else:
	print("Couldn't rename BadForgeTemplate.kt because it doesn't exist")

baseFile = otherFolder / f'{newName}.kt'
if baseFile.exists():
	with baseFile.open(mode = 'r+', encoding = 'UTF-8') as f:
		newText = f.read().replace('BadForgeTemplate', newName)
		newText = newText.replace('badforgetemplate', newName.lower())
		if changeAuthor:
			newText = newText.replace('eutrix', newAuthor)
		newText = newText.replace('badforgemodid', newModID)
		f.seek(0)
		f.write(newText)
		f.truncate()
		print(f'Finished writing {newName}.kt')
else:
	print(f"Couldn't rename {newName}.kt because it doesn't exist")