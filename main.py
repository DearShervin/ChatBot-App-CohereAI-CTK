import cohere
import customtkinter as ctk

co = cohere.Client("Your API Key")

class App():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("800x300")
        self.root.title('Co:here API App')
        self.mainframe = ctk.CTkFrame(master=self.root)
        self.mainframe.pack(pady=10, padx=10, fill='both', expand="True")

        self.text = ctk.CTkLabel(master=self.mainframe, text="Ask Anything",
                                 text_color="White", font=("Calibri Light", 18))
        self.text.grid(row=0, column=0)

        self.text_field = ctk.CTkEntry(
            master=self.mainframe, width=615, height=10)
        self.text_field.grid(row=1, column=0, pady=5, padx=5, sticky="NWES")

        self.text_button = ctk.CTkButton(
            master=self.mainframe, text="Enter", command=self.Resp)
        self.text_button.grid(row=1, pady=5, column=1, sticky="NWES")

        self.text_1 = ctk.CTkTextbox(
            self.root, pady=10, padx=50, width=780, height=280)
        self.text_1.pack()

        self.root.mainloop()
        return

    def Resp(self):
        self.prompt = self.text_field.get()
        self.response = co.generate(
            model='command-xlarge-nightly',
            prompt=self.prompt,
            max_tokens=300,
            temperature=0.6,
            stop_sequences=["--"])
        self.answer = self.response.generations[0].text
        self.text_1.insert('end', text=self.answer)

if __name__ == "__main__":
    App()