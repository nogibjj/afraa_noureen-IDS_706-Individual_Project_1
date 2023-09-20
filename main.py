"""main module"""
import platform

def display_system_info():
    """
    Display system information including the OS and hardware details.

    :return: A string containing system information.
    """
    system_info = f"Operating System: {platform.system()} {platform.release()}\n"
    system_info += f"Node Name: {platform.node()}\n"
    system_info += f"Processor: {platform.processor()}\n"
    system_info += f"Architecture: {platform.architecture()[0]}\n"
    return system_info
