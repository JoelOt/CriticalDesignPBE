-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 11-11-2023 a las 20:04:28
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
-- Base de datos: `PBE_BD`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `marks`
--

CREATE TABLE `marks` (
  `subject` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `mark` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `marks`
--

INSERT INTO `marks` (`subject`, `name`, `mark`) VALUES
('AST', 'Parcial', 8),
('ICOM ', 'Parcial 1', 3.5),
('AST', 'Parcial', 8),
('ICOM ', 'Parcial 1', 3.5),
('IPAV', 'Parcial 1', 2.5),
('IPAV', 'Parcial 2', 7.5),
('IPAV', 'Parcial 1', 2.5),
('IPAV', 'Parcial 2', 7.5),
('RP', 'Practica 1', 10),
('RP', 'Practica 2', 7.5),
('RP', 'Practica 3', 8.5),
('ICOM', 'Practica 1', 7),
('ICOM', 'Practica 2', 7.5),
('DSBM', 'Practica 1 ', 8.35),
('DSBM ', 'Practica 2 ', 7.5),
('DSBM ', 'Parcial ', 5.5),
('RP', 'Parcial', 6.5),
('PBE', 'Puzzle 1', 8),
('PBE ', 'Puzzle 2', 8),
('RP', 'Practica 1', 10),
('RP', 'Practica 2', 7.5),
('RP', 'Practica 3', 8.5),
('ICOM', 'Practica 1', 7),
('ICOM', 'Practica 2', 7.5),
('DSBM', 'Practica 1 ', 8.35),
('DSBM ', 'Practica 2 ', 7.5),
('DSBM ', 'Parcial ', 5.5),
('RP', 'Parcial', 6.5),
('PBE', 'Puzzle 1', 8),
('PBE ', 'Puzzle 2', 8);

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
