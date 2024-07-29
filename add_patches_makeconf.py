makeConf = open("etc/portage/make.conf", "r")
Conf = open(input("Enter path for patches file: "))
AlterContent = Conf.readlines()
Conf.close()

content = ""

makeConfLines = makeConf.readlines()
makeConf.close()
linesToAppend = []

for line in AlterContent:
	found = False
	for i in range(0, len(makeConfLines)):
		if(line.split("=")[0]==makeConfLines[i].split("=")[0]):
			makeConfLines[i] = makeConfLines[i][0:len(makeConfLines[i])-2]+" "+line.split("\"")[1]+"\"\n"
			found = True
	if not found:
		linesToAppend.append(line)
for line in makeConfLines:
	content+=line
for line in linesToAppend:
	content+=line
makeConf = open("etc/portage/make.conf", "w")
makeConf.write(content)
makeConf.flush()
makeConf.close()
