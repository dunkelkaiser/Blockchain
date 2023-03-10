# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:14:42 2023

@author: Balam
"""

# Módulo 1 - Crear una Cadena de Bloques

# Importar librerias
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Parte 1 - Crear la cadena de bloques
class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : str(datetime.datetime.now()),
            'proof' : proof,
            'previous_hash' : previous_hash
            }
        self.chain.append(block)
        return block
    
    def get_previous_hash(self):
        return self.chain[-1]
    
    def proof_of_woork(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            has_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if has_operation[:4] == '0000':
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
    
# Parte 2 - Minado de un Bloque de la Cadena

    
# Crear una aplicación web
app = Flask(__name__)

# Crear una blockchain
blockchain = Blockchain()






























































