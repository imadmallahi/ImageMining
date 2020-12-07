# USAGE
# python search.py --index index.csv --query queries/103100.png --result-path dataset

# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher

import cv2


# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread("655016.jpg")
features = cd.describe(query)

# display the query
cv2.imshow("Query", query)

# perform the search
searcher = Searcher("indexation.csv")
results = searcher.search(features)



# loop over the results
for (score, resultID) in results:
	# load the result image and display it
	result = cv2.imread("DataSet" + "/" + resultID)    
	cv2.imshow("Result"+str(resultID), result)
	cv2.waitKey(5)
    
