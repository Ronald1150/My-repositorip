import flet as ft
from login import second_page

def main(page: ft.Page):
    # Configuración inicial de la página
    page.title = "Ransa Negocio"
    page.bgcolor = "#FFFFFF"  # Fondo de la página en hexadecimal

    # Crear AppBar con botones personalizados
    page.appbar = ft.AppBar(
        title=ft.Text("Ransa Negocio", color=ft.colors.WHITE),
        bgcolor="#1B5051",  # Fondo de la AppBar
        center_title=False,  # No centrar el título
        actions=[
            ft.TextButton(
                "Iniciar sesión",
                on_click=lambda _: print("Iniciar sesión"),
                style=ft.ButtonStyle(color=ft.colors.WHITE70),
            ),
            ft.TextButton(
                "Contactos",
                on_click=lambda _: print("Contactos"),
                style=ft.ButtonStyle(color=ft.colors.WHITE70),
            ),
            ft.TextButton(
                "Sobre nosotros",
                on_click=lambda _: print("Sobre nosotros"),
                style=ft.ButtonStyle(color=ft.colors.WHITE70),
            ),
        ],
    )

    # Crear contenedor izquierdo con imagen y texto
    left_container = ft.Container(
        content=ft.Row(
            controls=[
                ft.Image(src="Imagene-de-mercado.png", width=700, height=250),
                ft.Column(
                    controls=[
                        ft.Text(
                            "Acuerdos comerciales y financieros",
                            weight=ft.FontWeight.NORMAL,
                            size=20,  # Tamaño de la fuente
                            color=ft.colors.BLACK,  # Color del texto
                            text_align=ft.TextAlign.LEFT,  # Alineación del texto
                        ),
                    ],
                    alignment=ft.CrossAxisAlignment.START,  # Alinear el texto a la izquierda
                    spacing=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,  # Alinear todo el contenido a la izquierda
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.colors.WHITE,
        padding=20,
        border_radius=10,
    )

    # Crear contenedor derecho con imagen y texto
    right_container = ft.Container(
        content=ft.Row(
            controls=[
                ft.Image(src="imagenen-de-camion.png", width=700, height=250),
                ft.Column(
                    controls=[
                        ft.Text(
                            "Servicio de transporte de mercancías",
                            weight=ft.FontWeight.NORMAL,
                            size=20,  # Tamaño de la fuente
                            color=ft.colors.BLACK,  # Color del texto
                            text_align=ft.TextAlign.LEFT,  # Alineación del texto
                        ),
                    ],
                    alignment=ft.CrossAxisAlignment.START,  # Alinear el texto a la izquierda
                    spacing=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,  # Alinear todo el contenido a la izquierda
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.colors.WHITE,
        padding=20,
        border_radius=10,
    )

    # Crear el texto con fondo personalizado
    top_content = ft.Container(
        content=ft.Text(
            "Transporta tus productos o mercadería con la flota de camiones tipo carguero.",
            size=24,
            weight=ft.FontWeight.NORMAL,
            color=ft.colors.BLACK,  # Texto blanco para contraste
            text_align=ft.TextAlign.CENTER,  # Alinear el texto al centro
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,  # Fondo del contenedor
        border_radius=10,  # Esquinas redondeadas
    )

    # Contenido principal con disposición en columnas y filas
    main_content = ft.Column(
        controls=[
            top_content,
            left_container,
            right_container
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20,
        expand=True  # Asegura que la columna principal tome todo el espacio disponible
    )

    # Botón en la parte inferior derecha
    bottom_right_button = ft.Container(
        content=ft.ElevatedButton(
            "Saber más",
            on_click=lambda _: print("Saber más"),
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor="#1B5051",  # Fondo del botón
                shape=ft.RoundedRectangleBorder(radius=8),  # Esquinas redondeadas
            ),
        ),
        padding=20
    )

    # Agregar el contenido principal y el botón a la página
    page.add(
        ft.Column(
            controls=[
                main_content,
                ft.Row(
                    controls=[
                        ft.Container(expand=True),
                        bottom_right_button
                    ],
                    alignment=ft.MainAxisAlignment.END
                )
            ],
            expand=True
        )
    )

# Ejecutar la aplicación
ft.app(target=main)
