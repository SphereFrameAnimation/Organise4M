import maya.api.OpenMaya as om

class O4MColourCmd(om.MPxCommand):

    kPluginCmdName = "o4m_colour"
    def __init__(self):
        om.MPxCommand.__init__(self)

    @staticmethod
    def creator():
        return O4MColourCmd()

    def doIt(self, args):
        syntax = om.MSyntax();
        syntax.addArg(om.MSyntax.kLong) #R
        syntax.addArg(om.MSyntax.kLong) #G
        syntax.addArg(om.MSyntax.kLong) #B

        argp = om.MArgParser(syntax, args)

        selection = om.MGlobal.getActiveSelectionList()
        selItr = om.MItSelectionList(selection)

        for sel in selItr:
            dNode = om.MFnDagNode(sel.getDagPath().node())
            red = argp.commandArgumentFloat(0)
            blue = argp.commandArgumentFloat(1)
            green = argp.commandArgumentFloat(2)
            dNode.objectColorRGB = om.MColor((red, green, blue, 1.0))