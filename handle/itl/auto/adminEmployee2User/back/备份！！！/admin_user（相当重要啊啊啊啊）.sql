-- phpMyAdmin SQL Dump
-- version 4.4.15.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2017-05-04 09:52:13
-- 服务器版本： 5.6.31-log
-- PHP Version: 5.4.37

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `itianluo`
--

-- --------------------------------------------------------

--
-- 表的结构 `admin_user`
--

CREATE TABLE IF NOT EXISTS `admin_user` (
  `id` int(11) NOT NULL,
  `account` char(12) NOT NULL,
  `mobile` char(12) NOT NULL DEFAULT '0',
  `nickname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `last_login_time` int(11) unsigned DEFAULT '0',
  `last_login_ip` varchar(40) DEFAULT NULL,
  `login_count` mediumint(8) unsigned DEFAULT '0',
  `create_time` int(11) unsigned NOT NULL,
  `update_time` int(11) unsigned NOT NULL,
  `status` tinyint(1) DEFAULT '1',
  `role_id` tinyint(3) NOT NULL DEFAULT '0' COMMENT '角色id',
  `zone_id` int(10) NOT NULL DEFAULT '0' COMMENT '小区id',
  `zone_ids` varchar(1000) NOT NULL COMMENT '小区范围'
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `admin_user`
--

INSERT INTO `admin_user` (`id`, `account`, `mobile`, `nickname`, `password`, `last_login_time`, `last_login_ip`, `login_count`, `create_time`, `update_time`, `status`, `role_id`, `zone_id`, `zone_ids`) VALUES
(1, 'itianluo', '15168209723', '管理员', 'f3bff7e836604e4113d7a74aa8cc5e56', 1493862307, '218.109.26.21', 4403, 1222907803, 1239977420, 1, 1, 0, '20,19,18,17,16,15,14,13,12,11,10,9,5,2,1'),
(2, 'beier', '15555555555', '贝儿', '9542f7bcd85b1bd50da90bdd2c21d00f', 1492585881, '115.236.1.30', 99, 0, 0, 1, 1, 2, '20,19,18,17,16,15,14,13,12,11,10,9,5,2,1'),
(4, 'jide', '13758251024', '基德', '862f0e116dfb4d921a10be92a1a557fc', 1489743930, '218.109.26.21', 14, 0, 0, 1, 1, 1, '18,17,16,15,14,13,10,9,2'),
(8, 'guoguiying', '18257193360', '郭桂英', '3aa20c424608f527548898d06c1140eb', 1492492287, '39.174.62.213', 23, 0, 0, 1, 3, 2, '2'),
(10, 'kongchenchen', '18314868950', '孔晨晨', '709dcaa888e8bbcd0013ab4d40001c25', 1493811879, '39.181.46.11', 238, 0, 0, 1, 3, 2, ''),
(12, 'lufei', '18789980806', '路飞', '23e8e998df7b9658ff651c2b26d881f5', 1484729587, '218.109.26.21', 15, 0, 0, 1, 6, 1, '22,21,20,19,18,17,16,15,14,13,12,11,10,9,5,2,1'),
(14, 'jiangshenghu', '18857123671', '江升华', 'cd0d964d492f972fdb29687743543bbc', 1492739878, '218.109.26.21', 34, 0, 0, 1, 2, 2, '20,19,18,17,16,15,14,13,10,9,5,2'),
(16, 'luoyongyuan', '18368123326', '罗永源', '824f13cd09f2f1fc280f967ea905f883', 1491447222, '218.109.26.21', 24, 0, 0, 1, 7, 2, '18,17,16,15,14,13,12,5,2'),
(18, 'liuyanqing', '13616555604', '刘艳青', '93115a173ac5731bf38a392d73338bd2', 1483947513, '218.109.26.21', 3, 0, 0, 1, 2, 1, '1'),
(22, 'honglu', '18551087726', '洪璐', '18c396df3c3f3cb9e4fb1ac043c53f84', 1489714827, '218.109.26.21', 24, 0, 0, 1, 1, 20, '20,19,18,17,16,15,14,13,10,9,2'),
(24, 'bijingyuan', '18888775271', '碧景园', '32f68a60cef40faedbc6af20298c1a1e', 1479291233, '218.109.243.10', 1, 0, 0, 1, 2, 9, '9'),
(26, 'huanglongyay', '15957633213', '黄龙雅苑', '32f68a60cef40faedbc6af20298c1a1e', 0, NULL, 0, 0, 0, 1, 2, 10, '10'),
(30, 'fengjin', '13588443036', '冯瑾', '52a9e7a028365f63e6498e4159f6ce58', 1489038134, '218.109.26.21', 24, 0, 0, 1, 2, 2, '20,1'),
(32, 'jialipeng', '18611928086', '贾利鹏', 'cce0f80174e420ef3ff2b135df88543f', 1481856660, '218.109.26.21', 4, 0, 0, 1, 2, 2, '18,17,16,15,14,13,10,9,2'),
(38, 'chenjian', '13336103666', '陈坚', '0e70463d56d6bc65144552afbd9be6a0', 0, NULL, 0, 0, 0, 1, 9, 10, '10'),
(41, 'liqinlin', '13967161469', '李勤林', 'cd1e04052083766bf7da7d6264ed789f', 0, NULL, 0, 0, 0, 1, 9, 9, '9'),
(43, 'dingkai', '15505888250', '丁凯', 'cc784a1e8912a72ddffeee37837bcf10', 0, NULL, 0, 0, 0, 1, 9, 13, '17,16,15,14,13'),
(45, 'zhoujianhui', '18888775271', '周建辉', '642815095d38a5c3b0244a4a2babb101', 0, NULL, 0, 0, 0, 1, 9, 9, '9'),
(47, 'jinsiqi', '15957633213', '金思琪', '4b4606688012ae4c7dda909623d507b5', 0, NULL, 0, 0, 0, 1, 9, 10, '10'),
(49, 'xuweiming', '13758116649', '徐威明', 'c73afdcb054ec4e4459931ac354d1ecd', 1489806760, '218.109.26.21', 4, 0, 0, 1, 9, 13, '17,16,15,14,13'),
(51, 'zhangjinping', '13372562169', '章金平', 'e6ea869007bfd866b25312e11e7f1dda', 0, NULL, 0, 0, 0, 1, 9, 16, '16,14'),
(54, 'longyaofang', '18868700368', '龙耀芳', '1101836270b21f58905ca26eb1513f7f', 0, NULL, 0, 0, 0, 1, 9, 18, '18'),
(56, 'hanweiping', '13588194587', '韩卫平', '644e2f8748ab1a6b5a1191298006e613', 1489659298, '218.109.26.21', 21, 0, 0, 1, 9, 18, '18'),
(57, 'zhaidian', '13858120552', '翟电', '8d1699c721b65e2ea84a341e0d060df3', 1489814336, '218.109.26.21', 2, 0, 0, 1, 9, 2, '2'),
(62, 'yaqi', '13094804590', '管理层亚奇', '8f0a3bd6496da630de23ea538d2e9e9c', 0, NULL, 0, 0, 0, 1, 9, 20, '20,2,1'),
(64, 'wangxiejing', '15957203020', '汪谢景', 'd5de60c1606165fde9fbb609500d5652', 0, NULL, 0, 0, 0, 1, 9, 18, '18'),
(66, 'xuxun', '13646850399', '续珣', 'a8e909c197ddb6542c2eae6737c94c4c', 0, NULL, 0, 0, 0, 1, 9, 19, '19'),
(69, 'huangshan', '13588881597', '黄山', 'bc5ecde0bd92fa39f07eec324c510f7c', 1491545600, '218.109.26.21', 1, 0, 0, 1, 1, 12, '22,21,20,19,18,17,16,15,14,13,12,10,9,2'),
(72, 'fangyuyu', '15925677587', '方瑜瑜', '48481503a5654c932d428e57e7cdf3e3', 0, NULL, 0, 0, 0, 1, 9, 21, '22,21'),
(74, 'zhaixuenan', '18072753210', '翟学南', '6a852e0236fa3b643e766cdd35c0a5fd', 0, NULL, 0, 0, 0, 1, 9, 21, '21'),
(76, 'houchaoyang', '18858184699', '侯朝洋', '0a1936688985fda9a56df3047048ac60', 0, NULL, 0, 0, 0, 1, 9, 22, '22'),
(78, 'yuhuiping', '13516811716', '於慧萍', '7461fae9793e4c3f1ff0c89c94e61f4f', 0, NULL, 0, 0, 0, 1, 9, 22, '22,21'),
(81, 'yangjunmin', '15088532883', '杨俊敏', 'd93443a7392bbe582653525143def8de', 0, NULL, 0, 0, 0, 1, 9, 22, '22,21'),
(83, 'qiantangping', '13989803986', '钱塘品管', '06587296bd9bce60a4aaf67d1dc9ebe6', 0, NULL, 0, 0, 0, 1, 9, 17, '17,16,15,14,13'),
(85, 'daizhifeng', '13819163873', '代志锋', 'a8660647416ecac607cb197c5c07c94c', 0, NULL, 0, 0, 0, 1, 9, 22, '22,21'),
(87, 'chenyuyang', '13968070555', '陈宇阳', '829b51559b7a5e61e1b0f6fd01bfc014', 0, NULL, 0, 0, 0, 1, 9, 22, ''),
(89, 'zhangyaowen', '13812289135', '张耀文', 'acea8bed5615aea26af621eb62d9a1dd', 0, NULL, 0, 0, 0, 1, 9, 22, ''),
(91, 'wangjiming', '13967120605', '王继明', 'acd31e03fef6ceb7fe6177bc3484cf36', 0, NULL, 0, 0, 0, 1, 9, 22, ''),
(93, 'yejian', '15958028212', '叶剑', '7c630b81b5558626198370836ba33e1c', 0, NULL, 0, 0, 0, 1, 9, 22, '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_user`
--
ALTER TABLE `admin_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account` (`account`(6)) USING BTREE,
  ADD KEY `mobile` (`mobile`(6)) USING BTREE;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_user`
--
ALTER TABLE `admin_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=94;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
