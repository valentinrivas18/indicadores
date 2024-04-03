from PIL import Image, ImageTk

def logopcba(ruta):
    # logo del pcba
    pcba_img = Image.open(ruta)
    pcba_redimen = pcba_img.resize((150,150))
    return ImageTk.PhotoImage(pcba_redimen)
