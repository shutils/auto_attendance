import flet as ft
import configparser
import re

config_ini = configparser.ConfigParser()
config_ini.read("config.ini", encoding="utf-8")
start_list = re.findall('[0-9]+:[0-9]+', config_ini.get("SETUP", "startlist"))
end_list = re.findall('[0-9]+:[0-9]+', config_ini.get("SETUP", "endlist"))
old_start = config_ini.get("SAVE", "oldstart")
old_end = config_ini.get("SAVE", "oldend")
old_type = config_ini.get("SAVE", "oldtype")


def main(page: ft.Page):
    page.title = "auto_attendance"
    page.window_width = 250
    page.window_height = 300

    def change_start_time(e):
        config_ini["SAVE"]["oldstart"] = start_time.value
        with open("config.ini", "w", encoding="utf-8") as f:
            config_ini.write(f)

    def change_end_time(e):
        config_ini["SAVE"]["oldend"] = end_time.value
        with open("config.ini", "w", encoding="utf-8") as f:
            config_ini.write(f)

    def change_work_type(e):
        config_ini["SAVE"]["oldtype"] = work_type.value
        with open("config.ini", "w", encoding="utf-8") as f:
            config_ini.write(f)

    label_start = ft.Text("開始時刻")
    label_end = ft.Text("終了時刻")
    start_time = ft.Dropdown(width=100, value=old_start, on_change=change_start_time)
    for time in start_list:
        start_time.options.append(ft.dropdown.Option(time))

    end_time = ft.Dropdown(width=100, value=old_end, on_change=change_end_time)
    for time in end_list:
        end_time.options.append(ft.dropdown.Option(time))
    work_type = ft.RadioGroup(
        content=ft.Row([ft.Radio(value="出社", label="出社"),
                        ft.Radio(value="在宅", label="在宅")]), value=old_type, on_change=change_work_type)

    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        work_type
                    ]
                ),
                ft.Row(
                    [
                        ft.Column(
                            [
                                label_start,
                                start_time,
                            ]
                        ),
                        ft.Column(
                            [
                                label_end,
                                end_time,
                            ]
                        ),
                    ],
                ),
                ft.ElevatedButton(text="実行", width=250)
            ]
        )
    )


ft.app(target=main)
