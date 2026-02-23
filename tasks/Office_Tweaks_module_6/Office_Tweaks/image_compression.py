from PIL import Image, ImageSequence
import os

class ImageCompressor:

    def compression(self, image, quality_percent):
        img = Image.open(image)
        #img.thumbnail((800, 800))
        #max_size = (800, 800)

        name, ext = os.path.splitext(image)
        ext = ext.lower()
        output_file = name + "_compressed" + ext

        if ext in [".jpg", ".jpeg"]:
            img = img.convert("RGB")
            img.save(output_file, quality=quality_percent, optimize=True)

        elif ext == ".png":
            #img.thumbnail(max_size)
            colors = max(2, int(quality_percent * 256 / 100))
            img = img.convert("P", palette=Image.ADAPTIVE, colors=colors)
            img.save(output_file, optimize=True)

        elif ext == ".gif":
            frames = []
            for frame in ImageSequence.Iterator(img):
                frame = frame.convert("P", palette=Image.ADAPTIVE, colors=max(2, int(quality_percent * 256 / 100)))
                #frame.thumbnail(max_size)
                frames.append(frame)

            # Сохраняем все кадры с сохранением анимации
            frames[0].save(output_file, save_all=True, append_images=frames[1:], loop=0, optimize=True)

        return output_file