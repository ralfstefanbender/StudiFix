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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat`
--

LOCK TABLES `chat` WRITE;
/*!40000 ALTER TABLE `chat` DISABLE KEYS */;
INSERT INTO `chat` VALUES (1,'Chati','2021-05-12 13:53:07'),(2,'Mathe Chat','2021-05-15 14:47:11');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_invitation`
--

LOCK TABLES `chat_invitation` WRITE;
/*!40000 ALTER TABLE `chat_invitation` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_message`
--

LOCK TABLES `chat_message` WRITE;
/*!40000 ALTER TABLE `chat_message` DISABLE KEYS */;
INSERT INTO `chat_message` VALUES (1,'Beispiel Text: Blablabla','2021-05-15 15:05:45',1,1);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_invitation`
--

LOCK TABLES `group_invitation` WRITE;
/*!40000 ALTER TABLE `group_invitation` DISABLE KEYS */;
INSERT INTO `group_invitation` VALUES (1,'2021-05-15 16:37:50',0,3,3,1),(2,'2021-05-15 16:39:53',0,3,3,1);
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
  KEY `FK_user_idx` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learning_profile`
--

LOCK TABLES `learning_profile` WRITE;
/*!40000 ALTER TABLE `learning_profile` DISABLE KEYS */;
INSERT INTO `learning_profile` VALUES (1,'Mathe','Mittelmäßig',4,3,5,4,5,'Algebrah','Mathematik','2021-11-28 10:56:35'),(2,'Informatik','Garkeine',2,3,4,5,6,'','Wirtschaftsinformatik','2021-05-15 16:41:13');
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
  `group_name` varchar(45) NOT NULL,
  `creation_date` datetime NOT NULL,
  `chat_id` int NOT NULL,
  `learning_profile_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_group_chat_idx` (`chat_id`),
  KEY `FK_group_lp_idx` (`learning_profile_id`),
  CONSTRAINT `FK_group_chat` FOREIGN KEY (`chat_id`) REFERENCES `chat` (`id`),
  CONSTRAINT `FK_group_learning_profile` FOREIGN KEY (`learning_profile_id`) REFERENCES `learning_profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studygroup`
--

LOCK TABLES `studygroup` WRITE;
/*!40000 ALTER TABLE `studygroup` DISABLE KEYS */;
INSERT INTO `studygroup` VALUES (1,'Studifix1','2021-05-15 13:34:50',1,1),(2,'Studifix1','2021-05-15 13:40:32',1,1),(3,'Studifix1','2021-05-15 13:41:07',1,1),(4,'Studifix1','2021-05-15 13:41:36',1,1),(5,'Studifix1','2021-05-15 16:40:31',1,1),(6,'Studifix1','2021-05-20 12:02:43',1,1);
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
  `learning_profile_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_user_learning_p_idx` (`learning_profile_id`),
  CONSTRAINT `FK_user_learning_profile_id` FOREIGN KEY (`learning_profile_id`) REFERENCES `learning_profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Kelly','Dean','P.O. Box 563, 2352 Nunc Avenue','ornare.egestas@ligulaelitpretium.ca','16060601 6962','2021-11-28 10:56:35',1),(2,'Tate','Macias','4764 Et Rd.','sit@auctorveliteget.co.uk','16440226 3778','2020-06-22 16:34:58',1),(3,'Andrew','Washington','P.O. Box 980, 334 Eget, Rd.','ac.feugiat@ategestasa.org','16500301 6168','2022-02-06 02:20:07',1),(4,'Darius','Hancock','Ap #422-9294 A, St.','ornare.In@anuncIn.net','16030710 1717','2021-03-24 11:31:06',1),(5,'Alvin','Todd','312-9423 Enim. Avenue','diam@Craslorem.edu','16480323 0053','2021-12-23 12:33:01',1),(6,'Gil','Collier','P.O. Box 284, 1387 Lacus Rd.','eu.erat@dapibusrutrumjusto.org','16271030 0761','2021-02-01 20:10:00',1),(7,'Ross','Mclaughlin','P.O. Box 490, 2002 Hendrerit Rd.','elementum.purus@atfringilla.ca','16010907 0862','2020-07-10 03:24:59',1),(8,'Blake','Rodriquez','P.O. Box 704, 6190 Mauris St.','inceptos@nec.ca','16150311 1740','2020-10-02 13:11:22',1),(9,'Wade','Juarez','P.O. Box 157, 3452 Eu, Rd.','eget@faucibus.co.uk','16030203 7254','2021-05-24 09:52:37',2),(10,'Colby','Suarez','P.O. Box 590, 4373 Erat. Street','egestas.Fusce.aliquet@scelerisque.edu','16350322 4564','2022-04-20 05:52:29',1),(11,'Ignatius','Moreno','9339 Nunc St.','odio.auctor@aauctor.edu','16771211 1108','2021-10-31 00:46:50',2),(12,'Aladdin','Skinner','Ap #232-9250 Sodales St.','ornare.tortor@sem.ca','16650508 7780','2020-05-23 21:52:48',1),(13,'Bernard','Goff','530-4584 A Rd.','facilisis.Suspendisse@Donecsollicitudin.edu','16120907 7351','2021-02-21 02:32:17',2),(14,'Cadman','Wood','451 Egestas Avenue','ullamcorper.Duis@faucibusorciluctus.co.uk','16150126 0390','2021-03-17 17:48:11',1),(15,'Ivor','Hull','492 Enim Rd.','vel.arcu.Curabitur@Sed.org','16940112 7940','2022-03-09 10:27:50',2),(16,'Lance','Pope','P.O. Box 195, 788 Rutrum Av.','enim@Nam.co.uk','16390515 0938','2022-03-11 03:19:46',1),(17,'Sean','Morrow','156-4117 Pede, St.','tortor.Integer.aliquam@ante.co.uk','16831104 2041','2021-06-04 21:15:29',2),(18,'Cody','Glenn','P.O. Box 869, 5061 Eros Road','amet@Sedpharetrafelis.co.uk','16970430 1325','2020-09-01 00:20:30',1),(19,'Jakeem','Sosa','4718 Erat. Avenue','Nam@magna.edu','16520202 9137','2021-07-27 03:24:51',2),(20,'Eagan','Morales','Ap #374-5463 Inceptos St.','ante.blandit@laoreetipsum.org','16820404 6034','2020-06-17 17:03:45',1),(21,'Chester','Burks','P.O. Box 258, 9641 Suspendisse Road','risus.Donec@nonlobortisquis.net','16460601 0785','2020-07-22 09:33:57',2),(22,'Clayton','Watts','1205 Sapien, St.','posuere.cubilia@laciniaorciconsectetuer.co.uk','16211005 2772','2020-06-12 16:31:19',1),(23,'Zeph','Rosa','6806 Sed Av.','Nunc.mauris.sapien@nonluctussit.net','16940515 7745','2021-03-27 21:15:53',1),(24,'Norman','Burton','Ap #966-5152 Malesuada Ave','a@urnaNullamlobortis.com','16030210 0425','2021-03-07 10:42:46',1),(25,'Harding','Townsend','P.O. Box 690, 6735 Orci Avenue','a@velitPellentesque.net','16821113 6521','2020-10-22 07:22:23',1),(26,'Abel','Douglas','P.O. Box 314, 524 Malesuada Ave','quis@cursusinhendrerit.ca','16470524 6041','2020-06-22 01:04:27',1),(27,'Luke','Bell','P.O. Box 683, 5657 Auctor Av.','primis.in@vulputate.com','16820515 1676','2021-11-16 01:10:39',1),(28,'Dolan','Duncan','P.O. Box 986, 4152 Erat, Ave','lobortis.nisi.nibh@Curabitursed.org','16710408 2305','2022-04-14 10:07:22',1),(29,'Mohammad','Barrett','127-5220 Neque Road','eget.magna@tortordictumeu.com','16550729 4998','2020-12-17 22:20:16',1),(30,'Moses','Koch','P.O. Box 737, 7742 Nam Street','erat.vel.pede@porttitorvulputate.ca','16380205 1072','2021-12-02 23:56:48',1),(31,'Reece','Livingston','Ap #124-3326 Placerat, Road','ac.tellus@elit.org','16891028 4465','2022-04-25 07:32:22',1),(32,'Dennis','Nixon','7083 Ut, Street','erat.volutpat@est.com','16900512 1521','2020-11-22 14:47:25',1),(33,'Austin','Blevins','216-862 Nec St.','pede.malesuada.vel@Nullamlobortis.org','16910707 0345','2021-07-20 05:32:43',1),(34,'Rogan','Hooper','P.O. Box 961, 6543 Felis Avenue','euismod@ac.co.uk','16770713 5542','2021-05-15 12:17:43',1),(35,'Damian','Wright','Ap #116-6163 Placerat St.','in.magna.Phasellus@Pellentesquehabitantmorbi.net','16851205 5594','2020-06-11 14:37:40',1),(36,'Travis','Barnes','8541 Eu Street','Nullam.scelerisque.neque@porttitoreros.co.uk','16760530 5155','2021-03-27 15:30:32',1),(37,'Ignatius','Terry','3244 Nec Rd.','nunc@bibendumsed.ca','16161205 7917','2020-07-02 11:00:47',1),(38,'Derek','Fry','Ap #647-4501 Mauris Av.','cursus.a@Duisrisusodio.co.uk','16300501 8761','2021-07-30 18:06:57',1),(39,'Avram','Casey','420 Cras Av.','pharetra.ut@mattisIntegereu.org','16110211 0028','2020-08-10 09:34:56',1),(40,'Bradley','Williams','9396 Vulputate, Street','Suspendisse.sagittis@tellus.edu','16230204 7408','2021-05-31 16:33:27',1),(41,'Peter','Thornton','P.O. Box 881, 2474 Etiam Ave','aliquet@sem.edu','16770727 1065','2022-04-28 00:23:17',1),(42,'Kenyon','Kerr','Ap #737-662 Euismod St.','semper.auctor@Maecenaslibero.ca','16231016 5374','2021-07-08 08:51:14',2),(43,'Bevis','Molina','626-6143 Pharetra. Ave','vitae.risus@eleifendvitaeerat.org','16020430 2392','2020-07-12 06:17:35',1),(44,'Xanthus','Snider','7104 Nunc. St.','consectetuer@pharetranibhAliquam.edu','16310123 3900','2022-02-11 21:53:03',2),(45,'Allistair','Shepard','P.O. Box 525, 7842 Mattis. Road','Morbi.accumsan@ac.org','16150820 4979','2021-09-27 21:53:06',1),(46,'Andrew','Cruz','Ap #162-2144 Nisi Av.','nec@maurisrhoncusid.com','16411111 6937','2020-08-31 13:03:36',2),(47,'Oleg','Odom','P.O. Box 664, 7496 Duis Rd.','metus@laoreet.edu','16730103 3721','2020-07-18 12:44:27',1),(48,'Hall','Foreman','980-7969 Lacus, Ave','massa@hendreritaarcu.edu','16641107 6935','2021-01-10 23:10:01',2),(49,'Carter','Shaw','4303 Donec Rd.','litora@urna.ca','16971014 1491','2022-02-08 11:49:18',1),(50,'Tanner','Hickman','Ap #452-9496 Nec Road','mi.tempor@in.co.uk','16701106 0899','2021-01-31 10:38:51',2),(51,'Orlando','Atkinson','P.O. Box 505, 7594 In Road','lacus.vestibulum.lorem@mifelisadipiscing.org','16741130 1893','2020-09-18 13:25:35',1),(52,'Arsenio','Summers','3784 Lobortis Rd.','ridiculus@orciDonec.edu','16310508 0356','2021-02-19 05:18:50',2),(53,'Martin','Schultz','Ap #301-4029 Arcu Av.','lorem.vitae.odio@dignissimmagnaa.co.uk','16750102 7374','2020-10-30 15:59:31',1),(54,'Yardley','Barton','Ap #528-7084 Rutrum St.','pede.ac@volutpatNulla.com','16750404 3733','2020-11-05 09:40:24',2),(55,'Ferdinand','Mcconnell','3296 A St.','metus.Aliquam.erat@Nullaaliquet.com','16881118 7668','2020-09-23 10:16:22',1),(56,'Hakeem','Richmond','P.O. Box 891, 2358 Ac Ave','auctor.ullamcorper@fringillapurusmauris.com','16690624 5979','2020-05-16 22:28:15',2),(57,'Kasper','Kelly','474-3795 Ligula. Road','parturient.montes@ametorciUt.net','16690717 8336','2020-06-02 12:54:03',2),(58,'Cade','Newman','P.O. Box 756, 6690 Eros Rd.','fermentum@lorem.com','16300206 4040','2022-01-25 08:44:18',1),(59,'Abbot','Dillon','7978 Ante Road','Duis.at.lacus@vulputate.co.uk','16720318 3673','2021-03-10 02:46:28',1),(60,'Lewis','Jimenez','Ap #972-3725 Tellus. Avenue','dui.semper@enim.org','16501214 7921','2022-01-07 09:19:11',1),(61,'Conan','Carson','Ap #956-4531 Nunc. Rd.','orci.consectetuer@dapibusquamquis.net','16280523 4636','2021-02-09 21:45:32',2),(62,'Troy','Woods','7305 In Street','a.ultricies@ac.org','16400617 8422','2022-04-30 22:26:10',2),(63,'Hamish','Kennedy','Ap #304-3444 Mollis. Ave','non.enim@vel.com','16420509 7076','2021-10-19 03:42:54',2),(64,'Baker','Shannon','P.O. Box 745, 6853 Nisl. Rd.','nec.tellus@nibh.edu','16530504 7721','2021-01-10 01:37:32',1),(65,'Graham','Gray','Ap #315-5504 Hendrerit Ave','dapibus.rutrum@ametlorem.co.uk','16160703 1851','2022-04-01 15:34:00',1),(66,'Orlando','Avery','P.O. Box 695, 9064 Odio. Avenue','mauris@tinciduntnunc.ca','16660828 7238','2022-01-03 03:10:39',1),(67,'Jonah','Valencia','5883 Nunc Street','egestas@Namnullamagna.ca','16880619 0594','2020-07-13 06:01:29',1),(68,'Holmes','Reynolds','P.O. Box 803, 374 Quis Road','varius.Nam@augueeutempor.ca','16400322 0318','2020-10-06 12:10:49',1),(69,'Herrod','Joseph','8375 Sollicitudin Rd.','elementum@etmagnis.ca','16111111 0480','2022-01-22 12:44:27',2),(70,'Simon','Tyler','867 Dui Av.','erat.vel.pede@faucibusutnulla.net','16100610 1610','2020-07-23 19:36:30',1),(71,'Christian','Gutierrez','8338 Laoreet, Rd.','gravida@volutpatNulladignissim.edu','16511108 2110','2021-06-09 03:12:10',2),(72,'Kibo','Hinton','P.O. Box 232, 4432 Egestas Rd.','ornare.In@Sed.ca','16090117 6859','2020-08-03 12:19:35',1),(73,'Yuli','Carney','Ap #509-1018 Velit. St.','rutrum.magna.Cras@gravidasagittis.org','16260719 1992','2021-12-17 23:39:47',2),(74,'Caleb','Hall','Ap #421-8088 Eu, Street','diam.Proin.dolor@id.edu','16470110 0945','2021-02-24 04:13:56',2),(75,'Ali','Hinton','Ap #585-1950 Lectus. Av.','In.tincidunt.congue@luctusCurabitur.net','16290221 6585','2021-02-28 01:38:58',1),(76,'Emery','Haney','P.O. Box 944, 3698 Rutrum Rd.','turpis.In@pedeCum.com','16061028 5785','2021-06-23 08:28:30',1),(77,'Jamal','Burt','P.O. Box 665, 8606 Suspendisse Rd.','eu.ligula.Aenean@egetodioAliquam.net','16131226 2890','2021-08-30 04:04:52',1),(78,'Macon','Gilliam','Ap #232-2982 Magna. Street','Phasellus@odioEtiam.net','16850311 3014','2021-10-07 17:07:59',2),(79,'Hakeem','Wood','4996 Nunc Street','mi.enim.condimentum@dolorsit.ca','16491012 6996','2022-04-18 04:08:26',2),(80,'Channing','Dyer','Ap #654-1363 Fringilla Rd.','Nunc@Proin.net','16740206 2488','2022-02-06 05:11:33',2),(81,'Ronan','Sawyer','P.O. Box 136, 5220 Lobortis Rd.','lacus@utmolestiein.edu','16220501 2640','2021-07-15 06:29:04',1),(82,'Nehru','Mccoy','414-3864 Pellentesque Avenue','laoreet.libero@ligula.net','16830527 5326','2020-10-13 10:22:03',1),(83,'Gage','Combs','3970 Justo. St.','amet@Utsagittis.ca','16241020 4289','2020-12-08 12:03:07',2),(84,'Zephania','Burch','P.O. Box 737, 7730 Nisi Avenue','magna@ac.net','16330808 1276','2021-07-13 00:34:24',2),(85,'Solomon','Hall','2072 Non, Road','ipsum.primis@congue.ca','16110922 6868','2020-08-04 09:21:20',2),(86,'Avram','Roman','303-4097 Eu Street','eleifend.nec.malesuada@quamdignissimpharetra.org','16780902 2093','2021-03-21 01:12:10',1),(87,'Avram','Oneil','Ap #974-8808 Vitae Av.','arcu@nibh.co.uk','16500324 8621','2020-11-22 20:32:40',1),(88,'Patrick','Brennan','5930 Aliquam St.','ullamcorper.Duis@scelerisquescelerisquedui.org','16700411 0214','2021-01-25 16:10:19',2),(89,'Stuart','Warren','1243 Ac, Avenue','nec.euismod@inceptos.org','16090902 9647','2021-03-15 07:25:12',1),(90,'Vance','Daugherty','132-7929 Sodales Rd.','rhoncus@et.net','16121019 0276','2021-02-28 06:01:29',2),(91,'Leo','Burns','P.O. Box 728, 4440 Malesuada Av.','non.luctus.sit@sapien.co.uk','16540513 8669','2021-01-02 05:56:36',2),(92,'Kibo','Holden','P.O. Box 851, 5455 Sociis Ave','tincidunt@iaculis.com','16420325 0834','2021-08-22 19:21:55',1),(93,'Driscoll','Mcintosh','Ap #623-3585 Lacus. Avenue','Quisque.libero.lacus@etipsumcursus.com','16340230 4426','2020-12-04 08:57:34',2),(94,'Francis','Kramer','451-1874 Sed Avenue','rutrum.magna.Cras@ridiculusmus.co.uk','16670717 5318','2022-02-10 14:14:41',1),(95,'Graiden','Doyle','1373 Donec Av.','lobortis.augue@nunc.com','16990827 0466','2021-09-06 22:17:00',2),(96,'Kane','Tyler','Ap #545-3962 Sed, Ave','in.lobortis.tellus@pharetranibh.co.uk','16320630 2923','2021-05-29 04:58:11',1),(97,'Tobias','Lamb','1032 Sapien. St.','neque@egestasAliquamfringilla.edu','16070612 9632','2021-01-23 17:33:02',2),(98,'Finn','Reid','618 Non Rd.','tellus.Phasellus@egestashendrerit.edu','16440520 1080','2020-11-02 23:13:07',1),(99,'Daniel','Reid','Ap #541-896 At, St.','lobortis.quam@ipsum.co.uk','16311207 5530','2021-03-14 00:08:48',2),(100,'Garrison','Puckett','P.O. Box 548, 4531 Aenean Street','molestie.in@facilisis.com','16220918 7661','2021-02-24 11:25:19',1);
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

-- Dump completed on 2021-05-20 12:07:35
