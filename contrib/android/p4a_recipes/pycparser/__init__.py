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
from pythonforandroid.recipes.pycparser import PycparserRecipe


assert PycparserRecipe._version == "2.14"
assert PycparserRecipe.depends == ['setuptools', 'python3']
assert PycparserRecipe.python_depends == []


class PycparserRecipePinned(PycparserRecipe):
    version = "2.22"
    sha512sum = "c9a81c78d87162f71281a32a076b279f4f7f2e17253fe14c89c6db5f9b3554a6563ff700c385549a8b51ef8832f99f7bb4ac07f22754c7c475dd91feeb0cf87f"


recipe = PycparserRecipePinned()
