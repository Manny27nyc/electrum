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
from electrum.simple_config import ConfigVar, SimpleConfig

SimpleConfig.PAYSERVER_PORT = ConfigVar('plugins.payserver.port', default=8080, type_=int, plugin=__name__)
SimpleConfig.PAYSERVER_ROOT = ConfigVar('plugins.payserver.root', default='/r', type_=str, plugin=__name__)
SimpleConfig.PAYSERVER_ALLOW_CREATE_INVOICE = ConfigVar('plugins.payserver.allow_create_invoice', default=False, type_=bool, plugin=__name__)
