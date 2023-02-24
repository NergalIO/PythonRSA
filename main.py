if __name__ == "__main__":
    try:
        from Form.main import create_form

        form = create_form()
            
        form.start()

    except Exception as error:
        from tkinter import messagebox
        print(error)
        messagebox.showerror(error.__class__.__name__, f"Exception ({error.__class__.__name__}) raised from {error.__traceback__.tb_frame.f_code.co_filename} with message (\n  {error.args[0]}\n)")