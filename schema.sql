CREATE DATABASE "Restaurante"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Guatemala.1252'
    LC_CTYPE = 'Spanish_Guatemala.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE areas (
    id_area   INTEGER NOT NULL,
    tipo_area VARCHAR(100) NOT NULL,
    fumador   CHAR(1) NOT NULL
);

ALTER TABLE areas ADD CONSTRAINT areas_pk PRIMARY KEY ( id_area );

CREATE TABLE encuesta (
    id_personal INTEGER NOT NULL,
    amabilidad  NUMERIC NOT NULL,
    exactitud   NUMERIC NOT NULL,
    encuesta_id NUMERIC NOT NULL
);

ALTER TABLE encuesta ADD CONSTRAINT encuesta_pk PRIMARY KEY ( encuesta_id );

ALTER TABLE encuesta ADD CONSTRAINT encuesta_pkv1 UNIQUE ( id_personal );

CREATE TABLE menu (
    id_elemento     INTEGER NOT NULL,
    nombre_elemento VARCHAR(100) NOT NULL,
    tipo_elemento   VARCHAR(10) NOT NULL,
    descripcion     VARCHAR(200) NOT NULL,
    precio          NUMERIC NOT NULL
);

COMMENT ON COLUMN menu.tipo_elemento IS
    'Comida o bedida';

ALTER TABLE menu ADD CONSTRAINT menu_pk PRIMARY KEY ( id_elemento );

CREATE TABLE menu_orden (
    id_elemento  INTEGER NOT NULL,
    id_orden     INTEGER NOT NULL,
    cantidad     INTEGER NOT NULL,
    estatus    VARCHAR(10) NOT NULL
);

ALTER TABLE menu_orden ADD CONSTRAINT menu_orden_pk PRIMARY KEY ( id_elemento,
                                                                  id_orden );

CREATE TABLE mesas (
    id_mesa      INTEGER NOT NULL,
    capacidad    INTEGER NOT NULL,
    movibilidad  CHAR(1) NOT NULL,
    habilitada   CHAR(1) NOT NULL,
    mesas_juntas INTEGER
);

ALTER TABLE mesas ADD CONSTRAINT mesas_pk PRIMARY KEY ( id_mesa );

CREATE TABLE mesas_areas (
    id_area        INTEGER NOT NULL,
    id_mesa        INTEGER NOT NULL,
    mesas_mesas_id NUMERIC NOT NULL
);

ALTER TABLE mesas_areas ADD CONSTRAINT mesas_areas_pk PRIMARY KEY ( id_mesa,
                                                                    id_area );

CREATE TABLE meseros (
    id_personal INTEGER NOT NULL,
    id_area     INTEGER,
    id_mesero   INTEGER NOT NULL,
    tipo        VARCHAR(7) NOT NULL
);

ALTER TABLE meseros
    ADD CONSTRAINT ch_inh_meseros CHECK ( tipo IN ( 'Meseros' ) );

ALTER TABLE meseros ADD CONSTRAINT meseros_pk PRIMARY KEY ( id_personal );

ALTER TABLE meseros ADD CONSTRAINT meseros_pkv1 UNIQUE ( id_mesero );

CREATE TABLE orden (
    id_orden       INTEGER NOT NULL,
    id_mesa        INTEGER NOT NULL,
    total_orden    NUMERIC,
    estado_orden   VARCHAR(10) NOT NULL,
    propina        NUMERIC,
    id_mesero      INTEGER NOT NULL,
    nit            VARCHAR(50),
    nombre_nit     VARCHAR(50),
    direccion      VARCHAR(20),
    mesas_mesas_id NUMERIC NOT NULL,
    hora           TIMESTAMP NOT NULL
);

ALTER TABLE orden ADD CONSTRAINT orden_pk PRIMARY KEY ( id_orden );

CREATE TABLE orden_pago (
    id_pago   INTEGER NOT NULL,
    cantidad  NUMERIC NOT NULL,
    id_orden  INTEGER NOT NULL
);

ALTER TABLE orden_pago ADD CONSTRAINT orden_pago_pk PRIMARY KEY ( id_pago,
                                                                  id_orden );

CREATE TABLE pago (
    id_pago   INTEGER NOT NULL,
    tipo_pago VARCHAR(15) NOT NULL
);

COMMENT ON COLUMN pago.tipo_pago IS
    'Efectivo / Tarjeta';

ALTER TABLE pago ADD CONSTRAINT pago_pk PRIMARY KEY ( id_pago );

CREATE TABLE personal (
    id_personal          INTEGER NOT NULL,
    nombre_personal      VARCHAR(100) NOT NULL,
    id_queja             INTEGER,
    password             VARCHAR(255) NOT NULL,
    clasificacion            VARCHAR(100) NOT NULL
);

ALTER TABLE personal ADD CONSTRAINT personal_pk PRIMARY KEY ( id_personal );

CREATE TABLE quejas (
    id_personal   INTEGER NOT NULL,
    motivo        VARCHAR(200) NOT NULL,
    id_queja      INTEGER NOT NULL,
    fecha         DATE NOT NULL,
    hora          VARCHAR(10) NOT NULL,
    clasificacion VARCHAR(50) NOT NULL
);

ALTER TABLE quejas ADD CONSTRAINT quejas_pk PRIMARY KEY ( id_queja );

ALTER TABLE mesas_areas
    ADD CONSTRAINT areasfkmesas FOREIGN KEY ( id_area )
        REFERENCES areas ( id_area );

--ALTER TABLE personal
--    ADD CONSTRAINT encuestafkpersonal FOREIGN KEY ( id_personal )
--        REFERENCES encuesta ( encuesta_id );

ALTER TABLE meseros
    ADD CONSTRAINT hierarchy_1 FOREIGN KEY ( id_personal )
        REFERENCES personal ( id_personal );

ALTER TABLE menu_orden
    ADD CONSTRAINT menufkmenu_orden FOREIGN KEY ( id_elemento )
        REFERENCES menu ( id_elemento );

ALTER TABLE mesas_areas
    ADD CONSTRAINT mesasfkareas FOREIGN KEY ( id_mesa )
        REFERENCES mesas ( id_mesa );

ALTER TABLE orden
    ADD CONSTRAINT mesasfkorden FOREIGN KEY ( id_mesa )
        REFERENCES mesas ( id_mesa );

ALTER TABLE areas
    ADD CONSTRAINT meserofkarea FOREIGN KEY ( id_mesero )
        REFERENCES meseros ( id_mesero );

ALTER TABLE orden
    ADD CONSTRAINT meserofkorden FOREIGN KEY ( id_mesero )
        REFERENCES meseros ( id_mesero );

ALTER TABLE menu_orden
    ADD CONSTRAINT ordenfkmenu_orden FOREIGN KEY ( id_orden )
        REFERENCES orden ( id_orden );

ALTER TABLE orden_pago
    ADD CONSTRAINT ordenfkorden_pago FOREIGN KEY ( id_orden )
        REFERENCES orden ( id_orden );

ALTER TABLE orden_pago
    ADD CONSTRAINT pagofkorden_pago FOREIGN KEY ( id_pago )
        REFERENCES pago ( id_pago );

ALTER TABLE personal
    ADD CONSTRAINT quejadkpersonal FOREIGN KEY ( id_queja )
        REFERENCES quejas ( id_queja );
