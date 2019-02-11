CREATE TABLE joueur
(
    id INT PRIMARY KEY NOT NULL,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    taille INT,
	poids INT,
    date_naissance DATE
)

SELECT AddGeometryColumn( 'joueur', 'ville_naissance', 4326, 'POINT', 2)

ALTER TABLE joueur ADD imc AS (poids/((taille/100)^2))