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

insert into pago (id_pago,tipo_pago)
Values
	(1,'Efectivo'),
	(2,'Tarjeta');