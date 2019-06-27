# Modélisation de température

## Branchements sur Wipy

![Image du cablage](https://image.noelshack.com/fichiers/2019/26/2/1561474011-wipy-branchements.png)

## Ajouter un bloc LED

Ajouter et adapter les BLOCs au niveaux des commentaires "INSERER" (exemple : **si on ajoute un sixième bloc LED, remplacer les X par des 6**).

### Dans le fichier **main.py**

**BLOC 1 :**
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
```
**BLOC 2 :**
```
led_rouge_X = fonction.translate(val_X,config.leftMin,config.leftMax,0,255)
led_bleu_X = 255 - led_rouge_X
```
**BLOC 3 :**
```
(led_rouge_X, 0, led_bleu_X),
(led_rouge_X, 0, led_bleu_X),
(led_rouge_X, 0, led_bleu_X),
(led_rouge_X, 0, led_bleu_X),
(led_rouge_X, 0, led_bleu_X),
```
**BLOC 4 :**
```
bloc=bloc+1
mathe.requete(config.host,val_X,bloc)
```
### Dans le fichier **config.php**
**BLOC 1 :**
```
capteur_X = "P??"
```
### Dans le fichier **index.php**

**BLOC 1 :**
```
$dataX = '';
```
**BLOC 2 :**
```
$sql = "SELECT * FROM tempe WHERE id_boite = X ";
	$result = mysqli_query($mysqli, $sql);

//loop through the returned data
while ($row = mysqli_fetch_array($result)) {

	$dataX = $dataX . '"'. $row['temp'].'",';
}
```
**BLOC 3 :**
```
	$dataX = trim($dataX,",");
```
**BLOC 4 :**
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

host = "adresse_ip"
```
