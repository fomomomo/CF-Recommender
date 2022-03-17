from flask import Flask, request, jsonify
from Recommender import Recommender
import os

app = Flask(__name__)

REC = Recommender()


@app.route('/productRecommendation', methods=['GET'])
def getRecommendations():
    if request.method == 'GET':
        productId = request.args.get('productId')
        print(productId)
        if productId != None:
            recommendations = REC.getProductRecommendation(int(productId))
        print(recommendations)
        return jsonify(recommendations)


@app.route('/getProductList', methods=['GET'])
def getProductList():
    if request.method == 'GET':
        return jsonify(REC.productList)






@app.route('/')
def index():
    api_urls = {
		'Product List':'/getProductList',
		'Get Products Similar to a product':'/productRecommendation?productId=<str:productID>',
	}
    return jsonify(api_urls)


PORT = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(port=PORT, debug=True, use_reloader=False)
