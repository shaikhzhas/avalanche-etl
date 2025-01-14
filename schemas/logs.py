LOGS_SCHEMA = [
    {
        "name": "log_index",
        "type": "INT64",
        "mode": "REQUIRED",
        "description": "Integer of the log index position in the block"
    },
    {
        "name": "transaction_hash",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Hash of the transactions this log was created from"
    },
    {
        "name": "transaction_index",
        "type": "INT64",
        "mode": "REQUIRED",
        "description": "Integer of the transactions index position log was created from"
    },
    {
        "name": "block_hash",
        "type": "STRING",
        "description": "Hash of the block where this log was in"
    },
    {
        "name": "block_number",
        "type": "INT64",
        "description": "The block number where this log was in"
    },
    {
        "name": "address",
        "type": "STRING",
        "description": "Address from which this log originated"
    },
    {
        "name": "data",
        "type": "STRING",
        "description": "Contains one or more 32 Bytes non-indexed arguments of the log"
    },
    {
        "name": "topics",
        "type": "STRING",
        "mode": "REPEATED",
        "description": "Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)"
    }
]