DIRECTORIES = [
	"icon_packs/playstation",
	"icon_packs/xbox",
	"fallback_icon_pack"
]

import subprocess
import os
import shutil
base_cwd = os.getcwd()

for directory in DIRECTORIES:
	os.chdir(directory)

	if os.path.isdir("notes_temp"):
		shutil.rmtree("notes_temp")
	os.mkdir("notes_temp")

	for _file in os.listdir("notes"):
		if _file.endswith(".png"):
			if not "target" in _file and not "small" in _file:
				subprocess.call(["magick", "convert", "notes/"+_file, "(", "+clone", "-background", "black", "-shadow", "80x0+10+10", ")", "+swap", "-background", "none", "-layers", "merge", "+repage", "-crop", "128x128+0+0", "notes_temp/" + _file])
			else:
				shutil.copy("notes/"+_file, "notes_temp/"+_file)
	subprocess.call(["atlasify", "-ast", "-o", "atlas.png", "-p", "2", "--trim", "--extrude", "1", "-m 1024,1024", "--save", "./notes_temp"])
	shutil.rmtree("notes_temp")
	os.chdir(base_cwd)
