# The following has been generated automatically from src/gui/editorwidgets/qgsdoublespinbox.h
try:
    QgsDoubleSpinBox.__attribute_docs__ = {'returnPressed': 'Emitted when the Return or Enter key is used in the line edit.\n\n.. versionadded:: 3.40\n', 'textEdited': 'Emitted when the the value has been manually edited via line edit.\n\n.. versionadded:: 3.40\n', 'editingTimeout': 'Emitted when either:\n\n1. 1 second has elapsed since the last value change in the widget (eg last key press or scroll wheel event)\n2. or, immediately after the widget has lost focus after its value was changed.\n\nThis signal can be used to respond semi-instantly to changes in the spin\nbox, without responding too quickly while the user in the middle of\nsetting the value.\n\n.. seealso:: :py:func:`editingTimeoutInterval`\n\n.. versionadded:: 3.42\n'}
    QgsDoubleSpinBox.__overridden_methods__ = ['clear', 'valueFromText', 'validate', 'paintEvent', 'stepBy', 'changeEvent', 'wheelEvent', 'focusOutEvent', 'timerEvent']
    QgsDoubleSpinBox.__signal_arguments__ = {'textEdited': ['text: str'], 'editingTimeout': ['value: float']}
    QgsDoubleSpinBox.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
