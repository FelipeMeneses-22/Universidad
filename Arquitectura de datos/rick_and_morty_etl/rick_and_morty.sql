CREATE DATABASE IF NOT EXISTS rick_morty_dw
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE rick_morty_dw;

-- Tabla de ubicaciones / planetas
CREATE TABLE IF NOT EXISTS ubicaciones (
    ubicacion_id INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    url VARCHAR(500)
) ENGINE=InnoDB;

-- Tabla de episodios
CREATE TABLE IF NOT EXISTS episodios (
    episodio_id INT PRIMARY KEY,
    url VARCHAR(500) NOT NULL
) ENGINE=InnoDB;

-- Tabla de personajes
CREATE TABLE IF NOT EXISTS personajes (
    personaje_id INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    estado VARCHAR(30),
    especie VARCHAR(100),
    tipo_personaje VARCHAR(255),
    genero VARCHAR(30),
    origen_id INT NULL,
    ubicacion_id INT NULL,
    url_imagen VARCHAR(500),
    url_api VARCHAR(500),
    creado_en DATETIME NULL,

    CONSTRAINT fk_personaje_origen
        FOREIGN KEY (origen_id)
        REFERENCES ubicaciones(ubicacion_id),

    CONSTRAINT fk_personaje_ubicacion
        FOREIGN KEY (ubicacion_id)
        REFERENCES ubicaciones(ubicacion_id)
) ENGINE=InnoDB;

-- Tabla intermedia para la relación de muchos a muchos entre personajes y episodios
CREATE TABLE IF NOT EXISTS personaje_episodios (
    personaje_id INT NOT NULL,
    episodio_id INT NOT NULL,

    PRIMARY KEY (personaje_id, episodio_id),

    CONSTRAINT fk_pe_personaje
        FOREIGN KEY (personaje_id)
        REFERENCES personajes(personaje_id),

    CONSTRAINT fk_pe_episodio
        FOREIGN KEY (episodio_id)
        REFERENCES episodios(episodio_id)
) ENGINE=InnoDB;