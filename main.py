import flet as ft
from components.tabs_view import Tabs_view

def main(page: ft.Page):
    page.title = "App Cochera"
    menu = Tabs_view()
    
    page.add(menu)

ft.app(main)
