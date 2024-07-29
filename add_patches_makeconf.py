makeConf = open("etc/portage/make.conf", "r")
Conf = open(input())
AlterContent = Conf.readlines()
close(Conf)

content = ""

makeConfLines = makeConf.readlines()
close(makeConf)
linesToAppend = []

for line in AlterContent:
	found = False
	for dstLine in makeConfLines:
		if(line.split("=")[0]==dstLine[0]):
			dstLine = dstLine[0:dstLine.length()]+" "+line.split("\"")[1]+"\""
			found = True
	if not found:
		linesToApped.append(line)
for line in makeConfLines:
	content+=line+"\n"
for line in linesToAppend:
	content+=line+"\n"
makeConf = open("etc/portage/make.conf", "w")
makeConf.write(content)
makeConf.flush()
close(makeConf)
