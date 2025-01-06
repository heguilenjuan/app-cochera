import flet as ft
from components.tabs_view import Tabs_view
from models.app_state import AppState

def main(page: ft.Page):
    page.title = "App Cochera"
    menu = Tabs_view(page, AppState)
    page.theme_mode = ft.ThemeMode.DARK
    
    page.add(menu)

ft.app(main)
