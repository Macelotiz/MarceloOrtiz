# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 78},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 91}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 84},
            {"day": "Jueves", "temp": 85},
            {"day": "Viernes", "temp": 82},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 90}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 79},
            {"day": "Martes", "temp": 83},
            {"day": "Miércoles", "temp": 81},
            {"day": "Jueves", "temp": 85},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 93},
            {"day": "Domingo", "temp": 94}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 77},
            {"day": "Miércoles", "temp": 81},
            {"day": "Jueves", "temp": 78},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 92}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 60},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 80},
            {"day": "Viernes", "temp": 70},
            {"day": "Sábado", "temp": 71},
            {"day": "Domingo", "temp": 78}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 72},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 78},
            {"day": "Viernes", "temp": 71},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 85}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 82},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 67},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 77},
            {"day": "Sábado", "temp": 73},
            {"day": "Domingo", "temp": 85}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 74},
            {"day": "Martes", "temp": 87},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 73},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 71},
            {"day": "Domingo", "temp": 84}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 82},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 81},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 84}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 82},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 94},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 91}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")
