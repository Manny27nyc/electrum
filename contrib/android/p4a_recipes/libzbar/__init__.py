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
import os

from pythonforandroid.recipes.libzbar import LibZBarRecipe
from pythonforandroid.util import load_source

util = load_source('util', os.path.join(os.path.dirname(os.path.dirname(__file__)), 'util.py'))


assert LibZBarRecipe.depends == ['libiconv']
assert LibZBarRecipe.python_depends == []


class LibZBarRecipePinned(util.InheritedRecipeMixin, LibZBarRecipe):
    version = "bb05ec54eec57f8397cb13fb9161372a281a1219"
    url = "https://github.com/mchehab/zbar/archive/{version}.zip"
    sha512sum = "186312ef0a50404efef79a5fbed34534569fab2873a6bb6d2e3d8ea64fa461c5537ca4fb0e659670d72b021e514f8fd4651b1e85954bf987015d8eb2e6f68375"
    patches = []  # werror.patch not needed for modern zbar


recipe = LibZBarRecipePinned()
