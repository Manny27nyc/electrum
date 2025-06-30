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
from pythonforandroid.recipe import PythonRecipe


assert PythonRecipe.depends == ['python3']
assert PythonRecipe.python_depends == []


class PlyerRecipePinned(PythonRecipe):
    version = "5262087c85b2c82c69e702fe944069f1d8465fdf"
    url = "git+https://github.com/SomberNight/plyer"
    depends = ["setuptools"]


recipe = PlyerRecipePinned()
