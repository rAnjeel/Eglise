--sqlcmd -S DESKTOP-RCL8G7D\SQLEXPRESS -E

CREATE TABLE fiangonana (
    id INT PRIMARY KEY,
    nom NVARCHAR(100)
);

CREATE TABLE caisse (
    idCaisse INT PRIMARY KEY,
    idFiangonana INT,
    montant DECIMAL(18, 2),
    dateInsertion DATE,
    FOREIGN KEY (idFiangonana) REFERENCES fiangonana(id)
);

CREATE TABLE mpiangona (
    IdMpiangona INT PRIMARY KEY,
    idFiangonana INT,
    login NVARCHAR(100),
    mdp NVARCHAR(100),
    is_pasitera BIT, -- boolean
    FOREIGN KEY (idFiangonana) REFERENCES fiangonana(id)
);

CREATE TABLE pret (
    idPret INT PRIMARY KEY,
    idMpino INT,
    idFiangonana INT,
    montant DECIMAL(18, 2),
    dateObtention DATE,
    FOREIGN KEY (idMpino) REFERENCES mpiangona(IdMpiangona),
    FOREIGN KEY (idFiangonana) REFERENCES fiangonana(id)
);




