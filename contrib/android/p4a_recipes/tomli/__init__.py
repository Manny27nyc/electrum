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
from pythonforandroid.recipes.tomli import TomliRecipe


assert TomliRecipe._version == "2.0.1"
assert TomliRecipe.depends == ["setuptools", "python3"]
assert TomliRecipe.python_depends == []


class TomliRecipePinned(TomliRecipe):
    #version = "2.0.1"
    # note: can't be easily updated as base recipe has version number hardcoded in custom "patch"-like setup.py
    sha512sum = "fd410039e255e2b3359e999d69a5a2d38b9b89b77e8557f734f2621dfbd5e1207e13aecc11589197ec22594c022f07f41b4cfe486a3a719281a595c95fd19ecf"


recipe = TomliRecipePinned()
