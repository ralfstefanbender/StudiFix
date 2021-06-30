USE `studi_fix_database`;
-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: studi_fix_database
-- ------------------------------------------------------
-- Server version	8.0.21

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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat`
--

LOCK TABLES `chat` WRITE;
/*!40000 ALTER TABLE `chat` DISABLE KEYS */;
INSERT INTO `chat` VALUES (1,'Dummy Chat','2021-10-20 01:34:52'),(2,'Mathe Gruppe','2021-06-30 18:10:57'),(3,'Wirtschaftsinformatiker','2021-06-30 18:11:21'),(4,'WI Tutoren','2021-06-30 18:12:28'),(5,'Erstsemester Verpackungstechnik','2021-06-30 18:12:51'),(6,'League Suchties','2021-06-30 18:13:07'),(7,'Stuttgart beste','2021-06-30 18:13:22'),(8,'HdM Bachelor Group','2021-06-30 18:13:38'),(9,'Coole Gruppe','2021-06-30 18:15:07'),(10,'Das A Team','2021-06-30 18:15:29'),(11,'Kellerkinder','2021-06-30 18:15:41'),(12,'Swagetti Yolonese','2021-06-30 18:16:05'),(13,'Kinda Sus','2021-06-30 18:16:15'),(14,'Auslandssemester Stuggi','2021-06-30 18:17:19'),(15,'4 gewinnt','2021-06-30 18:17:34'),(16,'Ess-Bar Gönner','2021-06-30 18:18:19'),(17,'WI Studies','2021-06-30 18:20:27'),(18,'IT Projekt Suizidgruppe','2021-06-30 18:20:56'),(19,'Mildi Gang','2021-06-30 18:21:39'),(20,'Patrick Singer - Kelly','2021-06-30 18:42:06'),(21,'Patrick Singer - Tate','2021-06-30 18:42:07'),(22,'Patrick Singer - Andrew','2021-06-30 18:42:09'),(23,'Patrick Singer - Darius','2021-06-30 18:42:11');
/*!40000 ALTER TABLE `chat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat_invitation`
--

DROP TABLE IF EXISTS `chat_invitation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chat_invitation` (
  `id` int NOT NULL,
  `creation_date` datetime NOT NULL,
  `is_accepted` tinyint NOT NULL,
  `chat_id` int NOT NULL,
  `target_user` int NOT NULL,
  `source_user` int NOT NULL,
  KEY `FK_source_user_chat_idx` (`source_user`),
  KEY `FK_target_user_chat_idx` (`target_user`),
  KEY `FK_chat_idx` (`chat_id`),
  CONSTRAINT `FK_chat` FOREIGN KEY (`chat_id`) REFERENCES `chat` (`id`),
  CONSTRAINT `FK_source_user_chat` FOREIGN KEY (`source_user`) REFERENCES `user` (`id`),
  CONSTRAINT `FK_target_user_chat` FOREIGN KEY (`target_user`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_invitation`
--

LOCK TABLES `chat_invitation` WRITE;
/*!40000 ALTER TABLE `chat_invitation` DISABLE KEYS */;
INSERT INTO `chat_invitation` VALUES (1,'2021-06-30 18:39:44',1,20,31,1),(2,'2021-06-30 18:40:04',1,21,31,2),(3,'2021-06-30 18:40:07',1,22,31,3),(4,'2021-06-30 18:40:09',1,23,31,4),(5,'2021-06-30 18:40:11',0,1,31,5),(6,'2021-06-30 18:40:15',0,1,31,6),(7,'2021-06-30 18:40:18',0,1,31,7),(8,'2021-06-30 18:40:22',0,1,31,8),(9,'2021-06-30 18:40:25',0,1,31,9),(10,'2021-06-30 18:40:28',0,1,31,10);
/*!40000 ALTER TABLE `chat_invitation` ENABLE KEYS */;
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
  `chat_id` int NOT NULL,
  `user_id` int NOT NULL,
  KEY `FK_chat_message_idx` (`chat_id`),
  KEY `FK_message_user_idx` (`user_id`),
  CONSTRAINT `FK_chat_message` FOREIGN KEY (`chat_id`) REFERENCES `chat` (`id`),
  CONSTRAINT `FK_message_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
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
  `is_accepted` tinyint NOT NULL,
  `study_group_id` int NOT NULL,
  `target_user` int NOT NULL,
  `source_user` int NOT NULL,
  KEY `FK_source_user_group_idx` (`source_user`),
  KEY `FK_target_user_group_idx` (`target_user`),
  KEY `FK_group_idx` (`study_group_id`),
  CONSTRAINT `FK_group` FOREIGN KEY (`study_group_id`) REFERENCES `studygroup` (`id`),
  CONSTRAINT `FK_source_user_group` FOREIGN KEY (`source_user`) REFERENCES `user` (`id`),
  CONSTRAINT `FK_target_user_group` FOREIGN KEY (`target_user`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_invitation`
--

LOCK TABLES `group_invitation` WRITE;
/*!40000 ALTER TABLE `group_invitation` DISABLE KEYS */;
INSERT INTO `group_invitation` VALUES (1,'2021-06-30 18:41:38',1,1,31,31),(2,'2021-06-30 18:42:36',1,2,31,31),(3,'2021-06-30 18:42:38',1,3,31,31),(4,'2021-06-30 18:42:40',1,4,31,31),(5,'2021-06-30 18:43:24',0,1,1,1),(6,'2021-06-30 18:43:29',0,1,2,2),(7,'2021-06-30 18:43:34',0,3,2,2),(8,'2021-06-30 18:43:40',0,2,7,7),(9,'2021-06-30 18:43:45',0,2,5,5);
/*!40000 ALTER TABLE `group_invitation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `learning_profile_group`
--

DROP TABLE IF EXISTS `learning_profile_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `learning_profile_group` (
  `id` int NOT NULL,
  `group_id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `prev_knowledge` int NOT NULL,
  `extroversion` int NOT NULL,
  `study_state` int NOT NULL,
  `frequency` int NOT NULL,
  `learntyp` int NOT NULL,
  `semester` int NOT NULL,
  `interest` varchar(45) NOT NULL,
  `degree_course` varchar(45) NOT NULL,
  `creation_date` datetime NOT NULL,
  KEY `FK_LPG_study_group_idx` (`group_id`),
  CONSTRAINT `FK_LPG_study_group` FOREIGN KEY (`group_id`) REFERENCES `studygroup` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learning_profile_group`
--

LOCK TABLES `learning_profile_group` WRITE;
/*!40000 ALTER TABLE `learning_profile_group` DISABLE KEYS */;
INSERT INTO `learning_profile_group` VALUES (1,1,'Datenstrukturen',5,3,1,3,4,4,'Geschichte','Wirtschaft','2021-06-20 07:26:14'),(2,2,'Alles oder Nix',5,2,1,3,2,3,'Marketing','Verpackungstechnik','2021-01-09 11:43:26'),(3,3,'Algorithmen',1,3,1,5,5,9,'Mathe','Informationsdesign','2021-05-23 19:43:12'),(4,4,'Organisation',5,4,1,4,1,1,'Organisation','Medieninformatik','2022-03-21 17:23:55'),(5,5,'Informatik',2,2,2,2,1,5,'Programmieren','Medieninformatik','2021-06-13 21:27:06'),(6,6,'Informatik',1,3,1,1,4,7,'Geschichte','Informationsdesign','2021-01-14 14:44:05'),(7,7,'Alles oder Nix',2,1,2,2,3,3,'Mathe','Wirtschaftsinformatik','2021-02-22 22:22:33'),(8,8,'Alles oder Nix',4,2,2,1,4,4,'Algebra','Informationsdesign','2020-09-01 06:11:53'),(9,9,'Algorithmen',2,2,1,1,4,10,'Geschichte','Medieninformatik','2021-09-02 01:42:24'),(10,10,'Algorithmen',2,2,2,1,1,4,'Mediengestaltung','Verpackungstechnik','2021-08-16 17:48:13'),(11,11,'Alles oder Nix',2,4,2,2,1,3,'Rechnungswesen','Wirtschaftsinformatik','2020-06-30 08:44:17'),(12,12,'Alles oder Nix',2,1,1,1,5,12,'Programmieren','Medieninformatik','2022-06-16 00:50:48'),(13,13,'Organisation',4,4,1,5,1,1,'Informatik','Medieninformatik','2021-07-12 03:57:31'),(14,14,'Geschichte',2,2,1,5,4,11,'Algorithmen','Wirtschaftsinformatik','2022-03-11 01:20:05'),(15,15,'Geschichte',5,2,2,4,5,4,'Rechnungswesen','Wirtschaftsinformatik','2022-02-25 14:30:25'),(16,16,'Organisation',1,4,1,2,2,7,'Marketing','Verpackungstechnik','2021-05-16 21:40:25'),(17,17,'Marketing',3,4,1,2,3,9,'Datenstrukturen','Medieninformatik','2022-05-09 21:20:33'),(18,18,'Geschichte',1,3,2,1,3,4,'Datenstrukturen','Verpackungstechnik','2020-09-29 02:41:45');
/*!40000 ALTER TABLE `learning_profile_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `learning_profile_user`
--

DROP TABLE IF EXISTS `learning_profile_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `learning_profile_user` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `prev_knowledge` int NOT NULL,
  `extroversion` int NOT NULL,
  `study_state` int NOT NULL,
  `frequency` int NOT NULL,
  `learntyp` int NOT NULL,
  `semester` int NOT NULL,
  `interest` varchar(45) NOT NULL,
  `degree_course` varchar(45) NOT NULL,
  `creation_date` datetime NOT NULL,
  KEY `FK_LPU_user_idx` (`user_id`),
  CONSTRAINT `FK_LPU_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learning_profile_user`
--

LOCK TABLES `learning_profile_user` WRITE;
/*!40000 ALTER TABLE `learning_profile_user` DISABLE KEYS */;
INSERT INTO `learning_profile_user` VALUES (1,1,'ac,',2,3,1,5,1,6,'Zocken','Wirtschaft','2021-03-21 18:45:56'),(2,2,'velit.',3,3,1,2,1,8,'IT','Wirtschaftsinformatik','2020-03-06 03:26:11'),(3,3,'Proin',1,4,1,4,4,11,'Tennis','Informationsdesign','2021-11-30 23:12:08'),(4,4,'nisi',1,2,1,4,2,5,'Gitarre','Medienwirtschaft','2021-02-12 21:20:13'),(5,5,'Quisque',3,4,1,1,1,1,'Zocken','Medienwirtschaft','2020-09-22 18:43:17'),(6,6,'dui.',4,5,2,2,5,12,'Golf','Medieninformatik','2021-04-02 07:18:05'),(7,7,'Mauris',4,2,2,2,3,9,'Autos','Verpackungstechnik','2022-02-15 18:35:21'),(8,8,'vulputate',5,3,2,5,5,8,'Gitarre','Verpackungstechnik','2020-01-06 02:32:45'),(9,9,'dui',3,3,1,2,1,2,'Geschichte','Verpackungstechnik','2021-02-04 01:40:19'),(10,10,'risus.',1,3,1,4,2,1,'Tennis','Informationsdesign','2021-03-19 06:24:26'),(11,11,'Maecenas',3,4,2,2,5,3,'Golf','Informationsdesign','2022-03-24 23:43:54'),(12,12,'vel',1,1,1,2,1,2,'Golf','Wirtschaftsinformatik','2022-01-30 03:20:17'),(13,13,'ipsum.',3,1,2,3,5,6,'Schwimmen','Medieninformatik','2020-12-15 03:25:12'),(14,14,'aliquam',4,5,1,1,5,12,'Schwimmen','Medienwirtschaft','2022-05-29 18:42:51'),(15,15,'posuere',1,1,1,4,3,4,'Gitarre','Informationsdesign','2021-07-17 13:36:49'),(16,16,'cursus',2,2,1,4,5,12,'Tennis','Informationsdesign','2020-03-20 15:53:58'),(17,17,'Suspendisse',4,4,2,2,2,2,'Zocken','Online Medienmanagement','2021-06-09 07:29:45'),(18,18,'ante,',5,1,1,4,3,4,'IT','Medienwirtschaft','2022-05-08 08:04:33'),(19,19,'Suspendisse',5,5,2,5,3,6,'Autos','Verpackungstechnik','2020-11-05 15:38:39'),(20,20,'egestas.',5,3,1,5,3,8,'Golf','Wirtschaft','2020-06-18 14:49:54'),(21,21,'mauris',3,3,1,5,1,2,'Autos','Informationsdesign','2020-01-08 08:50:33'),(22,22,'luctus',1,5,1,4,4,10,'Golf','Verpackungstechnik','2021-11-27 20:52:05'),(23,23,'ligula.',3,1,1,5,4,5,'Zocken','Informationsdesign','2020-08-23 17:27:28'),(24,24,'mauris',3,4,2,5,4,12,'Fußball','Wirtschaftsinformatik','2020-04-17 22:37:01'),(25,25,'Proin',2,4,1,2,1,4,'IT','Wirtschaftsinformatik','2020-04-28 23:44:39'),(26,26,'eget',3,4,1,5,1,11,'Golf','Informationsdesign','2022-06-10 05:29:38'),(27,27,'porttitor',2,5,2,1,4,3,'Fußball','Medienwirtschaft','2022-03-12 20:20:53'),(28,28,'non',2,1,1,5,3,8,'Golf','Wirtschaftsinformatik','2020-05-14 08:21:13'),(29,29,'orci,',3,2,2,5,2,7,'Geschichte','Wirtschaftsinformatik','2021-10-20 01:34:52'),(30,30,'penatibus',2,4,2,5,2,1,'Fußball','Wirtschaftsinformatik','2022-02-20 16:41:23'),(31,31,'profile',4,3,1,4,3,9,'Gitarre','Wirtschaftsinformatik','2021-06-30 17:54:13'),(32,32,'profile',3,3,1,5,3,9,'Gitarre','Wirtschaftsinformatik','2021-06-30 17:57:50');
/*!40000 ALTER TABLE `learning_profile_user` ENABLE KEYS */;
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
  `chat_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_group_chat_idx` (`chat_id`),
  CONSTRAINT `FK_group_chat` FOREIGN KEY (`chat_id`) REFERENCES `chat` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studygroup`
--

LOCK TABLES `studygroup` WRITE;
/*!40000 ALTER TABLE `studygroup` DISABLE KEYS */;
INSERT INTO `studygroup` VALUES (1,'Mathe Gruppe','2021-06-30 18:29:02',2),(2,'Wirtschaftsinformatiker','2021-06-30 18:29:44',3),(3,'WI Tutoren','2021-06-30 18:29:55',4),(4,'Erstsemester Verpackungstechnik','2021-06-30 18:30:06',5),(5,'League Suchties','2021-06-30 18:30:14',6),(6,'Stuttgart beste','2021-06-30 18:30:25',7),(7,'HdM Bachelor Group','2021-06-30 18:30:36',8),(8,'Coole Gruppe','2021-06-30 18:30:46',9),(9,'Das A Team','2021-06-30 18:30:57',10),(10,'Kellerkinder','2021-06-30 18:31:05',11),(11,'Swagetti Yolonese','2021-06-30 18:31:15',12),(12,'Kinda Sus','2021-06-30 18:31:24',13),(13,'Auslandssemester Stuggi','2021-06-30 18:31:31',14),(14,'A4 gewinnt','2021-06-30 18:31:39',15),(15,'Ess-Bar Gönner','2021-06-30 18:31:49',16),(16,'WI Studies','2021-06-30 18:32:00',17),(17,'IT Projekt Suizidgruppe','2021-06-30 18:32:08',18),(18,'Mildi Gang','2021-06-30 18:32:18',19);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Kelly','Dean','P.O. Box 563, 2352 Nunc Avenue','ornare.egestas@ligulaelitpretium.ca','16060601 6962','2021-11-28 10:56:35'),(2,'Tate','Macias','4764 Et Rd.','sit@auctorveliteget.co.uk','16440226 3778','2020-06-22 16:34:58'),(3,'Andrew','Washington','P.O. Box 980, 334 Eget, Rd.','ac.feugiat@ategestasa.org','16500301 6168','2022-02-06 02:20:07'),(4,'Darius','Hancock','Ap #422-9294 A, St.','ornare.In@anuncIn.net','16030710 1717','2021-03-24 11:31:06'),(5,'Alvin','Todd','312-9423 Enim. Avenue','diam@Craslorem.edu','16480323 0053','2021-12-23 12:33:01'),(6,'Gil','Collier','P.O. Box 284, 1387 Lacus Rd.','eu.erat@dapibusrutrumjusto.org','16271030 0761','2021-02-01 20:10:00'),(7,'Ross','Mclaughlin','P.O. Box 490, 2002 Hendrerit Rd.','elementum.purus@atfringilla.ca','16010907 0862','2020-07-10 03:24:59'),(8,'Blake','Rodriquez','P.O. Box 704, 6190 Mauris St.','inceptos@nec.ca','16150311 1740','2020-10-02 13:11:22'),(9,'Wade','Juarez','P.O. Box 157, 3452 Eu, Rd.','eget@faucibus.co.uk','16030203 7254','2021-05-24 09:52:37'),(10,'Colby','Suarez','P.O. Box 590, 4373 Erat. Street','egestas.Fusce.aliquet@scelerisque.edu','16350322 4564','2022-04-20 05:52:29'),(11,'Ignatius','Moreno','9339 Nunc St.','odio.auctor@aauctor.edu','16771211 1108','2021-10-31 00:46:50'),(12,'Aladdin','Skinner','Ap #232-9250 Sodales St.','ornare.tortor@sem.ca','16650508 7780','2020-05-23 21:52:48'),(13,'Bernard','Goff','530-4584 A Rd.','facilisis.Suspendisse@Donecsollicitudin.edu','16120907 7351','2021-02-21 02:32:17'),(14,'Cadman','Wood','451 Egestas Avenue','ullamcorper.Duis@faucibusorciluctus.co.uk','16150126 0390','2021-03-17 17:48:11'),(15,'Ivor','Hull','492 Enim Rd.','vel.arcu.Curabitur@Sed.org','16940112 7940','2022-03-09 10:27:50'),(16,'Lance','Pope','P.O. Box 195, 788 Rutrum Av.','enim@Nam.co.uk','16390515 0938','2022-03-11 03:19:46'),(17,'Sean','Morrow','156-4117 Pede, St.','tortor.Integer.aliquam@ante.co.uk','16831104 2041','2021-06-04 21:15:29'),(18,'Cody','Glenn','P.O. Box 869, 5061 Eros Road','amet@Sedpharetrafelis.co.uk','16970430 1325','2020-09-01 00:20:30'),(19,'Jakeem','Sosa','4718 Erat. Avenue','Nam@magna.edu','16520202 9137','2021-07-27 03:24:51'),(20,'Eagan','Morales','Ap #374-5463 Inceptos St.','ante.blandit@laoreetipsum.org','16820404 6034','2020-06-17 17:03:45'),(21,'Chester','Burks','P.O. Box 258, 9641 Suspendisse Road','risus.Donec@nonlobortisquis.net','16460601 0785','2020-07-22 09:33:57'),(22,'Clayton','Watts','1205 Sapien, St.','posuere.cubilia@laciniaorciconsectetuer.co.uk','16211005 2772','2020-06-12 16:31:19'),(23,'Zeph','Rosa','6806 Sed Av.','Nunc.mauris.sapien@nonluctussit.net','16940515 7745','2021-03-27 21:15:53'),(24,'Norman','Burton','Ap #966-5152 Malesuada Ave','a@urnaNullamlobortis.com','16030210 0425','2021-03-07 10:42:46'),(25,'Harding','Townsend','P.O. Box 690, 6735 Orci Avenue','a@velitPellentesque.net','16821113 6521','2020-10-22 07:22:23'),(26,'Abel','Douglas','P.O. Box 314, 524 Malesuada Ave','quis@cursusinhendrerit.ca','16470524 6041','2020-06-22 01:04:27'),(27,'Luke','Bell','P.O. Box 683, 5657 Auctor Av.','primis.in@vulputate.com','16820515 1676','2021-11-16 01:10:39'),(28,'Dolan','Duncan','P.O. Box 986, 4152 Erat, Ave','lobortis.nisi.nibh@Curabitursed.org','16710408 2305','2022-04-14 10:07:22'),(29,'Mohammad','Barrett','127-5220 Neque Road','eget.magna@tortordictumeu.com','16550729 4998','2020-12-17 22:20:16'),(30,'Moses','Koch','P.O. Box 737, 7742 Nam Street','erat.vel.pede@porttitorvulputate.ca','16380205 1072','2021-12-02 23:56:48'),(31,'Patrick Singer','','','patrick.singer1999@gmail.com','bUIElVVYTQPW22h4Sc4SvzjnMLx1','2021-06-30 17:54:13'),(32,'Patrick Singer','','','patrick.singer23@gmail.com','73h6OZTUtZceUb2iduxQFfAB7wg1','2021-06-30 17:57:50');
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

-- Dump completed on 2021-06-30 18:45:37
