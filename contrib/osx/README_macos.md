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
# Running Electrum from source on macOS (development version)

## Prerequisites

- [brew](https://brew.sh/)
- python3
- git

## Main steps

### 1. Check out the code from GitHub:
```
$ git clone https://github.com/spesmilo/electrum.git
$ cd electrum
$ git submodule update --init
```

### 2. Prepare for compiling libsecp256k1

To be able to build the `electrum-ecc` package from source
(which is pulled in when installing Electrum in the next step),
you need:
```
$ brew install autoconf automake libtool coreutils
```

### 3. Install Electrum

Run install (this should install the dependencies):
```
$ python3 -m pip install --user -e ".[gui,crypto]"
```

### 4. Run electrum:
```
$ ./run_electrum
```
