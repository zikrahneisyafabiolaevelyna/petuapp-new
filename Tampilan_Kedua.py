from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.metrics import dp, sp
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class ImageButton(ButtonBehavior, Image):
    pass


class TampilanMenuapp(Screen):

    def tekan_trapesium(self, *args):
        self.manager.current = "TrapesiumScreen"

    def tekan_persegi(self, *args):
        self.manager.current = "PersegiScreen"

    def tekan_segitiga(self, *args):
        self.manager.current = "SegitigaScreen"

    def tekan_persegipanjang(self, *args):
        self.manager.current = "PersegiPanjangScreen"

    def tekan_layanglayang(self, *args):
        self.manager.current = "LayangLayangScreen"

    def tekan_lingkaran(self, *args):
        self.manager.current = "LingkaranScreen"

    def tekan_belahketupat(self, *args):
        self.manager.current = "BelahKetupatScreen"

    def tekan_jajargenjang(self, *args):
        self.manager.current = "JajarGenjangScreen"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(20)
        )

        # JUDUL
        judul1 = Label(
                text="Pilih Bangun Datar",
                font_size=sp(50),
                font_name="MondayTuesdayDEMO.otf",
                color=(1, 0.41, 0.71, 1),
                size_hint_y=0.15
            )
        layout.add_widget(judul1)

        # GRID MENU
        grid = GridLayout(
            cols=4,
            spacing=dp(30),
            padding=dp(20),
            size_hint_y=0.7
        )

        icons = [
            ("persegi.png", self.tekan_persegi),
            ("persegipanjang.png", self.tekan_persegipanjang),
            ("segitiga.png", self.tekan_segitiga),
            ("trapesium.png", self.tekan_trapesium),
            ("layanglayang.png", self.tekan_layanglayang),
            ("lingkaran.png", self.tekan_lingkaran),
            ("belahketupat.png", self.tekan_belahketupat),
            ("jajargenjang.png", self.tekan_jajargenjang),
        ]

        for img, action in icons:
            btn = ImageButton(
                source=img,
                size_hint=(1, 1),
                allow_stretch=True,
                keep_ratio=True
            )
            if action:
                btn.bind(on_press=action)
            grid.add_widget(btn)

        layout.add_widget(grid)

        # TOMBOL BACK
        layout.add_widget(
            Button(
                text="BACK",
                font_size=sp(16),
                font_name= "Voyage Rush.otf",
                size_hint = (None, None),
                size=(dp(120), dp(45)),
                pos_hint={"right": 0.98, "y":0.02},
                background_color= (1, 1, 1, 1),
                background_down="",
                background_normal="",
                color=(0,0,0,1),
                on_release=lambda x: setattr(self.manager, "current", "awal")
            )
        )

        self.add_widget(layout)