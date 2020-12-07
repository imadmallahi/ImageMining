function CBIR_Recherche(Ireq,features, Image_names)
% Ireq: Image requéte
% features: Matrice des indexes
% Image_names: liste des noms des images
disp('Recherche...');
% extraire le vecteur descripteur
[~, fsize]=size(features);
feature_req=getFeatures(Ireq, fsize);
% calculer la distance euclidienne à la matrice de caractéristiques
Distance(:,2) = pdist2(features(:,1:fsize-1),feature_req,'euclidean');
Sorted_Distance=sort(Distance,'ascend');
% Affichage des images similaires par ordre de similarité
figure;
subplot (3,2,1); imshow(Ireq), title('Image requéte');
for i=1:5    
    [aa,bb,~]=find(Distance==Sorted_Distance(i));
    subplot (3,2,i+1); imshow(imread(char(Image_names(aa(1))))),title(char(Image_names(aa(1))));
end
end