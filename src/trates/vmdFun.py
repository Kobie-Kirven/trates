def runTclFile(vmdPath, fileName):
        """Run the TCL file"""
        os.system(
            vmdPath + " -dispdev text -e " + fileName + " > out.txt"
        )
        os.system("rm " + fileName)


def createTclFile(
    templateFileName, replaceDict, newFileName="temp.tcl"
):
    with open(newFileName, "w") as merge:
        lines = EditStructure.readTemplateFile(templateFileName)
        for line in lines:
            for i in replaceDict:
                if i in line:
                    line = line.replace(i, str(replaceDict[i]))
            merge.write(line)

def readTemplateFile(templateFileName):
        with open(
            pkg_resources.resource_filename("src", "tcl_scripts")
            + "/"
            + templateFileName
        ) as fn:
            return fn.readlines()

def makeAndRunTclFile(templateFileName, replaceDict, vmdPath):
    EditStructure.createTclFile(templateFileName, replaceDict)
    EditStructure.runTclFile(vmdPath, "temp.tcl")