import numpy as np
data = np.array([[9,2,2],[5,1,0],[9,3,2],[8,3,1],[6,0,0]])
target = np.array([0,0,1,1,1])

#Relief
from ReliefF import ReliefF
fs = ReliefF(n_neighbors=1, n_features_to_keep=2)
X_train = fs.fit_transform(data, target)
print(X_train)

#RFE
from sklearn.feature_selection import SelectFromModel
from sklearn.svm import LinearSVC
lsvc=LinearSVC().fit(data,target)
model = SelectFromModel(lsvc, prefit=True)
X_new = model.transform(data) 

#chi2
import sklearn
chi2=sklearn.feature_selection.chi2(data, target)

#StandardScaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(data)
data_scaler = scaler.transform(data)

#PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data)

#LDA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis(n_components=3)
lda_data = lda.fit(data, target).transform(data)