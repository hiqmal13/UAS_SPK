-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 19 Des 2023 pada 11.12
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hiqmal`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `ponsel`
--

CREATE TABLE `ponsel` (
  `id` int(11) NOT NULL,
  `brand` varchar(100) DEFAULT NULL,
  `ram` varchar(20) DEFAULT NULL,
  `prosesor` varchar(100) DEFAULT NULL,
  `storage` varchar(20) DEFAULT NULL,
  `baterai` varchar(20) DEFAULT NULL,
  `harga` int(11) DEFAULT NULL,
  `ukuran_layar` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `ponsel`
--

INSERT INTO `ponsel` (`id`, `brand`, `ram`, `prosesor`, `storage`, `baterai`, `harga`, `ukuran_layar`) VALUES
(1, 'Samsung Galaxy S23', '8 GB', 'SM8550 Snapdragon 8 Gen 2', '128 GB', '3.900 mAh', 11050000, '6.1 inch'),
(2, 'Samsung Galaxy S23+', '8 GB', 'SM8550 Snapdragon 8 Gen 2', '256 GB', '4.700 mAh', 13850000, '6.6 inch'),
(3, 'Samsung Galaxy S23 Ultra 5G', '12 GB', 'SM8550-AC Snapdragon 8 Gen 2', '256 GB', '5.000 mAh', 19999000, '6.8 inch'),
(4, 'Samsung Galaxy S22 5G', '8 GB', 'Snapdragon 8 Gen 1', '128 GB', '3.700 mAh', 8600000, '6.1 inch'),
(5, 'Samsung Galaxy S22 Plus 5G', '8 GB', 'Snapdragon 8 Gen 1', '128 GB', '4.500 mAh', 9600000, '6.6 inch'),
(6, 'Samsung Galaxy S22 Ultra 5G', '12 GB', 'Snapdragon 8 Gen 1', '256 GB', '5.000 mAh', 14500000, '6.8 inch'),
(7, 'Samsung Galaxy S21 FE 5G', '8 GB', 'Dimensity 2100', '128 GB', '4.500 mAh', 7500000, '6.4 inch'),
(8, 'Samsung Galaxy S21 5G', '8 GB', 'Dimensity 2100', '256 GB', '4.000 mAh', 12000000, '6.2 inch'),
(9, 'Samsung Galaxy S21 + 5G', '8 GB', 'Dimensity 2100', '256 GB', '4.800 mAh', 14300000, '6.7 inch'),
(10, 'Samsung Galaxy S21 Ultra 5G', '12 GB', 'Dimensity 2100', '256 GB', '5.000 mAh', 8899000, '6.8 inch');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `ponsel`
--
ALTER TABLE `ponsel`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `ponsel`
--
ALTER TABLE `ponsel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
