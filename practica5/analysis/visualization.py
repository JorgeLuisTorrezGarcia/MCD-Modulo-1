import matplotlib.pyplot as plt
import pandas as pd

def plot_salaries(df, filename='salary_plot.png'):
    """Genera un gráfico de barras de los salarios y lo guarda en un archivo."""
    plt.figure(figsize=(10, 6))
    plt.bar(df.index, df['salario'], color='skyblue')
    plt.xlabel('ID de Empleado')
    plt.ylabel('Salario')
    plt.title('Salarios de los Empleados')
    plt.xticks(df.index)
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Gráfico guardado como {filename}")

def plot_ages(df, filename='age_plot.png'):
    """Genera un gráfico de barras de las edades y lo guarda en un archivo."""
    plt.figure(figsize=(10, 6))
    plt.bar(df.index, df['edad'], color='lightgreen')
    plt.xlabel('ID de Empleado')
    plt.ylabel('Edad')
    plt.title('Edades de los Empleados')
    plt.xticks(df.index)
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Gráfico guardado como {filename}")
