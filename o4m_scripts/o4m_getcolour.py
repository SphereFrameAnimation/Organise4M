import maya.api.OpenMaya as om

class O4MGetColourCmd(om.MPxCommand):

    kPluginCmdName = "o4m_getcolour"
    def __init__(self):
        om.MPxCommand.__init__(self)

    @staticmethod
    def creator():
        return O4MGetColourCmd()

    def doIt(self, args):

        selection = om.MGlobal.getActiveSelectionList()
        selItr = om.MItSelectionList(selection)

        for sel in selItr:
            dNode = om.MFnDagNode(sel.getDagPath().node())
            om.MGlobal.displayInfo(str(dNode.objectColorRGB))