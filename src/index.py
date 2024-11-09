from varasto import Varasto

def tulosta_varastotila(varasto, nimi):
    print(f"{nimi}: {varasto}")

def testaa_getterit(varasto):
    print("Olut getterit:")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")

def testaa_mehuvaraston_setterit(varasto):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    varasto.lisaa_varastoon(50.7)
    tulosta_varastotila(varasto, "Mehuvarasto")
    print("Otetaan 3.14")
    varasto.ota_varastosta(3.14)
    tulosta_varastotila(varasto, "Mehuvarasto")

def testaa_virhetilanteet():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)
    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def testaa_olutvaraston_lisays_ja_otto(varasto):
    print("olutta.lisaa_varastoon(1000.0)")
    varasto.lisaa_varastoon(1000.0)
    tulosta_varastotila(varasto, "Olutvarasto")

    print("olutta.ota_varastosta(1000.0)")
    saatiin = varasto.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    tulosta_varastotila(varasto, "Olutvarasto")

def testaa_mehuvaraston_virheellinen_otto(varasto):
    print("mehua.lisaa_varastoon(-666.0)")
    varasto.lisaa_varastoon(-666.0)
    tulosta_varastotila(varasto, "Mehuvarasto")

    print("mehua.otaVarastosta(-32.9)")
    saatiin = varasto.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    tulosta_varastotila(varasto, "Mehuvarasto")

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    tulosta_varastotila(mehua, "Mehuvarasto")
    tulosta_varastotila(olutta, "Olutvarasto")

    testaa_getterit(olutta)
    testaa_mehuvaraston_setterit(mehua)
    testaa_virhetilanteet()
    testaa_olutvaraston_lisays_ja_otto(olutta)
    testaa_mehuvaraston_virheellinen_otto(mehua)

if __name__ == "__main__":
    main()
