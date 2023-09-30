import maya.api.OpenMaya as om

class O4MRenameCmd(om.MPxCommand):

    kPluginCmdName = "o4m_rename"
    def __init__(self):
        om.MPxCommand.__init__(self)

    @staticmethod
    def creator():
        return O4MRenameCmd()

    def doIt(self, args):
        syntax = om.MSyntax()
        syntax.addFlag("p", "prefix", [om.MSyntax.kString, om.MSyntax.kLong])
        syntax.addFlag("pe", "prefixEdit", [om.MSyntax.kString, om.MSyntax.kLong])
        syntax.addFlag("s", "suffix", [om.MSyntax.kString, om.MSyntax.kLong])
        syntax.addFlag("se", "suffixEdit", [om.MSyntax.kString, om.MSyntax.kLong])
        syntax.addArg(om.MSyntax.kString)
        syntax.addArg(om.MSyntax.kLong)

        argp = om.MArgParser(syntax, args)
        selection = om.MGlobal.getActiveSelectionList(orderedSelectionIfAvailable = True)
        selItr = om.MItSelectionList(selection)

        if(argp.isFlagSet("p")):
            prefix = argp.flagArgumentString("p", 0)
            pad = argp.flagArgumentInt("p", 1)
            index = 0
            for sel in selItr:
                node = om.MFnDependencyNode(sel.getDependNode())
                node.setName(prefix.replace("#", str(index).zfill(pad)) + "_" + node.name())
                index += 1

        elif(argp.isFlagSet("pe")):
            prefix = argp.flagArgumentString("pe", 0)
            pad = argp.flagArgumentInt("pe", 1)
            index = 0
            for sel in selItr:
                node = om.MFnDependencyNode(sel.getDependNode())
                nameLs = node.name().split("_")
                nameLs[0] = prefix.replace("#", str(index).zfill(pad))
                node.setName("_".join(nameLs))
                index += 1

        else:
            rstr = argp.commandArgumentString(0)
            pad = argp.commandArgumentInt(1)
            index = 0
            for sel in selItr:
                node = om.MFnDependencyNode(sel.getDependNode())
                node.setName(rstr.replace("#", str(index).zfill(pad)))
                index += 1