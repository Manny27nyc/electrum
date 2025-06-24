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
# Python Jade Library

This is a slightly modified version of the official [Jade](https://github.com/Blockstream/Jade) python library.

This modified version was made from tag [1.0.31](https://github.com/Blockstream/Jade/releases/tag/1.0.31).

## Changes

- Removed BLE module, reducing transitive dependencies
- _http_request() function removed, so cannot be used as unintentional fallback
