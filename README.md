# LAN Scanner - Python

Escáner de red local rápido, multithread y compatible con Windows.  
Detecta dispositivos activos en la red, mostrando:

- IP  
- MAC  
- Nombre del dispositivo (hostname o NetBIOS)  
- Fabricante aproximado por MAC

---

## ⚡ Características

- Escaneo de red completo (192.168.1.0/24 por defecto)  
- Multithreading para rapidez (hasta 50 hilos simultáneos)  
- Evita duplicados y mantiene la salida limpia  
- Funciona completamente en Windows  
- Lookup de fabricante por OUI (local o web)

---

## 💻 Requisitos

- Python 3.10+  
- Windows (revisar compatibilidad con ping y ARP)  

---

## 🚀 Uso

Clonar el repositorio y ejecutar:

```bash
python netscan.py
```


## Licencia

Este proyecto está bajo la [MIT License](LICENSE).
