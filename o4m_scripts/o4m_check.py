import maya.api.OpenMaya as om

class O4MCheckCmd(om.MPxCommand):

    kPluginCmdName = "o4m_check"
    def __init__(self):
        om.MPxCommand.__init__(self)

    @staticmethod
    def creator():
        return O4MCheckCmd()

    def doIt(self, args):
        print("Organise4M is loaded!")