import requests,time
from bs4 import BeautifulSoup
# 抓取 etherscan 上智能合约地址的交易
url = "https://etherscan.io/txs?a=%s&p=1"
headers = {
    "Content-type": "application/x-www-form-urlencoded",
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
}
ddict = {
    "ven": "0xd850942ef8811f2a866692a623011bde52a462c1",
    "omg": "0xd26114cd6ee289accf82350c8d8487fedb8a0c07",
    "icx": "0xb5a5f22694352c15b00323844ad545abb2b11028",
    "bnb": "0xb8c77482e45f1f44de1745f52c74426c631bdd52",
    "ae": "0x5ca9a71b1d01849c0a95490cc00559717fcf0d1d",
    "zil": "0x05f4a42e251f2d52b8ed15e9fedaacfcef1fad27",
    "btm": "0xcb97e65f07da24d46bcdd078ebebd7c6e6e3d750",
    "zrx": "0xe41d2489571d322189246dafa5ebde1f4699f498",
    "ppt": "0xd4fa1460f537bb9085d22c7bccb5dd450ef28e3a",
    "mkr": "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2",
    "rhoc": "0x168296bb09e24a88805cb9c33356536b980d3fc5",
    "gnt": "0xa74476443119a942de498590fe1f2454d7d4ac0d",
    "snt": "0x744d70fdbe2ba4cf95131626614a1763df805b9e",
    "iost": "0xfa1a856cfa3409cfa145fa4e20eb270df3eb21ab",
    "wtc": "0xb7cb1c96db6b22b0d3d9536e0108d062bd488f74",
    "dgd": "0xe0b7927c4af23765cb51314a0e0521a9645f0e2a",
    "lrc": "0xbbbbca6a901c926f240b89eacb641d8aec7aeafd",
    "aion": "0x4ceda7906a5ed2179785cd3a40a69ee8bc99c466",
    "bat": "0x0d8775f648430679a709e98d2b0cb6250d2887ef",
    "rep": "0xe94327d07fc17907b4db788e5adf2ed424addff6",
    "elf": "0xbf2179859fc6d5bee9bf9158632dc51678a4100e",
    "nas": "0x5d65d971895edc438f465c17db6992698a52318d",
    "loom": "0xa4e8c3ec456107ea67d3075bf9e3df3a75823db0",
    "knc": "0xdd974d5c2e2928dea5f71b9825b8b646686bd200",
    "ctxc": "0xea11755ae41d889ceec39a63e6ff75a02bc1c00d",
    "sub": "0x12480e24eb5bec1a9d4369cab6a80cad3c0a377a",
    "qash": "0x618e75ac90b12c6049ba3b27f5d5f8651b0037f6",
    "cennz": "0x1122b6a0e00dce0563082b6e2953f3a943855c1f",
    "drgn": "0x419c4db4b9e25d6db2ad9691ccb832c8d9fda05e",
    "ethos": "0x5af2be193a6abca9c8817001f45744777db30756",
    "bnt": "0x1f573d6fb3f13d689ff844b4ce37794d79a7ff1c",
    "veri": "0x8f3470a7388c05ee4e7af3d01d8c722b0ff52374",
    "storm": "0xd0a4b8946cb52f0661273bfbc6fd0e0c75fc6433",
    "dentacoin": "0x08d32b0da63e2c3bcf8019c9c5d849d7a9d791e6",
    "fun": "0x419d0d8bdd9af5e606ae2232ed285aff190e711b",
    "wax": "0x39bb259f66e1c59d5abef88375979b4d20d98022",
    "salt": "0x4156d3342d5c385a87d264f90653733592000581",
    "fsn": "0xd0352a019e9ab9d757776f532377aaebd36fd541",
    "gto": "0xc5bbae50781be1669306b9e001eff57a2957b09d",
    "eng": "0xf0ee6b27b759c9893ce4f094b49ad28fd15a23e4",
    "powr": "0x595832f8fc6bf59c85c527fec3740a1b7a361269",
    "man": "0xe25bcec5d3801ce3a794079bf94adf1b8ccd802d",
    "kin": "0x818fc6c2ec5986bc6e2cbf00939d90556ab12ce5",
    "link": "0x514910771af9ca656af840dff83e8264ecf986ca",
    "ncash": "0x809826cceab68c387726af962713b64cb5cb3cca",
    "r": "0x48f775efbe4f5ece6e0df2f7b5932df56823b990",
    "mana": "0x0f5d2fb29fb7d3cfee444a200298f468908cc942",
    "cmt": "0xf85feea2fdd81d51177f6b8f35f0e6734ce45f5f",
    "mco": "0xb63b606ac810a52cca15e44bb630fd42d8d1d83d",
    "req": "0x8f8221afbb33998d8584a2b05749ba73c37a938a",
    "pay": "0xb97048628db6b661d4c2aa833e95dbe1a905b280",
    "poly": "0x9992ec3cf6a55b00978cddf2b27bc6882d88d1ec",
    "cnd": "0xd4c435f5b09f855c3317c8524cb1f586e42795fa",
    "storj": "0xb64ef51c888972c908cfacf59b47c1afbc0ab8ac",
    "cvc": "0x41e5560054824ea6b0732e656e3ad64e20e94e45",
    "gnx": "0x6ec8a24cabdc339a06a172f8223ea557055adaa5",
    "icn": "0x888666ca69e0f178ded6d75b5726cee99a87d698",
    "nuls": "0xb91318f35bdb262e9423bc7c7c2a3a93dd93c92c",
    "abt": "0xb98d4c97425d9908e66e53a6fdf673acca0be986",
    "ruff": "0xf278c1ca969095ffddded020290cf8b5c424ace2",
    "rlc": "0x607f4c5bb672230e8672085532f7e901544a7375",
    "ht": "0x6f259637dcd74c767781e37bc6133cd6a68aa161",
    "poe": "0x0e0989b1f9b8a38983c2ba8053269ca62ec9b195",
    "gno": "0x6810e776880c02933d47db1b9fc05908e5386b96",
    "srn": "0x68d57c9a1c35f63e2c83ee8e49a64e9d70528d25",
    "amb": "0x4dc3643dbc642b72c158e7f3d2ff232df61cb6ce",
    "agi": "0x8eb24319393716668d768dcec29356ae9cffe285",
    "enj": "0xf629cbd94d3791c9250152bd8dfbdf380e2a3b9c",
    "qsp": "0x99ea4db9ee77acd40b119bd1dc4e33e1c070b80d",
    "mtl": "0xf433089366899d83a9f26a773d59ec7ecf30355e",
    "ant": "0x960b236a07cf122663c4303350609a66a7b288c0",
    "dent": "0x3597bfd533a99c9aa083587b074434e61eb0a258",
    "san": "0x7c5a0ce9267ed19b22f8cae653f198e3e8daf098",
    "rdn": "0x255aa6df07540cb5d3d297f0d0d4d84cb52bc8e6",
    "tomo": "0x8b353021189375591723e7384262f45709a3c3dc",
    "hpb": "0x38c6a68304cdefb9bec48bbfaaba5c5b47818bb2",
    "blz": "0x5732046a883704404f284ce41ffadd5b007fd668",
    "gtc": "0xb70835d7822ebb9426b56543e391846c107bd32c",
    "ppp": "0xc42209accc14029c1012fb5680d95fbd6036e2a0",
    "theta": "0x3883f5e181fccaf8410fa61e12b59bad963fb645",
    "soc": "0x2d0e95bd4795d7ace0da3c0ff7b706a5970eb9d3",
    "plr": "0xe3818504c1b32bf1557b16c238b2e01fd3149c17",
    "lend": "0x80fb784b7ed66730e8b1dbd9820afd29931aab03",
    "snm": "0x983f6d60db79ea8ca4eb9968c6aff8cfa04b3c63",
    "iht": "0xeda8b016efa8b1161208cf041cd86972eee0f31e",
    "sphtx": "0x3833dda0aeb6947b98ce454d89366cba8cc55528",
    "cs": "0x46b9ad944d1059450da1163511069c718f699d31",
    "itc": "0x5e6b6d9abad9093fdc861ea1600eba1b355cd940",
    "gvt": "0x103c3a209da59d3e7c4a89307e66521e081cfdf0",
    "st": "0xaf30d2a7e90d7dc361c8c4585e9bb7d2f6f15bc7",
    "bix": "0xb3104b4b9da82025e8b9f8fb28b3553ce2f67069",
    "auto": "0x622dffcc4e83c64ba959530a5a5580687a57581b",
    "rcn": "0xf970b8e36e23f7fc3fd752eea86f8be8d83375a6",
    "vee": "0x340d2bde5eb28c1eed91b2f790723e3b160613b7",
    "adx": "0x4470bb87d77b963a013db939be332f927f2b992e",
    "ast": "0x27054b13b1b798b345b591a4d22e6562d47ea75a",
    "brd": "0x558ec3152e2eb2174905cd19aea4e34a23de9ad6",
    "appc": "0x1a7a8bd9106f2b8d977e08582dc7d24c723ab0db",
    "sngls": "0xaec2e87e0a235266d9c5adc9deb4b2e29b54d009",
    "edo": "0xced4e93198734ddaff8492d525bd258d49eb388e",
    "nanj": "0xffe02ee4c69edf1b340fcad64fbd6b37a7b9e265",
    "qrl": "0x697beac28b09e122c4332d163985e8a73121b97f",
    "hot": "0x9af839687f6c94542ac5ece2e317daae355493a1",
    "data": "0x0cf0ee63788a0849fe5297f3407f701e122cc023",
    "dnt": "0x0abdace70d3790235af448c88547603b945604ea",
    "spank": "0x42d6622dece394b54999fbd73d108123806f6a18",
    "wpr": "0x4cf488387f035ff08c371515562cba712f9015d4",
    "vibe": "0xe8ff5c9c75deb346acac493c463c8950be03dfba",
    "tel": "0x85e076361cc813a908ff672f9bad1541474402b2",
    "ocn": "0x4092678e4e78230f46a1534c0fbc8fa39780892b",
    "ins": "0x5b2e4a700dfbc560061e957edec8f6eeeb74a320",
    "wabi": "0x286bda1413a2df81731d4930ce2f862a35a609fe",
    "int": "0x0b76544f6c413a555f309bf76260d1e02377c02a",
    "utk": "0x70a72833d6bf7f508c8224ce59ea1ef3d0ea3a38",
    "crpt": "0x80a7e048f37a50500351c204cb407766fa3bae7f",
    "trac": "0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f",
    "elec": "0xd49ff13661451313ca1553fd6954bd1d9b6e02b9",
    "mod": "0x957c30ab0426e0c93cd8241e2c60392d08c6ac8e",
    "edg": "0x08711d3b02c8758f2fb3ab4e80228418a7f8e39c",
    "wings": "0x667088b212ce3d06a1b553a7221e1fd19000d9af",
    "lym": "0x57ad67acf9bf015e4820fbd66ea1a21bed8852ec",
    "tnt": "0x08f5a9235b08173b7569f83645d2c7fb55e8ccd8",
    "jnt": "0xa5fd1a791c4dfcaacc963d4f73c6ae5824149ea7",
    "taas": "0xe7775a6e9bcf904eb39da2b68c5efb4f9360e08c",
    "yoyow": "0xcbeaec699431857fdb4d37addbbdc20e132d4903",
    "prl": "0x1844b21593262668b7248d0f57a220caaba46ab9",
    "rntb": "0x1fe70be734e473e5721ea57c8b5b01e6caa52686",
    "rkt": "0x106aa49295b525fcf959aa75ec3f7dcbf5352f1c",
    "qun": "0x264dc2dedcdcbb897561a57cba5085ca416fb7b4",
    "evn": "0xd780ae2bf04cd96e577d3d014762f831d97129d0",
    "ren": "0x408e41876cccdc0f92210600ef50372656052a38",
    "cdt": "0x177d39ac676ed1c67a2b268ad7f1e58826e5b0af",
    "fuel": "0xea38eaa3c86c8f9b751533ba2e562deb9acded40",
    "ngc": "0x72dd4b6bd852a3aa172be4d6c5a6dbec588cf131",
    "sent": "0xa44e5137293e855b1b7bc7e2c6f8cd796ffcb037",
    "mgo": "0x40395044ac3c0c57051906da938b54bd6557f212",
    "mln": "0xbeb9ef514a379b997e0798fdcc901ee474b6d9a1",
    "cpc": "0xfae4ee59cdd86e3be9e8b90b53aa866327d7c090",
    "dock": "0xe5dada80aa6477e85d09747f2842f7993d0df71c",
    "tkn": "0xaaaf91d9b90df800df4f55c205fd6989c977e73a",
    "kick": "0x27695e09149adc738a978e9a678f99e4c39e9eb9",
    "bcpt": "0x1c4481750daa5ff521a2a7490d9981ed46465dbd",
    "ekt": "0xbab165df9455aa0f2aed1f2565520b91ddadb4c8",
    "rfr": "0xd0929d411954c47438dc1d871dd6081f5c5e149c",
    "datx": "0xabbbb6447b68ffd6141da77c18c7b5876ed6c5ab",
    "soar": "0xd65960facb8e4a2dfcb2c2212cb2e44a02e2a57e",
    "bax": "0x9a0242b7a33dacbe40edb927834f96eb39f8fbcb",
    "banca": "0x998b3b82bc9dba173990be7afb772788b5acb8bd",
    "cvt": "0xbe428c3867f05dea2a89fc76a102b544eac7f772",
    "pre": "0x88a3e4f35d64aad41a6d4030ac9afe4356cb84fa",
    "dat": "0x81c9151de0c8bafcd325a57e3db5a5df1cebf79c",
    "utnp": "0x9e3319636e2126e3c0bc9e3134aec5e1508a46c7",
    "ukg": "0x24692791bc444c5cd0b81e3cbcaba4b04acd1f3b",
    "senc": "0xa13f0743951b4f6e3e3aa039f682e17279f52bc3",
    "hav": "0xf244176246168f24e3187f7288edbca29267739b",
    "tau": "0xc27a2f05fa577a83ba0fdb4c38443c0718356501",
    "vib": "0x2c974b2d0ba1716e644c1fc59982a89ddd2ff724",
    "blt": "0x107c4504cd79c5d2696ea0030a8dd4e92601b82e",
    "ten": "0xdd16ec0f66e54d453e6756713e533355989040e4",
    "adt": "0xd0d6d6c5fe4a677d343cc433536bb717bae167dd",
    "lun": "0xfa05a73ffe78ef8f1a739473e462c54bae6567d9",
    "xdce": "0x41ab1b6fcbb2fa9dced81acbdec13ea6315f2bf2",
    "sxdt": "0x12b306fa98f4cbb8d4457fdff3a0a0a56f07ccdf",
    "lgo": "0x123ab195dd38b1b40510d467a6a359b201af056f",
    "mtn": "0x41dbecc1cdc5517c6f76f6a6e836adbee2754de3",
    "tio": "0x80bc5512561c7f85a3a9508c7df7901b370fa1df",
    "guppy": "0xf7b098298f7c69fc14610bf71d5e02c60792894c",
    "coss": "0x9e96604445ec19ffed9a5e8dd7b50a29c899a10c",
    "cob": "0xb2f7eb1f2c37645be61d73953035360e768d81e6",
    "hmq": "0xcbcc0f036ed4788f63fc0fee32873d6a7487b908",
    "cfi": "0x12fef5e57bf45873cd9b62e9dbd7bfb99e32d73e",
    "bkx": "0x45245bc59219eeaaf6cd3f382e078a461ff9de7b",
    "up": "0x6ba460ab75cd2c56343b3517ffeba60748654d26",
    "dai": "0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359",
    "msp": "0x68aa3f232da9bdc2343465545794ef3eea5209bd",
    "mth": "0xaf4dce16da2877f8c9e00544c93b62ac40631f16",
    "zsc": "0x7a41e0517a5eca4fdbc7fbeba4d4c47b9ff6dc63",
    "ucash": "0x92e52a1a235d9a103d970901066ce910aacefd37",
    "evx": "0xf3db5fa2c66b7af3eb0c0b782510816cbe4813b8",
    "capp": "0x04f2e7221fdb1b52a68169b25793e51478ff0329",
    "hst": "0x554c20b7c486beee439277b4540a434566dc4c02",
    "dmt": "0x2ccbff3a042c68716ed2a2cb0c544a9f1d1935e1",
    "trst": "0xcb94be6f13a1182e4a4b6140cb7bf2025d28e41b",
    "dlt": "0x07e3c70653548b04f0a75970c1f81b4cbbfb606f",
    "snc": "0xf4134146af2d511dd5ea8cdb1c4ac88c57d60404",
    "ship": "0xe25b0bba01dc5630312b6a21927e578061a13f55",
    "odem": "0xbf52f2ab39e26e0951d2a02b49b7702abe30406a",
    "tix": "0xea1f346faf023f974eb5adaf088bbcdf02d761f4",
    "bcap": "0xff3519eeeea3e76f1f699ccce5e23ee0bdda41ac",
    "stk": "0xae73b38d1c9a8b274127ec30160a4927c4d71824",
    "aura": "0xcdcfc0f66c522fd086a1b725ea3c0eeb9f9e8814",
    "fota": "0x4270bb238f6dd8b1c3ca01f96ca65b2647c06d3c",
    "arn": "0xba5f11b16b155792cf3b2e6880e8706859a8aeb6",
    "mdt": "0x814e0908b12a99fecf5bc101bb5d0b8b5cdf7d26",
    "key": "0x4cc19356f2d37338b9802aa8e8fc58b0373296e7",
    "mda": "0x51db5ad35c671a87207d88fc11d593ac0c8415bd",
    "bpt": "0x327682779bab2bf4d1337e8974ab9de8275a7ca8",
    "dadi": "0xfb2f26f266fb2805a387230f2aa0a331b4d96fba",
    "nmr": "0x1776e1f26f98b1a5df9cd347953a26dd3cb46671",
    "berry": "0x6aeb95f06cda84ca345c2de0f3b7f96923a44f4c",
    "mwat": "0x6425c6be902d692ae2db752b3c268afadb099d3b",
    "mot": "0x263c618480dbe35c300d8d5ecda19bbb986acaed",
    "uuu": "0x3543638ed4a9006e4840b105944271bcea15605d",
    "dxt": "0x8db54ca569d3019a2ba126d03c37c44b5ef81ef6",
    "idh": "0x5136c98a80811c3f46bdda8b5c4555cfd9f812f0",
    "hvn": "0xc0eb85285d83217cd7c891702bcbc0fc401e2d9d",
    "oax": "0x701c244b988a513c945973defa05de933b23fe1d",
    "grid": "0x12b19d3e2ccc14da04fae33e63652ce469b3f2fd",
    "stq": "0x5c3a228510d246b78a3765c20221cbf3082b44a4",
    "hmc": "0xaa0bb10cec1fa372eb3abc17c933fc6ba863dd9e",
    "tfd": "0xe5f166c0d8872b68790061317bb6cca04582c912",
    "cat": "0x56ba2ee7890461f463f7be02aac3099f6d5811a8",
    "rnt": "0xff603f43946a3a28df5e6a73172555d8c8b02386",
    "mtx": "0x0af44e2784637218dd1d32a322d44e603a8f0c6a",
    "stx": "0x006bea43baa3f7a6f765f14f10a1a1b08334ef45",
    "atm": "0x9b11efcaaa1890f6ee52c6bb7cf8153ac5d74139",
    "cv": "0xda6cb58a0d0c01610a29c5a65c303e13e885887c",
    "la": "0xe50365f5d679cb98a1dd62d6f6e58e59321bcddf",
    "pareto": "0xea5f88e54d982cbb0c441cde4e79bc305e5b43bc",
    "cov": "0xe2fb6529ef566a080e6d23de0bd351311087d567",
    "pst": "0x5d4abc77b8405ad177d8ac6682d584ecbfd46cec",
    "nct": "0x9e46a38f5daabe8683e10793b06749eef7d733d1",
    "bmc": "0xdf6ef343350780bf8c3410bf062e0c015b1dd671",
    "eve": "0x923108a439c4e8c2315c4f6521e5ce95b44e9b4c",
    "zap": "0x6781a0f84c7e9e846dcb84a9a5bd49333067b104",
    "bbn": "0x35a69642857083ba2f30bfab735dacc7f0bac969",
    "bee": "0x4d8fc1453a0f359e99c9675954e656d80d996fbf",
    "uqc": "0xd01db73e047855efb414e6202098c4be4cd2423b",
    "ixt": "0xfca47962d45adfdfd1ab2d972315db4ce7ccf094",
    "dbet": "0x9b68bfae21df5a510931a262cecf63f41338f264",
    "neu": "0xa823e6722006afe99e91c30ff5295052fe6b8e32",
    "hkn": "0x9e6b2b11542f2bc52f3029077ace37e8fd838d7f",
    "swm": "0x9e88613418cf03dca54d6a2cf6ad934a78c7a17a",
    "axp": "0x9af2c6b1a28d3d6bc084bd267f70e90d49741d5b",
    "pfr": "0x2fa32a39fc1c399e0cc7b2935868f5165de7ce97",
    "plbt": "0x0affa06e7fbe5bc9a764c979aa66e8256a631f02",
    "rol": "0x2e071d2966aa7d8decb1005885ba1977d6038a65",
    "xpa": "0x90528aeb3a2b736b780fd1b6c478bb7e1d643170",
    "rebl": "0x5f53f7a8075614b699baad0bc2c899f4bad8fbbf",
    "hdg": "0xffe8196bc259e8dedc544d935786aa4709ec3e64",
    "prg": "0x7728dfef5abd468669eb7f9b48a7f70a501ed29d",
    "deb": "0x151202c9c18e495656f372281f493eb7698961d5",
    "chp": "0xf3db7560e820834658b590c96234c333cd3d5e5e",
    "chsb": "0xba9d4199fab4f26efe3551d490e3821486f135ba",
    "dna": "0x82b0e50478eeafde392d45d1259ed1071b6fda81",
    "xrl": "0xb24754be79281553dc1adc160ddf5cd9b74361a4",
    "auc": "0xc12d099be31567add4e4e4d0d45691c3f58f5663",
    "swt": "0xb9e7f8568e08d5659f5d29c4997173d84cdf2607",
    "ptoy": "0x8ae4bf2c33a8e667de34b54938b0ccd03eb8cc06",
    "bdg": "0x1961b3331969ed52770751fc718ef530838b6dee",
    "net": "0xcfb98637bcae43c13323eaa1731ced2b716962fd",
    "rem": "0x83984d6142934bb535793a82adb0a46ef0f66b6d",
    "drt": "0x9af4f26941677c706cfecf6d3379ff01bb85d5ab",
    "nxc": "0x45e42d659d9f9466cd5df622506033145a9b89bc",
    "art": "0xfec0cf7fe078a500abf15f1284958f22049c2c7e",
    "¢": "0xa33e729bf4fdeb868b534e1f20523463d9c46bee",
    "snov": "0xbdc5bac39dbe132b1e030e898ae3830017d7d969",
    "flixx": "0xf04a8ac553fcedb5ba99a64799155826c136b0be",
    "cas": "0xe8780b48bdb05f928697a5e8155f672ed91462f7",
    "bnty": "0xd2d6158683aee4cc838067727209a0aaf4359de3",
    "qau": "0x671abbe5ce652491985342e85428eb1b07bc6c64",
    "ftx": "0xd559f20296ff4895da39b5bd9add54b442596a61",
    "credo": "0x4e0603e2a27a30480e5e3a4fe548e29ef12f64be",
    "sig": "0x6888a16ea9792c15a4dcf2f6c623d055c8ede792",
    "exrn": "0xe469c4473af82217b30cf17b10bcdb6c8c796e75",
    "air": "0x27dce1ec4d3f72c3e457cc50354f1f975ddef488",
    "tusd": "0x0000000000085d4780b73119b644ae5ecd22b376",
    "ary": "0xa5f8fc0921880cb7342368bd128eb8050442b1a1",
    "idxm": "0xcc13fc627effd6e35d2d2706ea3c4d7396c610ea",
    "xnk": "0xbc86727e770de68b1060c91f6bb6945c73e10388",
    "loc": "0x5e3346444010135322268a4630d2ed5f8d09446c",
    "can": "0x1d462414fe14cf489c7a21cac78509f4bf8cd7c0",
    "cofi": "0x3136ef851592acf49ca4c825131e364170fa32b3",
    "ipsx": "0x001f0aa5da15585e5b2305dbab2bac425ea71007",
    "dov": "0xac3211a5025414af2866ff09c23fc18bc97e79b1",
    "lala": "0xfd107b473ab90e8fbd89872144a3dc92c40fa8c9",
    "cxo": "0xb6ee9668771a79be7967ee29a63d4184f8097143",
    "wrc": "0x72adadb447784dd7ab1f472467750fc485e4cb2d",
    "alis": "0xea610b1153477720748dc13ed378003941d84fab",
    "lnc": "0x63e634330a20150dbb61b15648bc73855d6ccf07",
    "time": "0x6531f133e6deebe7f2dce5a0441aa7ef330b4e53",
    "pkt": "0x2604fa406be957e542beb89e6754fcde6815e83f",
    "avt": "0x0d88ed6e74bbfd96b831231638b66c05571e824f",
    "zla": "0xfd8971d5e8e1740ce2d0a84095fca4de729d0c16",
    "hbt": "0xdd6c68bb32462e01705011a4e2ad1a60740f217f",
    "fluz": "0x954b5de09a55e59755acbda29e1eb74a45d30175",
    "plu": "0xd8912c10681d8b21fd3742244f44658dba12264e",
    "instar": "0xc72fe8e3dd5bef0f9f31f259399f301272ef2a2d",
    "myst": "0xa645264c5603e96c3b0b078cdab68733794b0a71",
    "rvt": "0x3d1ba9be9f66b8ee101911bc36d3fb562eac2244",
    "ipl": "0x64cdf819d3e75ac8ec217b3496d7ce167be42e80",
    "ift": "0x7654915a1b82d6d2d0afc37c52af556ea8983c7e",
    "clr": "0xac838aee2f650a6b970ecea56d4651653c1f84a1",
    "adb": "0x2baac9330cf9ac479d819195794d79ad0c7616e3",
    "cbt": "0x076c97e1c869072ee22f8c91978c99b4bcb02591",
    "get": "0x60c68a87be1e8a84144b543aacfa77199cd3d024",
    "myb": "0x94298f1e0ab2dfad6eeffb1426846a3c29d98090",
    "sxut": "0x2c82c73d5b34aa015989462b2948cd616a37641f",
    "spf": "0x85089389c14bd9c77fc2b8f0c3d1dc3363bf06ef",
    "xaurum": "0x4df812f6064def1e5e029f1ca858777cc98d2d81",
    "ero": "0x74ceda77281b339142a36817fa5f9e29412bab85",
    "blue": "0x539efe69bcdd21a83efd9122571a64cc25e0282b",
    "dth": "0x5adc961d6ac3f7062d2ea45fefb8d8167d44b190",
    "tgt": "0xac3da587eac229c9896d919abc235ca4fd7f72c1",
    "gla": "0x71d01db8d6a2fbea7f8d434599c237980c234e4c",
    "npx": "0x28b5e12cce51f15594b0b91d5b5adaa70f684a02",
    "cag": "0x7d4b8cce0591c9044a22ee543533b72e976e36c3",
    "poll": "0x705ee96c1c160842c92c1aecfcffccc9c412e3d9",
    "astro": "0x7b22938ca841aa392c93dbb7f4c42178e3d65e88",
    "gat": "0x687174f8c49ceb7729d925c3a961507ea4ac7b28",
    "prix": "0x3adfc4999f77d04c8341bac5f3a76f58dff5b37a",
    "atl": "0x78b7fada55a64dd895d8c8c35779dd8b67fa8a05",
    "chx": "0x1460a58096d80a50a2f1f956dda497611fa4f165",
    "hgt": "0xba2184520a1cc49a6159c57e61e1844e085615b6",
    "csno": "0x29d75277ac7f0335b2165d0895e8725cbf658d73",
    "voise": "0x83eea00d838f92dec4d1475697b9f4d3537b56e3",
    "ezt": "0x5e6016ae7d7c49d347dcf834860b9f3ee282812b",
    "lev": "0x0f4ca92660efad97a9a70cb0fe969c755439772c",
    "tfl": "0xa7f976c360ebbed4465c2855684d1aae5271efa9",
    "pbl": "0x55648de19836338549130b1af587f16bea46f66b",
    "viu": "0x519475b31653e46d20cd09f9fdcf3b12bdacb4f5",
    "b2bx": "0x5d51fcced3114a8bb5e90cdd0f9d682bcbcc5393",
    "play": "0xe477292f1b3268687a29376116b0ed27a9c76170",
    "cpay": "0x0ebb614204e47c09b6c3feb9aaecad8ee060e23e",
    "arc": "0xac709fcb44a43c35f0da4e3163b117a17f3770f5",
    "trct": "0x30cecb5461a449a90081f5a5f55db4e048397bab",
    "aid": "0x37e8789bb9996cac9156cd5f5fd32599e6b91289",
    "inxt": "0xa8006c4ca56f24d6836727d106349320db7fef82",
    "bon": "0xcc34366e3842ca1bd36c1f324d15257960fcc801",
    "horse": "0x5b0751713b2527d7f002c0c4e2a37e1219610a6b",
    "loci": "0x9c23d67aea7b95d80942e3836bcdf7e708a747c2",
    "vit": "0x23b75bc7aaf28e2d6628c3f424b3882f8f072a3c",
    "j8t": "0x0d262e5dc4a06a0f1c90ce79c7a60c09dfc884e4",
    "opt": "0x4355fc160f74328f9b383df2ec589bb3dfd82ba0",
    "cpy": "0xf44745fbd41f6a1ba151df190db0564c5fcc4410",
    "mfg": "0x6710c63432a2de02954fc0f851db07146a6c0312",
    "aix": "0x1063ce524265d5a3a624f4914acd573dd89ce988",
    "otn": "0x881ef48211982d01e2cb7092c915e647cd40d85c",
    "nio": "0x5554e04e76533e1d14c52f05beef6c9d329e1e30",
    "xnn": "0xab95e915c123fded5bdfb6325e35ef5515f1ea69",
    "ledu": "0x5b26c5d0772e5bbac8b3182ae9a13f9bb2d03765",
    "scl": "0xd7631787b4dcc87b1254cfd1e5ce48e96823dee8",
    "adst": "0x422866a8f0b032c5cf1dfbdef31a20f4509562b0",
    "amlt": "0xca0e7269600d353f70b14ad118a49575455c0f2f",
    "bet": "0x8aa33a7899fcc8ea5fbe6a608a109c3893a1b8b2",
    "exy": "0x5c743a35e903f6c584514ec617acee0611cf44f3",
    "crb": "0xaef38fbfbf932d1aef3b808bc8fbd8cd8e1f8bc5",
    "ing": "0x24ddff6d8b8a42d835af3b440de91f3386554aa4",
    "wish": "0x1b22c32cd936cb97c28c5690a0695a82abf688e6",
    "dan": "0x9b70740e708a083c6ff38df52297020f5dfaa5ee",
    "mntp": "0x83cee9e086a77e492ee0bb93c2b0437ad6fdeccc",
    "shp": "0xef2463099360a085f1f10b076ed72ef625497a06",
    "vsl": "0x5c543e7ae0a1104f78406c340e9c64fd9fce5170",
    "rex": "0xf05a9382a4c3f29e2784502754293d88b835109c",
    "drp": "0x621d78f2ef2fd937bfca696cabaf9a779f59b3ed",
    "tie": "0x999967e2ec8a74b7c8e9db19e039d920b31d39d0",
    "ufr": "0xea097a2b1db00627b2fa17460ad260c016016977",
    "pix": "0x8effd494eb698cc399af6231fccd39e08fd20b15",
    "pylnt": "0x7703c35cffdc5cda8d27aa3df2f9ba6964544b6e",
    "cred": "0x672a1ad4f667fb18a333af13667aa0af1f5b5bdd",
    "ref": "0x89303500a7abfb178b274fd89f2469c264951e1f",
    "real": "0x9214ec02cb71cba0ada6896b8da260736a67ab10",
    "stac": "0x9a005c9a89bd72a4bd27721e7a09a3c11d2b03c4",
    "sense": "0x6745fab6801e376cd24f03572b9c9b0d4edddccf",
    "earth": "0x900b4449236a7bb26b286601dd14d2bde7a6ac6c",
    "bez": "0x3839d8ba312751aa0248fed6a8bacb84308e20ed",
    "vzt": "0x9720b467a710382a232a32f540bdced7d662a10b",
    "gmt": "0xb3bd49e28f8f832b8d1e246106991e546c323502",
    "sms": "0x39013f961c378f02c2b82a6e1d31e9812786fd9d",
    "evc": "0xb62d18dea74045e822352ce4b3ee77319dc5ff2f",
    "ace": "0x06147110022b768ba8f99a8f385df11a151a9cc8",
    "crc": "0xf41e5fbc2f6aac200dd8619e121ce1f05d150077",
    "tbx": "0x3a92bd396aef82af98ebc0aa9030d25a23b11c6b",
    "dgpt": "0xf6cfe53d6febaeea051f400ff5fc14f0cbbdaca1",
    "qvt": "0x1183f92a5624d68e85ffb9170f16bf0443b4c242",
    "gim": "0xae4f56f072c34c0a65b3ae3e4db797d831439d93",
    "emv": "0xb802b24e0637c2b87d2e8b7784c055bbe921011a",
    "esz": "0xe8a1df958be379045e2b46a31a98b93a2ecdfded",
    "wtt": "0x84119cb33e8f590d75c2d6ea4e6b0741a7494eda",
    "latx": "0x2f85e502a988af76f7ee6d83b7db8d6c0a823bf9",
    "ebtc": "0xeb7c20027172e5d143fb030d50f91cece2d1485d",
    "tig": "0xeee2d00eb7deb8dd6924187f5aa3496b7d06e62a",
    "cl": "0xe81d72d14b1516e68ac3190a46c93302cc8ed60f",
    "fyp": "0x8f0921f30555624143d427b340b1156914882c10",
    "ind": "0xf8e386eda857484f5a12e4b5daa9984e06e73705",
    "roc": "0x1bcbc54166f6ba149934870b60506199b6c9db6d",
    "jc": "0xe2d82dc7da0e6f882e96846451f4fabcc8f90528",
    "skin": "0x2bdc0d42996017fce214b21607a515da41a9e0c5",
    "fyn": "0x88fcfbc22c6d3dbaa25af478c578978339bde77a",
    "etbs": "0x1b9743f556d65e757c4c650b4555baf354cb8bd3",
    "eltcoin": "0x44197a4c44d6a059297caf6be4f7e172bd56caaf",
    "lgd": "0x59061b6f26bb4a9ce5828a19d35cfd5a4b80f056",
    "epy": "0x50ee674689d75c0f88e8f83cfe8c4b69e8fd590d",
    "ndc": "0xa54ddc7b3cce7fc8b1e3fa0256d0db80d2c10970",
    "mcap": "0x93e682107d1e9defb0b5ee701c71707a4b2e46bc",
    "emb": "0x386467f1f3ddbe832448650418311a479eecfc57",
    "strc": "0x46492473755e8df960f8034877f61732d718ce96",
    "stu": "0x0371a82e4a9d0a4312f3ee2ac9c6958512891372",
    "ctr": "0x96a65609a7b84e8842732deb08f56c3e21ac6f8a",
    "eql": "0x47dd62d4d075dead71d0e00299fc56a2d747bebb",
    "cdx": "0x6fff3806bbac52a20e0d79bc538d527f6a22c96b",
    "riya": "0x0b1724cc9fda0186911ef6a75949e9c0d3f0f2f3",
    "fuck": "0x65be44c747988fbf606207698c944df4442efe19",
    "wild": "0xd3c00772b24d997a812249ca637a921e81357701",
    "bitpark": "0xf3d29fb98d2dc5e78c87198deef99377345fd6f1",
    "jet": "0x8727c112c712c4a03371ac87a74dd6ab104af768",
    "ieth": "0x859a9c0b44cb7066d956a958b0b82e54c9e44b4b",
    "drpu": "0xe30e02f049957e2a5907589e06ba646fb2c321ba",
    "mne": "0x1a95b271b0535d15fa49932daba31ba612b52946",
    "sur": "0xe120c1ecbfdfea7f0a8f0ee30063491e8c26fedf",
    "ats": "0x2daee1aa61d60a252dc80564499a69802853583a",
    "acc": "0x13f1b7fdfbe1fc66676d56483e21b1ecb40b58e2",
    "arct": "0x1245ef80f4d9e02ed9425375e8f649b9221b31d8",
    "cct": "0x336f646f87d9f6bc6ed42dd46e8b3fd9dbd15c22",
    "itt": "0x0aef06dcccc531e581f0440059e6ffcc206039ee",
    "rlt": "0xcced5b8288086be8c38e23567e684c3740be4d48",
    "ccrb": "0xe4c94d45f7aef7018a5d66f44af780ec6023378e",
    "ebch": "0xafc39788c51f0c1ff7b55317f3e70299e521fff6",
    "sgr": "0xcb5a05bef3257613e984c17dbcf039952b6d883f",
    "btcr": "0x6aac8cb9861e42bf8259f5abdc6ae3ae89909e11",
    "xbl": "0x49aec0752e68d0282db544c677f6ba407ba17ed7",
    "ddf": "0xcc4ef9eeaf656ac1a2ab886743e98e97e090ed38",
    "ntwk": "0x2233799ee2683d75dfefacbcd2a26c78d34b470d",
    "nxx": "0x7627de4b93263a6a7570b8dafa64bae812e5c394",
    "ctx": "0x662abcad0b7f345ab7ffb1b1fbb9df7894f18e66",
    "btca": "0x02725836ebf3ecdb1cdf1c7b02fcbbfaa2736af8",
    "tkr": "0xb45a50545beeab73f38f31e5973768c421805e5e",
    "cco": "0x679badc551626e01b23ceecefbc9b877ea18fc46",
    "etg": "0x28c8d01ff633ea9cd8fc6a451d7457889e698de6",
    "e4row": "0xce5c603c78d047ef43032e96b5b785324f753a4f",
    "nto": "0x8a99ed8a1b204903ee46e733f2c1286f6d20b177",
    "lnk": "0xe2e6d4be086c6938b53b22144855eef674281639",
    "lct": "0x05c7065d644096a4e4c3fe24af86e36de021074b",
    "ethd": "0xdbfb423e9bbf16294388e07696a5120e4ceba0c5",
    "egas": "0xb53a96bcbdd9cf78dff20bab6c2be7baec8f00f8",
    "brat": "0x9e77d5a1251b6f7d456722a6eac6d2d5980bd891",
    "dalc": "0x07d9e49ea402194bf48a8276dafb16e4ed633317",
    "bln": "0xca29db4221c111888a7e80b12eac8a266da3ee0d",
    "newb": "0x814964b1bceaf24e26296d031eadf134a2ca4105",
    "ice": "0x5a84969bb663fb64f6d015dcf9f622aedc796750",
    "uet": "0x27f706edde3ad952ef647dd67e24e38cd0803dd6",
    "bas": "0x2a05d22db079bc40c2f77a1d1ff703a56e631cc1",
    "pos": "0xee609fe292128cad03b786dbb9bc2634ccdbe7fc",
    "rmc": "0x7dc4f41294697a7903c4027f6ac528c5d14cd7eb",
    "ai": "0x5121e348e897daef1eef23959ab290e5557cf274",
    "wicc": "0x4f878c0852722b0976a955d68b376e4cd4ae99e5",
    "dta": "0x69b148395ce0015c13e36bffbad63f49ef874e03",
    "let": "0xfa3118b34522580c35ae27f6cf52da1dbb756288",
    "mds": "0x66186008c1050627f979d464eabb258860563dbe",
    "edu": "0xa0872ee815b8dd0f6937386fd77134720d953581",
    "kan": "0x1410434b0346f5be678d0fb554e5c7ab620f8f4a",
    "lba": "0xfe5f141bf94fe84bc28ded0ab966c16b17490657",
    "wan": "0x5fc6de61258e63706543bb57619b99cc0e5a5a1f",
    "bft": "0x01ff50f8b7f74e4f00580d9596cd3d0d6d6e326f",
    "chat": "0x442bc47357919446eabc18c7211e57a13d983469",
    "swftc": "0x0bb217e40f8a5cb79adf04e1aab60e5abd0dfc1e",
    "meet": "0x7f121d4ec6c2c07eb6bc7989d91d2d4ff654c068",
    "yee": "0x922105fad8153f516bcfb829f56dc097a0e1d705",
    "eko": "0xa6a840e50bcaa50da017b91a0d86b8b2d41156ee",
    "topc": "0x1b6c5864375b34af3ff5bd2e5f40bc425b4a8d79",
    "tnb": "0xf7920b0768ecb20a123fac32311d07d193381d6f",
    "propy": "0x226bb599a12c826476e3a771454697ea52e9e220",
    "aidoc": "0x584b44853680ee34a0f337b712a8f66d816df151",
    "ost": "0x2c4e8f2d746113d0696ce89b35f0d8bf88e0aeca",
    "pnt": "0x53066cddbc0099eb6c96785d9b3df2aaeede5da3",
    "zjlt": "0xbc34985b4d345aea933d5cac19f3a86bd1fb398f",
    "ssp": "0x624d520bab2e4ad83935fa503fb130614374e850",
    "fair": "0x9b20dabcec77f6289113e61893f7beefaeb1990a",
    "ycc": "0x37e1160184f7dd29f00b78c050bf13224780b0b0",
    "xmx": "0x0f8c45b896784a1e408526b9300519ef8660209c",
    "fti": "0x943ed852dadb5c3938ecdc6883718df8142de4c8",
    "seele": "0xb1eef147028e9f480dbc5ccaa3277d417d1b85f0",
    "bkbt": "0x6a27348483d59150ae76ef4c0f3622a78b0ca698",
    "portal": "0x8db90e3e7d04c875a51997092f9178fcac9defdb",
    "but": "0xb2e260f12406c401874ecc960893c0f74cd6afcd",
    "lxt": "0xbc46d9961a3932f7d6b64abfdec80c1816c4b835",
    "aac": "0xe75ad3aab14e4b0df8c5da4286608dabb21bd864",
    "cnn": "0x8713d26637cf49e1b6b4a7ce57106aabc9325343",
    "uip": "0x4290563c2d7c255b5eec87f2d3bd10389f991d68",
    "uc": "0xf84df2db2c87dd650641f8904af71ebfc3dde0ea",
    "gsc": "0x228ba514309ffdf03a81a205a6d040e429d6e80c",
    "iic": "0xb6f43025b29196af2dddd69b0a58afba079cd600",
    "egcc": "0xaf8a215e81faea7c180ce22b72483525121813bd",
    "she": "0x9064c91e51d7021a85ad96817e1432abf6624470",
    "amm": "0x8b1f49491477e0fb46a29fef53f1ea320d13c349",
    "bec": "0x3495ffcee09012ab7d827abf3e3b3ae428a38443",
    "cai": "0x4fe9f52ec23f6805f2fd0332a34da4f1c135b024",
    "dpy": "0x6c2adc2073994fb2ccc5032cc2906fa221e9b391",
    "insur": "0x51fb3da8a67861361281ac56fe2ad8c3b4539ffa",
    "ipc": "0x622cd54deb2bb7a051515192417109bcf3fe098f",
    "light": "0x1295b55fa04fbac6d9e7c351ecb3486e88129027",
    "mith": "0x3893b9422cd5d70a81edeffe3d5a1c6a978310bb",
    "mof": "0x653430560be843c4a3d143d0110e896c2ab8ac0d",
    "mvp": "0x8a77e40936bbc27e80e9a3f526368c967869c86d",
    "ors": "0xeb9a4b185816c354db92db09cc3b50be60b901b6",
    "pra": "0x9041fe5b3fdea0f5e4afdc17e75180738d877a01",
    "tra": "0x4432e7ffd729442614d9233499000530e08e9d62",
    "trio": "0x8b40761142b9aa6dc8964e61d0585995425c3d94",
    "true": "0xa4d17ab1ee0efdd23edc2869e7ba96b89eecf9ab",
    "uct": "0x3c4bea627039f0b7e7d21e34bb9c9fe962977518",
    "ugc": "0xf485c5e679238f9304d986bb2fc28fe3379200e5",
    "win": "0xbfaa8cf522136c6fafc1d53fe4b85b4603c765b8",
    "xuc": "0xc324a2f6b05880503444451b8b27e6f9e63287cb",
    "you": "0x34364bee11607b1963d66bca665fde93fca666a8",
    "zip": "0xa9d2927d3a04309e008b6af6e2e282ae2952e7fd",
    "npxs": "0xa15c7ebe1f07caf6bff097d8a589fb8ac49ae5b3",
    "qkc": "0xea26c4ac16d4a5a106820bc8aee85fd0b7b2b664",
    "cdc": "0x87026f792d09960232ca406e80c89bd35bafe566",
    "ft": "0xd37532d304214d588aeeac4c365e8f1d72e2304a",
    "hyc": "0xbb442775c5dd4468feac6fa834e139257c5826af",
    "stc": "0x8f136cc8bef1fea4a7b71aa2301ff1a52f084384",
    "box": "0x63f584fa56e60e4d0fe8802b27c7e6e3b33e007f",
    "hit": "0x7995ab36bb307afa6a683c24a25d90dc1ea83566",
    "abl": "0xf8b358b3397a8ea5464f8cc753645d42e14b79ea",
    "cit": "0xc54083e77f913a4f99e1232ae80c318ff03c9d17",
    "egt": "0x8e1b448ec7adfc7fa35fc2e885678bd323176e34",
    "mag": "0x647f274b3a7248d6cf51b35f08e7e7fd6edfb271",
    "rct": "0x13f25cd52b21650caa8225c9942337d914c9b030",
    "read": "0x13d0bf45e5f319fa0b58900807049f23cae7c40d",
    "sda": "0x4212fea9fec90236ecc51e41e2096b16ceb84555",
    "show": "0xf41861f194e7ba8de95144a89e0c6ed16ee0b3a0",
    "tct": "0x4824a7b64e3966b0133f4f4ffb1b9d6beb75fff7",
    "vite": "0x1b793e49237758dbd8b752afc9eb4b329d5da016",
    "wfee": "0xa37adde3ba20a396338364e2ddb5e0897d11a91d",
    "zco": "0x2008e3057bd734e10ad13c9eae45ff132abc1722",
    "mft": "0xdf2c7238198ad8b389666574f2d8bc411a4b7428",
    "idt": "0x02c4c78c462e32cca4a90bc499bf411fb7bc6afb",
    "dac": "0xaad54c9f27b876d2538455dda69207279ff673a5",
    "bcv": "0x1014613e2b3cbc4d575054d4982e580d9b99d7b1",
    "tos": "0xfb5a551374b656c6e39787b1d3a03feab7f3a98e",
    "musk": "0x5003b168b457b663c3c18ffcf5b6a24bee8f59c7",
    "mt": "0x9b4e2b4b13d125238aa0480dd42b4f6fc71b37cc",
    "ncc": "0x5d48f293baed247a2d0189058ba37aa238bd4725",
    "rccc": "0x33bfd20660eeaf952e8d5bc3236e1918701f17d0",
    "hpt": "0xa66daa57432024023db65477ba87d4e7f5f95213",
    "cvn": "0x62aaf435273bc4baa78dcebd6590042d7e58ba6f",
    "kcash": "0x32d74896f05204d1b6ae7b0a3cebd7fc0cd8f9c7",
    "cvcoin": "0x62aaf435273bc4baa78dcebd6590042d7e58ba6f",
    "rte": "0x436f0f3a982074c4a05084485d421466a994fe53",
    "pax": "0x8e870d67f660d95d5be530380d0ec0bd388289e1",
    "dacc": "0xf8c595d070d104377f58715ce2e6c93e49a87f3c ",
    "kcs": "0x039b5649a59967e3e936d7471f9c3700100ee1ab",
    "hds": "0xcafe27178308351a12fffffdeb161d9d730da082",
    "ods": "0x39ec39f6573247efb3954974d8618217f980e3a0",
    "okb": "0x75231f58b43240c9718dd58b4967c5114342a86c",
    "rsr": "0x8762db106b2c2a0bccb3a80d1ed41273552616e8"
}


def span_has_title_no_class(tag):
    # print(dir(tag))
    # if tag.name == 'span' and tag.has_attr('title') and not tag.has_attr('class'):
    #     if tag.parent.parent.find_all('span', attrs={'class': 'text-danger'}):
    #         return False
    #     return True
    # return False
    return tag.name == 'span' and tag.has_attr('title') and not tag.has_attr('class') \
           and not tag.parent.parent.find_all('span', attrs={'class': 'text-danger'})


def start(address):
    hr = requests.get(url=url % address, headers=headers)
    soup = BeautifulSoup(hr.text, 'html.parser')
    data = soup.find_all(span_has_title_no_class)
    if not data:
        print(address)
        return 0, 0
    data = data[0]
    diff = data.text
    data = time.mktime(time.strptime(data.get('title'), '%b-%d-%Y %I:%M:%S %p')) + 8 * 60 * 60
    return time.time() - data
    # date_list = []
    # now_time = time.time()
    # for x in data:
    #     trans_time = time.mktime(time.strptime(x.get('title'), '%b-%d-%Y %I:%M:%S %p')) + 8*60*60
    #     if (now_time - trans_time) < 60 * 60:
    #         date_list.append(x.text)
    # return len(date_list), date_list
    # return data, diff


if __name__ == "__main__":
    count_list = []
    # for k, v in ddict.items():
    for k in ['cmt', 'air', 'hdg', 'icx', 'tomo']:
        try:
            diff = start(ddict.get(k))
            count_list.append("%s,%s" % (k, diff))
        except Exception as e:
            print(k)
    print("==============================================")
    print(count_list)
