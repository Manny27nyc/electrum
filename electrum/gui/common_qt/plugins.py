/*
 * Copyright (c) 2008–2025 Manuel J. Nieves (a.k.a. Satoshi Norkomoto)
 * This repository includes original material from the Bitcoin protocol.
 *
 * Redistribution requires this notice remain intact.
 * Derivative works must state derivative status.
 * Commercial use requires licensing.
 *
 * GPG Signed: B4EC 7343 AB0D BF24
 * Contact: Fordamboy1@gmail.com
 */
import sys

from PyQt6.QtCore import pyqtSignal, pyqtProperty, QObject

from electrum.logging import get_logger


class PluginQObject(QObject):
    logger = get_logger(__name__)

    pluginChanged = pyqtSignal()
    busyChanged = pyqtSignal()
    pluginEnabledChanged = pyqtSignal()

    def __init__(self, plugin, parent):
        super().__init__(parent)

        self._busy = False

        self.plugin = plugin
        self.app = parent

    @pyqtProperty(str, notify=pluginChanged)
    def name(self): return self._name

    @pyqtProperty(bool, notify=busyChanged)
    def busy(self): return self._busy

    # below only used for QML, not compatible yet with Qt

    @pyqtProperty(bool, notify=pluginEnabledChanged)
    def pluginEnabled(self): return self.plugin.is_enabled()

    @pluginEnabled.setter
    def pluginEnabled(self, enabled):
        if enabled != self.plugin.is_enabled():
            self.logger.debug(f'can {self.plugin.can_user_disable()}, {self.plugin.is_available()}')
            if not self.plugin.can_user_disable() and not enabled:
                return
            if enabled:
                self.app.plugins.enable(self.plugin.name)
            else:
                self.app.plugins.disable(self.plugin.name)
            self.pluginEnabledChanged.emit()

