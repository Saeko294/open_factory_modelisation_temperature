from ws2812 import WS2812
from network import WLAN
import pycom
import time
import machine
import urequest
import config
import mathe
wlan = WLAN()
adc = machine.ADC() # Initialisation des ports analogiques

while True:

    print("Mesure de la temperature...")

    apin = adc.channel(pin=config.capteur_1) # Définition du port
    val = apin() # Variable qui enregistre la tension du capteur
    val_11 = 58000/val # Opération qui calcule la température en degrés celsius à partir de la tension

    val = apin()
    val_12 = 58000/val

    val = apin()
    val_13 = 58000/val
    time.sleep(1)
    val = apin()
    val_14 = 58000/val

    val = apin()
    val_15 = 58000/val

    val = apin()
    val_16 = 58000/val
    val_1 = (val_11+val_12+val_13+val_14+val_15+val_16)/6 #calcule qui détermine la moyenne des trois mesures, cela permet de réduire les valeurs erronées
    print("Temperature C1: %d C" % val_1) # Affichage de la température dans le terminal

    apin = adc.channel(pin=config.capteur_2)
    val = apin()
    val_21 = 66880/val

    val = apin()
    val_22 = 66880/val

    val = apin()
    val_23 = 66880/val
    time.sleep(1)
    val = apin()
    val_24 = 58000/val

    val = apin()
    val_25 = 58000/val

    val = apin()
    val_26 = 58000/val
    val_2 = (val_21+val_22+val_23+val_24+val_25+val_26)/6
    print("Temperature C2: %d C" % val_2)

    apin = adc.channel(pin=config.capteur_3)
    val = apin()
    val_31 = 60000/val

    val = apin()
    val_32 = 60000/val

    val = apin()
    val_33 = 60000/val
    time.sleep(1)
    val = apin()
    val_34 = 60000/val

    val = apin()
    val_35 = 60000/val

    val = apin()
    val_36 = 60000/val
    val_3 = (val_31+val_32+val_33+val_34+val_35+val_36)/6
    print("Temperature C3: %d C" % val_3)

    apin = adc.channel(pin=config.capteur_4)
    val = apin()
    val_41 = 83000/val

    val = apin()
    val_42 = 83000/val

    val = apin()
    val_43 = 83000/val
    time.sleep(1)
    val = apin()
    val_44 = 83000/val

    val = apin()
    val_45 = 83000/val

    val = apin()
    val_46 = 83000/val
    val_4 = (val_41+val_42+val_43+val_44+val_45+val_46)/6
    print("Temperature C4: %d C" % val_4)

    apin = adc.channel(pin=config.capteur_5)
    val = apin()
    val_51 = 65000/val

    val = apin()
    val_52 = 65000/val

    val = apin()
    val_53 = 65000/val
    time.sleep(1)
    val = apin()
    val_54 = 65000/val

    val = apin()
    val_55 = 67300/val

    val = apin()
    val_56 = 65000/val
    val_5 = (val_51+val_52+val_53+val_54+val_55+val_56)/6
    print("Temperature C5: %d C" % val_5)

    """ INSERER LE BLOC 1 ICI """

    # Fonction mathématique qui va convertir la température des capteurs en signaL-
    #-lumineux de couleur (Variation de rouge et de bleu pour symboliser le chaud et le froid)

    led_rouge_1 = mathe.translate(val_1,config.leftMin,config.leftMax,0,255)
    led_bleu_1 = 255 - led_rouge_1

    led_rouge_2 = mathe.translate(val_2,config.leftMin,config.leftMax,0,255)
    led_bleu_2 = 255 - led_rouge_2

    led_rouge_3 = mathe.translate(val_3,config.leftMin,config.leftMax,0,255)
    led_bleu_3 = 255 - led_rouge_3

    led_rouge_4 = mathe.translate(val_4,config.leftMin,config.leftMax,0,255)
    led_bleu_4 = 255 - led_rouge_4

    led_rouge_5 = mathe.translate(val_5,config.leftMin,config.leftMax,0,255)
    led_bleu_5 = 255 - led_rouge_5


    avg = (val_1 + val_2 + val_3 + val_4 + val_5)/5

    print("Temperature moyenne: %d C" % avg)


    """ INSERER LE BLOC 2 ICI """

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
        #INSERER LE BLOC 3 ICI
        ]
    chain.show(data)

    if wlan.isconnected():
        print("Envoi vers MySQL...")
        bloc=0
        bloc=bloc+1
        ## Requête HTTP qui va récuperer les données des capteurs et les envoyer vers le script write_data.php pour les inserer dans la base de données
        mathe.requete(config.host,val_1,avg,bloc)
        bloc=bloc+1
        mathe.requete(config.host,val_2,avg,bloc)
        bloc=bloc+1
        mathe.requete(config.host,val_3,avg,bloc)
        bloc=bloc+1
        mathe.requete(config.host,val_4,avg,bloc)
        bloc=bloc+1
        mathe.requete(config.host,val_5,avg,bloc)
        """ INSERER LE BLOC 4 ICI """
#config.delay
        time.sleep(config.delay) # Pause de X temp entre chaques mesures (en secondes)
    else:

        time.sleep(config.delay) # Pause de X temp entre chaques mesures (en secondes)
