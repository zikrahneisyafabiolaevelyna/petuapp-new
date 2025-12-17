from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.metrics import sp, dp
from datetime import datetime



class PersegiPanjangScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ROOT
        root = FloatLayout()

        # BACKGROUND
        with root.canvas.before:
            self.bg = Rectangle(
                source="bg_persegipanjang.jpg",
                pos=root.pos,
                size=root.size
            )

        root.bind(size=self.update_bg, pos=self.update_bg)

        # LAYOUT UTAMA
        layout = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(10),
            size_hint=(1, 1)
        )

        # JUDUL
        layout.add_widget(Label(
            text="HITUNG LUAS PERSEGI PANJANG",
            font_name="MondayTuesdayDemo.otf",
            font_size=sp(30),
            color=(0.56, 0.49, 0.76, 1),
            size_hint_y=0.1,
            height=dp(60), 
            halign="center",
            valign="middle"
        ))

        # GAMBAR
        layout.add_widget(Image(
            source="persegipanjang.png",
            height=dp(300),
            allow_stretch=True,
            keep_ratio=True
        ))

        # RUMUS 
        layout.add_widget(Label(
            text="Rumus: panjang × lebar",
            font_name="Blustrue.otf",
            font_size=sp(15),
            color=(0, 0, 0, 1),
            size_hint_y=0.15,
            height=dp(30),
            halign="center"
        ))

        # INPUT
        self.inputPanjang = TextInput(
            hint_text="panjang (p)",
            font_name="AksaraKomik-Regular.otf",
            multiline=False,
            input_filter="float",
            size_hint=(0.25, 0.14),
            font_size=(sp(15)),
            padding=(dp(10),dp(6)),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        layout.add_widget(self.inputPanjang)

        self.inputLebar = TextInput(
            hint_text="lebar (l)",
            font_name="AksaraKomik-Regular.otf",
            multiline=False,
            input_filter="float",
            size_hint=(0.25, 0.14),
            font_size=(sp(15)),
            padding=(dp(10),dp(6)),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        layout.add_widget(self.inputLebar)


        # TOMBOL HITUNG
        btn_hitung = Button(
            text="Hitung Luas",
            font_name="Voyage Rush.otf",
            size_hint=(0.2, 0.14),
            font_size=(sp(15)),
            padding=(dp(10),dp(6)),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        btn_hitung.bind(on_press=self.hitung_luas)
        layout.add_widget(btn_hitung)

        # TOMBOL CLEAR
        btn_clear = Button(
            text="CLEAR",
            font_name="Voyage Rush.otf",
           size_hint=(0.2, 0.14),
            font_size=(sp(15)),
            padding=(dp(10),dp(6)),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        btn_clear.bind(on_press=self.clear)
        layout.add_widget(btn_clear)

        # HASIL
        self.label_hasil = TextInput(
            hint_text="Luas akan muncul di sini",
            multiline=False,
            readonly=True,
            size_hint=(0.3, 0.14),
            font_size=(sp(15)),
            padding=(dp(10),dp(6)),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            background_color=(1, 1, 0.9, 1)
        )
        self.label_hasil.bind(
            size=lambda *x: setattr(self.label_hasil, "text_size", self.label_hasil.size)
        )
        layout.add_widget(self.label_hasil)

        root.add_widget(layout)

        # TOMBOL BACK
        btn_back = Button(
            text="BACK",
            font_name="Voyage Rush.otf",
            color=(0, 0, 0, 1),
            size_hint=(None, None),
            size=(dp(120), dp(50)),
            background_color=(0.56, 0.49, 0.76, 1),
            background_normal="",
            background_down="",
            pos_hint={"right": 0.95, "y": 0.05}
        )
        btn_back.bind(on_release=lambda x: setattr(self.manager, "current", "menu"))
        root.add_widget(btn_back)

        self.add_widget(root)

    # UPDATE BACKGROUND
    def update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    # HITUNG LUAS
    def hitung_luas(self, instance):
        try:
            p = float(self.inputPanjang.text)
            l = float(self.inputLebar.text)
            luas = p * l
            self.label_hasil.text = f"Luas Persegi Panjang: {luas:.2f}"
            self.label_hasil.color = (0, 0, 0, 1)

            self.simpan_data(p, l, luas)
            
        except ValueError:
            self.label_hasil.text = "Input harus angka!"
            self.label_hasil.color = (1, 0, 0, 1)

    # CLEAR
    def clear(self, instance):
        self.inputPanjang.text = ""
        self.inputLebar.text = ""
        self.label_hasil.text = "Luas akan muncul di sini"
        self.label_hasil.color = (0, 0, 0, 1)

    def simpan_data(self, p, l, luas):
        waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open("data_bangundatar.txt", "a", encoding="utf-8") as file:
            file.write(
                f"{waktu} | p={p} | l={l}  | luas={luas}\n"
            )