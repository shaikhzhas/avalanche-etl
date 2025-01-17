CONSTRACT_SCHEMA = [
    {
        "name": "address",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Address of the contract"
    },
    {
        "name": "bytecode",
        "type": "STRING",
        "description": "Bytecode of the contract"
    },
    {
        "name": "function_sighashes",
        "type": "STRING",
        "mode": "REPEATED",
        "description": "4-byte function signature hashes"
    },
    {
        "name": "is_erc20",
        "type": "BOOLEAN",
        "description": "Whether this contract is an ERC20 contract"
    },
    {
        "name": "is_erc721",
        "type": "BOOLEAN",
        "description": "Whether this contract is an ERC721 contract"
    },
    {
        "name": "block_number",
        "type": "INT64",
        "mode": "REQUIRED",
        "description": "Block number where this contract was created"
    }
]