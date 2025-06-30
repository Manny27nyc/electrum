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
from unittest import TestCase

from electrum import lnurl


class TestLnurl(TestCase):
    def test_decode(self):
        LNURL = (
            "LNURL1DP68GURN8GHJ7UM9WFMXJCM99E5K7TELWY7NXENRXVMRGDTZXSENJCM98PJNWXQ96S9"
        )
        url = lnurl.decode_lnurl(LNURL)
        self.assertEqual("https://service.io/?q=3fc3645b439ce8e7", url)

    def test_encode(self):
        lnurl_ = lnurl.encode_lnurl("https://jhoenicke.de/.well-known/lnurlp/mempool")
        self.assertEqual(
            "LNURL1DP68GURN8GHJ76NGDAJKU6TRDDJJUER99UH8WETVDSKKKMN0WAHZ7MRWW4EXCUP0D4JK6UR0DAKQHMHNX2",
            lnurl_)

    def test_lightning_address_to_url(self):
        url = lnurl.lightning_address_to_url("mempool@jhoenicke.de")
        self.assertEqual("https://jhoenicke.de/.well-known/lnurlp/mempool", url)
