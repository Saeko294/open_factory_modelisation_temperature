from ws2812 import WS2812
import pycom
import time
import machine
import urequest
import config
import fonction

adc = machine.ADC() # Initialisation des ports analogiques

while True:

    bloc=0

    print("Mesure de la temperature...")

    apin = adc.channel(pin=config.capteur_1) # Définition du port
    val = apin() # Variable qui enregistre la tension du capteur
    val_11 = 58000/val # Opération qui calcule la température en degrés celsius à partir de la tension
    val = apin()
    val_12 = 58000/val
    val = apin()
    val_13 = 58000/val
    val_1 = (val_11+val_12+val_13)/3 #calcule qui détermine la moyenne des trois mesures, cela permet de réduire les valeurs erronées
    print("Temperature C1: %d C" % val_1) # Affichage de la température dans le terminal

    # Valeur qui sert à defnir l'id du bloc qui mesure la tension auprès de la base de donnée
    bloc=bloc+1

    # Requête HTTP qui va envoyer les données des capteurs à un script PHP (xampp/htdocs/write_data.php), ce script va generer une requête SQL qui va envoyer ces données dans la base de données
    urequest.request("GET","https://{ip}/write_data.php?value={id_boite}&value_2={temp}".format(ip=config.host,id_boite=bloc,temp=val_1),None)

    apin = adc.channel(pin=config.capteur_2)
    val = apin()
    val_21 = 66880/val
    val = apin()
    val_22 = 66880/val
    val = apin()
    val_23 = 66880/val
    val_2 = (val_21+val_22+val_23)/3
    print("Temperature C2: %d C" % val_2)

    bloc=bloc+1
    urequest.request("GET","https://{ip}/write_data.php?value={id_boite}&value_2={temp}".format(ip=config.host,id_boite=bloc,temp=val_2),None)

    apin = adc.channel(pin=config.capteur_3)
    val = apin()
    val_31 = 65000/val
    val = apin()
    val_32 = 65000/val
    val = apin()
    val_33 = 65000/val
    val_3 = (val_31+val_32+val_33)/3
    print("Temperature C3: %d C" % val_3)

    bloc=bloc+1
    urequest.request("GET","https://{ip}/write_data.php?value={id_boite}&value_2={temp}".format(ip=config.host,id_boite=bloc,temp=val_3),None)

    apin = adc.channel(pin=config.capteur_4)
    val = apin()
    val_41 = 85000/val
    val = apin()
    val_42 = 85000/val
    val = apin()
    val_43 = 85000/val
    val_4 = (val_41+val_42+val_43)/3
    print("Temperature C4: %d C" % val_4)

    bloc=bloc+1
    urequest.request("GET","https://{ip}/write_data.php?value={id_boite}&value_2={temp}".format(ip=config.host,id_boite=bloc,temp=val_4),None)

    apin = adc.channel(pin=config.capteur_5)
    val = apin()
    val_51 = 69000/val
    val = apin()
    val_52 = 69000/val
    val = apin()
    val_53 = 69000/val
    val_5 = (val_51+val_52+val_53)/3
    print("Temperature C5: %d C" % val_5)

    bloc=bloc+1
    urequest.request("GET","https://{ip}/write_data.php?value={id_boite}&value_2={temp}".format(ip=config.host,id_boite=bloc,temp=val_5),None)


    # faire fonctionner thermometre même sans connection

    # Fonction mathématique qui va convertir la température des capteurs en signa  l lumineux de couleur (Variation de rouge et de bleu pour symboliser le chaud et le froid)

    led_rouge_1 = fonction.translate(val_1,config.leftMin,config.leftMax,0,255)
    led_bleu_1 = 255 - led_rouge_1


    led_rouge_2 = fonction.translate(val_2,config.leftMin,config.leftMax,0,255)
    led_bleu_2 = 255 - led_rouge_2


    led_rouge_3 = fonction.translate(val_3,config.leftMin,config.leftMax,0,255)
    led_bleu_3 = 255 - led_rouge_3


    led_rouge_4 = fonction.translate(val_4,config.leftMin,config.leftMax,0,255)
    led_bleu_4 = 255 - led_rouge_4


    led_rouge_5 = fonction.translate(val_5,config.leftMin,config.leftMax,0,255)
    led_bleu_5 = 255 - led_rouge_5

# Affichage du signal lumineux sur la bande LED

    chain = WS2812(ledNumber=25)
    data = [
        (led_rouge_1, 0, led_bleu_1),
        (led_rouge_1, 0, led_bleu_1),
        (led_rouge_1, 0, led_bleu_1),
        (led_rouge_1, 0, led_bleu_1),
        (led_rouge_1, 0, led_bleu_1),
        (led_rouge_2, 0, led_bleu_2),
        (led_rouge_2, 0, led_bleu_2),
        (led_rouge_2, 0, led_bleu_2),
        (led_rouge_2, 0, led_bleu_2),
        (led_rouge_2, 0, led_bleu_2),
        (led_rouge_3, 0, led_bleu_3),
        (led_rouge_3, 0, led_bleu_3),
        (led_rouge_3, 0, led_bleu_3),
        (led_rouge_3, 0, led_bleu_3),
        (led_rouge_3, 0, led_bleu_3),
        (led_rouge_4, 0, led_bleu_4),
        (led_rouge_4, 0, led_bleu_4),
        (led_rouge_4, 0, led_bleu_4),
        (led_rouge_4, 0, led_bleu_4),
        (led_rouge_4, 0, led_bleu_4),
        (led_rouge_5, 0, led_bleu_5),
        (led_rouge_5, 0, led_bleu_5),
        (led_rouge_5, 0, led_bleu_5),
        (led_rouge_5, 0, led_bleu_5),
        (led_rouge_5, 0, led_bleu_5),
        
        ]
    chain.show(data)

    time.sleep(config.delay) # Pause de X temp entre chaques mesures (en secondes)
