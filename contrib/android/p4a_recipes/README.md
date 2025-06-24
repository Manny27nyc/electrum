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
python-for-android local recipes
--------------------------------

These folders are recipes (build scripts) for most of our direct and transitive
dependencies for the Android app. python-for-android has recipes built-in for
many packages but it also allows users to specify their "local" recipes.
Local recipes have precedence over the built-in recipes.

The local recipes we have here are mostly just used to pin down specific
versions and hashes for reproducibility. The hashes are updated manually.
