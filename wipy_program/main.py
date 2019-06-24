from ws2812 import WS2812
import pycom
import time
import machine
import urequest
import config
import fonction

adc = machine.ADC() # Initialisation des ports analogiques

while True:
    print("Mesure de la temperature...")

    apin = adc.channel(pin=config.capteur_1) # Définition du port
    val_11 = apin() # Variable qui enregistre la tension du capteur
    val_1 = 54000/val_11 # Opération qui calcule la température en degrés celsius à partir de la tension
    print("Temperature C1: %d C" % val_1) # Affichage de la température dans le terminal

    apin = adc.channel(pin=config.capteur_2)
    val_22 = apin()
    val_2 = 66880/val_22
    print("Temperature C2: %d C" % val_2)

    apin = adc.channel(pin=config.capteur_3)
    val_33 = apin()
    val_3 = 66880/val_33
    print("Temperature C3: %d C" % val_3)

    apin = adc.channel(pin=config.capteur_4)
    val_44 = apin()
    val_4 = 85000/val_44
    print("Temperature C4: %d C" % val_4)

    apin = adc.channel(pin=config.capteur_5)
    val_55 = apin()
    val_5 = 69000/val_55
    print("Temperature C5: %d C" % val_5)

# Requête HTTP qui va envoyer les données des capteurs à un script PHP (xampp/htdocs/write_data.php), ce script va generer une requête SQL qui va envoyer ces données dans la base de données

    urequest.request("GET","https://172.19.241.240/write_data.php?value={temp1}&value_2={temp2}&value_3={temp3}&value_4={temp4}&value_5={temp5}".format(temp1=val_1,temp2=val_2,temp3=val_3,temp4=val_4,temp5=val_5),None)

# Fonction mathématique qui va convertir la température des capteurs en signal lumineux de couleur (Variation de rouge et de bleu pour symboliser le chaud et le froid)

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
