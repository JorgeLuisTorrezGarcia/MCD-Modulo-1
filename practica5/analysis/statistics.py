import numpy as np

def calculate_age_statistics(ages):
    """Calcula la media, mínima y máxima edad."""
    ages_np = np.array(ages)
    mean_age = np.mean(ages_np)
    min_age = np.min(ages_np)
    max_age = np.max(ages_np)
    return {
        'media_edad': mean_age,
        'min_edad': min_age,
        'max_edad': max_age
    }

def calculate_salary_statistics(salaries):
    """Calcula la media y desviación estándar de los salarios."""
    salaries_np = np.array(salaries)
    mean_salary = np.mean(salaries_np)
    std_salary = np.std(salaries_np)
    return {
        'media_salario': mean_salary,
        'desviacion_estandar_salario': std_salary
    }