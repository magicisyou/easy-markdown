import flet as ft

from utils import variables as var
from components import snackbar

FILE_PATH=None

file_indicator=ft.Text(f"File : {FILE_PATH}")

def update_file_indicator():
    file_indicator.value=f"File : {FILE_PATH}"
    file_indicator.update()

def pick_files_result(e: ft.FilePickerResultEvent):
    global FILE_PATH
    if e.files:
        for file in e.files:
            FILE_PATH=file.path
            with open(FILE_PATH, "r") as file:
                file_content=file.read()
                markdown_text_field.value=file_content
                markdown_output.value=file_content
                markdown_text_field.update()
                markdown_output.update()
                file.close()
                update_file_indicator()

def save_file_result(e: ft.FilePickerResultEvent):
    global FILE_PATH
    FILE_PATH = e.path if e.path else None
    if FILE_PATH:
        save_to_file()
        update_file_indicator()

def save_to_file():
    if FILE_PATH:
        with open(FILE_PATH, "w") as file:
            file.write(markdown_text_field.value)
            file.close()
            snackbar.show_snackbar(f"Saved as {FILE_PATH}")
    else:
        file_saver.save_file(file_type=ft.FilePickerFileType.CUSTOM, allowed_extensions=['md'])

def close_file():
    global FILE_PATH
    FILE_PATH=None
    markdown_text_field.value=''
    markdown_output.value=''
    markdown_text_field.update()
    markdown_output.update()
    update_file_indicator()

file_picker=ft.FilePicker(
    on_result=pick_files_result,
)
file_saver=ft.FilePicker(
    on_result=save_file_result,
)

markdown_text_field=ft.TextField(
    multiline=True,
    min_lines=20,
    max_lines=20,
    on_change=lambda _:render_markdown(),
    label='Markdown',
    hint_text='Write markdown here',
    autofocus=True,
    autocorrect=False,
    
)

markdown_output=ft.Markdown(
    '',
    extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
    expand=True,
    selectable=True,
    code_theme="atom-one-dark",
    code_style=ft.TextStyle(font_family="Roboto Mono"),
    auto_follow_links=True,
)

def render_markdown():
    markdown_output.value=markdown_text_field.value
    markdown_output.update()

def content():
    var.PAGE.overlay.append(file_picker)
    var.PAGE.overlay.append(file_saver)

    var.PAGE.appbar=ft.AppBar(
        leading=ft.Image(
            src="icon.svg",
            fit=ft.ImageFit.SCALE_DOWN,
        ),
        title=ft.Text('Easy Markdown'),
        bgcolor=ft.colors.SURFACE_VARIANT,
        center_title=False,
        actions=[
            file_indicator,
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        icon=ft.icons.FILE_OPEN,
                        text='Open',
                        on_click=lambda _: file_picker.pick_files(
                            allow_multiple=False,
                            allowed_extensions=['md'],
                            file_type=ft.FilePickerFileType.CUSTOM
                        )
                    ),
                    ft.PopupMenuItem(
                        icon=ft.icons.SAVE,
                        text='Save',
                        on_click=lambda _:save_to_file(),
                    ),
                    ft.PopupMenuItem(
                        icon=ft.icons.SAVE_AS,
                        text='Save as',
                        on_click=lambda _:file_saver.save_file(
                            file_type=ft.FilePickerFileType.CUSTOM,
                            allowed_extensions=['md'],
                        ),
                    ),
                    ft.PopupMenuItem(
                        icon=ft.icons.CLOSE,
                        text='Close File',
                        on_click=lambda _:close_file(),
                    ),
                    ft.PopupMenuItem(
                        icon=ft.icons.EXIT_TO_APP,
                        text='Exit',
                        on_click=lambda _:var.PAGE.window_close(),
                    ),
                    ft.PopupMenuItem(
                        text=('Created by youaremagic'),
                        on_click=lambda _:snackbar.show_snackbar(
                            (
                                "Easy Markdown is a free and open source markdown editor and viewer"
                                " created by youaremagic"
                            )
                        )
                    ),
                ]
            )
        ],
    )

    return ft.SafeArea(
        ft.Column(
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col=6,
                            controls=[
                                markdown_text_field,
                            ],
                        ),
                        ft.Column(
                            col=6,
                            controls=[
                                markdown_output,
                            ],
                            scroll=ft.ScrollMode.AUTO,
                        ),
                    ],
                ),
            ],
        ),
    )
