# TFG: Control de centros de datos multitenant mediante SDN

## Autor
Alejandro García Bautista

## Descripción

Este proyecto implementa y compara dos arquitecturas para el control de centros de datos multitenant:

- **SDN con OpenFlow** (Mininet + Ryu)
- **BGP EVPN** (Containerlab + FRR + Ansible)

## Estructura del proyecto

- **SDN/**
  - `Scripts_mininet/`: Script de creación de Topología en Mininet.
  - `Scripts_Ryu/`: Programa controlador Ryu, utilidades y configuración de políticas.
- **BGP-EVPN/**
  - `topology.yml`: Script de topología para Containerlab.
  - `playbooks/`: Playbooks de Ansible para automatización de la configuración de red.
  - `inventory/`: Inventarios de Ansible.
  - `network_testing.py`: Script para pruebas de red y generación de tráfico.
  - `delay_adder.py`: Script para añadir retardo a los enlaces.
- **resultados/**
  - En este directorio se encuentran los resultados obtenidos con diferentes delays, así como scripts para obtener los resultados en un formato más claro.

## Ejecución

### SDN (Mininet + Ryu)

1. Levanta el controlador Ryu con los scripts en `SDN/Scripts_Ryu/`.
    ```sh
    ryu-manager --observe-links TopologyManager.py RoutingManager.py
    ```
2. Lanza la topología Mininet:
   ```sh
   python3 SDN/Scripts_mininet/topology.py
   ```

### BGP EVPN (Containerlab + FRR + Ansible)

1. Despliega la topología con Containerlab:
   ```sh
   containerlab deploy -t BGP-EVPN/topology.yml
   ```

2. Entrar el contenedor Ansible para poder ejecutar los playbooks de Ansible:
    ```sh
    docker exec -it clab-tfg-frr-ansible-ansible bash
    ```


### Procesado de resultados

Guardar los resultados en un directorio y ejecutar los siguientes scripts:
```sh
python3 extract.py
python3 result_calculator.py
```

## Requisitos

- Python 3.9
- Mininet
- Ryu
- Containerlab
- Docker
