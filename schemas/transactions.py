TRANSACTIONS_SCHEMA = [
    {
        "name": "hash",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Hash of the transaction"
    },
    {
        "name": "nonce",
        "type": "INT64",
        "mode": "REQUIRED",
        "description": "The number of transactions made by the sender prior to this one"
    },
    {
        "name": "block_hash",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Hash of the block where this transaction was in"
    },
    {
        "name": "block_number",
        "type": "INT64",
        "mode": "REQUIRED",
        "description": "Block number where this transaction was in"
    },
    {
        "name": "transaction_index",
        "type": "INT64",
        "mode": "REQUIRED",
        "description": "Integer of the transactions index position in the block"
    },
    {
        "name": "from_address",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Address of the sender"
    },
    {
        "name": "to_address",
        "type": "STRING",
        "description": "Address of the receiver. null when its a contract creation transaction"
    },
    {
        "name": "value",
        "type": "NUMERIC",
        "description": "Value transferred in Wei"
    },
    {
        "name": "gas",
        "type": "INT64",
        "description": "Gas provided by the sender"
    },
    {
        "name": "gas_price",
        "type": "INT64",
        "description": "Gas price provided by the sender in Wei"
    },
    {
        "name": "input",
        "type": "STRING",
        "description": "The data sent along with the transaction"
    },
    {
        "name": "max_fee_per_gas",
        "type": "INT64",
        "description": "Total fee that covers both base and priority fees"
    },
    {
        "name": "max_priority_fee_per_gas",
        "type": "INT64",
        "description": "Fee given to miners to incentivize them to include the transaction"
    },
    {
        "name": "transaction_type",
        "type": "INT64",
        "description": "Transaction type. One of 0 (Legacy), 1 (Legacy), 2 (EIP-1559)"
    }
]