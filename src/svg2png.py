#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# Description: Convert svg file to png/pdf
# 1.pip install cairosvg   # svg to pdf/png
# 2.pip install svglib     # svg to pdf/png
# 3.pip install pdf2image  # pdf to png/jpeg
# Date: 2021/05/08
# Author: Steven Huang, Auckland, NZ

from common import gImageOutputPath
import cairosvg
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from pdf2image import convert_from_path
import PIL
# import tempfile


def svg2Image(svg_file, dst, fmt='pdf', dpi=96):
    if 0:  # svglib
        drawing = svg2rlg(svg_file)
        if fmt == 'pdf':
            renderPDF.drawToFile(drawing, dst)
        elif fmt == 'png':
            renderPM.drawToFile(drawing, dst, fmt="PNG", dpi=300)

    else:  # cairosvg default dpi=96
        if fmt == 'pdf':
            cairosvg.svg2pdf(url=svg_file, write_to=dst, dpi=dpi)
        elif fmt == 'png':
            cairosvg.svg2png(url=svg_file, write_to=dst, dpi=dpi)
        elif fmt == 'ps':
            cairosvg.svg2ps(url=svg_file, write_to=dst, dpi=dpi)
        else:
            print('error, format=', fmt)


def set_image_dpi_resize(image, dst):
    """
    Rescaling image to 300dpi while resizing
    :param image: An image
    :return: A rescaled image
    """
    length_x, width_y = image.size
    factor = min(1, float(1024.0 / length_x))
    size = int(factor * length_x), int(factor * width_y)
    image_resize = image.resize(size, PIL.Image.ANTIALIAS)
    # temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='1.png')
    # temp_filename = temp_file.name
    image_resize.save(dst, dpi=(300, 300))
    # return temp_filename


def pdf2Image(file, dst, page=0, fmt='png', dpi=96):
    images = convert_from_path(file)
    for i, image in enumerate(images):
        if page == i:
            print('type=', type(image))
            # image = set_image_dpi_resize(image, dst)
            image.save(dst, 'PNG')  # JPEG
            break


def main():
    file = gImageOutputPath + r'\dataFrame.svg'

    dst_file = gImageOutputPath + r'\dataFrame.svg.pdf'
    svg2Image(svg_file=file, dst=dst_file)

    dst_file = gImageOutputPath + r'\dataFrame.svg.png'
    svg2Image(svg_file=file, dst=dst_file, fmt='png', dpi=300)

    # dst_file = gImageOutputPath + r'\dataFrame.svg.pdf.png'
    # pdf2Image(file, dst_file)


if __name__ == '__main__':
    main()
