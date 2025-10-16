import sqlite3

DATABASE = 'spish.db'

vocab = "el supermercado=supermarket+por supuesto=of course+tal=such+la talla=clothing size+también=also/too+tampoco=neither+tan, tanto=so, so much+las tapas=tapas+la tarde=afternoon+la tarea=homework, task+la tarjeta=card+el té=tea+el teatro=theatre+el techo=ceiling, roof+el tema=theme+temprano=early+tener (*)=to have+tener que (*)=to have to+tener ganas (*)=to want to+tener hambre (*)=to be hungry+tener miedo (*)=to be scared+tener prisa (*)=to be in a hurry+tener razón (*)=to be right+tener sed (*)=to be thirsty+tener sueño (*)=to be tired+terminar=to finish+la terraza=terrace+el tiempo=time, weather+la tienda=shop+la tierra=earth+el tío=uncle+el tipo=guy, type+tirar=to throw+la toalla=towel+tocar=to get, play, touch+todavía=still+todo=all+todo el mundo=everyone+tomar=to take+tomar una copa=to have a drink+tonto=stupid+la tormenta=storm+el toro=bull+la tortilla española=Spanish omelet+Toser=to cough+la tostada=toast+trabajar=to work+el trabajo=job+traer (traigo)=to bring+el traje=suit+tranquilo=chill, quiet+el tren=train+triste=sad+el turista=tourist+último=last, latest+único=only+la universidad=university+útil=useful+utilizar=to use+la uva=grape+la vaca=cow+las vacaciones=holidays+valer la pena=to be worthwhile+valer=to be worth+los vaqueros=jeans+varios=several+el vecino=neighbor+la vela=candle, sailing+el vendedor=sales person+vender=to sell+venir (*)=to come+la ventana=window+ver (*)=to see, watch+el verano=summer+la verdad=truth+verde=green+las verduras=vegetables+el vestido=dress+vestirse (i) (r)=to get dressed+la vez=occasion, time+a la vez=at the same time+de vez en cuando=from time to time+dos veces=twice+viajar=to travel+el viaje=trip+la vida=life+viejo=old+el viento=wind+el vino=wine+visitar=to visit+la vista=view+vivir=to live+vivo=alive+el voleibol=volleyball+volver=to return+la voz=voice+el vuelo=flight+la vuelta=return+y=and+ya=already+ya no=no longer+el zapato=shoe+el zumo=juice+a=at, to+a la izquierda de=to the left of+a través de=through+bajo=under (one word)+contra=against+de=from, of+debajo de=under (two words)+delante de=in front of+dentro=inside+desde=from, since+detrás de=behind+en=at, on+encima de=above+enfrente de=in front of, opposite+en medio de=in the middle of+entre=between+fuera de=outside+hacia=towards+hasta=until+para=by (date), for, in order to+por=by (transport/work), for, through+sobre=about (one word)+enero=January+febrero=February+marzo=March+abril=April+mayo=May+junio=June+julio=July+agosto=August+septiembre=September+octubre=October+noviembre=November+diciembre=December+lunes=Monday+martes=Tuesday+miércoles=Wednesday+jueves=Thursday+viernes=Friday+sábado=Saturday+domingo=Sunday"

terms = vocab.split('+')
print(terms[0])

for term in terms:
    spanish,english = term.split('=')
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = f'INSERT INTO table1 (eng, spn) VALUES ("'+ english + '", "' + spanish + '");'
        cursor.execute(sql)
    print('done')
