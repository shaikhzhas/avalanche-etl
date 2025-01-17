TOKENS_SCHEMA = [
    {
        "name": "address",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "The address of the ERC20 token"
    },
    {
        "name": "symbol",
        "type": "STRING",
        "description": "The symbol of the ERC20 token"
    },
    {
        "name": "name",
        "type": "STRING",
        "description": "The name of the ERC20 token"
    },
    {
        "name": "decimals",
        "type": "STRING",
        "description": "The number of decimals the token uses. Use safe_cast for casting to NUMERIC or FLOAT64"
    },
    {
        "name": "total_supply",
        "type": "STRING",
        "description": "The total token supply. Use safe_cast for casting to NUMERIC or FLOAT64"
    },
    {
        "name": "block_number",
        "type": "INT64",
        "mode": "REQUIRED",
        "description": "Block number where this token was created"
    }
]