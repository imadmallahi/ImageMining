%% Fonction d'Indexation
function [features, Image_names]=CBIR_Indexation(fsize)

% features: matrice des caract�ristiques
% Image_names: Nom des images de la base
% lister les images contenues dans le dossier
list= dir('obj_decoys'); % retourne une structure
% Lecture de l'image requ�te
n=length(list)-2;
% v est un vecteur qui va contenir le nombre de points simlaires entre
% image requ�te et chacune des images de la base
features=zeros(n-2,fsize);
% boucler sur les toutes les images de la base et les comparer avec l'image
% requ�te
% Indexation
filename=[]
disp('Debut d''Indexation')
for i=3:n
IDB=imread(strcat(list(i).folder,'/',list(i).name))
features(i-2,:)=[getFeatures(IDB, fsize), i-2];
path = strcat('DataSet/obj_decoys/',list(i).name);
filename(i)=path;
end
Image_names=filename';
disp('Fin d''Indexation');
end
