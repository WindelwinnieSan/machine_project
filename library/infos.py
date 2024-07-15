"""
Infos Modul (infos.py)


folgende platform funktionen werden für pcap benötigt: functions: platform(), machine(), processor(), system(), version(), python_implementation(), python_version_tuple()
"""

import platform


def computer_name():
    """The networkname of the computer."""
    return platform.node()


def operating_system():
    """operating system of machine."""
    return platform.platform()


def cpu():
    """operating system of machine."""
    return platform.processor()


def machine():
    """machine."""
    return platform.machine()


def version():
    """python version tuple."""
    return platform.python_version_tuple()


def implementation():
    """Implementierung (Python interpreter)."""
    return platform.python_implementation()


def system():
    """Implementierung (Python interpreter)."""
    return platform.system, platform.version()
