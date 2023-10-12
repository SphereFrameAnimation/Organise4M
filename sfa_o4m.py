from o4m_scripts.o4m_check import O4MCheckCmd
from o4m_scripts.o4m_colour import O4MColourCmd
from o4m_scripts.o4m_rename import O4MRenameCmd
from o4m_scripts.o4m_getcolour import O4MGetColourCmd
import maya.api.OpenMaya as om

def maya_useNewAPI():

    pass

def initializePlugin(plugin):

    pluginFn = om.MFnPlugin(plugin)
    try:
        pluginFn.registerCommand(O4MCheckCmd.kPluginCmdName, O4MCheckCmd.creator)
        pluginFn.registerCommand(O4MRenameCmd.kPluginCmdName, O4MRenameCmd.creator)
        pluginFn.registerCommand(O4MColourCmd.kPluginCmdName, O4MColourCmd.creator)
        pluginFn.registerCommand(O4MGetColourCmd.kPluginCmdName, O4MGetColourCmd.creator)

    except:
        om.MGlobal.displayError("Error Initializing O4M")
        raise

def uninitializePlugin(plugin):

    pluginFn = om.MFnPlugin(plugin)
    try:
        pluginFn.deregisterCommand(O4MCheckCmd.kPluginCmdName)
        pluginFn.deregisterCommand(O4MRenameCmd.kPluginCmdName)
        pluginFn.deregisterCommand(O4MGetColourCmd.kPluginCmdName)

    except:
        om.MGlobal.displayError("Error Uninitializing O4M")
        raise