CREATE DATABASE  IF NOT EXISTS `login_reg_schema` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `login_reg_schema`;
-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: localhost    Database: login_reg_schema
-- ------------------------------------------------------
-- Server version	8.0.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email_address` varchar(75) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `pass_hash` char(60) NOT NULL,
  `spam_ok` tinyint NOT NULL DEFAULT '0',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_address_UNIQUE` (`email_address`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'jim@bob.com','Jim','Bob','$2b$12$av27uwrIcIYd/u9ARNKrVOwuZ0cJBSlZ8ZqtqxJuj7xsN/JL3kIIO',0,'2021-05-17 12:54:12','2021-05-17 12:54:12'),(2,'billy@joe.com','Billy','Joe','$2b$12$KsZaG35pQOdidjHWwCghTuBgNkSs9yCAbzx.vqbdjfkCSsDXZiyPm',0,'2021-05-17 12:54:53','2021-05-17 12:54:53'),(3,'annie@bob.com','annie','bob','$2b$12$aiwcT3Q2AUNHUKl1owKTU.XF79AWvuQ/S22DL/F1DTuhvAQTh2DF2',0,'2021-05-17 12:57:02','2021-05-17 12:57:02'),(4,'jen@jenny.com','Jenny','jen','$2b$12$oAivlngqrEtrZ.SiioqWbed.YFOxkWRUjONmePP4DJHVNnyoOyhH2',0,'2021-05-17 13:03:27','2021-05-17 13:03:27'),(5,'dan@dan.com','dan','daniels','$2b$12$1tTwhlTRfL9N7SQS7uVFludsHp./IWK0MK.GKotowtX6mjnADXKp2',0,'2021-05-17 13:04:33','2021-05-17 13:04:33'),(6,'dude@abides.com','dude','abides','$2b$12$cQc6NeRHQm3ZUlaO/d3Hn.jwM0/ZRP.VefdxHgP7v9vpaHDeh64Qa',0,'2021-05-17 15:44:00','2021-05-17 15:44:00'),(7,'han@solo.com','han','solo','$2b$12$f7XmQbq4Vz1A.RPcQnjPc.WOBzE/2PE2vwFfn7LP0SByUy4yBHi7e',0,'2021-05-17 15:44:38','2021-05-17 15:44:38'),(8,'tim@allen.com','tim','allen','$2b$12$kACWVsNEJOO2hRuyvnYN6erZXQX.p1EvhI1Ui0mJ1l.RqUE42dSkW',1,'2021-05-17 16:05:08','2021-05-17 16:05:08'),(9,'vick@vock.com','vick','vock','$2b$12$8bUs3Wv434a0lLY6eowPxOf5.lWvfd39zvDfwH16Jc.Lqtk2.UqvO',0,'2021-05-17 16:08:43','2021-05-17 16:08:43'),(10,'mack@truck.com','Mack','Truck','$2b$12$Kac.oe9gzy741Pb1c8NwYuwtmbskGqMgPTrX5IAi0E1IOuv4zmMdy',0,'2021-05-17 18:12:36','2021-05-17 18:12:36');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-17 18:14:57
