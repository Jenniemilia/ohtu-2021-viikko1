import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_konstruktori_ei_voi_luoda_negatiivista_varastoa(self):
        uusi_varasto = Varasto(-10)
        self.assertEqual(uusi_varasto.tilavuus, 0)

    def test_konstruktori_ei_voi_luoda_negatiivista_saldoa(self):
        uusi_varasto = Varasto(8, -10)
        self.assertEqual(uusi_varasto.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_ei_voi_lisata_negatiivista_saldoa(self):
        self.varasto.lisaa_varastoon(-6)
        self.assertEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ei_voi_lisata_enempaa_kuin_on_tilaa(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
        self.assertEqual(self.varasto.tilavuus, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_varastosta_ei_voi_ottaa_enempaa_kuin_saldo(self):
        otetaan = self.varasto.ota_varastosta(15)
        maksimimaara = self.varasto.saldo
        self.assertEqual(otetaan, maksimimaara)
        
    def test_varastosta_ei_voi_ottaa_mitaan_jos_saldo_nolla(self):   
        uusi_varasto = Varasto(0)
        self.varasto.ota_varastosta(-5)
        self.assertEqual(uusi_varasto.saldo, 0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    
    def tulostus_toimii_oikein(self):
        saldo = self.varasto.saldo
        kapasiteetti = self.varasto.paljonko_mahtuu()
        tulostus = f"saldo = {saldo}, vielä tilaa = {kapasiteetti}")
        vastaus = str(self.varasto)
        self.assertEqual(vastaus, tulostus)
