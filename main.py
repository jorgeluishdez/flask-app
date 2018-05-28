''' Importing needed modules '''
from flask import Flask, jsonify


APP = Flask(__name__)


@APP.route('/')
def hello_world():
    '''Main app function '''
    return jsonify([{
        "_id": {
            "$oid": "5968dd23fc13ae04d9000001"
        },
        "product_name": "sildenafil citrate",
        "supplier": "Wisozk Inc",
        "quantity": 261,
        "unit_cost": "$10.47"
    }, {
        "_id": {
            "$oid": "5968dd23fc13ae04d9000002"
        },
        "product_name": "Mountain Juniperus ashei",
        "supplier": "Keebler-Hilpert",
        "quantity": 292,
        "unit_cost": "$8.74"
    }, {
        "_id": {
            "$oid": "5968dd23fc13ae04d9000003"
        },
        "product_name": "Dextromathorphan HBr",
        "supplier": "Schmitt-Weissnat",
        "quantity": 211,
        "unit_cost": "$20.53"
    }])


if __name__ == '__main__':
    APP.run()
