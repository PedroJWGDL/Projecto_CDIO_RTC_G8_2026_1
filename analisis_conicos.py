import math
    
    def __init__(self, dientes_piñon, dientes_corona, modulo):
        self.z1 = dientes_piñon
        self.z2 = dientes_corona
        self.m = modulo
        
    def calcular_geometria(self):
        # Relación de transmisión
        i = self.z2 / self.z1
        
        # Ángulos de paso (pitch angles)
        gamma1 = math.atan(self.z1 / self.z2)
        gamma2 = math.atan(self.z2 / self.z1)
        
        # Diámetros primitivos
        d1 = self.m * self.z1
        d2 = self.m * self.z2
        
        return {
            "relacion_transmision": round(i, 3),
            "angulo_pinhon_rad": round(gamma1, 4),
            "angulo_corona_rad": round(gamma2, 4),
            "diametro_pinhon": d1,
            "diametro_corona": d2
        }

# Ejemplo de uso
if __name__ == "__main__":
    pipñon = 20
    corona = 60
    modulo = 3
    
    analisis = EngranajeConico(piñon, corona, modulo)
    resultados = analisis.calcular_geometria()
    
    print(f"--- Análisis de Engranajes Cónicos (m={modulo}) ---")
    print(f"Relación de transmisión: {resultados['relacion_transmision']}:1")
    print(f"Diámetro primitivo piñón: {resultados['diametro_pinhon']} mm")
    print(f"Diámetro primitivo corona: {resultados['diametro_corona']} mm")
    print(f"Ángulo de paso piñón: {math.degrees(resultados['angulo_pinhon_rad']):.2f}°")
