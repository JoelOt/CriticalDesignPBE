-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-11-2023 a las 14:17:16
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `pbe_bd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `marks`
--

CREATE TABLE `marks` (
  `subject` varchar(15) NOT NULL,
  `name` varchar(15) NOT NULL,
  `mark` float NOT NULL,
  `id` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `marks`
--

INSERT INTO `marks` (`subject`, `name`, `mark`, `id`) VALUES
('AST ', 'Lab1', 4, '938B506'),
('AST', 'Lab2 ', 5, '938B506'),
('ICOM ', 'Practica1', 8, '938B506'),
('ICOM ', 'Ex Parcial', 6, '938B506'),
('IPAV', 'Parcial', 2.5, '938B506'),
('IPAV', 'Practica1', 8.5, '938B506'),
('RP', 'Control1', 10, '938B506'),
('RP', 'Control2', 9, '938B506'),
('rp', 'Parcial', 8, '938B506'),
('ICOM', 'Practica2', 6.5, '938B506'),
('AST', 'Control Teoria', 7, '938B506'),
('DSBM', 'Entregable1 ', 7, '938B506'),
('DSBM', 'Entregable2', 10, '938B506'),
('DSBM', 'Parcial', 7.5, '938B506'),
('DSBM ', 'Practica1', 7.4, '938B506'),
('PSAVC', 'Parcial', 6, 'D1FDE202'),
('PSAVC', 'Practica1 ', 7, 'D1FDE202'),
('PSAVC', 'Practica2', 8, 'D1FDE202'),
('RP', 'Control1', 9, 'D1FDE202'),
('RP', 'Control2', 9, 'D1FDE202'),
('PBE', 'Puzzle1', 7.5, 'D1FDE202'),
('PBE', 'Puzzle2', 8, 'D1FDE202'),
('PBE', 'Qüestionari1', 10, 'D1FDE202'),
('PBE', 'Qüestionari2', 10, 'D1FDE202'),
('AST', 'Lab1', 4, 'D1FDE202'),
('AST ', 'Lab2', 6, 'D1FDE202'),
('AST', 'Control Teoria', 9, 'D1FDE202'),
('DSBM', 'Control ', 8, 'D1FDE202'),
('DSBM', 'Practica1', 9, 'D1FDE202'),
('DSBM', 'Practica2', 6.4, 'D1FDE202'),
('DSBM ', 'Entregable1', 3.5, 'D1FDE202'),
('DSBM', 'Entregable2', 4, 'D1FDE202'),
('DSBM ', 'Practica3', 2, 'D1FDE202'),
('AST ', 'Lab1', 4, '938B506'),
('AST', 'Lab2 ', 5, '938B506'),
('ICOM ', 'Practica1', 8, '938B506'),
('ICOM ', 'Ex Parcial', 6, '938B506'),
('IPAV', 'Parcial', 2.5, '938B506'),
('IPAV', 'Practica1', 8.5, '938B506'),
('RP', 'Control1', 10, '938B506'),
('RP', 'Control2', 9, '938B506'),
('rp', 'Parcial', 8, '938B506'),
('ICOM', 'Practica2', 6.5, '938B506'),
('AST', 'Control Teoria', 7, '938B506'),
('DSBM', 'Entregable1 ', 7, '938B506'),
('DSBM', 'Entregable2', 10, '938B506'),
('DSBM', 'Parcial', 7.5, '938B506'),
('DSBM ', 'Practica1', 7.4, '938B506'),
('PSAVC', 'Parcial', 6, 'D1FDE202'),
('PSAVC', 'Practica1 ', 7, 'D1FDE202'),
('PSAVC', 'Practica2', 8, 'D1FDE202'),
('RP', 'Control1', 9, 'D1FDE202'),
('RP', 'Control2', 9, 'D1FDE202'),
('PBE', 'Puzzle1', 7.5, 'D1FDE202'),
('PBE', 'Puzzle2', 8, 'D1FDE202'),
('PBE', 'Qüestionari1', 10, 'D1FDE202'),
('PBE', 'Qüestionari2', 10, 'D1FDE202'),
('AST', 'Lab1', 4, 'D1FDE202'),
('AST ', 'Lab2', 6, 'D1FDE202'),
('AST', 'Control Teoria', 9, 'D1FDE202'),
('DSBM', 'Control ', 8, 'D1FDE202'),
('DSBM', 'Practica1', 9, 'D1FDE202'),
('DSBM', 'Practica2', 6.4, 'D1FDE202'),
('DSBM ', 'Entregable1', 3.5, 'D1FDE202'),
('DSBM', 'Entregable2', 4, 'D1FDE202'),
('DSBM ', 'Practica3', 2, 'D1FDE202');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `students`
--

CREATE TABLE `students` (
  `uid` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `userName` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `students`
--

INSERT INTO `students` (`uid`, `userName`) VALUES
('D1FDE202', 'Joel Otero'),
('938B506', 'Ariadna Marcos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tasks`
--

CREATE TABLE `tasks` (
  `date` date NOT NULL,
  `subject` varchar(10) NOT NULL,
  `name` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tasks`
--

INSERT INTO `tasks` (`date`, `subject`, `name`) VALUES
('2023-11-23', 'DSBM ', 'Entr 5'),
('2023-11-12', 'DSBM', 'Practica 2'),
('2023-11-29', 'ICOM ', 'EP 3'),
('2023-11-12', 'ICOM', 'Memòria 2'),
('2023-11-27', 'IPAV', 'EP 2'),
('2023-11-24', 'IPAV', 'Pràctica 4'),
('2023-11-22', 'PBE', 'CDR'),
('2023-11-19', 'PBE', 'Entrega CD'),
('2023-11-19', 'RP', 'Control 3');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `timetables`
--

CREATE TABLE `timetables` (
  `day` varchar(10) NOT NULL,
  `hour` time(6) NOT NULL,
  `subject` varchar(10) NOT NULL,
  `room` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `timetables`
--

INSERT INTO `timetables` (`day`, `hour`, `subject`, `room`) VALUES
('Tue ', '08:00:00.000000', 'AST', 'A4001'),
('Mon', '08:00:00.000000', 'DSBM', 'C5S101A'),
('Fri', '08:00:00.000000', 'IPAV', 'A4102'),
('Wen', '08:00:00.000000', 'PBE', 'A4105'),
('Mon', '10:00:00.000000', 'AST', 'A4001'),
('Tue', '10:00:00.000000', 'ICOM', 'A3102'),
('Fri', '10:00:00.000000', 'ICOM', 'A4102'),
('Wen', '12:00:00.000000', 'AST', 'A4002'),
('Tue', '14:00:00.000000', 'DSBM', 'A4105'),
('Mon ', '14:00:00.000000', 'RP', 'A4105'),
('Tue', '16:00:00.000000', 'RP', 'A4105'),
('Tue', '17:00:00.000000', 'DSBM', 'A4105'),
('Mon', '18:00:00.000000', 'PBE', 'A4105');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tasks`
--
ALTER TABLE `tasks`
  ADD PRIMARY KEY (`subject`,`name`);

--
-- Indices de la tabla `timetables`
--
ALTER TABLE `timetables`
  ADD PRIMARY KEY (`hour`,`subject`,`room`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

