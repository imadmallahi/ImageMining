%% Affichage des 6 premi�res images
% lister les images contenues dans le dossier
list= dir('DataSet/obj_decoys'); % retourne une structure
% pour v�rifier le nombre de fichier, ex�cuter "length(list)"
% la taille est +2 ".." et "."
length(list)
% afficher le nom du fichier num�ro 10
disp (list(12).name)
% afficher l'image
path = strcat('DataSet/obj_decoys/',list(12).name);

imshow(path)
% boucler et afficher les 6 premi�res images
for i=1:length(list)
    path2=strcat('DataSet/obj_decoys/',list(i+2).name);
    subplot (3,2,i); imshow(path2), title(list(i+2).name);
end

