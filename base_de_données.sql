CREATE TABLE `temperature` (
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `temp` float NOT NULL,
  `temp_2` float NOT NULL,
  `temp_3` float NOT NULL,
  `temp_4` float NOT NULL,
  `temp_5` float NOT NULL,
  PRIMARY KEY (`time`)
)
