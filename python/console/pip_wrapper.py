"""
***************************************************************************
    pip_wrapper.py
    ---------------------
    Date                 : March 2023
    Copyright            : (C) 2023 by Yoann Quenach de Quivillic
    Email                : yoann dot quenach at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

import importlib
import subprocess

from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtWidgets import QMessageBox, QPushButton
from qgis.utils import iface
from qgis.core import Qgis
from qgis.gui import QgsMessageBarItem


def promptInstall(module, messageBar=None, level=Qgis.MessageLevel.Info):
    """ Display a message in the QgsMessageBar prompting the user to install a module using pip"""

    if messageBar is None:
        messageBar = iface.messageBar()

    # If the module is already installed, display a info message and return
    try:
        importlib.import_module(module)
        messageBar.pushMessage(
            QCoreApplication.translate("PythonConsole", "Pip"),
            QCoreApplication.translate("PythonConsole", "Module {0} already installed").format(module),
            duration=2
        )
        return
    except ModuleNotFoundError:
        pass

    # Create a custom message bar item with a button to install the module
    installButton = QPushButton(QCoreApplication.translate("PythonConsole", "Install"))
    item = QgsMessageBarItem(
        QCoreApplication.translate("PythonConsole", "Reformat code"),
        QCoreApplication.translate("PythonConsole", "{0} module missing. Install it?").format(module),
        installButton)

    # Prevent the button from being garbage collected
    item.widget = installButton

    def onClick():
        messageBar.popWidget(item)
        install(module, messageBar)

    installButton.clicked.connect(onClick)
    messageBar.pushWidget(item, level, 5)


def install(module, messageBar=None):
    """ Try to install a module using pip """

    if messageBar is None:
        messageBar = iface.messageBar()

    # If the module is already installed, do nothing and return it
    try:
        return importlib.import_module(module)
    except ModuleNotFoundError:
        pass

    # Check if pip is installed on the system
    try:
        import pip
    except ModuleNotFoundError:
        messageBar.pushCritical(
            QCoreApplication.translate("PythonConsole", "Pip"),
            QCoreApplication.translate("PythonConsole", "Pip not found. Try installing python3-pip with your package manager"),
        )
        return None

    # Run pip install as a subprocess
    result = subprocess.run(f"python3 -m pip install {module}", shell=True, capture_output=True)
    if result.returncode != 0:
        messageBar.pushCritical(
            QCoreApplication.translate("PythonConsole", "Pip"),
            QCoreApplication.translate("PythonConsole", "Pip error: {0}").format(result.stderr.decode('utf8')),
        )
        return None

    # Even if the subprocess returned 0, the module might not be installed
    try:
        res = importlib.import_module(module)
        messageBar.pushSuccess(
            QCoreApplication.translate("PythonConsole", "Pip"),
            QCoreApplication.translate("PythonConsole", "Module {0} installed").format(module)
        )
        return res
    except ModuleNotFoundError:
        messageBar.pushCritical(
            QCoreApplication.translate("PythonConsole", "Pip"),
            QCoreApplication.translate("PythonConsole", "Module {0} not installed").format(module),
        )
        return None
