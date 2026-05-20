import math
    
    def __init__(self, dientes_piñon, dientes_corona, modulo):
        self.z1 = dientes_piñon
        self.z2 = dientes_corona
        self.m = modulo
        
    def calcular_geometria(self):

        i = self.z2 / self.z1
        
        gamma1 = math.atan(self.z1 / self.z2)
        gamma2 = math.atan(self.z2 / self.z1)
        
        d1 = self.m * self.z1
        d2 = self.m * self.z2
        
        return {
            "relacion_transmision": round(i, 3),
            "angulo_piñon_rad": round(gamma1, 4),
            "angulo_corona_rad": round(gamma2, 4),
            "diametro_piñon": d1,
            "diametro_corona": d2
        }

if nombre == "main":
    piñon = 20
    corona = 60
    modulo = 3
    
    analisis = EngranajeConico(piñon, corona, modulo)
    resultados = analisis.calcular_geometria()
    
    print(f"--- Análisis de Engranajes Cónicos (m={modulo}) ---")
    print(f"Relación de transmisión: {resultados['relacion_transmision']}:1")
    print(f"Diámetro primitivo piñón: {resultados['diametro_piñon']} mm")
    print(f"Diámetro primitivo corona: {resultados['diametro_corona']} mm")
    print(f"Ángulo de paso piñón: {math.degrees(resultados['angulo_piñon_rad']):.2f}°")
