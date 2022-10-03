from PIL import Image, ImageDraw


def create_image(text: list, img_file=None):
    size = (400, 400)
    if img_file:
        with Image.open(img_file) as image:
            image.load()
            image.thumbnail(size)
            back = Image.new(image.mode, (image.width, image.height + 40), (255, 255, 255))
            draw_text = ImageDraw.Draw(back, back.mode)
            draw_text.text((10, 5), '\n'.join(text), fill='#555555')
            back.paste(image, (0, 40))
            return back
    else:
        back = Image.new('RGB', (400, 200), (255, 255, 255))
        draw_text = ImageDraw.Draw(back, back.mode)
        draw_text.text((170, 90), '\n'.join(text), fill='#FF0000')
        return back


if __name__ == '__main__':
    from simpsons import models, classify
    labels = [m_name + ': ' + classify('./static/test_imgs/gil.jpeg', model)
              for m_name, model in models.items()]
    im = create_image(labels, './static/test_imgs/gil.jpeg')
    im.show()
