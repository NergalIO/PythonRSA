from tkinter import filedialog
from Parser.setting import Parse
from Environment.env import *
from RSA.main import *
from tkinter import *

class Form(Tk):
    def __init__(self, *args, **kwargs) -> None:
        Tk.__init__(self, *args, **kwargs)

        # Инициализация переменных
        self.rsa = CreateInstance(key_length = Parse().get("keylength", 32))
        self.resolution = [int(elem) for elem in Parse().get("resolution")]

        # Инициализация формы и окон ввода и вывода
        self.title('RSA Encrypter')
        self.geometry(f"{self.resolution[0]}x{self.resolution[1]}")
        self.entry = Input(self, text='write')
        self.label = Label(self, text='Output window')
        self.output = Output(self)
        self.status_bar = Output(self)

        # Инициализация контекстного и верхнего меню
        self.top_menu = TopMenu(self, tearoff = 0)
        self.top_menu.create_cascad(
            "Data", 
            {
                "Open": self.call_openkeys,
                "Save": self.call_savekeys,
                "Generate": self.call_generate,
                "Get": self.call_getkeys,
            }
        )
        self.top_menu.create_cascad(
            "Files",
            {
                "Encode": self.call_file_encrypt,
                "Decode": self.call_file_decrypt,
            }
        )
        self.config(menu=self.top_menu)

        # Инициализация кнопок
        self.decode_button = Button(self, text='decode', command=self.call_decode)
        self.encode_button = Button(self, text='encode', command=self.call_encode)

        # Размещение виджетов на форме
        self.label.place(x=10, y=45)
        self.entry.place(x=10, y=10, width=self.resolution[0] - 110, height=25)
        self.output.place(x=10, y=65, width=self.resolution[0] - 20, height=self.resolution[1] - 100)
        self.status_bar.place(x=10, y=self.resolution[1] - 30, width=self.resolution[0] - 20, height=20)
        self.decode_button.place(x=self.resolution[0] - 60, y=10, width=50, height=25)
        self.encode_button.place(x=self.resolution[0] - 110, y=10, width=50, height=25)

        # Вывод приветсвенного сообщения
        self.hello_message()

    def call_decode(self) -> None:
        try:
            self.update_status_bar("Decoding...")
            self.print(f"Decoded: {decode(self.rsa, self.entry.get())}")
            self.update_status_bar('Decoded')
        except KeyError:
            self.update_status_bar("Warning: To encrypt text, you need to import or generate keys")

    def call_encode(self) -> None:
        try:
            self.update_status_bar("Encoding...")
            self.print(f"Encoded: {encode(self.rsa, self.entry.get())}")
            self.update_status_bar('Encoded')
        except KeyError:
            self.update_status_bar("Warning: To decrypt the text, you need to import or generate keys")

    def call_generate(self) -> None:
        self.update_status_bar("Generating data...")
        generate(self.rsa)
        self.update_status_bar('Generated!')

    def call_getkeys(self) -> None:
        self.print(get_keys(self.rsa))

    def call_file_encrypt(self) -> None:
        try:
            self.update_status_bar("Encrypting file...")
            with filedialog.askopenfile(mode='rb') as file:
                file_encrypt(self.rsa, file.read(), file.name)
                self.update_status_bar(f"File {file.name} encrypted!")
        except Exception as error:
            self.update_status_bar(f"Warning: {error}")

    def call_file_decrypt(self) -> None:
        try:
            self.update_status_bar("Decrypting file...")
            with filedialog.askopenfile(mode='rb') as file:
                file_decrypt(self.rsa, file.read(), file.name)
            self.update_status_bar(f"File {file.name} decrypted!")
        except Exception as error:
            self.update_status_bar(f"Warning: {error}")

    def call_savekeys(self) -> None:
        try:
            self.update_status_bar("Saving file...")
            with filedialog.asksaveasfile(mode='wb', defaultextension='.data') as file:
                file.write(prepare_keys(self.rsa))
                self.update_status_bar(f"Data saved in {file.name}")
        except Exception as error:
            self.update_status_bar(f"Warning: {error}")

    def call_openkeys(self) -> None:
        try:
            self.update_status_bar("Opening file...")
            with filedialog.askopenfile(mode='rb', defaultextension='.data') as file:
                import_keys(self.rsa, file.read())
                self.update_status_bar(f"Data readed from {file.name}")
        except Exception as error:
            self.update_status_bar(f"Warning: {error}")

    def hello_message(self) -> None:
        text = """                          Welcome to RSA Encryption program.
        To use the programs, please generate or open the keys. 
        To generate/open the keys, press 'Data' -> 'Open'/'Generate'.
        Author: WokasWokas          Version: 2.0        Update Date: 16.09.2022
        github: https://github.com/WokasWokas
        """
        self.print(text)

    def print(self, text: str) -> None:
        self.output.configure(state='normal')
        self.output.insert(END, str(text) + '\n')
        self.output.configure(state='disable')
    
    def update_status_bar(self, text: str) -> None:
        self.status_bar.configure(state='normal')
        self.status_bar.delete("1.0", 'end')
        self.status_bar.insert(END, str(text))
        self.status_bar.configure(state='disable')

    def start(self) -> None:
        self.mainloop()

class TopMenu(Menu):
    def __init__(self, parent: Tk, *args, **kwargs) -> None:
        Menu.__init__(self, parent, *args, **kwargs)
        self.cascades = []

    def create_cascad(self, name: str, commands: dict[str, any]) -> None:
        cascad = Menu(self, tearoff=0)
        for command, func in commands.items():
            cascad.add_command(label=command, command=func)
        self.add_cascade(label=name, menu=cascad)
        self.cascades.append(cascad)

class Input(Entry):
    def __init__(self, parent, **kwargs):
        Entry.__init__(self, parent, **kwargs)
        self.context_menu = ContextMenu(self, tearoff = 0)

class Output(Text):
    def __init__(self, parent, **kwargs):
        Text.__init__(self, parent, **kwargs)
        self.context_menu = ContextMenu(self, tearoff = 0)
        self.configure(state='disable')

class ContextMenu(Menu):
    def __init__(self, parent: Text | Entry, *args, **kwargs) -> None:
        Menu.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.add_command(label="Copy", accelerator="Ctrl+C", command=self.call_copy)
        self.add_command(label="Paste", accelerator="Ctrl+V", command=self.call_paste)
        self.add_command(label="Cut", accelerator="Ctrl+X", command=self.call_cut)
        self.parent.bind("<Button-3>", self.do_popup)

    def call_copy(self, event=None) -> None:
        self.parent.clipboard_clear()
        text = self.parent.get('sel.first', 'sel.last')
        self.parent.clipboard_append(text)
    
    def call_paste(self, event=None) -> None:
        text = self.parent.selection_get(selection='CLIPBOARD')
        self.parent.insert('insert', text)

    def call_cut(self, event=None) -> None:
        self.call_copy()
        self.parent.delete("sel.first", "sel.last")

    def do_popup(self, event):
        try:
            self.tk_popup(event.x_root, event.y_root)
        finally:
            self.grab_release()
        
