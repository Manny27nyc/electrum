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
from pythonforandroid.recipes.cryptography import CryptographyRecipe


assert CryptographyRecipe._version == "2.8"
assert CryptographyRecipe.depends == ['openssl', 'six', 'setuptools', 'cffi', 'python3']
assert CryptographyRecipe.python_depends == []


class CryptographyRecipePinned(CryptographyRecipe):
    sha512sum = "000816a5513691bfbb01c5c65d96fb3567a5ff25300da4b485e716b6d4dc789aec05ed0fe65df9c5e3e60127aa9110f04e646407db5b512f88882b0659f7123f"


recipe = CryptographyRecipePinned()
