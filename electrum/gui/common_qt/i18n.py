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
from PyQt6.QtCore import QTranslator

from electrum.i18n import _


class ElectrumTranslator(QTranslator):
    """Delegator for Qt translations to gettext"""
    def __init__(self, parent=None):
        super().__init__(parent)

        # explicit enumeration of translatable strings from Qt standard library, so these
        # will be included in the electrum gettext translation template
        self._strings = [_('&Undo'), _('&Redo'), _('Cu&t'), _('&Copy'), _('&Paste'), _('Select All'),
                         _('Copy &Link Location')]

    def translate(self, context, source_text: str, disambiguation, n):
        return _(source_text, context=context)
