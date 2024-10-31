import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_ei_ole_nolla_tai_negatiivinen(self):
        varasto = Varasto(0)

        self.assertAlmostEqual(varasto.tilavuus, 0.0)

    def test_uuden_varaston_saldo_ei_ole_negatiivinen(self):
        varasto = Varasto(10, -1)

        self.assertAlmostEqual(varasto.saldo, 0.0)

    def test_uuden_varaston_ylisuuri_alkusaldo_ei_ylita_tilavuutta(self):
        varasto = Varasto(10, 11)

        self.assertAlmostEqual(varasto.saldo, 10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varaston_maximitilavuus_ei_ylity(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivinen_ottaminen_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(saatu_maara, 0.0)

    def test_saldon_ylittava_ottaminen_antaa_kaiken(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(6)

        self.assertAlmostEqual(saatu_maara, 5)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tulostus_nayttaa_oikeat_maarat(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = -1, vielä tilaa 10")
