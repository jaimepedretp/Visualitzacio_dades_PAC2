from arcplot import ArcDiagram

nodes = [
    "aa21623129",
    "ahorapodemos",
    "anap1958",
    "ancorlan",
    "antoniobb1953",
    "AntParra",
    "BlaancaNiieves",
    "boye_g",
    "cc9d4e5f3cf34f8",
    "CiudadanosCs",
    "Clare1959",
    "Cs_LaCanonja",
    "CsMAljarafe",
    "CsSantaEularia",
    "diana_alforja",
    "DuroBelinda",
    "Enedina37049621",
    "espartano533",
    "gpscongreso",
    "joluga68",
    "kafkanario",
    "mtgarcia82",
    "Nacho_JISF",
    "Pablo_Iglesias_",
    "pasandoeldia1",
    "PedroMiretBetan",
    "PozoJulian",
    "PSOE",
    "RobertoVegaRam2",
    "sanchezcastejon",
    "socialistes_cat",
    "Tersenn",
    "vegaparrilla",
    "vickycb65",
    "vox_es",
    "WillyLozano",
]

title = "Retweets arc diagram - who is retweeten whom?"
arc_diagram = ArcDiagram(nodes, title)
custom_colors = [
    "#386641",
    "#f2e8cf",
    "#8b3422",
    "#6f7714",
    "#ff9b54",
    "#e2d9c5",
    "#9a8237",
    "#dbab85",
    "#d64620",
    "#f6bd60",
    "#283618",
    "#a98467",
]
#arc_diagram.set_custom_colors(custom_colors)
arc_diagram.set_background_color("#262522")
arc_diagram.set_label_rotation_degree(90)

arc_diagram.connect("DuroBelinda","BlaancaNiieves",8)
arc_diagram.connect("pasandoeldia1","pasandoeldia1",6)
arc_diagram.connect("Tersenn","Tersenn",4)
arc_diagram.connect("Enedina37049621","PSOE",4)
arc_diagram.connect("Clare1959","PSOE",4)
arc_diagram.connect("espartano533","vox_es",4)
arc_diagram.connect("CsSantaEularia","CiudadanosCs",4)
arc_diagram.connect("diana_alforja","socialistes_cat",4)
arc_diagram.connect("vegaparrilla","PSOE",4)
arc_diagram.connect("gpscongreso","PSOE",3)
arc_diagram.connect("ancorlan","Pablo_Iglesias_",3)
arc_diagram.connect("aa21623129","vox_es",3)
arc_diagram.connect("PozoJulian","ahorapodemos",3)
arc_diagram.connect("AntParra","sanchezcastejon",3)
arc_diagram.connect("RobertoVegaRam2","ahorapodemos",3)
arc_diagram.connect("antoniobb1953","PSOE",3)
arc_diagram.connect("WillyLozano","PSOE",3)
arc_diagram.connect("PedroMiretBetan","CiudadanosCs",3)
arc_diagram.connect("Nacho_JISF","mtgarcia82",3)
arc_diagram.connect("kafkanario","ahorapodemos",3)
arc_diagram.connect("anap1958","PSOE",3)
arc_diagram.connect("CsMAljarafe","CiudadanosCs",10)
arc_diagram.connect("Cs_LaCanonja","CiudadanosCs",10)
arc_diagram.connect("joluga68","CiudadanosCs",3)
arc_diagram.connect("vickycb65","boye_g",3)
arc_diagram.connect("cc9d4e5f3cf34f8","vox_es",3)


arc_diagram.show_plot()