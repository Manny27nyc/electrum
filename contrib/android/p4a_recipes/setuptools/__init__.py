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
from pythonforandroid.recipes.setuptools import SetuptoolsRecipe


assert SetuptoolsRecipe._version == "51.3.3"
assert SetuptoolsRecipe.depends == ['python3']
assert SetuptoolsRecipe.python_depends == []


class SetuptoolsRecipePinned(SetuptoolsRecipe):
    sha512sum = "5a3572466a68c6f650111448ce3343f64c62044650bb8635edbff97e2bc7b216b8bbe3b4e3bccf34e6887f3bedc911b27ca5f9a515201cae49cf44fbacf03345"


recipe = SetuptoolsRecipePinned()
