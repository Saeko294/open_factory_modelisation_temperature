def translate(sensor_val, in_from, in_to, out_from, out_to):

    out_range = out_to - out_from
    in_range = in_to - in_from
    in_val = sensor_val - in_from
    val=(float(in_val)/in_range)*out_range
    out_val = out_from+val

    return out_val

def requete(adress,val,bloc):
    import urequest
    urequest.request("GET","https://{ip}/write_data.php?value={id_boite}&value_2={temp}".format(ip=adress,id_boite=bloc,temp=val),None)
    bloc=bloc+1
