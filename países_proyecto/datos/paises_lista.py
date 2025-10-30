import csv
lista_diccionario = [
  {
    "continente": "America",
    "pais": "Argentina",
    "poblacion": 45851378,
    "superficie": 2736690
  },
  {
    "continente": "America",
    "pais": "Bolivia",
    "poblacion": 12637909,
    "superficie": 1083300
  },
  {
    "continente": "America",
    "pais": "Brasil",
    "poblacion": 213400000,
    "superficie": 8358140
  },
  {
    "continente": "America",
    "pais": "Chile",
    "poblacion": 19859921,
    "superficie": 743532
  },
  {
    "continente": "America",
    "pais": "Colombia",
    "poblacion": 53425635,
    "superficie": 1109500
  },
  {
    "continente": "America",
    "pais": "Ecuador",
    "poblacion": 18000000,
    "superficie": 256370
  },
  {
    "continente": "America",
    "pais": "Guyana",
    "poblacion": 830000,
    "superficie": 214969
  },
  {
    "continente": "America",
    "pais": "Paraguay",
    "poblacion": 7350000,
    "superficie": 406752
  },
  {
    "continente": "America",
    "pais": "Peru",
    "poblacion": 34600000,
    "superficie": 1285216
  },
  {
    "continente": "America",
    "pais": "Surinam",
    "poblacion": 640000,
    "superficie": 163820
  },
  {
    "continente": "America",
    "pais": "Uruguay",
    "poblacion": 3500000,
    "superficie": 176215
  },
  {
    "continente": "America",
    "pais": "Venezuela",
    "poblacion": 28720000,
    "superficie": 916445
  },
  {
    "continente": "America",
    "pais": "Guayana Francesa",
    "poblacion": 292354,
    "superficie": 83846
  },
  {
    "continente": "America",
    "pais": "Islas Malvinas",
    "poblacion": 3469,
    "superficie": 12170
  },
  {
    "continente": "America",
    "pais": "Guatemala",
    "poblacion": 18687881,
    "superficie": 107160
  },
  {
    "continente": "America",
    "pais": "Belice",
    "poblacion": 417072,
    "superficie": 22966
  },
  {
    "continente": "America",
    "pais": "El Salvador",
    "poblacion": 6366000,
    "superficie": 21040
  },
  {
    "continente": "America",
    "pais": "Honduras",
    "poblacion": 11005850,
    "superficie": 111890
  },
  {
    "continente": "America",
    "pais": "Nicaragua",
    "poblacion": 70000000,
    "superficie": 130373
  },
  {
    "continente": "America",
    "pais": "Costa Rica",
    "poblacion": 5159353,
    "superficie": 51060
  },
  {
    "continente": "America",
    "pais": "Panama",
    "poblacion": 4516000,
    "superficie": 75420
  },
  {
    "continente": "America",
    "pais": "Estados Unidos",
    "poblacion": 347275807,
    "superficie": 9147420
  },
  {
    "continente": "America",
    "pais": "Canada",
    "poblacion": 40126723,
    "superficie": 9093510
  },
  {
    "continente": "America",
    "pais": "Mexico",
    "poblacion": 131900000,
    "superficie": 1943950
  },
  {
    "continente": "America",
    "pais": "Guatemala",
    "poblacion": 18687881,
    "superficie": 108889
  },
  {
    "continente": "America",
    "pais": "Haiti",
    "poblacion": 11900000,
    "superficie": 27750
  },
  {
    "continente": "America",
    "pais": "Republica Dominicana",
    "poblacion": 11500000,
    "superficie": 48670
  },
  {
    "continente": "America",
    "pais": "Cuba",
    "poblacion": 11300000,
    "superficie": 109884
  },
  {
    "continente": "America",
    "pais": "Honduras",
    "poblacion": 11000000,
    "superficie": 112492
  },
  {
    "continente": "America",
    "pais": "Nicaragua",
    "poblacion": 7000000,
    "superficie": 130373
  },
  {
    "continente": "America",
    "pais": "El Salvador",
    "poblacion": 6300000,
    "superficie": 21041
  },
  {
    "continente": "America",
    "pais": "Costa Rica",
    "poblacion": 5191000,
    "superficie": 51100
  },
  {
    "continente": "America",
    "pais": "Panama",
    "poblacion": 4300000,
    "superficie": 75420
  },
  {
    "continente": "America",
    "pais": "Jamaica",
    "poblacion": 2753000,
    "superficie": 10991
  },
  {
    "continente": "America",
    "pais": "Trinidad y Tobago",
    "poblacion": 1368000,
    "superficie": 5128
  },
  {
    "continente": "America",
    "pais": "Bahamas",
    "poblacion": 409000,
    "superficie": 13880
  },
  {
    "continente": "America",
    "pais": "Belice",
    "poblacion": 465000,
    "superficie": 22966
  },
  {
    "continente": "America",
    "pais": "Antigua y Barbuda",
    "poblacion": 103600,
    "superficie": 443
  },
  {
    "continente": "America",
    "pais": "Barbados",
    "poblacion": 263700,
    "superficie": 430
  },
  {
    "continente": "America",
    "pais": "Dominica",
    "poblacion": 63200,
    "superficie": 751
  },
  {
    "continente": "America",
    "pais": "Saint Kitts y Nevis",
    "poblacion": 48400,
    "superficie": 261
  },
  {
    "continente": "America",
    "pais": "Saint Lucia",
    "poblacion": 186500,
    "superficie": 616
  },
  {
    "continente": "America",
    "pais": "Saint Vincent y las Granadinas",
    "poblacion": 112000,
    "superficie": 389
  },
  {
    "continente": "America",
    "pais": "Bermuda",
    "poblacion": 64555,
    "superficie": 50
  },
  {
    "continente": "America",
    "pais": "Groenlandia",
    "poblacion": 55745,
    "superficie": 410450
  },
  {
    "continente": "America",
    "pais": "Saint Pierre y Miquelon",
    "poblacion": 5574,
    "superficie": 230
  },
  {
    "continente": "Africa",
    "pais": "Angola",
    "poblacion": 35379000,
    "superficie": 1246700
  },
  {
    "continente": "Africa",
    "pais": "Argelia",
    "poblacion": 45400000,
    "superficie": 2381741
  },
  {
    "continente": "Africa",
    "pais": "Benin",
    "poblacion": 14503000,
    "superficie": 112622
  },
  {
    "continente": "Africa",
    "pais": "Botsuana",
    "poblacion": 2514000,
    "superficie": 581730
  },
  {
    "continente": "Africa",
    "pais": "Burkina Faso",
    "poblacion": 26840000,
    "superficie": 272967
  },
  {
    "continente": "Africa",
    "pais": "Burundi",
    "poblacion": 13491000,
    "superficie": 27834
  },
  {
    "continente": "Africa",
    "pais": "Cabo Verde",
    "poblacion": 525000,
    "superficie": 4033
  },
  {
    "continente": "Africa",
    "pais": "Camerun",
    "poblacion": 29784000,
    "superficie": 475442
  },
  {
    "continente": "Africa",
    "pais": "Chad",
    "poblacion": 19895000,
    "superficie": 1284000
  },
  {
    "continente": "Africa",
    "pais": "Congo",
    "poblacion": 6142000,
    "superficie": 342000
  },
  {
    "continente": "Africa",
    "pais": "Costa de Marfil",
    "poblacion": 29342000,
    "superficie": 322463
  },
  {
    "continente": "Africa",
    "pais": "Egipto",
    "poblacion": 107838000,
    "superficie": 995450
  },
  {
    "continente": "Africa",
    "pais": "Eritrea",
    "poblacion": 4785000,
    "superficie": 117600
  },
  {
    "continente": "Africa",
    "pais": "Etiopia",
    "poblacion": 111702000,
    "superficie": 1104300
  },
  {
    "continente": "Africa",
    "pais": "Esuatini",
    "poblacion": 1191000,
    "superficie": 17364
  },
  {
    "continente": "Africa",
    "pais": "Gab\u00f3n",
    "poblacion": 2431000,
    "superficie": 267668
  },
  {
    "continente": "Africa",
    "pais": "Gambia",
    "poblacion": 2727000,
    "superficie": 11295
  },
  {
    "continente": "Africa",
    "pais": "Ghana",
    "poblacion": 34121000,
    "superficie": 238533
  },
  {
    "continente": "Africa",
    "pais": "Guinea",
    "poblacion": 15865000,
    "superficie": 245857
  },
  {
    "continente": "Africa",
    "pais": "Guinea-Bisau",
    "poblacion": 2073000,
    "superficie": 36125
  },
  {
    "continente": "Africa",
    "pais": "Guinea Ecuatorial",
    "poblacion": 1711000,
    "superficie": 28051
  },
  {
    "continente": "Africa",
    "pais": "Kenia",
    "poblacion": 58246000,
    "superficie": 580367
  },
  {
    "continente": "Africa",
    "pais": "Lesoto",
    "poblacion": 2125000,
    "superficie": 30355
  },
  {
    "continente": "Africa",
    "pais": "Libia",
    "poblacion": 7358000,
    "superficie": 1759541
  },
  {
    "continente": "Africa",
    "pais": "Liberia",
    "poblacion": 6053000,
    "superficie": 111369
  },
  {
    "continente": "Africa",
    "pais": "Malawi",
    "poblacion": 22897000,
    "superficie": 118484
  },
  {
    "continente": "Africa",
    "pais": "Mali",
    "poblacion": 25859000,
    "superficie": 1240192
  },
  {
    "continente": "Africa",
    "pais": "Madagascar",
    "poblacion": 31456000,
    "superficie": 587041
  },
  {
    "continente": "Africa",
    "pais": "Mauritania",
    "poblacion": 5159000,
    "superficie": 1030700
  },
  {
    "continente": "Africa",
    "pais": "Marruecos",
    "poblacion": 38312000,
    "superficie": 710850
  },
  {
    "continente": "Africa",
    "pais": "Mozambique",
    "poblacion": 34096000,
    "superficie": 801590
  },
  {
    "continente": "Africa",
    "pais": "Namibia",
    "poblacion": 2781000,
    "superficie": 825615
  },
  {
    "continente": "Africa",
    "pais": "Niger",
    "poblacion": 28849000,
    "superficie": 1267000
  },
  {
    "continente": "Africa",
    "pais": "Nigeria",
    "poblacion": 233560000,
    "superficie": 910770
  },
  {
    "continente": "Africa",
    "pais": "Republica Centroafricana",
    "poblacion": 5893000,
    "superficie": 622984
  },
  {
    "continente": "Africa",
    "pais": "Republica Democratica del Congo",
    "poblacion": 109076000,
    "superficie": 2267050
  },
  {
    "continente": "Africa",
    "pais": "Ruanda",
    "poblacion": 14920000,
    "superficie": 26338
  },
  {
    "continente": "Africa",
    "pais": "Santo Tome y Principe",
    "poblacion": 245000,
    "superficie": 964
  },
  {
    "continente": "Africa",
    "pais": "Senegal",
    "poblacion": 19928000,
    "superficie": 196722
  },
  {
    "continente": "Africa",
    "pais": "Sierra Leona",
    "poblacion": 9132000,
    "superficie": 71740
  },
  {
    "continente": "Africa",
    "pais": "Somalia",
    "poblacion": 18143000,
    "superficie": 637657
  },
  {
    "continente": "Africa",
    "pais": "Sudafrica",
    "poblacion": 63430000,
    "superficie": 1213090
  },
  {
    "continente": "Africa",
    "pais": "Sudan",
    "poblacion": 50582000,
    "superficie": 1861484
  },
  {
    "continente": "Africa",
    "pais": "Sudan del Sur",
    "poblacion": 12278000,
    "superficie": 619745
  },
  {
    "continente": "Africa",
    "pais": "Seychelles",
    "poblacion": 106000,
    "superficie": 455
  },
  {
    "continente": "Africa",
    "pais": "Tanzania",
    "poblacion": 67529000,
    "superficie": 885800
  },
  {
    "continente": "Africa",
    "pais": "Togo",
    "poblacion": 9091000,
    "superficie": 56785
  },
  {
    "continente": "Africa",
    "pais": "Tunez",
    "poblacion": 12508000,
    "superficie": 163610
  },
  {
    "continente": "Africa",
    "pais": "Uganda",
    "poblacion": 51540000,
    "superficie": 241038
  },
  {
    "continente": "Africa",
    "pais": "Yibuti",
    "poblacion": 1042000,
    "superficie": 23200
  },
  {
    "continente": "Africa",
    "pais": "Zambia",
    "poblacion": 21324000,
    "superficie": 752612
  },
  {
    "continente": "Africa",
    "pais": "Zimbabue",
    "poblacion": 16897000,
    "superficie": 390757
  },
  {
    "continente": "Europa",
    "pais": "Rusia",
    "poblacion": 143997393,
    "superficie": 17098242
  },
  {
    "continente": "Europa",
    "pais": "Alemania",
    "poblacion": 84000000,
    "superficie": 357022
  },
  {
    "continente": "Europa",
    "pais": "Reino Unido",
    "poblacion": 67000000,
    "superficie": 243610
  },
  {
    "continente": "Europa",
    "pais": "Francia",
    "poblacion": 68000000,
    "superficie": 551695
  },
  {
    "continente": "Europa",
    "pais": "Italia",
    "poblacion": 59000000,
    "superficie": 301340
  },
  {
    "continente": "Europa",
    "pais": "Espana",
    "poblacion": 48000000,
    "superficie": 505990
  },
  {
    "continente": "Europa",
    "pais": "Polonia",
    "poblacion": 38000000,
    "superficie": 312696
  },
  {
    "continente": "Europa",
    "pais": "Rumania",
    "poblacion": 19000000,
    "superficie": 238397
  },
  {
    "continente": "Europa",
    "pais": "Paises Bajos",
    "poblacion": 18000000,
    "superficie": 41543
  },
  {
    "continente": "Europa",
    "pais": "Belgica",
    "poblacion": 11700000,
    "superficie": 30528
  },
  {
    "continente": "Europa",
    "pais": "Republica Checa",
    "poblacion": 10700000,
    "superficie": 78867
  },
  {
    "continente": "Europa",
    "pais": "Suecia",
    "poblacion": 10600000,
    "superficie": 450295
  },
  {
    "continente": "Europa",
    "pais": "Portugal",
    "poblacion": 10400000,
    "superficie": 92090
  },
  {
    "continente": "Europa",
    "pais": "Grecia",
    "poblacion": 10000000,
    "superficie": 131957
  },
  {
    "continente": "Europa",
    "pais": "Hungria",
    "poblacion": 9600000,
    "superficie": 93030
  },
  {
    "continente": "Europa",
    "pais": "Austria",
    "poblacion": 9100000,
    "superficie": 83879
  },
  {
    "continente": "Europa",
    "pais": "Bielorrusia",
    "poblacion": 9000000,
    "superficie": 207600
  },
  {
    "continente": "Europa",
    "pais": "Suiza",
    "poblacion": 8900000,
    "superficie": 41284
  },
  {
    "continente": "Europa",
    "pais": "Serbia",
    "poblacion": 6800000,
    "superficie": 88361
  },
  {
    "continente": "Europa",
    "pais": "Bulgaria",
    "poblacion": 6700000,
    "superficie": 110879
  },
  {
    "continente": "Europa",
    "pais": "Dinamarca",
    "poblacion": 5900000,
    "superficie": 43094
  },
  {
    "continente": "Europa",
    "pais": "Finlandia",
    "poblacion": 5500000,
    "superficie": 338455
  },
  {
    "continente": "Europa",
    "pais": "Eslovaquia",
    "poblacion": 5400000,
    "superficie": 49035
  },
  {
    "continente": "Europa",
    "pais": "Noruega",
    "poblacion": 5400000,
    "superficie": 385207
  },
  {
    "continente": "Europa",
    "pais": "Irlanda",
    "poblacion": 5200000,
    "superficie": 70273
  },
  {
    "continente": "Europa",
    "pais": "Croacia",
    "poblacion": 4000000,
    "superficie": 56594
  },
  {
    "continente": "Europa",
    "pais": "Bosnia y Herzegovina",
    "poblacion": 3200000,
    "superficie": 51197
  },
  {
    "continente": "Europa",
    "pais": "Albania",
    "poblacion": 2800000,
    "superficie": 28748
  },
  {
    "continente": "Europa",
    "pais": "Lituania",
    "poblacion": 2700000,
    "superficie": 65300
  },
  {
    "continente": "Europa",
    "pais": "Moldavia",
    "poblacion": 2600000,
    "superficie": 33846
  },
  {
    "continente": "Europa",
    "pais": "Eslovenia",
    "poblacion": 2100000,
    "superficie": 20273
  },
  {
    "continente": "Europa",
    "pais": "Macedonia del Norte",
    "poblacion": 2100000,
    "superficie": 25713
  },
  {
    "continente": "Europa",
    "pais": "Letonia",
    "poblacion": 1900000,
    "superficie": 64589
  },
  {
    "continente": "Europa",
    "pais": "Estonia",
    "poblacion": 1300000,
    "superficie": 45227
  },
  {
    "continente": "Europa",
    "pais": "Luxemburgo",
    "poblacion": 660000,
    "superficie": 2586
  },
  {
    "continente": "Europa",
    "pais": "Malta",
    "poblacion": 520000,
    "superficie": 316
  },
  {
    "continente": "Europa",
    "pais": "Islandia",
    "poblacion": 370000,
    "superficie": 103000
  },
  {
    "continente": "Europa",
    "pais": "Andorra",
    "poblacion": 80000,
    "superficie": 468
  },
  {
    "continente": "Europa",
    "pais": "Monaco",
    "poblacion": 39000,
    "superficie": 203
  },
  {
    "continente": "Europa",
    "pais": "Liechtenstein",
    "poblacion": 39000,
    "superficie": 160
  },
  {
    "continente": "Europa",
    "pais": "San Marino",
    "poblacion": 34000,
    "superficie": 61
  },
  {
    "continente": "Europa",
    "pais": "Armenia",
    "poblacion": 2800000,
    "superficie": 29743
  },
  {
    "continente": "Europa",
    "pais": "Georgia",
    "poblacion": 3700000,
    "superficie": 69700
  },
  {
    "continente": "Europa",
    "pais": "Azerbaiyan",
    "poblacion": 10300000,
    "superficie": 86600
  },
  {
    "continente": "Asia",
    "pais": "Afganistan",
    "poblacion": 42594582,
    "superficie": 652230
  },
  {
    "continente": "Asia",
    "pais": "Arabia Saudita",
    "poblacion": 35541000,
    "superficie": 2149690
  },
  {
    "continente": "Asia",
    "pais": "Bangladesh",
    "poblacion": 170000000,
    "superficie": 147570
  },
  {
    "continente": "Asia",
    "pais": "Barhein",
    "poblacion": 1701583,
    "superficie": 765
  },
  {
    "continente": "Asia",
    "pais": "Bhutan",
    "poblacion": 754394,
    "superficie": 38394
  },
  {
    "continente": "Asia",
    "pais": "Brunei",
    "poblacion": 437483,
    "superficie": 5765
  },
  {
    "continente": "Asia",
    "pais": "Camboya",
    "poblacion": 17000000,
    "superficie": 181035
  },
  {
    "continente": "Asia",
    "pais": "China",
    "poblacion": 1444216107,
    "superficie": 9596961
  },
  {
    "continente": "Asia",
    "pais": "Chipre",
    "poblacion": 1207359,
    "superficie": 9251
  },
  {
    "continente": "Asia",
    "pais": "Corea del Norte",
    "poblacion": 25778816,
    "superficie": 120538
  },
  {
    "continente": "Asia",
    "pais": "Corea del Sur",
    "poblacion": 51841712,
    "superficie": 100210
  },
  {
    "continente": "Asia",
    "pais": "Emiratos Arabes Unidos",
    "poblacion": 9890000,
    "superficie": 83600
  },
  {
    "continente": "Asia",
    "pais": "Filipinas",
    "poblacion": 113900000,
    "superficie": 300000
  },
  {
    "continente": "Asia",
    "pais": "India",
    "poblacion": 1407563847,
    "superficie": 3287263
  },
  {
    "continente": "Asia",
    "pais": "Indonesia",
    "poblacion": 276361783,
    "superficie": 1904569
  },
  {
    "continente": "Asia",
    "pais": "Iraq",
    "poblacion": 45604103,
    "superficie": 438317
  },
  {
    "continente": "Asia",
    "pais": "Israel",
    "poblacion": 9500000,
    "superficie": 20770
  },
  {
    "continente": "Asia",
    "pais": "Japon",
    "poblacion": 125710000,
    "superficie": 377975
  },
  {
    "continente": "Asia",
    "pais": "Jordania",
    "poblacion": 10203140,
    "superficie": 89342
  },
  {
    "continente": "Asia",
    "pais": "Kazajistan",
    "poblacion": 19233456,
    "superficie": 2724900
  },
  {
    "continente": "Asia",
    "pais": "Kuwait",
    "poblacion": 4418042,
    "superficie": 17818
  },
  {
    "continente": "Asia",
    "pais": "Laos",
    "poblacion": 7275556,
    "superficie": 236800
  },
  {
    "continente": "Asia",
    "pais": "L\u00edbano",
    "poblacion": 6825445,
    "superficie": 10452
  },
  {
    "continente": "Asia",
    "pais": "Malasia",
    "poblacion": 33100000,
    "superficie": 330803
  },
  {
    "continente": "Asia",
    "pais": "Maldivas",
    "poblacion": 540542,
    "superficie": 298
  },
  {
    "continente": "Asia",
    "pais": "Mongolia",
    "poblacion": 3225167,
    "superficie": 1564116
  },
  {
    "continente": "Asia",
    "pais": "Myanmar",
    "poblacion": 54045420,
    "superficie": 676578
  },
  {
    "continente": "Asia",
    "pais": "Nepal",
    "poblacion": 29136808,
    "superficie": 147516
  },
  {
    "continente": "Asia",
    "pais": "Oman",
    "poblacion": 5007000,
    "superficie": 309500
  },
  {
    "continente": "Asia",
    "pais": "Pakistan",
    "poblacion": 240485658,
    "superficie": 881913
  },
  {
    "continente": "Asia",
    "pais": "Qatar",
    "poblacion": 2891039,
    "superficie": 11586
  },
  {
    "continente": "Asia",
    "pais": "Singapur",
    "poblacion": 5638700,
    "superficie": 719
  },
  {
    "continente": "Asia",
    "pais": "Sri Lanka",
    "poblacion": 22286000,
    "superficie": 65610
  },
  {
    "continente": "Asia",
    "pais": "Siria",
    "poblacion": 18000000,
    "superficie": 185180
  },
  {
    "continente": "Asia",
    "pais": "Tailandia",
    "poblacion": 70300000,
    "superficie": 513120
  },
  {
    "continente": "Asia",
    "pais": "Tayikistan",
    "poblacion": 9751000,
    "superficie": 143100
  },
  {
    "continente": "Asia",
    "pais": "Timor Oriental",
    "poblacion": 1318442,
    "superficie": 14874
  },
  {
    "continente": "Asia",
    "pais": "Turkmenistan",
    "poblacion": 6200000,
    "superficie": 488100
  },
  {
    "continente": "Asia",
    "pais": "Uzbekistan",
    "poblacion": 35220000,
    "superficie": 447400
  },
  {
    "continente": "Asia",
    "pais": "Vietnam",
    "poblacion": 98168829,
    "superficie": 331210
  },
  {
    "continente": "Asia",
    "pais": "Yemen",
    "poblacion": 29825968,
    "superficie": 527968
  },
  {
    "continente": "Oceania",
    "pais": "Australia",
    "poblacion": 25687041,
    "superficie": 7692024
  },
  {
    "continente": "Oceania",
    "pais": "Fiyi",
    "poblacion": 896444,
    "superficie": 18272
  },
  {
    "continente": "Oceania",
    "pais": "Islas Marshall",
    "poblacion": 59190,
    "superficie": 181
  },
  {
    "continente": "Oceania",
    "pais": "Islas Salomon",
    "poblacion": 70000,
    "superficie": 28450
  },
  {
    "continente": "Oceania",
    "pais": "Kiribati",
    "poblacion": 119446,
    "superficie": 811
  },
  {
    "continente": "Oceania",
    "pais": "Micronesia",
    "poblacion": 115023,
    "superficie": 702
  },
  {
    "continente": "Oceania",
    "pais": "Nauru",
    "poblacion": 10834,
    "superficie": 21
  },
  {
    "continente": "Oceania",
    "pais": "Nueva Zelanda",
    "poblacion": 5084300,
    "superficie": 268838
  },
  {
    "continente": "Oceania",
    "pais": "Palaos",
    "poblacion": 18000,
    "superficie": 459
  },
  {
    "continente": "Oceania",
    "pais": "Papua Nueva Guinea",
    "poblacion": 8947027,
    "superficie": 462840
  },
  {
    "continente": "Oceania",
    "pais": "Samoa",
    "poblacion": 198410,
    "superficie": 2842
  },
  {
    "continente": "Oceania",
    "pais": "Tonga",
    "poblacion": 105695,
    "superficie": 747
  },
  {
    "continente": "Oceania",
    "pais": "Tuvalu",
    "poblacion": 11792,
    "superficie": 26
  },
  {
    "continente": "Oceania",
    "pais": "Vanuatu",
    "poblacion": 307150,
    "superficie": 12189
  }
]
campos = ['continente', 'pais', 'poblacion', 'superficie']

with open('paises.csv', 'w', newline='', encoding='utf-8') as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    
    # Escribimos la cabecera
    escritor.writeheader()
    
    # Escribimos cada país en una línea
    escritor.writerows(lista_diccionario)

print("✅ CSV generado correctamente")