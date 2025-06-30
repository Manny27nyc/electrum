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
class JadeError(Exception):
    # RPC error codes
    INVALID_REQUEST = -32600
    UNKNOWN_METHOD = -32601
    BAD_PARAMETERS = -32602
    INTERNAL_ERROR = -32603

    # Implementation specific error codes: -32000 to -32099
    USER_CANCELLED = -32000
    PROTOCOL_ERROR = -32001
    HW_LOCKED = -32002
    NETWORK_MISMATCH = -32003

    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data

    def __repr__(self):
        return "JadeError: " + str(self.code) + " - " + self.message \
            + " (Data: " + repr(self.data) + ")"

    def __str__(self):
        return repr(self)
