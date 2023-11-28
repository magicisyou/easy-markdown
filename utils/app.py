import flet as ft

from utils import variables as var

FILE_PATH=None

def content():
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
    
    def save_to_file():
        if FILE_PATH:
            with open(FILE_PATH, "w") as file:
                file.write(markdown_text_field.value)
                file.close()

    def close_file():
        global FILE_PATH
        FILE_PATH=None
        markdown_text_field.value=''
        markdown_output.value=''
        markdown_text_field.update()
        markdown_output.update()

    file_picker=ft.FilePicker(on_result=pick_files_result)
    file_picker.allowed_extensions=['md']
    var.PAGE.overlay.append(file_picker)

    var.PAGE.appbar=ft.AppBar(
        title=ft.Text('Easy Markdown'),
        bgcolor=ft.colors.SURFACE_VARIANT,
        center_title=False,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        content=ft.TextButton(
                            text='Open',
                            on_click=lambda _: file_picker.pick_files(allow_multiple=False)
                        )
                    ),
                    ft.PopupMenuItem(
                        content=ft.TextButton(
                            text='Save',
                            on_click=lambda _:save_to_file(),
                        )
                    ),
                    ft.PopupMenuItem(
                        content=ft.TextButton(
                            text='Close',
                            on_click=lambda _:close_file(),
                        )
                    ),
                ]
            )
        ],
    )

    markdown_text_field=ft.TextField(
        width=var.PAGE.window_width/2-50,
        multiline=True,
        min_lines=20,
        on_change=lambda _:render_markdown(),
        label='Markdown',
        hint_text='Write markdown here',
        autofocus=True,
    )

    markdown_output=ft.Markdown(
        '',
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        expand=True,
        selectable=True,
        code_theme="atom-one-dark",
        code_style=ft.TextStyle(font_family="Roboto Mono"),
        width=var.PAGE.window_width/2-50,
    )

    def render_markdown():
        markdown_output.value=markdown_text_field.value
        markdown_output.update()

    return ft.SafeArea(
      ft.Column(
          controls=[
              ft.Row(
                  controls=[
                      ft.Column(
                          controls=[
                              markdown_text_field,
                          ],
                      ),
                      ft.VerticalDivider(),
                      ft.Column(
                          controls=[
                              markdown_output,
                          ],
                          scroll=ft.ScrollMode.AUTO,
                          height=var.PAGE.window_height-50,
                      ),
                  ],
                  vertical_alignment=ft.CrossAxisAlignment.START,
                  height=var.PAGE.window_height,
                  alignment=ft.MainAxisAlignment.SPACE_AROUND,
              ),
          ],
      ),
  )