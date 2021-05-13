CREATE DATABASE  IF NOT EXISTS `studifix` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `studifix`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: studifix
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `chat`
--

DROP TABLE IF EXISTS `chat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chat` (
  `id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `creation_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_chat_group` FOREIGN KEY (`id`) REFERENCES `studygroup` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat`
--

LOCK TABLES `chat` WRITE;
/*!40000 ALTER TABLE `chat` DISABLE KEYS */;
/*!40000 ALTER TABLE `chat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat_invitaion`
--

DROP TABLE IF EXISTS `chat_invitaion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chat_invitaion` (
  `id` int NOT NULL,
  `creation_date` datetime NOT NULL,
  `accepted` tinyint NOT NULL,
  `chat_id` int NOT NULL,
  `target_user` int NOT NULL,
  `source_user` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_source_user_chat_idx` (`source_user`),
  KEY `FK_target_user_chat_idx` (`target_user`),
  CONSTRAINT `FK_chat` FOREIGN KEY (`id`) REFERENCES `chat` (`id`),
  CONSTRAINT `FK_source_user_chat` FOREIGN KEY (`source_user`) REFERENCES `user` (`id`),
  CONSTRAINT `FK_target_user_chat` FOREIGN KEY (`target_user`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_invitaion`
--

LOCK TABLES `chat_invitaion` WRITE;
/*!40000 ALTER TABLE `chat_invitaion` DISABLE KEYS */;
/*!40000 ALTER TABLE `chat_invitaion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat_message`
--

DROP TABLE IF EXISTS `chat_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chat_message` (
  `id` int NOT NULL,
  `text` varchar(200) NOT NULL,
  `creation_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_chat_message` FOREIGN KEY (`id`) REFERENCES `chat` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_message`
--

LOCK TABLES `chat_message` WRITE;
/*!40000 ALTER TABLE `chat_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `chat_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group_invitation`
--

DROP TABLE IF EXISTS `group_invitation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `group_invitation` (
  `id` int NOT NULL,
  `creation_date` datetime NOT NULL,
  `accepted` tinyint NOT NULL,
  `study_group_id` int NOT NULL,
  `target_user` int NOT NULL,
  `source_user` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_source_user_group_idx` (`source_user`),
  KEY `FK_target_user_group_idx` (`target_user`),
  CONSTRAINT `FK_group` FOREIGN KEY (`id`) REFERENCES `studygroup` (`id`),
  CONSTRAINT `FK_source_user_group` FOREIGN KEY (`source_user`) REFERENCES `user` (`id`),
  CONSTRAINT `FK_target_user_group` FOREIGN KEY (`target_user`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_invitation`
--

LOCK TABLES `group_invitation` WRITE;
/*!40000 ALTER TABLE `group_invitation` DISABLE KEYS */;
/*!40000 ALTER TABLE `group_invitation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `learning_profile`
--

DROP TABLE IF EXISTS `learning_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `learning_profile` (
  `id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `prev_knowledge` varchar(100) NOT NULL,
  `extroversion` int NOT NULL,
  `study_state` int NOT NULL,
  `frequency` int NOT NULL,
  `learntyp` int NOT NULL,
  `semester` int NOT NULL,
  `interest` varchar(45) NOT NULL,
  `degree_course` varchar(45) NOT NULL,
  `creation_date` datetime NOT NULL,
  KEY `FK_user_idx` (`id`),
  CONSTRAINT `FK_learning_profile_group` FOREIGN KEY (`id`) REFERENCES `studygroup` (`id`),
  CONSTRAINT `FK_user` FOREIGN KEY (`id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learning_profile`
--

LOCK TABLES `learning_profile` WRITE;
/*!40000 ALTER TABLE `learning_profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `learning_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studygroup`
--

DROP TABLE IF EXISTS `studygroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `studygroup` (
  `id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `creation_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studygroup`
--

LOCK TABLES `studygroup` WRITE;
/*!40000 ALTER TABLE `studygroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `studygroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL,
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `adress` varchar(45) NOT NULL,
  `email` varchar(100) NOT NULL,
  `google_id` varchar(100) NOT NULL,
  `creation_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-13 11:42:08
