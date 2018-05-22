/*
Navicat MySQL Data Transfer

Source Server         : che
Source Server Version : 50640
Source Host           : localhost:3306
Source Database       : che168

Target Server Type    : MYSQL
Target Server Version : 50640
File Encoding         : 65001

Date: 2018-05-04 17:57:03
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for che
-- ----------------------------
DROP TABLE IF EXISTS `che`;
CREATE TABLE `che` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `dealerid` char(11) DEFAULT NULL,
  `infoid` char(11) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `car_title` varchar(255) DEFAULT NULL COMMENT '标题',
  `car_price` char(10) DEFAULT NULL COMMENT '价格',
  `car_mileage` char(10) DEFAULT NULL COMMENT '行驶里程',
  `car_firstLicensed` char(10) DEFAULT NULL COMMENT '首次上牌时间',
  `car_displacement` char(10) DEFAULT NULL COMMENT '排量',
  `car_gearbox` char(10) DEFAULT NULL COMMENT '档位',
  `car_location` char(10) DEFAULT NULL COMMENT '所在地',
  `car_standard` char(10) DEFAULT NULL COMMENT '排放标准',
  `car_address` varchar(255) DEFAULT NULL COMMENT '看车地址',
  `car_inspection_date` varchar(255) DEFAULT NULL COMMENT '年检到期时间',
  `car_insurance_date` varchar(255) DEFAULT NULL COMMENT '保险到期时间',
  `car_expiration_date` varchar(255) DEFAULT NULL COMMENT '质保到期时间',
  `Change_number` char(11) DEFAULT NULL COMMENT '过户次数',
  `car_use` char(10) DEFAULT NULL COMMENT '用途',
  `maintain` varchar(255) DEFAULT NULL COMMENT '维护保养',
  `dealerName` varchar(255) DEFAULT NULL COMMENT '商家名称',
  `car_engine` varchar(255) DEFAULT NULL COMMENT '发送机',
  `car_level` char(10) DEFAULT NULL COMMENT '等级',
  `car_color` char(10) DEFAULT NULL COMMENT '颜色',
  `car_fuel_type` char(10) DEFAULT NULL COMMENT '燃油标号',
  `car_drive_mode` char(10) DEFAULT NULL COMMENT '驱动方式',
  `car_image` text COMMENT '图片地址链接',
  `is_down` int(11) DEFAULT '0' COMMENT '是否下载',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=167 DEFAULT CHARSET=utf8;
