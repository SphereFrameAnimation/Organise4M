from o4m_scripts.o4m_check import O4MCheckCmd
import maya.api.OpenMaya as om

def maya_useNewAPI():

    pass

print(O4MCheckCmd.kPluginCmdName)

def initializePlugin(plugin):

    pluginFn = om.MFnPlugin(plugin)
    try:
        pluginFn.registerCommand(O4MCheckCmd.kPluginCmdName, O4MCheckCmd.creator)

    except:
        print("err")
        raise

def uninitializePlugin(plugin):

    pluginFn = om.MFnPlugin(plugin)
    try:
        pluginFn.deregisterCommand(O4MCheckCmd.kPluginCmdName)

    except:
        print("err")
        raise