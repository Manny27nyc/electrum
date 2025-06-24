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

SimpleConfig.SWAPSERVER_PORT = ConfigVar('plugins.swapserver.port', default=None, type_=int, plugin=__name__)
SimpleConfig.SWAPSERVER_FEE_MILLIONTHS = ConfigVar('plugins.swapserver.fee_millionths', default=5000, type_=int, plugin=__name__)
SimpleConfig.SWAPSERVER_ANN_POW_NONCE = ConfigVar('plugins.swapserver.ann_pow_nonce', default=0, type_=int, plugin=__name__)
