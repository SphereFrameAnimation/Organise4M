from o4m_scripts.o4m_check import O4MCheckCmd
from o4m_scripts.o4m_rename import O4MRenameCmd
import maya.api.OpenMaya as om

def maya_useNewAPI():

    pass

def initializePlugin(plugin):

    pluginFn = om.MFnPlugin(plugin)
    try:
        pluginFn.registerCommand(O4MCheckCmd.kPluginCmdName, O4MCheckCmd.creator)
        pluginFn.registerCommand(O4MRenameCmd.kPluginCmdName, O4MRenameCmd.creator)

    except:
        print("Error Initializing O4M")
        raise

def uninitializePlugin(plugin):

    pluginFn = om.MFnPlugin(plugin)
    try:
        pluginFn.deregisterCommand(O4MCheckCmd.kPluginCmdName)
        pluginFn.deregisterCommand(O4MRenameCmd.kPluginCmdName)

    except:
        print("Error Uninitializing O4M")
        raise