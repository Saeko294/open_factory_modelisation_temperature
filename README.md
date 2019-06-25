# Modélisation de température

## Branchements sur Wipy

![Image du cablage](https://image.noelshack.com/fichiers/2019/26/2/1561474011-wipy-branchements.png)

## Ajouter un bloc LED

Ajouter et adapter les lignes de code suivantes (exemple : **si on ajoute un sixième bloc LED, remplacer les X par des 6**).

### Dans le fichier **main.py**

**À la ligne 84**
```
apin = adc.channel(pin=config.capteur_X)
    val = apin()
    val_X1 = 69000/val
    val = apin()
    val_X2 = 69000/val
    val = apin()
    val_X3 = 69000/val
    val_X = (val_X1+val_X2+val_X3)/3
    print("Temperature CX: %d C" % val_X)

    bloc=bloc+1
    urequest.request("GET","https://{ip}/write_data.php?value={id_boite}&value_2={temp}".format(ip=config.host,id_boite=bloc,temp=val_X),None)

```

**À la ligne 108 :**
```
led_rouge_X = fonction.translate(val_X,config.leftMin,config.leftMax,0,255)
led_bleu_X = 255 - led_rouge_X
```





**À la ligne 138 :**
```
(led_rouge_X, 0, led_bleu_X),
(led_rouge_X, 0, led_bleu_X),
(led_rouge_X, 0, led_bleu_X),
(led_rouge_X, 0, led_bleu_X),
(led_rouge_X, 0, led_bleu_X),
```
###Dans le fichier **index.php**

**À la ligne 16 :**
```
$dataX = '';
```
**À la ligne 63 :**
```
$sql = "SELECT * FROM tempe WHERE id_boite = X ";
	$result = mysqli_query($mysqli, $sql);

//loop through the returned data
while ($row = mysqli_fetch_array($result)) {

	$dataX = $dataX . '"'. $row['temp'].'",';
}
```
**À la ligne 69 :**
```
	$data5 = trim($data5,",");
```



**À la ligne 148 :**
```
{
		                label: 'Capteur X',
		                data: [<?php echo $dataX; ?>],
		                backgroundColor: 'transparent',
		                borderColor:'rgba(RRR, GGG, BBB)',
		                borderWidth: 3
		            },
```

## config.php

```
# Plage de température ( Elle va définir sur quelle plage de température la couleur des leds va varier )

leftMin = 15 #Température min
leftMax = 32 #Température max

# Définition des ports analogiques pour les thermistances CTN

capteur_1 = "P13"
capteur_2 = "P14"
capteur_3 = "P15"
capteur_4 = "P16"
capteur_5 = "P17"

# Délai entre les différentes mesures de la température (en secondes)

delay = 900

# Adresse du serveur

host = "172.19.241.240"
```
