START TRANSACTION;
CREATE TABLE IF NOT EXISTS "categories" (
	"id"	INTEGER,
	"name"	TEXT UNIQUE,
	"slug"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER,
	"name"	TEXT UNIQUE,
	"email"	TEXT UNIQUE,
	"password"	TEXT,
	"created"	DATETIME NOT NULL DEFAULT (DATETIME('now')),
	"updated"	DATETIME NOT NULL DEFAULT (DATETIME('now')),
	"role"	TEXT,
	"email_token"	TEXT,
	"verified"	INTEGER,
	"token"	TEXT,
	"token_expiration"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "products" (
	"id"	INTEGER,
	"title"	TEXT,
	"description"	TEXT,
	"photo"	TEXT,
	"price"	DECIMAL(10, 2),
	"category_id"	INTEGER,
	"seller_id"	INTEGER,
	"created"	DATETIME NOT NULL DEFAULT (DATETIME('now')),
	"updated"	DATETIME NOT NULL DEFAULT (DATETIME('now')),
	FOREIGN KEY("category_id") REFERENCES "categories"("id"),
	FOREIGN KEY("seller_id") REFERENCES "users"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "blocked_users" (
	"user_id"	INTEGER,
	"message"	TEXT,
	"created"	DATETIME,
	FOREIGN KEY("user_id") REFERENCES "users"("id"),
	PRIMARY KEY("user_id")
);
CREATE TABLE IF NOT EXISTS "banned_products" (
	"product_id"	INTEGER,
	"reason"	TEXT,
	"created"	DATETIME,
	FOREIGN KEY("product_id") REFERENCES "products"("id"),
	PRIMARY KEY("product_id")
);
CREATE TABLE IF NOT EXISTS "orders" (
	"id"	INTEGER,
	"product_id"	INTEGER,
	"buyer_id"	INTEGER,
	"offer"	MONEY,
	"created"	DATETIME,
	FOREIGN KEY("buyer_id") REFERENCES "users"("id"),
	FOREIGN KEY("product_id") REFERENCES "products"("id"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "confirmed_orders" (
	"order_id"	INTEGER,
	"created"	DATETIME,
	PRIMARY KEY("order_id"),
	FOREIGN KEY("order_id") REFERENCES "orders"("id")
);
INSERT INTO "categories" ("id","name","slug") VALUES (1,'Electrònica','electronica');
INSERT INTO "categories" ("id","name","slug") VALUES (2,'Roba','roba');
INSERT INTO "categories" ("id","name","slug") VALUES (3,'Joguines','joguines');
INSERT INTO "categories" ("id","name","slug") VALUES (4,'Alimentació','alimentacio');
INSERT INTO "categories" ("id","name","slug") VALUES (5,'Llibres','llibres');
INSERT INTO "categories" ("id","name","slug") VALUES (6,'Esport','esport');
INSERT INTO "categories" ("id","name","slug") VALUES (7,'Música','musica');
INSERT INTO "categories" ("id","name","slug") VALUES (8,'Mobles','mobles');
INSERT INTO "categories" ("id","name","slug") VALUES (9,'Jardineria','jardineria');
INSERT INTO "categories" ("id","name","slug") VALUES (10,'Animals','animals');
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (1,'Joan Pérez','joan@example.com','pbkdf2:sha256:600000$0V4gC1364OTsi89b$6fac477bb9885c5743738da4ad58c4d5ebd42f81954add7a8cad169e79ec0c0e','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','EQFu4jI8IEf6p1Udpf9HP6suUks',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (2,'Anna García','anna@example.com','pbkdf2:sha256:600000$vTn5CREjV9XsXJIs$b02418b6c27b017f0fbb410b8b4c84c8dedc03424173bc9b89c2852729b61243','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','lIRVVu7VArCUKqXabwCx23hjRJA',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (3,'Elia Rodríguez','elia@example.com','pbkdf2:sha256:600000$DsI8TMjDeUjC7ddk$10769dfdda442226d59f2cae1d3c2662b531f7f2f54f6f4d00b7ef3a9fad6732','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','sZiJjpdSad5xXUCNxhFQMI1XSVc',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (4,'Hedwiga','hdyott3@unesco.org','pbkdf2:sha256:600000$wEEU4LuIrMK4ujJX$6e7b029b59f380abca2d2235d1022a1929b149624a2eb6eb6f463f0980d0f3f5','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','KJHIbIb0Mq7Tk87lec6Od4UhPqY',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (5,'Nanon','nbrimley4@gravatar.com','pbkdf2:sha256:600000$hyqpDnpDpARHkbeK$2b48ed317abfac544b72877debffb8c2d374730d21421d1a5bb620975e12a36b','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','i_BnzkFzsJjc5YOojauxH0uhkCI',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (6,'Jacquenette','jgalia5@mac.com','pbkdf2:sha256:600000$mG1hnNpTSyJYpzzE$81e1ae1884c983b44ae853b539882564cec9beaff90588c2753045606a98a2b6','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','mq6QmksYD-4emoqNoJmEfDaB8wo',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (7,'Randall','rsywell6@vistaprint.com','pbkdf2:sha256:600000$NT5mDsqNSk1hp7QJ$0c06946019c0b181e91a5a45c24ec5425f49a733d362b693bcfa1f7df68ebe16','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','ljJLRXTwKa1l-Xx4rTgAa2yYPSk',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (8,'Salim','sgoosnell7@yellowbook.com','pbkdf2:sha256:600000$k10e47O9tWa5j4MF$2444e73524edaef352148fa4b1b83e73deb2f20b20bac8dc09e310260723b805','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','pNKZnMoYz9rAXk1_ej0Her67tqU',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (9,'Rolph','ralexsandrovich8@prweb.com','pbkdf2:sha256:600000$J9jbyBgy8fgxsjAu$83ca60a2de5623faf1a34f49cd28b65a7ee40d05cf5211a98066496ed857377a','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','VwBPgvyLT8QiDs-WXsiEiIwJvE0',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (10,'Shell','stunnacliffe9@blogspot.com','pbkdf2:sha256:600000$RisEZyeu6Qek3anM$65748a343917a0da5e699387e1b5e635500f15b296dad02b9838a493d79795a2','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','NLDftNnWSvS_nbbLYDUiG-9d3ps',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (11,'Belia','bchidwicka@google.cn','pbkdf2:sha256:600000$4MriQpiu7rHdUmfa$026a5c71af8cf215fe1eee3f51f4742396a17af2b4c09b984c7c3b4825eaa416','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','M0JNr_GHd_FE0EhQIIUDusg-G_E',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (12,'Aldrich','aclowserb@columbia.edu','pbkdf2:sha256:600000$yOrfv9W9odj424Ck$d8822a0538f0cce13afdc42fc207e4e3020d458a7384167499a699455c903bbc','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','k3olb3m4rNdXS-rG6VqHTTamfac',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (13,'Mitchell','msmullenc@artisteer.com','pbkdf2:sha256:600000$jXXITBaWwZLMBwGz$c47efb28ff2bd761eda59e033f207429603ec3fef2f8ee4ac871726a3fd31ecc','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','ULYNTvi7X5THW083yvaDJVJmqeA',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (14,'Minette','mlambourned@fda.gov','pbkdf2:sha256:600000$es8BWO8lWoYoZTZi$b84cb27418e0eceadbcaa0292cb9ea660a51ab9e283b774eb67dd8e6058cefdc','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','XI8aR0CqGq7q-7uC5QfC_VTgGVc',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (15,'Leyla','lsinniee@nationalgeographic.com','pbkdf2:sha256:600000$6FRZBMLgLWwNr6mt$a511dbd517dd3a3a4b8a1a1a1ebbbf63a13c33bc086a516a8e1dadf9e03028e6','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','RR6_QYOhdcJErBscTvGFo6Mv51E',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (16,'Dasya','debenezerf@springer.com','pbkdf2:sha256:600000$BCWhIdZCfmtrWegk$b55359d0e3bcf91690dd07069ac14be57f24eabbcd39e67f1d4e3d752c8b3efd','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','VT4d_HLQ93YGd86fubvz3wYpWDI',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (17,'Mandi','mcoolahang@youtube.com','pbkdf2:sha256:600000$6i2UB0j83DqkCSR9$e1906ca09fd55a23f21ba784acc925a6696db0e8100df5391e55e72e70108765','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','D2gGJ-hxGhWjwnuTdZRElHbSuuA',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (18,'Gaby','gluardh@is.gd','pbkdf2:sha256:600000$AtjVF9JCYWGKaHRA$e10b3d1c049927f99f978e888f1579760a423e936badb579776a0b910f22b201','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','xTh-ZM22fIpRo6tNomclSd1L8So',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (19,'Ethelind','ebilfooti@nymag.com','pbkdf2:sha256:600000$pLOjmyKH3ZOMnsWX$ed2802ad8f36df5a7de34d257b2d1ae3190db56b67c33da1bf3dcc99e5de7068','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','XR15mOtKUqvee-yocMwrd1_dC_E',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (20,'Marcellina','mrobesonj@theguardian.com','pbkdf2:sha256:600000$oJEI63M1mKkSFXRi$4312e582516c5c9f370e4b47d3a9ac756d36a194cbb6d75717ec89faa1391827','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','BsKN86KzsHTIc2od7F-T2Rny--E',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (21,'Sax','slunok@usatoday.com','pbkdf2:sha256:600000$0ijFdGvywiAAwgxX$66b704e07576ece4b4fbe7b9529c35286e86b6f333946fe9f0acb308d650c097','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','0rw9Ch4aE-9TvsbjWYiQdvYxEGQ',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (22,'Denys','dscudl@ifeng.com','pbkdf2:sha256:600000$rek9ZqIsZp2z5Lbs$109afa732d257665af8860421d17ae59d7dfc7a0fe56860b0d0ad7ea327a2073','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','jkao3LtjTn6w1opAJ7rCpViIzfc',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (23,'Cristine','ccowlamm@pcworld.com','pbkdf2:sha256:600000$pOPZTT4qIid0wRAb$97efa9649d4b06ce47e9a85ecea647ce7d545ee0e922855ab027ee98721844fd','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','6JHDTSFk52yMi-dCfsGeBGosdWo',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (24,'Thornton','tanniesn@ebay.co.uk','pbkdf2:sha256:600000$yhqlD9B48SAkK8pi$43b839c4596f37a072a5290b0ccf28932cc465c60bf1b82d84ef2ba51223dc1f','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','UgJ0OAfMbDv3IgmxOLSDTWbz5f8',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (25,'Lisbeth','lsawyero@webnode.com','pbkdf2:sha256:600000$FVgQhWSQ7IEKqMps$c0862bffa751f6b9c754012c7fe74e8efc3656ce7a9a27ce42e108e55b726187','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','bs3EU-KrTjqqjmK19nNT08-20NQ',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (26,'Eugene','egarwellp@google.com.hk','pbkdf2:sha256:600000$an8dfTDFWPeIplgM$23293c06bd9a86bda2458a557b2b41eac3141a9a99cc020c23ca8fed28602db4','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','wnOY0w34FL-c70H_u_jOjD60Czw',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (27,'Redford','rfairecloughq@storify.com','pbkdf2:sha256:600000$92MlcRasTdqwfJ7i$435acf830a76a096f077c67c7277b30626af27bf759251c5a37fb783316f0d7d','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','DFSM7HWjVfzC_4_4HL8D4QxjCRg',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (28,'Lorilyn','ltomasr@java.com','pbkdf2:sha256:600000$GSsbvHBbzTuqn0bo$2a51da8d58e6deb14234af782b486b7dd12dd675d518d37689e083a982a28c9c','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','wR3GOLysDJwgvYT4oSWpe4ZeGg0',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (29,'Nadya','njancs@cbslocal.com','pbkdf2:sha256:600000$4960rQ5DjcC7rQ4s$6b67d0d59e0c6a442551ccfab6a45d489aecd93dd12a7362ed2ef062d9607838','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','K04rd1RIeg_FXEgpcVTZyFYzljE',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (30,'Diego','dscuset@instagram.com','pbkdf2:sha256:600000$oANvYoMUvZ9WDSC3$0f344b8958714af8a18ae49b1020365312435aab062bf71c2fbd67d4dc751356','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','T_4rX25PTVplYP0R8819VANrq_4',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (31,'Celeste','cbrierlyu@etsy.com','pbkdf2:sha256:600000$ADdqaV6dIsybYBEx$b5a423e433d784f130e8da0963a4743d8c3d85a6616997342eccf79295ab3f53','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','p5ZPpRSz-kxMde9DG-GLcpTIoOw',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (32,'Allyce','awibberleyv@java.com','pbkdf2:sha256:600000$eHS5kewUVTsSw7nz$c192597e063a2507758a871e81d2aa1dbf75b8f22d4f88f6a7ff154971542445','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','f_d8vFhiHdYVw0ywpGi7tydqS_U',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (33,'Nathaniel','nkuhnew@sphinn.com','pbkdf2:sha256:600000$2yKc2xr8p554T3hU$28b77223264331ad4765ab63f1af2f16f783235d2609029536c35119dad01bd7','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','QCQYXhi4LyfLIgcgnVgHDAqFp_o',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (34,'Ferne','fgibbardx@ebay.co.uk','pbkdf2:sha256:600000$6SLE1kbo5BG2S9Ki$6c5037c9a364731166317de31bff190c7d2130204a989306964b3d37f10c516c','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','RbGqu_8qUwbNE28m9UsBzLSsjsE',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (35,'Frank','fbotleyy@seesaa.net','pbkdf2:sha256:600000$cEO9k8QHR7HpnnC0$fd7907fc8de55267fc33498be59b1847668c6d5b37dd57e7088d8e92bd6017a2','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','OXBS2cftiHN7yVPAUgxOpn0POvQ',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (36,'Eziechiele','ejoscelynez@toplist.cz','pbkdf2:sha256:600000$RVsdFfisYElDCu18$bb2842dfc50733eee5e3f162c5dd4b4be15df8f1e59db83ad25480066f76ebef','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','mnbEVNzZRuewIvV8Lv9FOhzz7Ac',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (37,'Darcie','delliot10@smugmug.com','pbkdf2:sha256:600000$6Jlg2IbiGTkGqE9M$5df795ea6b81bb69f2e5591dc83dc0b89296ff476239cbc4f99e0419e1d4a128','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','QhwaGBPjntvyC8C4uwn_ZE0Jyxc',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (38,'Nelli','nbrosch11@shareasale.com','pbkdf2:sha256:600000$xZtp0bNnJKn1mFge$1ebe30bd4938f8ebbe6aea86150b05ab0a4b64d987236cc55fd646cfe22aa71e','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','olnHttD_GVNC9NcqT1poZNQ3iL0',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (39,'Jasen','jjephcott12@flickr.com','pbkdf2:sha256:600000$v10ZYnzUX3vm9rIN$bfd94bfa985c25eece44d47d405231c199f2c75ad6b54498d17affeae149d1ca','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','kIUTJpcZ9DpJq4UKdboCFC3923U',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (40,'Elinore','einglesant13@dagondesign.com','pbkdf2:sha256:600000$1B9BZWR23XhIbcxL$d612a0242d7bcb7ded3b495905a186c2264b227c1931047f41ed47cc3ba790ef','2023-10-21 17:34:08','2023-10-21 17:34:08','wanner','zMXTyDjGBy5wE5rl0b4aifmQvZE',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (41,'Marc Tutusaus','pepito@pepeito.com','pbkdf2:sha256:600000$4miJNxrjtZHoYDPJ$6d310881f7800a5f46ba285bddfa275b66b15ce963172de0a73d8e697012dc58','2023-11-15 16:35:42.978771','2023-11-15 16:35:42.978774','wanner','xdEwINqmB9oorAlezIcclcsaEwA',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (42,'Marc','marc@marc.com','pbkdf2:sha256:600000$RiAyKjFtr8a92Bt2$d50754bc0416b263eccaddaa16d13eae73a071cfd519f887e8bf3033c7184c4d','2023-11-15 18:46:43.131696','2023-11-15 18:46:43.131699','viwer','BKtZqnQB6sVoW155wToAhvoxTAE',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (43,'axel','axelvirom@gmail.com','pbkdf2:sha256:260000$JU04HUUc6RilgNZ1$4852429fa52a2a678247285824f31a11a932d27df96e2035e20245256ec00e5e','2023-11-17 14:31:37.160212','2023-11-17 14:31:37.160216',NULL,'tljhCwaftGTx0TdNeNfdPLa0Eos',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (44,'wanner','wanner@wanner.com','pbkdf2:sha256:600000$Qx0pYWeJxVSidDO2$2e9da1047f4332dad67f8dcd829e7c476b15b2917e16133e7cae00bdb0f3e77f','2023-11-17 14:33:31.419724','2023-11-17 14:33:31.419729','wanner','BNi0WTSYiaFuNPpaBjmpiLAehvQ',1,'862c1da298fc86dc37de3bc8ae129004','2024-02-15 16:15:47.357674');
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (45,'moderator','moderator@moderator.com','pbkdf2:sha256:600000$Qx0pYWeJxVSidDO2$2e9da1047f4332dad67f8dcd829e7c476b15b2917e16133e7cae00bdb0f3e77f','2023-11-17 14:43:31.101120','2023-11-17 14:43:31.101123','moderator','byiVQEiTJ2cQ416Rvj8o-6l3Lns',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (46,'admin','admin@admin.com','pbkdf2:sha256:600000$Qx0pYWeJxVSidDO2$2e9da1047f4332dad67f8dcd829e7c476b15b2917e16133e7cae00bdb0f3e77f','2023-11-17 15:18:45.917374','2023-11-17 15:18:45.917377','admin','BjrEQfcM05fVxFXW7o9xejefOJQ',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (47,'adele','eses@fere.com','pbkdf2:sha256:260000$oXJRXaroSfZ1uNnS$f1da7561ab9cc383f0031d98221256540959683ccccb0648a8ed1e6b2744bc37','2023-11-17 17:55:08.959943','2023-11-17 17:55:08.959948','wanner','_23LkAHfR7Hc-DtvEJSnFt7-8TM',1,NULL,NULL);
INSERT INTO "users" ("id","name","email","password","created","updated","role","email_token","verified","token","token_expiration") VALUES (61,'Markitos','marcklk@gmail.com','scrypt:32768:8:1$vifwl25B5ggZcIYy$e4aa440805e939140d8f53c253464b0da6137c2c7b607863dd9c59be6d226035c5401659c53c1ec5a9136b17f148c46215bf872ca19b461675f3fd01d782ed5f','2024-02-05 11:13:01.401777','2024-02-05 11:13:01.401780','wanner','PNxMBwu3KI7wu4_hNDSXp-GIAZY',0,NULL,NULL);
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (4,'Nuevo titulo del producto','Nueva descripcion del producto','image-6.jpg',100,1,16,'2023-10-21 17:34:08','2024-02-06 19:02:14');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (7,'Beets - Mini Golden','Descripción del producto','image-7.jpg',99,10,27,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (8,'Radish - Black, Winter, Organic','Descripción del producto','image-8.jpg',99,9,16,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (9,'Soup - Knorr, Veg / Beef','Descripción del producto','image-9.jpg',99,1,1,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (10,'Broom - Push','Descripción del producto','image-10.jpg',99,5,28,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (11,'Plate - Foam, Bread And Butter','Descripción del producto','image-11.jpg',99,4,22,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (12,'Tea - Herbal - 6 Asst','Descripción del producto','image-12.jpg',999,5,18,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (13,'Veal - Inside Round / Top, Lean','Descripción del producto','image-13.jpg',9,10,36,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (14,'Sobe - Green Tea','Descripción del producto','image-14.jpg',9,1,40,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (15,'Pepper - Paprika, Hungarian','Descripción del producto','image-15.jpg',9,10,26,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (16,'Wine - Ej Gallo Sierra Valley','Descripción del producto','image-16.jpg',9,1,28,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (17,'Anchovy Paste - 56 G Tube','Descripción del producto','image-17.jpg',9,8,25,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (18,'Gelatine Powder','Descripción del producto','image-18.jpg',9,7,28,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (19,'Sobe - Lizard Fuel','Descripción del producto','image-19.jpg',9,3,7,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (20,'Towel Multifold','Descripción del producto','image-20.jpg',9,9,5,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (21,'Butter - Unsalted','Descripción del producto','image-21.jpg',99,1,31,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (22,'Lentils - Green Le Puy','Descripción del producto','image-22.jpg',77,7,32,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (23,'Wine - Chateau Timberlay','Descripción del producto','image-23.jpg',66,2,32,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (24,'Wine - Winzer Krems Gruner','Descripción del producto','image-24.jpg',5,4,27,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (25,'Onion Powder','Descripción del producto','image-25.jpg',4,8,39,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (27,'Duck - Legs','Descripción del producto','image-27.jpg',6,4,39,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (28,'Muffin Batt - Carrot Spice','Descripción del producto','image-28.jpg',7,7,36,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (29,'Eel - Smoked','Descripción del producto','image-29.jpg',8,6,23,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (30,'Flour - Bread','Descripción del producto','image-30.jpg',9,7,13,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (31,'Lid - 0090 Clear','Descripción del producto','image-31.jpg',9,4,12,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (32,'Beer - Moosehead','Descripción del producto','image-32.jpg',99,4,21,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (33,'Mushroom - Oyster, Fresh','Descripción del producto','image-33.jpg',999,1,26,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (34,'Celery','Descripción del producto','image-34.jpg',99,2,26,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (35,'Soup - Campbells, Cream Of','Descripción del producto','image-35.jpg',99,3,29,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (36,'Wine - Magnotta - Cab Franc','Descripción del producto','image-36.jpg',99,10,40,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (37,'Flour - Cake','Descripción del producto','image-37.jpg',999,8,31,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (38,'Lime Cordial - Roses','Descripción del producto','image-38.jpg',9999,7,4,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (39,'Cheese - Gouda Smoked','Descripción del producto','image-39.jpg',9,8,21,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (40,'Cheese - Goat With Herbs','Descripción del producto','image-40.jpg',9,1,1,'2023-10-21 17:34:08','2023-10-21 17:34:08');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (42,'Flores','Flores bonitas','a5394050-bfc1-4e23-9508-05436d1b37fe-captura_desde_2023-11-03_18-39-24.png',4.99,9,NULL,'2023-11-14 15:40:30','2023-11-14 15:40:30');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (43,'Tdadasd','asdasas','81fe0460-4530-4b84-9321-3f840c7eb88b-captura_desde_2023-10-30_19-03-23.png',4.44,1,NULL,'2023-11-14 18:30:54','2023-11-14 18:30:54');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (44,'asdasd','asdasda','7e5bbfe8-61b9-42b3-b0b2-d23c59de07c2-captura_desde_2023-10-30_19-03-50.png',55.55,1,NULL,'2023-11-14 19:33:42','2023-11-14 19:33:42');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (45,'test','test','c878b088-15e0-4723-9407-6171cfb18339-captura_desde_2023-11-03_18-44-30.png',33.33,1,NULL,'2023-11-14 19:37:20','2023-11-14 19:37:20');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (46,'sadsdas','asdasd','04eca07d-8e82-473a-b1f6-531607fad3dd-captura_desde_2023-11-03_18-39-24.png',222,1,1,'2023-11-14 19:54:36','2023-11-14 19:54:36');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (47,'ultim','dasdasd','5d8b55bb-ff1c-4771-8bc1-93f4dac1517a-captura_desde_2023-11-03_18-44-30.png',333,1,2,'2023-11-14 19:56:00','2023-11-14 19:56:00');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (48,'dasda','sadsad','d095c13b-1e5b-4404-9920-20d6f0d731df-captura_desde_2023-11-03_18-47-05.png',4.44,10,41,'2023-11-15 16:37:10','2023-11-15 16:37:10');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (50,'saddsasdd','sdaasdasd','6207cb82-6670-4385-bbe8-63bfa8cddc29-1200px-procyon_lotor_common_raccoon.jpg',5644,1,46,'2023-12-17 20:45:54','2023-12-17 20:45:54');
INSERT INTO "products" ("id","title","description","photo","price","category_id","seller_id","created","updated") VALUES (51,'Nuevo titulo pattwwwwwwrrrrrrrrrrrrrrrwwwwa','Nueva descripcion del producto',NULL,22,1,44,'2024-02-05 18:55:19','2024-02-15 15:16:10');
INSERT INTO "banned_products" ("product_id","reason","created") VALUES (6,'ddsfsdf','2023-12-17 20:00:44.662192');
INSERT INTO "banned_products" ("product_id","reason","created") VALUES (7,'sdfsdf','2023-12-17 20:00:46.625824');
INSERT INTO "banned_products" ("product_id","reason","created") VALUES (8,'sdfdsf','2023-12-17 20:00:49.727901');
INSERT INTO "banned_products" ("product_id","reason","created") VALUES (50,'por mamon','2023-12-17 20:52:25.271286');
INSERT INTO "orders" ("id","product_id","buyer_id","offer","created") VALUES (5,1,2,99.99,'2024-02-05 10:37:35.953340');
INSERT INTO "orders" ("id","product_id","buyer_id","offer","created") VALUES (6,4,6,101,'2024-02-07 15:26:03.903007');
INSERT INTO "orders" ("id","product_id","buyer_id","offer","created") VALUES (7,4,6,101,'2024-02-07 15:26:34.757495');
INSERT INTO "orders" ("id","product_id","buyer_id","offer","created") VALUES (8,4,NULL,101,'2024-02-14 18:26:09.566349');
INSERT INTO "orders" ("id","product_id","buyer_id","offer","created") VALUES (9,51,44,101,'2024-02-14 18:41:39.654503');
COMMIT;
