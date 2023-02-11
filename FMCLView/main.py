# coding:utf-8
"""
    启动GUI
"""
from FMCLView.tk_extend.frame import GUI
import FMCLView.styles as styles
from FMCLView.pages import launch, settings
from FMCLView.tk_extend import dialogs
import threading
import update

def main() -> None:
    """
        初始化并启动GUI
        :return: 无
    """
    # 创建窗口
    gui = GUI()
    threading.Thread(target=update.check).start()

    # 初始化样式
    styles.init()
    dialogs.DefaultStyle.default_root_args = styles.frame()
    dialogs.DefaultStyle.default_label_args = styles.label("image", "compound")
    dialogs.DefaultStyle.default_button_args = styles.button("image", "compound")
    dialogs.DefaultStyle.default_entry_args = styles.entry()

    # 窗口设定
    gui.geometry("640x360")
    gui.resizable(False, False)
    gui.title("First Minecraft Launcher")

    gui.page_func("launch")(launch.page)
    gui.page_func("settings")(settings.page)

    gui.show_page("launch")

    # 启动GUI
    gui.mainloop()


if __name__ == '__main__':
    main()
