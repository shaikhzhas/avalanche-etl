BLOCKS_SCHEMA = [
    {
        "name": "number",
        "type": "INT64",
        "mode": "REQUIRED",
        "description": "The block number"
    },
    {
        "name": "hash",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Hash of the block"
    },
    {
        "name": "parent_hash",
        "type": "STRING",
        "description": "Hash of the parent block"
    },
    {
        "name": "nonce",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Hash of the generated proof-of-work"
    },
    {
        "name": "sha3_uncles",
        "type": "STRING",
        "description": "SHA3 of the uncles data in the block"
    },
    {
        "name": "logs_bloom",
        "type": "STRING",
        "description": "The bloom filter for the logs of the block"
    },
    {
        "name": "transactions_root",
        "type": "STRING",
        "description": "The root of the transaction trie of the block"
    },
    {
        "name": "state_root",
        "type": "STRING",
        "description": "The root of the final state trie of the block"
    },
    {
        "name": "receipts_root",
        "type": "STRING",
        "description": "The root of the receipts trie of the block"
    },
    {
        "name": "miner",
        "type": "STRING",
        "description": "The address of the beneficiary to whom the mining rewards were given"
    },
    {
        "name": "difficulty",
        "type": "NUMERIC",
        "description": "Integer of the difficulty for this block"
    },
    {
        "name": "total_difficulty",
        "type": "NUMERIC",
        "description": "Integer of the total difficulty of the chain until this block"
    },
    {
        "name": "size",
        "type": "INT64",
        "description": "The size of this block in bytes"
    },
    {
        "name": "extra_data",
        "type": "STRING",
        "description": "The extra data field of this block"
    },
    {
        "name": "gas_limit",
        "type": "INT64",
        "description": "The maximum gas allowed in this block"
    },
    {
        "name": "gas_used",
        "type": "INT64",
        "description": "The total used gas by all transactions in this block"
    },
    {
        "name": "timestamp",
        "type": "INT64",
        "mode": "REQUIRED",
        "description": "The unix timestamp for when the block was collated"
    },
    {
        "name": "transaction_count",
        "type": "INT64",
        "description": "The number of transactions in the block"
    },
    {
        "name": "base_fee_per_gas",
        "type": "INT64",
        "description": "Protocol base fee per gas, which can move up or down"
    }
]