```mermaid
graph TD
    A([Inicio]) --> B[Definir parámetros: z1, z2, modulo]
    B --> C[Instanciar EngranajeConico]
    C --> D[Llamar método calcular_geometria]
    
    subgraph Proceso de Cálculo
    D --> E[Calcular Relación Transmision i = z2 / z1]
    E --> F[Calcular ángulos gamma1 y gamma2 usando atan]
    F --> G[Calcular diámetros d1 y d2]
    end
    
    G --> H[Retornar diccionario de resultados]
    H --> I[Convertir radianes a grados]
    I --> J[/Imprimir Resultados en Consola/]
    J --> K([Fin])
