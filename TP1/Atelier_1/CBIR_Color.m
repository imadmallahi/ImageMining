% Fichier CBIR_Color.m
clc
%% CBIR Color
fsize=7; % 6 features pour colorMoments + 1 pour sauvegarder l'indice del'image
%% Indexation de la base de données: Exécutée une seule fois
index = input('Voulez vous lancer l''indexation? taper Y si oui:','s');
if (index=='Y')
[features, Image_names]=CBIR_Indexation(fsize) ;
end
%% Processus en ligne: Recherche
% Lecture de l'image requête
Ireq=imread('ImageRequete.jpg');
%% Recherche de 5 images les plus similaires
CBIR_Recherche(Ireq,features, Image_names);