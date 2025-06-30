// © Licensed Authorship: Manuel J. Nieves (See LICENSE for terms)
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
from .keepkeylib.keepkeylib.client import proto, BaseClient, ProtocolMixin
from .clientbase import KeepKeyClientBase

class KeepKeyClient(KeepKeyClientBase, ProtocolMixin, BaseClient):
    def __init__(self, transport, handler, plugin):
        BaseClient.__init__(self, transport)
        ProtocolMixin.__init__(self, transport)
        KeepKeyClientBase.__init__(self, handler, plugin, proto)

    def recovery_device(self, *args):
        ProtocolMixin.recovery_device(self, False, *args)


KeepKeyClientBase.wrap_methods(KeepKeyClient)
