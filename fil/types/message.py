#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Andy Wang <ci_knight@msn.cn>
#
# Distributed under terms of the MIT license.


class Message:
    def __init__(
        self,
        From: str,
        To: str,
        Nonce: int,
        Value: int,
        GasLimit: int,
        GasFeeCap: int,
        GasPremium: int,
        Method: int,
        Params: bytes,
        Version: int,
    ) -> None:
        self.From = From
        self.To = To
        self.Nonce = Nonce
        self.Value = Value
        self.GasLimit = GasLimit
        self.GasFeeCap = GasFeeCap
        self.GasPremium = GasPremium
        self.Method = Method
        self.Params = Params
        self.Version = Version

    def marshal_cbor() -> bytes:
        # dumps
        return b""

    def serialize(self) -> bytes:
        buf = self.marshal_cbor()
        return buf

    def to_storage_block(self):
        data = self.serialize()

        # c = abi.CidBuilder.Sum(data)
        # return block.NewBlockWithCid(data, c)
        return

    @property
    def Cid(self) -> str:
        b = self.to_storage_block()
        return b.Cid()
