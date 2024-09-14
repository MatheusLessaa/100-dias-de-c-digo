import pandas as pd
import numpy as np

data = {
    'nome': ['Júlia', 'Matheus', 'Bruno', 'Maison', 'Augusto', 'Jão'],
    'departamento': ['TI', 'SS', 'Finaceiro', 'TI', 'RH', 'TI'],
    'salario': [7000, 6000, 5000, 4000, 5000, 6000] }

df = pd.DataFrame(data)

funcionarios_ti = df[df['departamento'] == 'TI']
print(funcionarios_ti)

media_salarial = funcionarios_ti['salario' ].mean()
print(f"Média salarial dos funcionários de TI: {media_salarial}")