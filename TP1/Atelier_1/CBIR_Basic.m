%%
clc
%% CBIR brut
% lister les images contenues dans le dossier
% Nous allons travailler sur un dossier de la base choisi au hasard et qui
% contient les images de deux catégories différentes (juste pour tester)
list= dir('DataSet/obj_decoys'); % retourne une structure
% list =dir('obj_decoys\*.jpg'); pour ne récuper que les jpg
% Lecture de l'image requête
n=length(list)-2; % -2 par ce list retourne aussi les .. et .
% boucler sur les toutes les images de la base et les comparer avec l'image
% requéte
% v est un vecteur qui va contenir le nombre de points similaires entre
% image requéte et chacune des images de la base
v=[];
% charger l'image requéte dans Ireq
Ireq=imread('ImageRequete.jpg');

for i=3:n
path = strcat('DataSet/obj_decoys/',list(i).name);
IDB=imread(path);
Ires=abs(diff(rgb2gray(IDB-Ireq)));
[m,~]=find(Ires==0);
v(i-2)=9480-size(m,1);
end
% charger l'image requéte dans Ireq
Ireq=imread('ImageRequete.jpg');
% Trier le vecteur v pour ne tenir en compte que les 5 premiers éléments
vsort=sort(v,'ascend');
% afficher l'image requête et les 5 images similaires par ordre de similarité
figure;
subplot (3,2,1); imshow(Ireq), title('Image requéte');
for i=1:5
[aa,bb,~]=find(v==vsort(i));
path2 = strcat('DataSet/obj_decoys/',list(bb(1)+2).name);
subplot (3,2,i+1); imshow(path2), title(list(bb(1)+2).name);
end