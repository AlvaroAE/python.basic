import random
import pandas as pd
import matplotlib.pyplot as plt

num=random.sample(range(1,100))
num.sort()
print(num)


frase=input('pon una frase ')
letra=input('pon que letra quieres ver ')
print(f'la frase tiene {frase.count(letra)}')

def csv():
    datos=pd.read_csv("C:\\Users\\Tecnicos\\Desktop\\Alvaro\\programacion")
    df=datos[["m3_registrats","núm_clients"]]

    df = datos.rename(columns={
        "m3_registrats": "m3",
        "núm_clients": "clientes",
    })

    df.RIO_CHARLES.value_counts().plot.pie()
    plt.show()
csv()