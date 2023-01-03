DROP TABLE IF EXISTS mot;
DROP TABLE IF EXISTS mot_categorie;
DROP TABLE IF EXISTS categorie;


CREATE TABLE IF NOT EXISTS categorie(
    id_categorie SERIAL,
    categorie_nom VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_categorie)
);

CREATE TABLE IF NOT EXISTS mot(
    id_mot SERIAL,
    id_kanji_to_kana INTEGER,
    mot_katakana VARCHAR(50),
    mot_hiragana VARCHAR(50),
    mot_kanji VARCHAR(50),
    type VARCHAR(50) NOT NULL CHECK (type in ('verbe',
                                             'nom_commun',
                                             'adjectif')),
    terminaison VARCHAR(50) CHECK(terminaison in ('う',
                                                'く',
                                                'ぐ',
                                                'す',
                                                'つ',
                                                'ぬ',
                                                'ぶ',
                                                'む',
                                                'る')),
    groupe INTEGER CHECK(groupe in (1,
                                   2,
                                   3)),
    PRIMARY KEY (id_mot)
);

CREATE TABLE IF NOT EXISTS mot_categorie(
    id_mot INTEGER NOT NULL,
    id_categorie INTEGER NOT NULL,
    PRIMARY KEY (id_mot, id_categorie),
    FOREIGN KEY (id_mot) REFERENCES mot(id_mot) ON DELETE CASCADE,
    FOREIGN KEY (id_categorie) REFERENCES categorie(id_categorie) ON DELETE CASCADE
);