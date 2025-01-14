RECEIPTS_SCHEMA = [
    {
        "name": "transaction_hash",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Hash of the transaction"
    },
    {
        "name": "transaction_index",
        "type": "INT64",
        "mode": "REQUIRED",
        "description": "Integer of the transactions index position in the block"
    },
    {
        "name": "block_hash",
        "type": "STRING",
        "description": "Hash of the block where this transaction was in"
    },
    {
        "name": "block_number",
        "type": "INT64",
        "description": "Block number where this transaction was in"
    },
    {
        "name": "cumulative_gas_used",
        "type": "INT64",
        "description": "The total amount of gas used when this transaction was executed in the block"
    },
    {
        "name": "gas_used",
        "type": "INT64",
        "description": "The amount of gas used by this specific transaction alone"
    },
    {
        "name": "contract_address",
        "type": "STRING",
        "description": "The contract address created, if the transaction was a contract creation, otherwise null"
    },
    {
        "name": "root",
        "type": "STRING",
        "description": "32 bytes of post-transaction stateroot (pre Byzantium)"
    },
    {
        "name": "status",
        "type": "INT64",
        "description": "Either 1 (success) or 0 (failure) (post Byzantium)"
    },
    {

        "name": "effective_gas_price",
        "type": "INT64",
        "description": "The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559"
    }
]