import maya.api.OpenMaya as om

class O4MRenameCmd(om.MPxCommand):

    kPluginCmdName = "o4m_rename"
    undoNameCache = []
    redoNameCache = []
    openSceneCB = 0
    
    def __init__(self):
        
        om.MPxCommand.__init__(self)
        
    @staticmethod
    def openEvent(*args, **kwargs):
        
        O4MRenameCmd.undoNameCache.clear()

    @staticmethod
    def creator():
        
        O4MRenameCmd.openSceneCB = om.MEventMessage.addEventCallback("SceneOpened", O4MRenameCmd)
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
            nameCache = []
            for sel in selItr:
                node = om.MFnDependencyNode(sel.getDependNode())
                nameCache.append(node.name())
                node.setName(prefix.replace("#", str(index).zfill(pad)) + "_" + node.name())
                index += 1
                
            O4MRenameCmd.undoNameCache.append(nameCache)

        elif(argp.isFlagSet("pe")):
            prefix = argp.flagArgumentString("pe", 0)
            pad = argp.flagArgumentInt("pe", 1)
            index = 0
            nameCache = []
            for sel in selItr:
                node = om.MFnDependencyNode(sel.getDependNode())
                nameCache.append(node.name())
                nameLs = node.name().split("_")
                nameLs[0] = prefix.replace("#", str(index).zfill(pad))
                node.setName("_".join(nameLs))
                index += 1
            
            O4MRenameCmd.undoNameCache.append(nameCache)

        elif(argp.isFlagSet("s")):
            suffix = argp.flagArgumentString("s", 0)
            pad = argp.flagArgumentInt("s", 1)
            index = 0
            nameCache = []
            for sel in selItr:
                node = om.MFnDependencyNode(sel.getDependNode())
                nameCache.append(node.name())
                node.setName(node.name() + "_" + suffix.replace("#", str(index).zfill(pad)))
                index += 1
            
            O4MRenameCmd.undoNameCache.append(nameCache)

        elif(argp.isFlagSet("se")):
            suffix = argp.flagArgumentString("se", 0)
            pad = argp.flagArgumentInt("se", 1)
            index = 0
            nameCache = []
            for sel in selItr:
                node = om.MFnDependencyNode(sel.getDependNode())
                nameCache.append(node.name())
                nameLs = node.name().split("_")
                nameLs[len(nameLs) - 1] = suffix.replace("#", str(index).zfill(pad))
                node.setName("_".join(nameLs))
                index += 1
            
            O4MRenameCmd.undoNameCache.append(nameCache)

        else:
            rstr = argp.commandArgumentString(0)
            pad = argp.commandArgumentInt(1)
            index = 0
            nameCache = []
            for sel in selItr:
                node = om.MFnDependencyNode(sel.getDependNode())
                nameCache.append(node.name())
                node.setName(rstr.replace("#", str(index).zfill(pad)))
                index += 1
            
            O4MRenameCmd.undoNameCache.append(nameCache)
    
    def isUndoable(self):
        
        return True

    def undoIt(self):
        
        sel = om.MGlobal.getActiveSelectionList()
        undoNames = O4MRenameCmd.undoNameCache.pop()
        redoNames = []
        
        for i in range(len(undoNames) - 1, -1, -1):
            
            node = om.MFnDependencyNode(sel.getDependNode(i))
            redoNames.append(node.name())
            node.setName(undoNames.pop())
        
        O4MRenameCmd.redoNameCache.append(redoNames)
        
    def redoIt(self):
        
        sel = om.MGlobal.getActiveSelectionList()
        redoNames = O4MRenameCmd.redoNameCache.pop()
        undoNames = []

        for i in range(0, len(redoNames)):
            
            node = om.MFnDependencyNode(sel.getDependNode(i))
            undoNames.append(node.name())
            node.setName(redoNames.pop())
        
        O4MRenameCmd.undoNameCache.append(undoNames)