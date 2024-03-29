--sqlcmd -S DESKTOP-RCL8G7D\SQLEXPRESS -E

CREATE TABLE fiangonana (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nom NVARCHAR(100)
);

CREATE TABLE caisse (
    idCaisse INT IDENTITY(1,1) PRIMARY KEY,
    idFiangonana INT,
    montant DECIMAL(18, 2),
    dateInsertion DATE,
    FOREIGN KEY (idFiangonana) REFERENCES fiangonana(id)
);

CREATE TABLE mpiangona (
    IdMpiangona INT IDENTITY(1,1) PRIMARY KEY,
    idFiangonana INT,
    login NVARCHAR(100),
    mdp NVARCHAR(100),
    is_pasitera BIT, -- boolean
    FOREIGN KEY (idFiangonana) REFERENCES fiangonana(id)
);

CREATE TABLE pret (
    idPret INT IDENTITY(1,1) PRIMARY KEY,
    idMpino INT,
    idFiangonana INT,
    montant DECIMAL(18, 2),
    dateObtention DATE,
    FOREIGN KEY (idMpino) REFERENCES mpiangona(IdMpiangona),
    FOREIGN KEY (idFiangonana) REFERENCES fiangonana(id)
);

CREATE TABLE demande (
    idDemande INT IDENTITY(1,1) PRIMARY KEY,
    idMpino INT,
    idFiangonana INT,
    montant DECIMAL(18, 2),
    dateDemande DATE,
    FOREIGN KEY (idMpino) REFERENCES mpiangona(IdMpiangona),
    FOREIGN KEY (idFiangonana) REFERENCES fiangonana(id)
);


--EXEMPLES DONNEES
INSERT INTO caisse (idFiangonana, montant, dateInsertion) VALUES
(1, 50000.00, '2023-01-01'),
(1, 70000.00, '2023-01-08'),
(1, 60000.00, '2023-01-15'),
(1, 55000.00, '2023-01-22'),
(1, 80000.00, '2023-01-29'),
(1, 65000.00, '2023-02-05'),
(1, 75000.00, '2023-02-12'),
(1, 90000.00, '2023-02-19'),
(1, 85000.00, '2023-02-26'),
(1, 95000.00, '2023-03-05'),
(1, 55000.00, '2023-03-12'),
(1, 60000.00, '2023-03-19'),
(1, 75000.00, '2023-03-26'),
(1, 80000.00, '2023-04-02'),
(1, 70000.00, '2023-04-09'),
(1, 85000.00, '2023-04-16'),
(1, 95000.00, '2023-04-23'),
(1, 90000.00, '2023-04-30'),
(1, 65000.00, '2023-05-07'),
(1, 75000.00, '2023-05-14'),
(1, 55000.00, '2023-05-21'),
(1, 80000.00, '2023-05-28'),
(1, 90000.00, '2023-06-04'),
(1, 95000.00, '2023-06-11'),
(1, 60000.00, '2023-06-18'),
(1, 70000.00, '2023-06-25'),
(1, 85000.00, '2023-07-02'),
(1, 80000.00, '2023-07-09'),
(1, 75000.00, '2023-07-16'),
(1, 95000.00, '2023-07-23'),
(1, 90000.00, '2023-07-30'),
(1, 65000.00, '2023-08-06'),
(1, 60000.00, '2023-08-13'),
(1, 55000.00, '2023-08-20'),
(1, 80000.00, '2023-08-27'),
(1, 70000.00, '2023-09-03'),
(1, 85000.00, '2023-09-10'),
(1, 95000.00, '2023-09-17'),
(1, 90000.00, '2023-09-24'),
(1, 75000.00, '2023-10-01'),
(1, 65000.00, '2023-10-08'),
(1, 75000.00, '2023-10-15'),
(1, 55000.00, '2023-10-22'),
(1, 80000.00, '2023-10-29'),
(1, 90000.00, '2023-11-05'),
(1, 95000.00, '2023-11-12'),
(1, 60000.00, '2023-11-19'),
(1, 70000.00, '2023-11-26'),
(1, 85000.00, '2023-12-03'),
(1, 80000.00, '2023-12-10'),
(1, 75000.00, '2023-12-17'),
(1, 95000.00, '2023-12-24'),
(1, 90000.00, '2023-12-31');

INSERT INTO caisse (idFiangonana, montant, dateInsertion) VALUES
(1, 50000.00, '2022-01-02'), -- Dimanche 2 janvier 2022
(1, 60000.00, '2022-01-09'),
(1, 70000.00, '2022-01-16'),
(1, 80000.00, '2022-01-23'),
(1, 90000.00, '2022-01-30'),
(1, 100000.00, '2022-02-06'),
(1, 110000.00, '2022-02-13'),
(1, 120000.00, '2022-02-20'),
(1, 130000.00, '2022-02-27'),
(1, 140000.00, '2022-03-06'),
(1, 150000.00, '2022-03-13'),
(1, 160000.00, '2022-03-20'),
(1, 170000.00, '2022-03-27'),
(1, 180000.00, '2022-04-03'),
(1, 190000.00, '2022-04-10'),
(1, 200000.00, '2022-04-17'),
(1, 210000.00, '2022-04-24'),
(1, 220000.00, '2022-05-01'),
(1, 230000.00, '2022-05-08'),
(1, 240000.00, '2022-05-15'),
(1, 250000.00, '2022-05-22'),
(1, 260000.00, '2022-05-29'),
(1, 270000.00, '2022-06-05'),
(1, 280000.00, '2022-06-12'),
(1, 290000.00, '2022-06-19'),
(1, 300000.00, '2022-06-26'),
(1, 310000.00, '2022-07-03'),
(1, 320000.00, '2022-07-10'),
(1, 330000.00, '2022-07-17'),
(1, 340000.00, '2022-07-24'),
(1, 350000.00, '2022-07-31'),
(1, 360000.00, '2022-08-07'),
(1, 370000.00, '2022-08-14'),
(1, 380000.00, '2022-08-21'),
(1, 390000.00, '2022-08-28'),
(1, 400000.00, '2022-09-04'),
(1, 410000.00, '2022-09-11'),
(1, 420000.00, '2022-09-18'),
(1, 430000.00, '2022-09-25'),
(1, 440000.00, '2022-10-02'),
(1, 450000.00, '2022-10-09'),
(1, 460000.00, '2022-10-16'),
(1, 470000.00, '2022-10-23'),
(1, 480000.00, '2022-10-30'),
(1, 490000.00, '2022-11-06'),
(1, 500000.00, '2022-11-13'),
(1, 510000.00, '2022-11-20'),
(1, 520000.00, '2022-11-27'),
(1, 530000.00, '2022-12-04'),
(1, 540000.00, '2022-12-11'),
(1, 550000.00, '2022-12-18'),
(1, 560000.00, '2022-12-25');

INSERT INTO caisse (idFiangonana, montant, dateInsertion)
VALUES
    (1, 500000, '2024-01-07'),
    (1, 750000, '2024-01-14'),
    (1, 600000, '2024-01-21'),
    (1, 850000, '2024-01-28'),
    (1, 750000, '2024-02-11')

--VIEW CREATION
-- Supprimer l'ancienne vue si elle existe
IF EXISTS (SELECT * FROM sys.views WHERE name = 'Vue_Caisse')
BEGIN
    DROP VIEW Vue_Caisse;
END
GO
--POUR VOIR LE NUMERO DIMANCHE DANS L'ANNEE ET DANS LE MOIS
CREATE VIEW Vue_Caisse AS
SELECT
    dateInsertion AS Date,
    YEAR(dateInsertion) AS Annee,
    DENSE_RANK() OVER (ORDER BY DATEPART(WEEK, dateInsertion)) AS Numero_Dimanche_Annee,
    DENSE_RANK() OVER (PARTITION BY YEAR(dateInsertion), MONTH(dateInsertion) ORDER BY DATEPART(WEEK, dateInsertion)) AS Numero_Dimanche_Mois,
    montant AS Montant
FROM caisse
WHERE YEAR(dateInsertion) = 2023 OR YEAR(dateInsertion) = 2022;




