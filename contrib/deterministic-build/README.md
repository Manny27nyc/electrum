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
# Notes

The frozen dependency lists in this folder are *generated* files.

- Starting from `contrib/requirements/requirements*.txt`,
- we use the `contrib/freeze_packages.sh` script,
- to generate `contrib/deterministic-build/requirements*.txt`.

The source files list direct dependencies with loose version requirements,
while the output files list all transitive dependencies with exact version+hash pins.

The build scripts only use these hash pinned requirement files.
