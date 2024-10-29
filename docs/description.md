# Optimización de Rutas para una Flota Heterogénea

## Descripción del Problema

Este problema de optimización de rutas consiste en planificar las rutas de una flota heterogénea de vehículos para satisfacer las órdenes de transporte entre un depósito y varios clientes con el menor costo en términos de distancia recorrida. A continuación, se detallan las características y restricciones del problema:

## Características del Problema

1. **Un Depósito y Múltiples Clientes**:
   - Existe un único depósito desde el cual se inician y finalizan todas las rutas.
   - Varios clientes requieren transporte de mercancías entre ellos y el depósito.

2. **Flota de Vehículos Heterogénea**:
   - La flota consta de vehículos con diferentes capacidades.
   - Cada vehículo tiene una capacidad máxima que no puede ser excedida.

3. **Órdenes de Transporte**:
   - Las órdenes especifican el origen, destino y cantidad de mercancías a transportar.
   - Todas las órdenes deben ser satisfechas, asegurando que cada cliente con una orden asociada sea visitado.

## Restricciones del Problema

1. **Visita Única a Cada Cliente**:
   - Cada cliente debe ser visitado una única vez para satisfacer todas sus órdenes asociadas.

2. **Capacidad del Vehículo**:
   - Ningún vehículo puede exceder su capacidad máxima en ningún momento durante la ruta.

3. **Inicio y Fin en el Depósito**:
   - Todas las rutas deben comenzar y terminar en el depósito.

4. **Órdenes Satisfechas**:
   - Todas las órdenes deben ser cumplidas, asegurando que todos los clientes con órdenes sean atendidos.

## Configuración Parametrizable

Para reflejar las carencias y limitaciones de la empresa, el modelo permite la configuración de si los vehículos pueden realizar múltiples rutas o no. Esto se puede configurar antes de ejecutar el código mediante el parámetro `allow_multiple_routes`.

## Componentes del Modelo

### Clases Principales

- **Depot**: Representa la ubicación del depósito.
- **Client**: Representa la ubicación de cada cliente.
- **Vehicle**: Representa cada vehículo de la flota con su capacidad y ruta asignada.
- **Problem**: Representa el problema de optimización de rutas y contiene la lógica para resolverlo.
- **DataReader**: Encargada de leer la información de las instancias de prueba desde un archivo de texto.
- **Visualizer**: Encargada de visualizar el estado inicial y la solución del problema utilizando Matplotlib.

## Ejecución del Modelo

La ejecución del modelo incluye la lectura de datos de un archivo de instancia, la resolución del problema según las restricciones y la visualización del resultado.

## Detalles del modelo
### 1. **Definición de las clases**:
- Depósito (Depot): El punto inicial y final de todas las rutas.
- Cliente (Client): Los puntos que requieren transporte de mercancías.
- Vehículo (Vehicle): Los medios de transporte con diferentes capacidades.
- Orden (Order): Las solicitudes de transporte, incluyendo el origen, destino y cantidad.

### 2. **Variables de Decisión**:
- Asignación de Vehículos a Rutas: Cada vehículo tendrá asignada una o más rutas.
- Secuencia de Visitas: El orden en que los vehículos visitarán los clientes.

### 3. **Función Objetivo**:
- Minimización de la Distancia Total: Queremos minimizar la distancia total recorrida por todos los vehículos.

### 4. **Restricciones**:
- Capacidad del Vehículo: Ningún vehículo puede exceder su capacidad máxima en ningún momento durante su ruta.
- Visita Única a Cada Cliente: Cada cliente debe ser visitado una única vez por un vehículo.
- Inicio y Fin en el Depósito: Todas las rutas deben comenzar y terminar en el depósito.
- Órdenes Cumplidas: Todas las órdenes de transporte deben ser satisfechas.