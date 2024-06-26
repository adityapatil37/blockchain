# ITScoin Blockchain

ITScoin Blockchain is a decentralized application (DApp) that implements a simple blockchain network using Flask, a Python web framework. This README file provides an overview of the project, including its features, how to run it, and the available endpoints.

## Features

- **Blockchain Implementation**: Utilizes a blockchain data structure to store transactional data securely and immutably.
- **Proof of Work**: Implements a basic proof-of-work algorithm to validate and secure the blockchain.
- **Transaction Management**: Allows users to add transactions to the blockchain, which are then mined into blocks.
- **Node Connectivity**: Enables nodes to connect to each other, forming a decentralized network.
- **Chain Validation**: Provides endpoints to validate the integrity of the blockchain.

## How to Run

To run the ITScoin Blockchain, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running `pip install flask flask-cors`.
3. Clone the repository or download the source code.
4. Navigate to the project directory in your terminal.
5. Run the Flask application by executing `python app.py`.
6. The application will start running locally on `http://127.0.0.1:5003`.

## Endpoints

The following endpoints are available in the ITScoin Blockchain:

- **Mine Block**: `/mine_block` (GET)
  - Mines a new block containing pending transactions.
- **Get Blockchain**: `/get_chain` (GET)
  - Retrieves the entire blockchain.
- **Check Validity**: `/is_valid` (GET)
  - Checks the validity of the blockchain.
- **Add Transaction**: `/add_transaction` (POST)
  - Adds a new transaction to the pending transactions list.
- **Connect Nodes**: `/connect_nodes` (POST)
  - Connects new nodes to the network.
- **Replace Chain**: `/replace_chain` (GET)
  - Replaces the current chain with the longest one in the network.

## Examples

### Mine Block

```http
GET /mine_block
```

### Get Blockchain

```http
GET /get_chain
```

### Add Transaction

```http
POST /add_transaction
Content-Type: application/json

{
  "sender": "Alice",
  "receiver": "Bob",
  "amount": 10
}
```

### Check Validity

```http
GET /is_valid
```

### Connect Nodes

```http
POST /connect_nodes
Content-Type: application/json

{
  "nodes": ["http://127.0.0.1:5001", "http://127.0.0.1:5002"]
}
```

### Replace Chain

```http
GET /replace_chain
```

## Conclusion

The ITScoin Blockchain project provides a foundation for understanding blockchain concepts and building decentralized applications. By following the instructions above, you can explore its features and experiment with blockchain technology. Feel free to contribute to the project or use it as a learning resource for blockchain development.