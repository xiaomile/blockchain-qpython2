# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from .BlockChain import Blockchain
import json
from uuid import uuid4
# Create your views here.
blockchain = Blockchain()
node_identifier = str(uuid4()).replace('-','')

def index(request):
    return render(request,"index.html")

def chain(request):
    response = {
        'chain':blockchain.chain,
        'length':len(blockchain.chain),
    }
    return HttpResponse(json.dumps(response), content_type="application/json")

def mine(request):
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(
        sender="0",
        recipient = node_identifier,
        amount = 1,
    )
    block = blockchain.new_block(proof)
    response = {
        'message':"New Block Forged",
        'index':block['index'],
        'transactions':block['transactions'],
        'proof':block['proof'],
        'previous_hash':block['previous_hash'],
    }
    return HttpResponse(json.dumps(response), content_type="application/json")

def new_transactions(request):
    #print(request.body)
    
    values = json.loads(request.body)
    #values = str(values)
    required = ['sender','recipient','amount']
    if not all(k in values for k in required):
        return 'Missing values',400

    index = blockchain.new_transaction(values['sender'],values['recipient'],values['amount'])
    response = {'message':f'Transactions will be added to Block {index}'}
    return HttpResponse(json.dumps(response), content_type="application/json")

