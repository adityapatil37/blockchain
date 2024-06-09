# import datetime               #Each block will have own timestamp
# import hashlib                     #Hash the block
# import json                             #Encode the block before we hash them
# from flask import Flask, jsonify, request

# import requests

# from uuid import uuid4
# from urllib.parse import urlparse

# class Blockchain:
#     def __init__(self):
#         self.chain=[]
        
#         self.transactions = []
#         self.create_block(proof=1,previous_hash='0')
        
#         self.nodes = set()
                
#     def create_block(self,proof,previous_hash):
#         block = {'index':len(self.chain)+1,
#                  'timestamp':str(datetime.datetime.now()),
#                  'proof' :proof,
#                  'previous_hash':previous_hash,
#                  'transaction': self.transactions
#                 }
#         self.transactions = []  
#         self.chain.append(block)
#         return block
    
#     def get_previous_block(self):
#         return self.chain[-1]
    
#     def proof_of_work(self, previous_proof):
#         new_proof=1
#         check_proof=False
#         while check_proof is False:
#             hash_operation=hashlib.sha256(str(new_proof**2-previous_proof**2).encode()).hexdigest()
#             if hash_operation[:4] == '0000':
#                 check_proof=True
#             else:
#                 new_proof += 1
#         return new_proof
        
#     def hash(self,block):
#         encoded_block=json.dumps(block, sort_keys=True).encode()
#         return hashlib.sha256(encoded_block).hexdigest()
    
#     def is_chain_valid(self,chain):
#         previous_block=chain[0]
#         block_index = 1
#         while block_index < len(chain):
#             block = chain[block_index]
            
#             if block['previous_hash'] != self.hash(previous_block):
#                 return False
#             previous_proof = previous_block['proof']
#             proof = block['proof']
#             hash_operation=hashlib.sha256(str(proof**2-previous_proof**2).encode()).hexdigest()
#             if hash_operation[:4] != '0000':
#                 return False
#             previous_block = block
#             block_index += 1
#         return True

#     def add_transaction(self, sender, receiver, amount):
#         self.transactions.append({'sender':sender,'receiver':receiver,'amount':amount})
        
#         previous_block = self.get_previous_block()
#         return previous_block['index']+1
    
    
#     def add_node(self,address):
#         parsed_url = urlparse(address)
#         self.nodes.add(parsed_url.netloc)

#     def replace_chain(self):
#         network = self.nodes   
#         max_length = len(self.chain)  
#         longest_chain = None   
        
#         for node in network:
#             response = requests.get(f'http://{node}/get_chain')
#             if response.status_code == 200:
#                 length = response.json()['length']
#                 chain = response.json()['chain']
#                 if length > max_length and self.is_chain_valid(chain):
#                     max_length = length
#                     longest_chain = chain
#         if longest_chain:
#             self.chain = longest_chain
#             return True
#         return False
    
# #Create a web app
# app = Flask(__name__)  

# node_address = str(uuid4()).replace('-','')

# blockchain=Blockchain()  

# #Part 2:- Mining of Blockchain
# @app.route('/mine_block', methods=['GET'])
# def mine_block():
    
    
#     previous_block = blockchain.get_previous_block()
    
#     previous_proof = previous_block['proof']
#     proof = blockchain.proof_of_work(previous_proof)
    
#     previous_hash = blockchain.hash(previous_block)
#     blockchain.add_transaction(sender=node_address,receiver='Rohan',
#                                amount=1)
#     block = blockchain.create_block(proof, previous_hash)
    
#     response = {'message':'Congrats, You mined a block',
#                 'index': block['index'],
#                 'timestamp': block['timestamp'],
#                 'proof' : block['proof'],
#                 'previous_hash': block['previous_hash'],
#                 'transaction':block[ 'transaction']}
#     return jsonify(response), 200

# @app.route('/get_chain', methods=['GET'])
# def get_chain():
#     response = {'chain':blockchain.chain,
#                 'length':len(blockchain.chain)
#                 }
#     return jsonify(response), 200

# @app.route('/is_valid', methods=['GET'])
# def is_valid():
#     is_valid = blockchain.is_chain_valid(blockchain.chain)
#     if is_valid:
#         response = {'Message':'The Chain is valid'}
#     else:
#         response = {'Message':'The Chain is not valid'}
#     return jsonify(response), 200

# @app.route('/add_transaction', methods=['POST'])
# def add_transaction():
#     json = request.get_json()
#     transaction_keys = ['sender','receiver','amount']
#     if not all(key in json for key in transaction_keys):
#         return 'Some elements are missing', 400
#     index = blockchain.add_transaction(json['sender'],json['receiver'],
#                                json['amount'])
#     response = {'Message':f'This transaction will be added to block {index}'}
#     return jsonify(response), 201

# @app.route('/connect_nodes', methods=['POST'])
# def connect_nodes():
#     json = request.get_json()  
#     nodes = json.get('nodes')  
                                
#     if nodes is None:
#         return "No Nodes",400
#     for node in nodes:
#         blockchain.add_node(node)
    
#     response = {'message':'All nodes are now connected. the ITScoin Blockchain now contains following nodes:',
#                 'total nodes': list(blockchain.nodes)}
#     return jsonify(response), 201

# @app.route('/replace_chain', methods=['GET'])
# def replace_chain():
#     is_chain_replaced = blockchain.replace_chain()
#     if is_chain_replaced:
#         response={"message":"The chain is replaces by largest one",
#                   "new_chain":blockchain.chain}
#     else:
#         response=response={"message":"The chain is largest one",
#                            "actual_chain":blockchain.chain}
#     return jsonify(response), 200
# #Run the app
# app.run(host='0.0.0.0', port=5001)



import datetime
import hashlib
import json
from flask import Flask, jsonify, request
from flask_cors import CORS

import requests
from uuid import uuid4
from urllib.parse import urlparse

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof=1, previous_hash='0')
        self.nodes = set()

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
            'transactions': self.transactions
        }
        self.transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        previous_block = self.get_previous_block()
        return previous_block['index'] + 1

    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)

        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain

        if longest_chain:
            self.chain = longest_chain
            return True
        return False

# Create a Flask web application
app = Flask(__name__)
CORS(app)

# Generate a globally unique address for this node
node_address = str(uuid4()).replace('-', '')

# Create a Blockchain instance
blockchain = Blockchain()

# Mine a new block endpoint
@app.route('/mine_block', methods=['GET'])
def mine_block():
    if not blockchain.transactions:
        response = {'message': 'No transactions to mine'}
        return jsonify(response), 400

    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    # Reward for mining (this node as the sender, "0" signifies a reward)
    blockchain.add_transaction(sender=node_address, receiver='Miner', amount=1)

    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'Congratulations, you mined a block!',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
        'transactions': block['transactions']
    }
    return jsonify(response), 200

# Get the full blockchain endpoint
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

# Check if the blockchain is valid endpoint
@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'The Blockchain is valid.'}
    else:
        response = {'message': 'The Blockchain is not valid.'}
    return jsonify(response), 200

# Add a new transaction endpoint
@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    json_data = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']
    if not all(key in json_data for key in transaction_keys):
        return 'Missing transaction elements', 400
    index = blockchain.add_transaction(json_data['sender'], json_data['receiver'], json_data['amount'])
    response = {'message': f'This transaction will be added to Block {index}'}
    return jsonify(response), 201

# Connect new nodes endpoint
@app.route('/connect_nodes', methods=['POST'])
def connect_nodes():
    json_data = request.get_json()
    nodes = json_data.get('nodes')
    if nodes is None:
        return "No nodes to connect", 400
    for node in nodes:
        blockchain.add_node(node)
    response = {
        'message': 'All the nodes are now connected. The ITScoin Blockchain now contains the following nodes:',
        'total_nodes': list(blockchain.nodes)
    }
    return jsonify(response), 201

# Replace the chain with the longest one if needed endpoint
@app.route('/replace_chain', methods=['GET'])
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {
            'message': 'The chain was replaced by the longest one.',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'The current chain is the longest one.',
            'actual_chain': blockchain.chain
        }
    return jsonify(response), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
 