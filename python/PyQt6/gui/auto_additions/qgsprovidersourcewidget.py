# The following has been generated automatically from src/gui/qgsprovidersourcewidget.h
try:
    QgsProviderSourceWidget.__attribute_docs__ = {'validChanged': 'Emitted whenever the validation status of the widget changes.\n\nIf ``isValid`` is ``False`` then the widget is not valid, and any dialog\nusing the widget should be prevented from being accepted.\n', 'changed': 'Emitted whenever the configuration of the widget changes.\n\n.. versionadded:: 3.30\n'}
    QgsProviderSourceWidget.__virtual_methods__ = ['groupTitle', 'setMapCanvas', 'mapCanvas']
    QgsProviderSourceWidget.__abstract_methods__ = ['setSourceUri', 'sourceUri']
    QgsProviderSourceWidget.__signal_arguments__ = {'validChanged': ['isValid: bool']}
except (NameError, AttributeError):
    pass
