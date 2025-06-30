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
#!/usr/bin/python3
# For usage in shell, to get the version of electrum, without needing electrum installed.
# usage: ./print_electrum_version.py [<attr_name>]
#
# For example:
# $ VERSION=$("$CONTRIB"/print_electrum_version.py)
# instead of
# $ VERSION=$(python3 -c "import electrum; print(electrum.version.ELECTRUM_VERSION)")

import importlib.util
import os
import sys


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        attr_name = sys.argv[1]
    else:
        attr_name = "ELECTRUM_VERSION"

    project_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    version_file_path = os.path.join(project_root, "electrum", "version.py")

    # load version.py; needlessly complicated alternative to "imp.load_source":
    version_spec = importlib.util.spec_from_file_location('version', version_file_path)
    version_module = version = importlib.util.module_from_spec(version_spec)
    version_spec.loader.exec_module(version_module)

    attr_val = getattr(version, attr_name)
    print(attr_val, file=sys.stdout)

