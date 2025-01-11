import flet as ft

class Program(ft.Container):
    def __init__(self,page):
        super().__init__()
        self.page = page
        self.page.title = "Sistema de cajas"
        self.page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }
        #Tema del programa
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.iconoTema = ft.IconButton(
            icon=ft.icons.DARK_MODE,
            tooltip="Cambiar tema",
            on_click= self.cambiarTema
        )
        self.appBar = ft.AppBar(
            title= ft.Text("Manejo y gestion de sucursal", font_family= "RobotoSLab"),
            center_title=True,
            bgcolor= ft.colors.SURFACE_VARIANT,
            actions=[self.iconoTema],
            leading= ft.PopupMenuButton(
                items= [
                    ft.PopupMenuButton(ft.Row(controls=[
                        ft.Text("Configuracion"),
                        ft.Icon(ft.Icons.SETTINGS)
                    ])),
                    ft.PopupMenuButton(ft.Row(controls=[
                        ft.Text("Ayuda"),
                        ft.Icon(ft.Icons.HELP_CENTER)
                    ]))
                ]
            )
        ) 
        #Variables de dropdown y dropdown 
        self.option1 = ft.dropdown.Option("Cachete")
        self.option2 = ft.dropdown.Option("Tripa")
        self.option3 = ft.dropdown.Option("Bofe")
        self.dropdown = ft.Dropdown(
            label="Producto",
            width=150,
            options= [
                self.option1, self.option2, self.option3
                ],border_color= ft.colors.SURFACE_VARIANT
            )

        #Variable gramos a comprar
        self.gramos = ft.TextField(label="Gramos a comprar", width= 200, border_color=ft.colors.SURFACE_VARIANT)
        
        self.contenedor = ft.Container(height=10)

        self.main = ft.Column(
            controls= [
            #Primer campo: GRAMOS A COMPRAR
            ft.Row(controls=[
                self.gramos
            ], alignment=ft.MainAxisAlignment.CENTER),     
                #Segundo campo  
                ft.Row(controls=[
                    self.dropdown,
                ft.ElevatedButton("Enviar", on_click=self.Cobrar)
            ], spacing= 15,alignment=ft.MainAxisAlignment.CENTER)
        ], spacing=20)

        self.page.add(self.appBar, self.contenedor, self.main)
    def Cobrar(self,e):
        self.opcion_escogida = self.dropdown.value
        self.gramos_comprar = int(self.gramos.value)
        
        if self.opcion_escogida == "Cachete":
            self.valor_cachete = 269
            self.precio = (self.valor_cachete * self.gramos_comprar) / 1000
 
        elif self.opcion_escogida == "Tripa":
            self.valor_tripa = 320
            self.precio = (self.valor_tripa * self.gramos_comprar) / 1000

        elif self.opcion_escogida == "Bofe":
            self.valor_bofe = 160
            self.precio = (self.valor_bofe * self.gramos_comprar) / 1000
    
        self.espaciado = ft.Container(height=10)

        self.cobro = ft.Row(controls=[
            ft.Container(
                content=ft.Text(f"Monto a cobrar al cliente: {self.precio}"),
                width=300,
                height=35,
                border_radius=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.SURFACE_VARIANT,     
            )
        ], alignment=ft.MainAxisAlignment.CENTER)

        self.campo_pagar = ft.TextField(hint_text="Pagar", width=200)
        self.pagar = ft.Column(
            controls=[
                ft.Row(controls=[
                   self.campo_pagar, 
                   ft.OutlinedButton("Listo", on_click=self.Cambio)
                ],alignment=ft.MainAxisAlignment.CENTER)
            ])
        self.page.add(self.cobro,self.pagar)
    
    def Cambio(self,e):
        self.pagar = int(self.campo_pagar.value)
        self.cambio =  self.pagar - self.precio

        self.pantalla_cambio = ft.Column(controls=[
            ft.Row(controls=[
                ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Ticket")),
                        ft.DataColumn(ft.Text("Informacion"))
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("Gramos comprados")),
                                ft.DataCell(ft.Text(self.gramos_comprar))
                            ]
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("Producto")),
                                ft.DataCell(ft.Text(self.opcion_escogida))
                            ]
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(f"Cobro: {self.precio}")),
                                ft.DataCell(ft.Text(f"Cambio: {self.cambio}"))
                            ]
                        )
                    ]
                ),
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[
                ft.OutlinedButton("Imprimir"),
                ft.OutlinedButton("Regresar", on_click= lambda e: self.page.close()) 
            ], alignment=ft.MainAxisAlignment.CENTER)
        ])

        self.page.add(ft.Container(height=10), self.pantalla_cambio)
    
    def cambiarTema(self, e):  
        self.page.theme_mode = ft.ThemeMode.LIGHT if self.page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        self.iconoTema.icon = ft.icons.DARK_MODE if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.LIGHT_MODE
        self.page.update() 
ft.app(target=Program)