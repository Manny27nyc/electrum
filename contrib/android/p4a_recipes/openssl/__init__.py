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

from pythonforandroid.recipes.openssl import OpenSSLRecipe
from pythonforandroid.util import load_source

util = load_source('util', os.path.join(os.path.dirname(os.path.dirname(__file__)), 'util.py'))


assert OpenSSLRecipe._version == "1.1"
assert OpenSSLRecipe.depends == []
assert OpenSSLRecipe.python_depends == []


class OpenSSLRecipePinned(util.InheritedRecipeMixin, OpenSSLRecipe):
    url_version = "1.1.1w"
    sha512sum = "b4c625fe56a4e690b57b6a011a225ad0cb3af54bd8fb67af77b5eceac55cc7191291d96a660c5b568a08a2fbf62b4612818e7cca1bb95b2b6b4fc649b0552b6d"


recipe = OpenSSLRecipePinned()
