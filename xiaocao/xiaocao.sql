/*
Navicat MySQL Data Transfer

Source Server         : che
Source Server Version : 50640
Source Host           : localhost:3306
Source Database       : xiaocao

Target Server Type    : MYSQL
Target Server Version : 50640
File Encoding         : 65001

Date: 2018-05-24 18:20:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for xiaocao_base
-- ----------------------------
DROP TABLE IF EXISTS `xiaocao_base`;
CREATE TABLE `xiaocao_base` (
  `id` int(11) DEFAULT NULL,
  `business_id` int(11) DEFAULT NULL,
  `business_classify` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `uesr_nick` varchar(255) DEFAULT NULL,
  `creat_date` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for xiaocao_picture
-- ----------------------------
DROP TABLE IF EXISTS `xiaocao_picture`;
CREATE TABLE `xiaocao_picture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `video_id` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `user_nick` varchar(255) DEFAULT NULL,
  `creat_date` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `video_path` varchar(255) DEFAULT NULL,
  `is_download` int(10) unsigned zerofill DEFAULT NULL,
  `local_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for xiaocao_text
-- ----------------------------
DROP TABLE IF EXISTS `xiaocao_text`;
CREATE TABLE `xiaocao_text` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `video_id` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `user_nick` varchar(255) DEFAULT NULL,
  `creat_date` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `video_path` varchar(255) DEFAULT NULL,
  `is_download` int(10) unsigned zerofill DEFAULT NULL,
  `local_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for xiaocao_video
-- ----------------------------
DROP TABLE IF EXISTS `xiaocao_video`;
CREATE TABLE `xiaocao_video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `business_id` varchar(255) DEFAULT NULL,
  `classify` varchar(255) DEFAULT NULL,
  `video_url` varchar(255) DEFAULT NULL,
  `is_download` int(10) unsigned zerofill DEFAULT NULL,
  `local_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
