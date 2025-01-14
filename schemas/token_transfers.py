TOKEN_TRANSFERS_SCHEMA = [
    {
        "name": "token_address",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "ERC20 token address"
    },
    {
        "name": "from_address",
        "type": "STRING",
        "description": "Address of the sender"
    },
    {
        "name": "to_address",
        "type": "STRING",
        "description": "Address of the receiver"
    },
    {
        "name": "value",
        "type": "STRING",
        "description": "Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64"
    },
    {
        "name": "transaction_hash",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Transaction hash"
    },
    {
        "name": "log_index",
        "type": "INT64",
        "mode": "REQUIRED",
        "description": "Log index in the transaction receipt"
    },
    {
        "name": "block_number",
        "type": "INT64",
        "description": "The block number"
    }
]