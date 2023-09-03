import cohere
import customtkinter as ctk
import threading

co = cohere.Client("APIKEY")

class App():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("900x400")
        self.root.title('Chat App')
        self.mainframe = ctk.CTkFrame(master=self.root)
        self.mainframe.pack(pady=10, padx=10, fill='both', expand="True")

        self.text = ctk.CTkLabel(master=self.mainframe, text="Input",
                                 text_color="White", font=("Calibri Light", 18))
        self.text.grid(row=0, column=0)

        self.text_field = ctk.CTkEntry(
            master=self.mainframe, width=700, height=10)
        self.text_field.grid(row=1, column=0, pady=5, padx=5, sticky="NWES")

        self.text_button = ctk.CTkButton(
            master=self.mainframe, text="Enter", command=self.on_click)
        self.text_button.grid(row=1, pady=5, column=1, sticky="NWES")

        self.text_1 = ctk.CTkTextbox(
            self.root, pady=10, padx=50, width=780, height=280)
        self.text_1.pack()

        self.root.bind('<Return>', self.on_click)

        self.root.mainloop()
        return

    def on_click(self, event=None):
        user_input = self.text_field.get()
        self.display_message(f'You: {user_input}')
        self.thread = threading.Thread(target=self.resp, args=(user_input,))
        self.thread.start()

    def display_message(self, message):
        formatted_message = f'{message}\n\n'
        self.text_1.insert('end', formatted_message)

    def resp(self, user_input):
        self.response = co.generate(
            model='command-xlarge-nightly',
            prompt=user_input,
            max_tokens=300,
            temperature=0.6,
            stop_sequences=["--"])
        api_output = f'Cohere: {self.response.generations[0].text}'
        self.display_message(api_output)
        self.text_field.delete(0, 'end')


if __name__ == "__main__":
    App()