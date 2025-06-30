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

SimpleConfig.WATCHTOWER_SERVER_PORT = ConfigVar('plugins.watchtower.server_port', default=None, type_=int, plugin=__name__)
SimpleConfig.WATCHTOWER_SERVER_USER = ConfigVar('plugins.watchtower.server_user', default=None, type_=str, plugin=__name__)
SimpleConfig.WATCHTOWER_SERVER_PASSWORD = ConfigVar('plugins.watchtower.server_password', default=None, type_=str, plugin=__name__)
