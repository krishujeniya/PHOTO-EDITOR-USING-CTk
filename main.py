import tkinter as tk
from rembg import remove
import customtkinter as cutk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image as kk, ImageTk, ImageDraw, ImageFont, ImageFilter

# App Title 

title = "Photo Editor"

font="//home//ai//Documents//Python//Photo_Editor_CTk//font.ttf"


cutk.set_appearance_mode('dark')
cutk.set_default_color_theme('dark-blue')
cutk.set_widget_scaling(1.5)
cutk.set_window_font(font)

# classes

class PhotoEditor(cutk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title(title)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.resizable(False,False)

        # Menubar
        
        self.menubar=tk.Menu(self)

        # File Menu

        def IMG_Select1(event):
            return self.IMG_Select()
        def IMG_Save1(event):
            return self.IMG_Save()
        def IMG_Exit1(event):
            return self.destroy()
        self.FM=tk.Menu(self.menubar,tearoff=False)
        self.menubar.add_cascade(label="File",underline=0,menu=self.FM)

        self.FM.add_command(label="Select",command=IMG_Select1)
        self.FM.add_command(label="Save",command=IMG_Save1)
        self.FM.add_command(label="Exit",command=IMG_Exit1)

        # Edit Menu 

        def IMG_Crop1(event):
            return self.IMG_Crop()
        def IMG_Rotate1(event):
            return self.IMG_Rotate()
        def IMG_Draw1(event):
            return self.IMG_Draw()
        def IMG_Text1(event):
            return self.IMG_Text()
        def IMG_Undo1(event):
            return self.IMG_Undo()
        def IMG_Redo1(event):
            return self.IMG_Redo()
        def IMG_RMBG1(event):
            return self.IMG_RMBG()
        def IMG_Filter1(event):
            return self.IMG_Filter()
        self.MM=tk.Menu(self.menubar,tearoff=False)
        self.menubar.add_cascade(label="Edit",underline=0,menu=self.MM)

        self.MM.add_command(label="Crop",command=IMG_Crop1)
        self.MM.add_command(label="Rotate",command=IMG_Rotate1)
        self.MM.add_command(label="Filter",command=IMG_Filter1)
        self.MM.add_command(label="Draw",command=IMG_Draw1)
        self.MM.add_command(label="Text",command=IMG_Text1)
        self.MM.add_command(label="Remove BG",command=IMG_RMBG1)
        self.MM.add_command(label="Undo",command=IMG_Undo1)
        self.MM.add_command(label="Redo",command=IMG_Redo1)

        # Window Menu 

        self.HM=tk.Menu(self.menubar,tearoff=False)
        self.menubar.add_cascade(label="Help",underline=0,menu=self.HM)

        self.HM.add_command(label="Select",accelerator="Ctrl+O")
        self.HM.add_command(label="Save",accelerator="Ctrl+S")
        self.HM.add_command(label="Exit",accelerator="Ctrl+Q")
        self.HM.add_command(label="Rotate",accelerator="Ctrl+R")
        self.HM.add_command(label="Crop",accelerator="Ctrl+C")
        self.HM.add_command(label="Filter",accelerator="Ctrl+F")
        self.HM.add_command(label="Draw",accelerator="Ctrl+D")
        self.HM.add_command(label="Text",accelerator="Ctrl+T")
        self.HM.add_command(label="Remove BG",accelerator="Ctrl+B")
        self.HM.add_command(label="Undo",accelerator="Ctrl+Z")
        self.HM.add_command(label="Redo",accelerator="Ctrl+Y")
        

        # ShortCuts

        self.config(menu=self.menubar)
        self.FM.bind_all("<Control-o>",IMG_Select1)
        self.FM.bind_all("<Control-s>",IMG_Save1)
        self.FM.bind_all("<Control-q>",IMG_Exit1)
        self.MM.bind_all("<Control-c>",IMG_Crop1)
        self.MM.bind_all("<Control-r>",IMG_Rotate1)
        self.MM.bind_all("<Control-d>",IMG_Draw1)
        self.MM.bind_all("<Control-t>",IMG_Text1)
        self.MM.bind_all("<Control-b>",IMG_RMBG1)
        self.MM.bind_all("<Control-f>",IMG_Filter1)
        self.MM.bind_all("<Control-z>",IMG_Undo1)
        self.MM.bind_all("<Control-y>",IMG_Redo1)


        # Class Variables

        self.list = []
        self.list2 = []
        self.filetypes = (("PNG image", "*.png"),("JPG image", "*.jpg"), ("All files", "*.*"))

        # Frame

        self.frame = cutk.CTkFrame(self, corner_radius=20, fg_color='transparent')

        self.inputcv = cutk.CTkCanvas(self.frame, width=300, height=300, bg='silver', highlightthickness=0)
        
        self.inputcv.pack()

        self.frame.pack(side="left", padx=50, pady=10)


        # Buttons

        cutk.CTkButton(self, text='Rotate', command=self.IMG_Rotate).pack(padx=10, pady=10)

        cutk.CTkButton(self, text='Text', command=self.IMG_Text).pack(padx=10, pady=10)

        cutk.CTkButton(self, text='Draw', command=self.IMG_Draw).pack(padx=10, pady=10)

        cutk.CTkButton(self, text='Filters', command=self.IMG_Filter).pack(padx=10, pady=10)

        cutk.CTkButton(self, text='Remove BG', command=self.IMG_RMBG).pack(padx=10, pady=10)

        cutk.CTkButton(self, text='Crop', command=self.IMG_Crop).pack(padx=10, pady=10)

        cutk.CTkButton(self, text='Undo', command=self.IMG_Undo).pack(padx=10, pady=10)

        cutk.CTkButton(self, text='Redo', command=self.IMG_Redo).pack(padx=10, pady=10)

        cutk.set_default_color_theme('green')

        cutk.CTkButton(self, text='Select', command=self.IMG_Select).pack(padx=10, pady=10)

        cutk.CTkButton(self, text='Save', command=self.IMG_Save).pack(padx=10, pady=10)


    def IMG_RMBG(self):

        try:
            img = remove(self.img)
            self.iimg = ImageTk.PhotoImage(img.resize((300, 300)))
            self.inputcv.create_image(0, 0, anchor=tk.NW, image=self.iimg)
            self.img = img
            self.list.append(self.img)
        except:
            messagebox.showerror(title, '')

    def IMG_Select(self):

        try:
            self.fpath = filedialog.askopenfilename(title=title, filetypes=[])
            img = kk.open(self.fpath).resize((300, 300))
            self.iimg = ImageTk.PhotoImage(img)
            self.inputcv.create_image(150, 150, image=self.iimg)
            self.img = img
        except:
            messagebox.showerror(title, '')

    def IMG_Rotate(self):

        class Rotate(cutk.CTk):
            def __init__(self, img, inputcv, list):
                super().__init__()
                self.title(title)

                # Class Variables

                self.img = img
                self.inputcv = inputcv
                self.list = list

                # Frame

                box = cutk.CTkFrame(self)

                # Buttons

                cutk.CTkButton(box, text="Turn Right",command=self.num90).pack(padx=10, pady=10)

                cutk.CTkButton(box, text="Flip", command=self.num180).pack(padx=10, pady=10)

                cutk.CTkButton(box, text="Turn Left",command=self.num270).pack(padx=10, pady=10)

                box.pack()

            def num90(self):

                try:
                    img = self.img.rotate(angle=int(90))
                    self.iimg = ImageTk.PhotoImage(img.resize((300, 300)))
                    self.inputcv.create_image(0, 0, anchor=tk.NW, image=self.iimg)
                    self.img = img
                    self.list.append(self.img)
                    return self.destroy()
                except:
                    messagebox.showerror(title, '')

            def num180(self):

                try:
                    img = self.img.rotate(angle=int(180))
                    self.iimg = ImageTk.PhotoImage(img.resize((300, 300)))
                    self.inputcv.create_image(0, 0, anchor=tk.NW, image=self.iimg)
                    self.img = img
                    self.list.append(self.img)
                    return self.destroy()
                except:
                    messagebox.showerror(title, '')

            def num270(self):

                try:
                    img = self.img.rotate(angle=int(270))
                    self.iimg = ImageTk.PhotoImage(img.resize((300, 300)))
                    self.inputcv.create_image(0, 0, anchor=tk.NW, image=self.iimg)
                    self.img = img
                    self.list.append(self.img)
                    return self.destroy()
                except:
                    messagebox.showerror(title, '')

        # Define class

        try:
            sas = Rotate(self.img, self.inputcv, self.list)
            sas.mainloop()
        except:
            messagebox.showerror(title, '')

    def IMG_Text(self):

        try:
            content = simpledialog.askstring(title=title, prompt="Enter text: ")
            color = simpledialog.askstring(title=title, prompt="Enter color: ")
            img = self.img

            def inadd(event):

                try:
                    d = ImageDraw.Draw(img)
                    font = ImageFont.truetype(font, 36)
                    d.text((event.x, event.y), content, fill=color, font=font)
                except:
                    messagebox.showerror(title, '')

                self.iimg = ImageTk.PhotoImage(img.resize((300, 300)))
                self.inputcv.create_image(0, 0, anchor=tk.NW, image=self.iimg)
                self.img = img
                self.list.append(self.img)

            self.inputcv.bind("<Button 1>", inadd)
        except:
            messagebox.showerror(title, '')

    def IMG_Save(self):

        try:
            file = filedialog.asksaveasfilename(title=title,defaultextension=".png", filetypes=self.filetypes)

            if file:
                self.img.save(file)
            else:
                pass

        except:
            messagebox.showerror(title, '')

    def IMG_Draw(self):

        try:
            color = (0, 0, 0)
            img = self.img
            li2 = []

            def draw_curve(event):

                try:
                    if (event.x <= img.size[0] and event.y <= img.size[1]):
                        draw_point(event)
                except:
                    messagebox.showerror(title, '')

            def draw_point1(im, x, y, color):

                try:
                    for x_coord in range(x-3, x+3):
                        for y_coord in range(y-3, y+3):
                            im.putpixel((x_coord, y_coord), color)

                    return im
                except:
                    messagebox.showerror(title, '')

            def draw_line(im, x1, y1, x2, y2, color):

                try:
                    d = ImageDraw.Draw(im)
                    d.line([(x1, y1), (x2, y2)], fill=color, width=3)

                    return im
                except:
                    messagebox.showerror(title, '')

            def draw_line(event):

                try:
                    if str(event.type) == "ButtonPress":
                        self.inputcv.old_coords = event.x, event.y
                    elif str(event.type) == "ButtonRelease":
                        first_x, first_y = self.inputcv.old_coords
                        second_x = event.x
                        second_y = event.y

                        img1 = draw_line(img, first_x, first_y,
                                         second_x, second_y, color)
                except:
                    messagebox.showerror(title, '')

                self.iimg = ImageTk.PhotoImage(img1.resize((300, 300)))
                self.inputcv.create_image(0, 0, anchor=tk.NW, image=self.iimg)
                self.img = img1
                li2.append(self.img)

            def draw_point(event):

                img2 = draw_point1(img, event.x, event.y, color)
                self.iimg = ImageTk.PhotoImage(img)
                self.inputcv.create_image(0, 0, anchor=tk.NW, image=self.iimg)
                self.img = img2
                li2.append(self.img)

            self.inputcv.bind("<Button 1>", draw_point)
            self.inputcv.bind("<B1-Motion>", draw_curve)
            self.inputcv.bind("<ButtonRelease-3>", draw_line)
            self.inputcv.bind("<ButtonPress-3>", draw_line)
            self.list.append(li2)
        except:
            messagebox.showerror(title, '')

    def IMG_Undo(self):

        if len(self.list) != 0:
            if len(self.list) > 1:
                img = self.list.pop(-2)
                self.list2.append(img)
            else:
                self.list2.append(self.list.pop())
                img = kk.open(self.fpath).resize((300, 300))
            self.iimg = ImageTk.PhotoImage(img)

            self.inputcv.create_image(0, 0, anchor=tk.NW, image=self.iimg)
            self.img = img

    def IMG_Redo(self):

        if len(self.list2) != 0:
            if len(self.list2) > 1:
                img = self.list2.pop(-1)

                if type(img) == type(list()):
                    img = img[-1]

                self.list.append(img)
            else:
                img = self.list2.pop()

                if type(img) == type(list()):
                    img = img[-1]

                self.list.append(img)
            self.iimg = ImageTk.PhotoImage(img)

            self.inputcv.create_image(0, 0, anchor=tk.NW, image=self.iimg)
            self.img = img

    def IMG_Filter(self):

        class Fil(cutk.CTk):
            def __init__(self, img, inputcv, list):
                super().__init__()
                self.title(title)

                # Class Variables

                self.img = img
                self.inputcv = inputcv
                self.list = list

                # Frame

                box = cutk.CTkFrame(self)

                # Buttons

                cutk.CTkButton(box, text="High Contrast Border", command=self.FIND_EDGES).pack(padx=10, pady=10)

                cutk.CTkButton(box, text="High Contrast",command=self.EDGE_ENHANCE_MORE).pack(padx=10, pady=10)

                cutk.CTkButton(box, text="Blur",  command=self.BLUR).pack(padx=10, pady=10)

                cutk.CTkButton(box, text="Inverse",command=self.CONTOUR).pack(padx=10, pady=10)

                cutk.CTkButton(box, text="Silver",command=self.EMBOSS).pack(padx=10, pady=10)

                box.pack()

            def BLUR(self):

                try:
                    img = self.img.filter(ImageFilter.BLUR)
                    self.iimg = ImageTk.PhotoImage(img.resize((300, 300)))
                    self.inputcv.create_image(0, 0, anchor=tk.NW, image=self.iimg)
                    self.img = img
                    self.list.append(self.img)
                    return self.destroy()
                except:
                    messagebox.showerror(title, '')

            def CONTOUR(self):

                try:
                    img = self.img.filter(ImageFilter.CONTOUR)
                    self.iimg = ImageTk.PhotoImage(img.resize((300, 300)))
                    self.inputcv.create_image(0, 0, anchor=tk.NW, image=self.iimg)
                    self.img = img
                    self.list.append(self.img)
                    return self.destroy()
                except:
                    messagebox.showerror(title, '')

            def FIND_EDGES(self):

                try:
                    img = self.img.filter(ImageFilter.FIND_EDGES)
                    self.iimg = ImageTk.PhotoImage(img.resize((300, 300)))
                    self.inputcv.create_image(0, 0, anchor=tk.NW, image=self.iimg)
                    self.img = img
                    self.list.append(self.img)
                    return self.destroy()
                except:
                    messagebox.showerror(title, '')

            def EDGE_ENHANCE_MORE(self):

                try:
                    img = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE)
                    self.iimg = ImageTk.PhotoImage(img.resize((300, 300)))
                    self.inputcv.create_image(0, 0, anchor=tk.NW, image=self.iimg)
                    self.img = img
                    self.list.append(self.img)
                    return self.destroy()
                except:
                    messagebox.showerror(title, '')

            def EMBOSS(self):

                try:
                    img = self.img.filter(ImageFilter.EMBOSS)
                    self.iimg = ImageTk.PhotoImage(img.resize((300, 300)))
                    self.inputcv.create_image(0, 0, anchor=tk.NW, image=self.iimg)
                    self.img = img
                    self.list.append(self.img)
                    return self.destroy()
                except:
                    messagebox.showerror(title, '')

        # Define class

        try:
            sas = Fil(self.img, self.inputcv, self.list)
            sas.mainloop()
        except:
            messagebox.showerror(title, '')
    def IMG_Crop(self):
        try:
            def on_button_press(event):
                try:
                    # save mouse drag start position
                    self.start_x = self.inputcv.canvasx(event.x)
                    self.start_y = self.inputcv.canvasy(event.y)

                    # create rectangle if not yet exist
                    if not self.rect:
                        self.rect = self.inputcv.create_rectangle(self.x, self.y, 1, 1, outline='red')
                except:
                    messagebox.showerror(title, '')
            def on_move_press(event):
                try:
                    curX = self.inputcv.canvasx(event.x)
                    curY = self.inputcv.canvasy(event.y)

                    w, h = self.inputcv.winfo_width(), self.inputcv.winfo_height()
                    if event.x > 0.9*w:
                        self.inputcv.xview_scroll(1, 'units')
                    elif event.x < 0.1*w:
                        self.inputcv.xview_scroll(-1, 'units')
                    if event.y > 0.9*h:
                        self.inputcv.yview_scroll(1, 'units')
                    elif event.y < 0.1*h:
                        self.inputcv.yview_scroll(-1, 'units')

                    # expand rectangle as you drag the mouse
                    self.inputcv.coords(self.rect, self.start_x, self.start_y, curX, curY)
                    self.im2 = self.im.crop((self.start_x, self.start_y, curX, curY))
                    self.iimg = ImageTk.PhotoImage(self.im2.resize((300,300)))
                except:
                    messagebox.showerror(title, '')
            def on_button_release(event):
                try:
                    self.inputcv.delete("all")
                    self.inputcv.create_image(0,0,anchor="nw",image=self.iimg)
                except:
                    messagebox.showerror(title, '')
            self.rect = None
            self.x = self.y = 0
            self.start_x = None
            self.start_y = None

            self.inputcv.bind("<ButtonPress-1>",on_button_press)
            self.inputcv.bind("<B1-Motion>", on_move_press)
            self.inputcv.bind("<ButtonRelease-1>", on_button_release)

            self.im = self.img
            self.tk_im = ImageTk.PhotoImage(self.im)
            self.inputcv.create_image(0,0,anchor="nw",image=self.tk_im)
        except:
            messagebox.showerror(title, '')



# Run The Code 

if __name__ == '__main__':
    app = PhotoEditor()
    app.mainloop()
