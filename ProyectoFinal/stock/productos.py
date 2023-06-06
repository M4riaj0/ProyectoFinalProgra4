import sys
import os
path = os.path.abspath('Model/')
sys.path.append(path)
import control_plagas
import fertilizantes
import antibioticos

def generar_productos():
    ListProductos = []

    ListProductos.append(control_plagas.ControlPlagas("1474", "TROMPA Hormiguicida", "15 dias" , "28600" , "2 años"))
    ListProductos.append(control_plagas.ControlPlagas("1557", "RIDOMIL Fungicida", "7 dias" , "28200" , "1 año"))
    ListProductos.append(control_plagas.ControlPlagas("1623", "FULLNEEM Plagicida", "30 dias" , "49990" , "3 años"))

    ListProductos.append(fertilizantes.Fertilizantes("1322", "ABIMGRA de gallinaza" , "7 dias" , "36824" , "5/12/2024"))
    ListProductos.append(fertilizantes.Fertilizantes("1525", "UREA GRANULAR" , "20 dias" , "60400" , "5/07/2025"))
    ListProductos.append(fertilizantes.Fertilizantes("1738", "FOSFORITA HUILA" , "40 dias" , "36824" , "5/01/2026"))

    ListProductos.append(antibioticos.Antibioticos("1345", "BENZATINICA" , "20" , "bovino", "45000"))
    ListProductos.append(antibioticos.Antibioticos("1678", "DRAXXIN" , "10" , "porcino", "45000"))
    ListProductos.append(antibioticos.Antibioticos("1634", "ROSTRUM" , "15" , "caprino" , "32200"))
    ListProductos.append(antibioticos.Antibioticos("1346", "AMOXIDEX" , "5" , "caprinos" , "25400"))

    return ListProductos