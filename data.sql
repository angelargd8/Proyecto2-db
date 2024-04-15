insert into areas (id_area,tipo_area,fumador) values (1, 'Patio', 1), (2, 'Salon 1', 0), (3, 'Salon 2', 0), (4, 'Pergola', 1);

insert into menu (id_elemento,nombre_elemento,tipo_elemento,descripcion,precio,img)
Values
	(1,'Hamburguesa con queso','comida','Hamburguesa con queso con acompañante de papas fritas',50.0,'img/HamburguesaConQueso.png'),
	(2,'Pollo frito','comida','Pollo frito con papas horneadas',50,'img/PolloFrito.png'),
	(3,'Tacos','comida',' Los Tacos pueden ser de birria/carne/pollo/al pastor',40,'img/Tacos.png'),
	(4,'Gaseosas','bebida','La gaseosa puede ser Coca cola/pepsi/sprite/grapete/naranjada',20,'img/Gaseosas.png'),
	(5,'Bebidas natural','bebida','Bebida natural de Sandia/piña/fresa/rosa de jamaica/horchata','35','img/BebidasNaturales.png'),
	(6,'pie de queso','comida','pie hecho de queso',20,'img/PieQueso.png'),
	(7,'helado','comida','bola de helado del sabor que desee',20,'img/Helado.png'),
	(8,'pastel de chocolate','comida','pastel hecho de chocolate con chispas de chocolate y chocolate con mas chocolate',20,'img/PastelChocolate.png');

insert into mesas (id_mesa,capacidad,movibilidad,habilitada) 
Values
	(1, 2, 1, 1),
	(2, 2, 1, 1),
	(3, 4, 1, 1),
	(4, 4, 1, 1),
	(5, 2, 0, 1),
	(6, 2, 1, 1),
	(7, 4, 0, 1),
	(8, 6, 0, 1),
	(9, 2, 0, 1),
	(10, 2, 1, 1),
	(11, 4, 0, 1),
	(12, 10, 0, 1),
	(13, 4, 1, 1),
	(14, 2, 1, 1),
	(15, 2, 1, 1),
	(16, 4, 1, 1),
	(17, 4, 1, 1);

insert into mesas_areas (id_area,id_mesa)
values
	(1, 1),
	(1, 2),
	(1, 3),
	(1, 4),
	(2, 5),
	(2, 6),
	(2, 7),
	(2, 8),
	(3, 9),
	(3, 10),
	(3, 11),
	(3, 12),
	(3, 13),
	(4, 14),
	(4, 15),
	(4, 16),
	(4, 17);

insert into personal(id_personal, nombre_personal, password, clasificacion) 
values
	(1000, 'Angela Garcia', '123','admin'),
	(1001,'Gerax', '123', 'admin'),
	(1002, 'Francis', '123', 'admin'),
	(1003, 'Fernando', '123', 'cocinero'),
	(1004, 'Fernanda', '123', 'cocinero'),
	(1005, 'Cesar', '123', 'mesero'),
	(1006, 'cesarina', '123', 'mesero'),
	(1007, 'Maria Jose', '123', 'mesero'),
	(1008, 'Jose Maria', '123', 'mesero'),
	(1009, 'Diego', '123', 'barista'),
	(10010, 'Diega', '123', 'barista');

insert into meseros (id_personal,id_area,id_mesero,tipo)
values
	(1005, 1, 1005, 'Meseros'),
	(1006, 2, 1006, 'Meseros'),
	(1007, 3, 1007, 'Meseros'),
	(1008, 4, 1008, 'Meseros');

insert into pago (id_pago,tipo_pago)
Values
	(1,'Efectivo'),
	(2,'Tarjeta');

insert into quejas (motivo,id_queja,fecha,hora,clasificacion,id_elemento)
values
	('La comida estaba fea',5,'2024-04-16',4,'comida',1),
	('Buaj que horrible',8,'2024-04-18',8,'comida',1),
	('Comida comida',15,'2024-04-11',3,'comida',8);

INSERT INTO quejas(
	id_personal, motivo, id_queja, fecha, hora, clasificacion)
VALUES (1005, 'no me gusto que el pollo frito tenga mucha grasa', 1, '11/04/2023', 4, 'comida'),
(1005, 'el mesero me atendio mal', 2, '18/04/2023', 4, 'servicio'),
(1006,'El mesero no funciona cambienlo',7,'18/04/2023',5,'servicio');

-- querys para insertar ordenes de prueba
INSERT INTO orden (id_orden, id_mesa, estado_orden, id_mesero, orden_llegada, cant_personas)
SELECT 1, 2, 'abierto', 1005, CURRENT_TIMESTAMP, 2
WHERE EXISTS (
    SELECT 1
    FROM mesas
    WHERE id_mesa = 1
    AND habilitada = '1'
	AND capacidad >= 2
);

UPDATE mesas
SET habilitada = '0'
WHERE id_mesa = 1;

INSERT INTO orden (id_orden, id_mesa, estado_orden, id_mesero, orden_llegada, cant_personas)
SELECT 2, 4, 'abierto', 1005, CURRENT_TIMESTAMP, 2
WHERE EXISTS (
    SELECT 1
    FROM mesas
    WHERE id_mesa = 2
    AND habilitada = '1'
	AND capacidad >= 2
);

UPDATE mesas
SET habilitada = '0'
WHERE id_mesa = 4;

--quejas
INSERT INTO public.quejas(
	id_personal, motivo, id_queja, fecha, hora, clasificacion)
VALUES (1005, 'no me gusto que el pollo frito tenga mucha grasa', 1, '11/04/2024', 4, 'comida');

INSERT INTO public.quejas(
	id_personal, motivo, id_queja, fecha, hora, clasificacion)
	VALUES (1005, 'el mesero me atendio mal', 2, '18/04/2024', 4, 'servicio');

INSERT INTO public.quejas(
	id_personal, motivo, id_queja, fecha, hora, clasificacion)
	VALUES (1006, 'se le paro una mosca a mi comida', 13, '11/04/2024', 4, 'comida');


insert into orden (id_orden,id_mesa,estado_orden,id_mesero)
values
(4,2,'cerrado',1005);

insert into pago(id_pago, tipo_pago)
values (4, 'Efectivo');

insert into orden_pago( id_pago, cantidad, id_orden)
values
(4,1,4);

update orden
set nit = 12345678, nombre_nit='papa orson scrum', direccion='combex'
where id_orden= 4;