from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.core.window import Window

from Tampilan_Kedua import TampilanMenuapp
from trapesium import TrapesiumScreen
from persegi import PersegiScreen
from segitiga import SegitigaScreen
from persegipanjang import PersegiPanjangScreen
from layanglayang import LayangLayangScreen
from lingkaran import LingkaranScreen
from belahketupat import BelahKetupatScreen
from jajargenjang import JajarGenjangScreen

Window.clearcolor = (1, 0.96, 0.86, 1)


class ImageButton(ButtonBehavior, Image):
    pass


class HalamanAwal(Screen):
    pass


class PETUapp(App):

    def ganti_ke_menu(self, *args):
        self.manager.current = "menu"

    def build(self):
        self.manager = ScreenManager()

        # =====================
        # HALAMAN AWAL
        # =====================
        awal = HalamanAwal(name="awal")

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(20)
        )

        judul = Label(
            text="Welcome to PETUapp",
            font_name="BACK TO SCHOOL.otf",
            font_size=sp(70),
            color=(1, 0.41, 0.71, 1),
            size_hint_y=0.1,
            height=dp(90),
            halign="center",
            valign="middle"
        )
        judul.bind(size=judul.setter("text_size"))


        image1 = Image(
            source="bg_awal.png",
            size_hint_x=1,
            size_hint_y=0.15,
            height=dp(250),
            allow_stretch=True,
            keep_ratio=True
        )

        tombol_play = ImageButton(
            source="play.png",
            size_hint_x=1,
            size_hint_y=0.1,
            height=dp(180),
            allow_stretch=True,
            keep_ratio=True
        )

        labelby = Label(text= "by : Sains Data Universitas Negeri Surabaya 2025",
                        font_name = "SantaNortPole.otf",
                        color=(1, 0.41, 0.71, 1),
                        size_hint=(None, None),
                        size=(dp(120), dp(50)),
                        pos_hint={"right": 0.9, "y": 0}
                        )
                        
        
        tombol_play.bind(on_press=self.ganti_ke_menu)

        layout.add_widget(judul)
        layout.add_widget(image1)
        layout.add_widget(tombol_play)
        layout.add_widget(labelby)

        awal.add_widget(layout)

        # =====================
        # SCREEN LAIN
        # =====================
        menu = TampilanMenuapp(name="menu")
        trapesium = TrapesiumScreen(name="TrapesiumScreen")
        persegi = PersegiScreen(name="PersegiScreen")
        segitiga = SegitigaScreen(name="SegitigaScreen")
        persegipanjang = PersegiPanjangScreen(name="PersegiPanjangScreen")
        layanglayang = LayangLayangScreen(name="LayangLayangScreen")
        lingkaran = LingkaranScreen(name="LingkaranScreen")
        belahketupat = BelahKetupatScreen(name="BelahKetupatScreen")
        jajargenjang = JajarGenjangScreen(name="JajarGenjangScreen")

        self.manager.add_widget(awal)
        self.manager.add_widget(menu)
        self.manager.add_widget(trapesium)
        self.manager.add_widget(persegi)
        self.manager.add_widget(segitiga)
        self.manager.add_widget(persegipanjang)
        self.manager.add_widget(layanglayang)
        self.manager.add_widget(lingkaran)
        self.manager.add_widget(belahketupat)
        self.manager.add_widget(jajargenjang)

        return self.manager


PETUapp().run()