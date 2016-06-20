/*CREATE DATABASE `sewa`; /*!40100 DEFAULT CHARACTER SET utf8 */

/*USE sewa; */

DROP TABLE IF exists category;
CREATE TABLE `category` (
  `categoryid` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`categoryid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF exists subcategory;
CREATE TABLE `subcategory` (
  `subcategoryid` INT NOT NULL AUTO_INCREMENT,
  `subcategory_name` VARCHAR(255) NULL,
  `categoryid` INT NOT NULL,
  PRIMARY KEY (`subcategoryid`),
  INDEX `categoryid_idx` (`categoryid` ASC),
  CONSTRAINT `categoryid`
    FOREIGN KEY (`categoryid`)
    REFERENCES `category` (`categoryid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

DROP TABLE IF exists user;
CREATE TABLE `user` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `username` bigint(20) NOT NULL,
  `password` varchar(50) NOT NULL,
  `name` varchar(150) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `area` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `postalcode` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

DROP TABLE IF exists service;
CREATE TABLE `service` (
  `serviceid` INT NOT NULL AUTO_INCREMENT,
  `categoryid` INT NOT NULL,
  `subcategoryid` INT NULL,
  `userid` INT NULL,
  `firmname` VARCHAR(255) NULL,
  PRIMARY KEY (`serviceid`),
  INDEX `categoryid_idx` (`categoryid` ASC),
  INDEX `subcategoryid_idx` (`subcategoryid` ASC),
  INDEX `userid_idx` (`userid` ASC),
  CONSTRAINT `categoryid_fk`
    FOREIGN KEY (`categoryid`)
    REFERENCES `sewa`.`Category` (`categoryid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `subcategoryid_fk`
    FOREIGN KEY (`subcategoryid`)
    REFERENCES `sewa`.`SubCategory` (`subcategoryid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `userid_fk`
    FOREIGN KEY (`userid`)
    REFERENCES `sewa`.`user` (`userid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

DROP TABLE IF exists job;
CREATE TABLE `job` (
  `jobid` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `details` VARCHAR(255) NULL,
  `serviceid` INT NOT NULL,
  PRIMARY KEY (`jobid`),
  INDEX `serviceid_idx` (`serviceid` ASC),
  CONSTRAINT `serviceid_fk`
    FOREIGN KEY (`serviceid`)
    REFERENCES `sewa`.`service` (`serviceid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

DROP TABLE IF EXISTS country;
CREATE TABLE `country` (
  `countryid` INT NOT NULL AUTO_INCREMENT,
  `countryname` VARCHAR(255) NULL,
  PRIMARY KEY (`countryid`));


DROP TABLE IF exists state;
CREATE TABLE `state` (
  `stateid` int(11) NOT NULL AUTO_INCREMENT,
  `statename` varchar(255) NOT NULL,
  `countryid` int(11) NOT NULL,
  PRIMARY KEY (`stateid`),
  KEY `countryid_fk_idx` (`countryid`),
  CONSTRAINT `countryid_fk` FOREIGN KEY (`countryid`) REFERENCES `country` (`countryid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF exists city;
CREATE TABLE `city` (
  `cityid` INT NOT NULL AUTO_INCREMENT,
  `cityname` VARCHAR(255) NOT NULL,
  `stateid` INT NOT NULL,
  PRIMARY KEY (`cityid`),
  INDEX `stateid_fk_idx` (`stateid` ASC),
  CONSTRAINT `stateid_fk`
    FOREIGN KEY (`stateid`)
    REFERENCES `sewa`.`state` (`stateid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

DROP TABLE IF exists area;
CREATE TABLE `area` (
  `areaid` INT NOT NULL AUTO_INCREMENT,
  `areaname` VARCHAR(255) NULL,
  `cityid` INT NOT NULL,
  PRIMARY KEY (`areaid`),
  INDEX `cityid_fk_idx` (`cityid` ASC),
  CONSTRAINT `cityid_fk`
    FOREIGN KEY (`cityid`)
    REFERENCES `sewa`.`city` (`cityid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

-- Data
INSERT INTO `country` (`countryname`) VALUES ('India'), ('US'), ('China'), ('Canada');

INSERT INTO `state` ( `statename`,`countryid`) VALUES
('ANDHRA PRADESH',1),
('ASSAM',1),
('ARUNACHAL PRADESH',1),
('BIHAR',1),
('GUJRAT',1),
('HARYANA',1),
('HIMACHAL PRADESH',1),
('JAMMU & KASHMIR',1),
('KARNATAKA',1),
('KERALA',1),
('MADHYA PRADESH',1),
('MAHARASHTRA',1),
('MANIPUR',1),
('MEGHALAYA',1),
('MIZORAM',1),
('NAGALAND',1),
('ORISSA',1),
('PUNJAB',1),
('RAJASTHAN',1),
('SIKKIM',1),
('TAMIL NADU',1),
('TRIPURA',1),
('UTTAR PRADESH',1),
('WEST BENGAL',1),
('DELHI',1),
('GOA',1),
('PONDICHERY',1),
('LAKSHDWEEP',1),
('DAMAN & DIU',1),
('DADRA & NAGAR',1),
('CHANDIGARH',1),
('ANDAMAN & NICOBAR',1),
('UTTARANCHAL',1),
('JHARKHAND',1),
('CHATTISGARH',1);

INSERT INTO `city` ( `cityname`,`stateid`) VALUES
('Mumbai', 12),
('Pune', 12),
('Kolhapur', 12),
('Nagpur', 12),
('Sangli', 12),
('Satara', 12),
('Jalgaon', 12),
('Latur', 12),
('Aurangabad', 12),
('Beed', 12),
('Usmanabad', 12),
('Solapur', 12),
('Karad', 12),
('Ratnagiri', 12),
('Dapoli', 12),
('Alibaug', 12);

INSERT INTO `area` ( `areaname`,`cityid`) VALUES
('Bavdhan', 2),
('Kothrud', 2),
('Swargate', 2),
('Katraj', 2),
('Dhankawadi', 2),
('Indiranagar', 2),
('Mayur Colony', 2),
('Hingane', 2),
('Ambegaon', 2),
('Erandawane', 2),
('Paud Road', 2),
('Karvenagar', 2),
('Waraje', 2),
('Sadashiv Peth', 2),
('Narayan Peth', 2),
('Tilak Road', 2);

