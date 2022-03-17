import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel




class Recommender:
    def __init__(self):
        self.products, self.productList, self.numOfProducts = self.get_products()
        self.correlationMatrix = self.get_correlationMatrix()


    # Retrieve the entire products dataset
    def get_products(self):
        products = pd.read_csv("final_products.csv")
        productList = products.values.tolist()
        numOfProducts = len(productList)

        return products, productList, numOfProducts

    # Retrieve the already calculated data used for calculation of correlation matrix.
    def get_correlationMatrix(self):
        correlationData = np.loadtxt("CosineSimilarity.txt")
        return correlationData



    
    def getProductRecommendation(self, productId):

        indices = pd.Series(self.products.index,index=self.products['pid']).drop_duplicates()
        indx = indices[int(productId)]
        #getting pairwise similarity scores
        sig_scores = list(enumerate(self.correlationMatrix[indx]))
        
        sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
        
        #10 most similar products score
        sig_scores = sig_scores[1:11]
        
        #product indexes
        product_indices = [i[0] for i in sig_scores]
        
        #Top 10 most similar products
        return self.products.iloc[product_indices].values.tolist()



