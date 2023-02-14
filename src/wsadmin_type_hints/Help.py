"""
You can use the Jython or Jacl scripting languages to find general help and dynamic online
information about the currently running MBeans with the `wsadmin` tool. 

Use the `Help` object as an aid in writing and running scripts with the `AdminControl` object.

For more info see the [official documentation](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=scripting-commands-help-object-using-wsadmin).
"""
from typing import Optional


def AdminApp() -> str:
    """
    Use the `AdminApp` command to view a summary of each available method for the `AdminApp` object.
    
    Returns:
        str: The list of available methods for the `AdminApp` object.


    Example:
        ```pycon
        >>> print(Help.AdminApp())
            WASX7095I: The AdminApp object allows application objects to
            be manipulated -- this includes installing, uninstalling, editing,
            and listing.  Most of the commands supported by AdminApp operate in two
            modes: the default mode is one in which AdminApp communicates with the
            product to accomplish its tasks.  A local mode is also
            possible, in which no server communication takes place.  The local
            mode of operation is invoked by bringing up the scripting client with
            no server connected using the command line "-conntype NONE" option or setting the 
            "com.ibm.ws.scripting.connectionType=NONE" property in the wsadmin.properties.
            [...]
        ```
    """
    pass


def AdminConfig() -> str:
    """Use the `AdminConfig` command to view a summary of each available method for the `AdminConfig` object.

    Returns:
        str: The list of available methods for the `AdminConfig` object.

    Example:
        ```pycon
        >>> print(Help.AdminApp())
            WASX7053I: The following functions are supported by AdminConfig: 
            [...]
        ```
    """
    pass

def AdminControl() -> str:
    """Use the `AdminControl` command to view a summary of the help commands and ways to invoke an administrative command.

    Returns:
        str: The list of available methods for the `AdminControl` command.

    Example:
        ```pycon
        >>> print(Help.AdminControl())
            WASX7027I: The following functions are supported by AdminControl:
            [...]
        ```
    """
    pass

def AdminTask() -> str:
    """Use the `AdminTask` command to view a summary of help commands and ways to invoke an administrative command with the AdminTask object.

    Returns:
        str: The list of available methods for the `AdminTask` command.

    Example:
        ```pycon
        >>> print(Help.AdminTask())
            WASX8001I: The AdminTask object enables the available administrative commands. AdminTask commands 
            operate in two modes: the default mode is one whichAdminTask communicates with the
            product to accomplish its task. A local mode 
            is also available in which no server communication takes place. The local mode of operation is invoked by 
            bringing up the scripting client using the command line "-conntype NONE" option or setting the
            "com.ibm.ws.scripting.connectiontype=NONE" property in wsadmin.properties file.
            [...]
        ```
    """
    pass

def all(mbean_name: str) -> str: # undocumented
    """Use the `all` command to view a summary of the information that the MBean defines by name.

    Args:
        mbean_name (str): The object name which identifies the desired MBean.

    Returns:
        str: Summary of the information requested.

    Example:
        ```pycon
        >>> mbean = AdminControl.queryNames('type=Server,*').splitlines()[0]
        >>> print(Help.all(mbean))
            Description: Managed object for overall server process.
            Class name: javax.management.modelmbean.RequiredModelMBean

            Attribute                       Type                            Access
            name                            java.lang.String                RO
            shortName                       java.lang.String                RO
            threadMonitorInterval           int                             RW
            threadMonitorThreshold          int                             RW
            threadMonitorAdjustmentThreshold  int                             RW
            pid                             java.lang.String                RO
            cellName                        java.lang.String                RO
            cellShortName                   java.lang.String                RO
            [...]
        ```
    """
    pass


def attributes(mbean_name: str, attribute_name: str = None) -> str: # undocumented
    """Use the `attributes` command to view a summary of all the attributes that the MBean defines by name. 
    
    - If you provide the `mbean_name` parameter, the command displays information about the attributes, operations, 
        constructors, description, notifications, and classname of the specified MBean. 
    
    - If you specify the `mbean_name` and `attribute_name`, the command displays information about the 
        specified attribute for the specified MBean.

    Args:
        mbean_name (str): The object name which identifies the desired MBean.
        attribute_name (str): The attribute of interest. Defaults to None.

    Returns:
        str: Summary of all the attributes of the specified MBean

    Example:
        ```pycon
        >>> mbean = AdminControl.queryNames('type=Server,*').splitlines()[0]
        >>> print(Help.attributes(mbean))
            Attribute                       Type                            Access
            name                            java.lang.String                RO
            shortName                       java.lang.String                RO
            threadMonitorInterval           int                             RW
            threadMonitorThreshold          int                             RW
            threadMonitorAdjustmentThreshold  int                             RW
            [...]


        >>> print(Help.attributes(mbean, "pid"))
            Attribute                       Type                            Access
            pid                             java.lang.String                RO

            Description: Process id for the server process.
        ```
    """
    pass

def classname(mbean_name: str) -> str: # undocumented
    """Use the `classname` command to view a class name that the MBean defines by name.

    Args:
        mbean_name (str): The object name which identifies the desired MBean.

    Returns:
        str: The class name represented by the MBean name.

    Example:
        ```pycon
        >>> mbean = AdminControl.queryNames('type=Server,*').splitlines()[0]
        >>> print(Help.classname(mbean))
            javax.management.modelmbean.RequiredModelMBean
        ```
    """
    pass

def constructors(mbean_name: str) -> str: # undocumented
    """Use the `constructors` command to view a summary of all of the constructors that the MBean defines by name.

    Args:
        mbean_name (str): The object name which identifies the desired MBean.

    Returns:
        str: The summary of all the constructors.
    
    Example:
        ```pycon
        >>> mbean = AdminControl.queryNames('type=Server,*').splitlines()[0]
        >>> print(Help.constructors(mbean))
            Constructors
        ```
    """
    pass

def description(mbean_name: str) -> str: # undocumented
    """Use the `description` command to view a description that the MBean defines by name.

    Args:
        mbean_name (str): The object name which identifies the desired MBean.

    Returns:
        str: The description of the requested MBean.
    
    Example:
        ```pycon
        >>> mbean = AdminControl.queryNames('type=Server,*').splitlines()[0]
        >>> print(Help.description(mbean))
            Managed object for overall server process.
        ```
    """
    pass

def help() -> str: # undocumented
    """Use the `help` command to view a summary of all the available methods for the `Help` object.

    Returns:
        str: Summary of all the available methods for the Help object.
    
    Example:
        ```pycon
        >>> print(Help.help())
            WASX7028I: The Help object has two purposes:
            [...]
        ```
    """
    pass

def message(message_id: str) -> str: # undocumented
    """Use the `message` command to view information for a message ID.

    Args:
        message_id (str): The desired message ID.

    Returns:
        str: A description for the provided message ID.

    Example:
        ```pycon
        >>> print(Help.message('CNTR0005W'))
            Explanation: The container was unable to passivate an enterprise bean due to exception {2} 
            User action: Take action based upon message in exception {2}
        ```
    """
    pass

def notifications(mbean_name: str) -> str: # undocumented
    """Use the `notifications` command to view a summary of all the notifications that the MBean defines by name.

    Args:
        mbean_name (str): The object name which identifies the desired MBean.

    Returns:
        str: All the notifications that the MBean defines by name.
    
    Example:
        ```pycon
        >>> mbean = AdminControl.queryNames('type=Server,*').splitlines()[0]
        >>> print(Help.notifications(mbean))
            Notifications
            j2ee.state.starting
            j2ee.state.running
            j2ee.state.stopping
            j2ee.state.stopped
            j2ee.state.failed
            j2ee.attribute.changed
            jmx.attribute.changed
        ```
    """
    pass

def operations(mbean_name: str, operation_name: str = None): # undocumented
    """Use the operations command with the MBean name parameter to view a summary of all the operations that the 
        MBean defines by name. 
        
    - Specify a value for the `mbean_name` and `operation_name` to display the signature of the operation
        for the MBean that is defined by name.

    Args:
        mbean_name (str): The object name which identifies the desired MBean.
        operation_name (str, optional): The operation of interest. Defaults to None.
    """
    pass
