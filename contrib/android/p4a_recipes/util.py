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


class InheritedRecipeMixin:

    def get_recipe_dir(self):
        """This is used to replace pythonforandroid.recipe.Recipe.get_recipe_dir.
        If one of our local recipes inherits from a built-in p4a recipe, this override
        ensures that potential patches and other local files used by the recipe will
        be looked for in the built-in recipe's folder.
        """
        return os.path.join(self.ctx.root_dir, 'recipes', self.name)
