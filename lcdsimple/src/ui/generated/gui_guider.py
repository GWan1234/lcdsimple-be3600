# Copyright 2022 NXP
# SPDX-License-Identifier: MIT
# The auto-generated can only be used on NXP devices

import SDL
import utime as time
import usys as sys
import lvgl as lv
import lodepng as png
import ustruct

lv.init()
SDL.init(w=284,h=100)

# Register SDL display driver.
disp_buf1 = lv.disp_draw_buf_t()
buf1_1 = bytearray(284*10)
disp_buf1.init(buf1_1, None, len(buf1_1)//4)
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.draw_buf = disp_buf1
disp_drv.flush_cb = SDL.monitor_flush
disp_drv.hor_res = 284
disp_drv.ver_res = 100
disp_drv.register()

# Regsiter SDL mouse driver
indev_drv = lv.indev_drv_t()
indev_drv.init() 
indev_drv.type = lv.INDEV_TYPE.POINTER
indev_drv.read_cb = SDL.mouse_read
indev_drv.register()

# Below: Taken from https://github.com/lvgl/lv_binding_micropython/blob/master/driver/js/imagetools.py#L22-L94

COLOR_SIZE = lv.color_t.__SIZE__
COLOR_IS_SWAPPED = hasattr(lv.color_t().ch,'green_h')

class lodepng_error(RuntimeError):
    def __init__(self, err):
        if type(err) is int:
            super().__init__(png.error_text(err))
        else:
            super().__init__(err)

# Parse PNG file header
# Taken from https://github.com/shibukawa/imagesize_py/blob/ffef30c1a4715c5acf90e8945ceb77f4a2ed2d45/imagesize.py#L63-L85

def get_png_info(decoder, src, header):
    # Only handle variable image types

    if lv.img.src_get_type(src) != lv.img.SRC.VARIABLE:
        return lv.RES.INV

    data = lv.img_dsc_t.__cast__(src).data
    if data == None:
        return lv.RES.INV

    png_header = bytes(data.__dereference__(24))

    if png_header.startswith(b'\211PNG\r\n\032\n'):
        if png_header[12:16] == b'IHDR':
            start = 16
        # Maybe this is for an older PNG version.
        else:
            start = 8
        try:
            width, height = ustruct.unpack(">LL", png_header[start:start+8])
        except ustruct.error:
            return lv.RES.INV
    else:
        return lv.RES.INV

    header.always_zero = 0
    header.w = width
    header.h = height
    header.cf = lv.img.CF.TRUE_COLOR_ALPHA

    return lv.RES.OK

def convert_rgba8888_to_bgra8888(img_view):
    for i in range(0, len(img_view), lv.color_t.__SIZE__):
        ch = lv.color_t.__cast__(img_view[i:i]).ch
        ch.red, ch.blue = ch.blue, ch.red

# Read and parse PNG file

def open_png(decoder, dsc):
    img_dsc = lv.img_dsc_t.__cast__(dsc.src)
    png_data = img_dsc.data
    png_size = img_dsc.data_size
    png_decoded = png.C_Pointer()
    png_width = png.C_Pointer()
    png_height = png.C_Pointer()
    error = png.decode32(png_decoded, png_width, png_height, png_data, png_size)
    if error:
        raise lodepng_error(error)
    img_size = png_width.int_val * png_height.int_val * 4
    img_data = png_decoded.ptr_val
    img_view = img_data.__dereference__(img_size)

    if COLOR_SIZE == 4:
        convert_rgba8888_to_bgra8888(img_view)
    else:
        raise lodepng_error("Error: Color mode not supported yet!")

    dsc.img_data = img_data
    return lv.RES.OK

# Above: Taken from https://github.com/lvgl/lv_binding_micropython/blob/master/driver/js/imagetools.py#L22-L94

decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png

def anim_x_cb(obj, v):
    obj.set_x(v)

def anim_y_cb(obj, v):
    obj.set_y(v)

def ta_event_cb(e,kb):
    code = e.get_code()
    ta = e.get_target()
    if code == lv.EVENT.FOCUSED:
        kb.set_textarea(ta)
        kb.move_foreground()
        kb.clear_flag(lv.obj.FLAG.HIDDEN)

    if code == lv.EVENT.DEFOCUSED:
        kb.set_textarea(None)
        kb.move_background()
        kb.add_flag(lv.obj.FLAG.HIDDEN)


error = lv.obj()
error.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_error_main_main_default
style_error_main_main_default = lv.style_t()
style_error_main_main_default.init()
style_error_main_main_default.set_radius(5)
style_error_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_main_main_default.set_bg_opa(0)
style_error_main_main_default.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_default.set_border_width(0)
style_error_main_main_default.set_border_opa(0)
style_error_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_error_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_error_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_error_main_main_default.set_text_font(lv.font_montserrat_16)
style_error_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for error
error.add_style(style_error_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_error_main_main_focused
style_error_main_main_focused = lv.style_t()
style_error_main_main_focused.init()
style_error_main_main_focused.set_radius(5)
style_error_main_main_focused.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_focused.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_focused.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_main_main_focused.set_bg_opa(0)
style_error_main_main_focused.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_focused.set_border_width(0)
style_error_main_main_focused.set_border_opa(0)
style_error_main_main_focused.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_error_main_main_focused.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_error_main_main_focused.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_error_main_main_focused.set_text_font(lv.font_montserrat_16)

# add style for error
error.add_style(style_error_main_main_focused, lv.PART.MAIN|lv.STATE.FOCUSED)

# create style style_error_main_main_pressed
style_error_main_main_pressed = lv.style_t()
style_error_main_main_pressed.init()
style_error_main_main_pressed.set_radius(5)
style_error_main_main_pressed.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_pressed.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_pressed.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_main_main_pressed.set_bg_opa(0)
style_error_main_main_pressed.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_pressed.set_border_width(0)
style_error_main_main_pressed.set_border_opa(0)
style_error_main_main_pressed.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_error_main_main_pressed.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_error_main_main_pressed.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_error_main_main_pressed.set_text_font(lv.font_montserrat_16)

# add style for error
error.add_style(style_error_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_error_main_main_checked
style_error_main_main_checked = lv.style_t()
style_error_main_main_checked.init()
style_error_main_main_checked.set_radius(5)
style_error_main_main_checked.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_checked.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_checked.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_main_main_checked.set_bg_opa(0)
style_error_main_main_checked.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_checked.set_border_width(0)
style_error_main_main_checked.set_border_opa(0)
style_error_main_main_checked.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_error_main_main_checked.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_error_main_main_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_error_main_main_checked.set_text_font(lv.font_montserrat_16)

# add style for error
error.add_style(style_error_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

# create style style_error_main_main_disabled
style_error_main_main_disabled = lv.style_t()
style_error_main_main_disabled.init()
style_error_main_main_disabled.set_radius(5)
style_error_main_main_disabled.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_disabled.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_disabled.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_main_main_disabled.set_bg_opa(0)
style_error_main_main_disabled.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_error_main_main_disabled.set_border_width(0)
style_error_main_main_disabled.set_border_opa(0)
style_error_main_main_disabled.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_error_main_main_disabled.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_error_main_main_disabled.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_error_main_main_disabled.set_text_font(lv.font_montserrat_16)

# add style for error
error.add_style(style_error_main_main_disabled, lv.PART.MAIN|lv.STATE.DISABLED)

error_label_21 = lv.label(error)
error_label_21.set_pos(int(0),int(0))
error_label_21.set_size(284,76)
error_label_21.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_error_label_21_main_main_default
style_error_label_21_main_main_default = lv.style_t()
style_error_label_21_main_main_default.init()
style_error_label_21_main_main_default.set_radius(0)
style_error_label_21_main_main_default.set_bg_color(lv.color_make(0x00,0x00,0x00))
style_error_label_21_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_21_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_label_21_main_main_default.set_bg_opa(255)
style_error_label_21_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_error_label_21_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_error_label_21_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_error_label_21_main_main_default.set_text_font(lv.font_montserrat_16)
style_error_label_21_main_main_default.set_text_letter_space(2)
style_error_label_21_main_main_default.set_text_line_space(0)
style_error_label_21_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_error_label_21_main_main_default.set_pad_left(0)
style_error_label_21_main_main_default.set_pad_right(0)
style_error_label_21_main_main_default.set_pad_top(8)
style_error_label_21_main_main_default.set_pad_bottom(0)

# add style for error_label_21
error_label_21.add_style(style_error_label_21_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

error_label_19 = lv.label(error)
error_label_19.set_pos(int(6),int(22))
error_label_19.set_size(272,49)
error_label_19.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_error_label_19_main_main_default
style_error_label_19_main_main_default = lv.style_t()
style_error_label_19_main_main_default.init()
style_error_label_19_main_main_default.set_radius(0)
style_error_label_19_main_main_default.set_bg_color(lv.color_make(0x14,0x11,0x26))
style_error_label_19_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_19_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_label_19_main_main_default.set_bg_opa(255)
style_error_label_19_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_error_label_19_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_error_label_19_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_error_label_19_main_main_default.set_text_font(lv.font_montserrat_16)
style_error_label_19_main_main_default.set_text_letter_space(0)
style_error_label_19_main_main_default.set_text_line_space(0)
style_error_label_19_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_error_label_19_main_main_default.set_pad_left(0)
style_error_label_19_main_main_default.set_pad_right(7)
style_error_label_19_main_main_default.set_pad_top(0)
style_error_label_19_main_main_default.set_pad_bottom(0)

# add style for error_label_19
error_label_19.add_style(style_error_label_19_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

error_label_17 = lv.label(error)
error_label_17.set_pos(int(195),int(21))
error_label_17.set_size(16,32)
error_label_17.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
error_label_17.set_text("4")
error_label_17.set_long_mode(lv.label.LONG.WRAP)
# create style style_error_label_17_main_main_default
style_error_label_17_main_main_default = lv.style_t()
style_error_label_17_main_main_default.init()
style_error_label_17_main_main_default.set_radius(0)
style_error_label_17_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_17_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_17_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_label_17_main_main_default.set_bg_opa(0)
style_error_label_17_main_main_default.set_text_color(lv.color_make(0xf9,0xba,0x2d))
try:
    style_error_label_17_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_error_label_17_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_error_label_17_main_main_default.set_text_font(lv.font_montserrat_16)
style_error_label_17_main_main_default.set_text_letter_space(2)
style_error_label_17_main_main_default.set_text_line_space(0)
style_error_label_17_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_error_label_17_main_main_default.set_pad_left(0)
style_error_label_17_main_main_default.set_pad_right(0)
style_error_label_17_main_main_default.set_pad_top(8)
style_error_label_17_main_main_default.set_pad_bottom(0)

# add style for error_label_17
error_label_17.add_style(style_error_label_17_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

error_label_13 = lv.label(error)
error_label_13.set_pos(int(38),int(21))
error_label_13.set_size(48,23)
error_label_13.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
error_label_13.set_text("已联网")
error_label_13.set_long_mode(lv.label.LONG.WRAP)
# create style style_error_label_13_main_main_default
style_error_label_13_main_main_default = lv.style_t()
style_error_label_13_main_main_default.init()
style_error_label_13_main_main_default.set_radius(0)
style_error_label_13_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_13_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_13_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_label_13_main_main_default.set_bg_opa(0)
style_error_label_13_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_error_label_13_main_main_default.set_text_font(lv.font_simsun_13)
except AttributeError:
    try:
        style_error_label_13_main_main_default.set_text_font(lv.font_montserrat_13)
    except AttributeError:
        style_error_label_13_main_main_default.set_text_font(lv.font_montserrat_16)
style_error_label_13_main_main_default.set_text_letter_space(2)
style_error_label_13_main_main_default.set_text_line_space(0)
style_error_label_13_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_error_label_13_main_main_default.set_pad_left(0)
style_error_label_13_main_main_default.set_pad_right(0)
style_error_label_13_main_main_default.set_pad_top(8)
style_error_label_13_main_main_default.set_pad_bottom(0)

# add style for error_label_13
error_label_13.add_style(style_error_label_13_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

error_img_12 = lv.img(error)
error_img_12.set_pos(int(15),int(38))
error_img_12.set_size(15,15)
error_img_12.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
error_img_12.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp1594921746.png','rb') as f:
        error_img_12_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp1594921746.png')
    sys.exit()

error_img_12_img = lv.img_dsc_t({
  'data_size': len(error_img_12_img_data),
  'header': {'always_zero': 0, 'w': 15, 'h': 15, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': error_img_12_img_data
})

error_img_12.set_src(error_img_12_img)
error_img_12.set_pivot(50,50)
error_img_12.set_angle(0)
# create style style_error_img_12_main_main_default
style_error_img_12_main_main_default = lv.style_t()
style_error_img_12_main_main_default.init()
style_error_img_12_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_error_img_12_main_main_default.set_img_recolor_opa(0)
style_error_img_12_main_main_default.set_img_opa(255)

# add style for error_img_12
error_img_12.add_style(style_error_img_12_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

error_label_16 = lv.label(error)
error_label_16.set_pos(int(183),int(42))
error_label_16.set_size(89,24)
error_label_16.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
error_label_16.set_text("已连接设备")
error_label_16.set_long_mode(lv.label.LONG.WRAP)
# create style style_error_label_16_main_main_default
style_error_label_16_main_main_default = lv.style_t()
style_error_label_16_main_main_default.init()
style_error_label_16_main_main_default.set_radius(0)
style_error_label_16_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_16_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_16_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_label_16_main_main_default.set_bg_opa(0)
style_error_label_16_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_error_label_16_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_error_label_16_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_error_label_16_main_main_default.set_text_font(lv.font_montserrat_16)
style_error_label_16_main_main_default.set_text_letter_space(2)
style_error_label_16_main_main_default.set_text_line_space(0)
style_error_label_16_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_error_label_16_main_main_default.set_pad_left(0)
style_error_label_16_main_main_default.set_pad_right(0)
style_error_label_16_main_main_default.set_pad_top(8)
style_error_label_16_main_main_default.set_pad_bottom(0)

# add style for error_label_16
error_label_16.add_style(style_error_label_16_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

error_label_18 = lv.label(error)
error_label_18.set_pos(int(31),int(42))
error_label_18.set_size(100,32)
error_label_18.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
error_label_18.set_text("1小时28分51秒")
error_label_18.set_long_mode(lv.label.LONG.WRAP)
# create style style_error_label_18_main_main_default
style_error_label_18_main_main_default = lv.style_t()
style_error_label_18_main_main_default.init()
style_error_label_18_main_main_default.set_radius(0)
style_error_label_18_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_18_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_18_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_label_18_main_main_default.set_bg_opa(0)
style_error_label_18_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_error_label_18_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_error_label_18_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_error_label_18_main_main_default.set_text_font(lv.font_montserrat_16)
style_error_label_18_main_main_default.set_text_letter_space(2)
style_error_label_18_main_main_default.set_text_line_space(0)
style_error_label_18_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_error_label_18_main_main_default.set_pad_left(0)
style_error_label_18_main_main_default.set_pad_right(0)
style_error_label_18_main_main_default.set_pad_top(8)
style_error_label_18_main_main_default.set_pad_bottom(0)

# add style for error_label_18
error_label_18.add_style(style_error_label_18_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

error_img_15 = lv.img(error)
error_img_15.set_pos(int(172),int(34))
error_img_15.set_size(20,20)
error_img_15.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
error_img_15.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp205760470.png','rb') as f:
        error_img_15_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp205760470.png')
    sys.exit()

error_img_15_img = lv.img_dsc_t({
  'data_size': len(error_img_15_img_data),
  'header': {'always_zero': 0, 'w': 20, 'h': 20, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': error_img_15_img_data
})

error_img_15.set_src(error_img_15_img)
error_img_15.set_pivot(50,50)
error_img_15.set_angle(0)
# create style style_error_img_15_main_main_default
style_error_img_15_main_main_default = lv.style_t()
style_error_img_15_main_main_default.init()
style_error_img_15_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_error_img_15_main_main_default.set_img_recolor_opa(0)
style_error_img_15_main_main_default.set_img_opa(255)

# add style for error_img_15
error_img_15.add_style(style_error_img_15_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

error_img_13 = lv.img(error)
error_img_13.set_pos(int(176),int(38))
error_img_13.set_size(12,12)
error_img_13.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
error_img_13.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp1264031863.png','rb') as f:
        error_img_13_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp1264031863.png')
    sys.exit()

error_img_13_img = lv.img_dsc_t({
  'data_size': len(error_img_13_img_data),
  'header': {'always_zero': 0, 'w': 12, 'h': 12, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': error_img_13_img_data
})

error_img_13.set_src(error_img_13_img)
error_img_13.set_pivot(50,50)
error_img_13.set_angle(0)
# create style style_error_img_13_main_main_default
style_error_img_13_main_main_default = lv.style_t()
style_error_img_13_main_main_default.init()
style_error_img_13_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_error_img_13_main_main_default.set_img_recolor_opa(0)
style_error_img_13_main_main_default.set_img_opa(255)

# add style for error_img_13
error_img_13.add_style(style_error_img_13_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

error_label_20 = lv.label(error)
error_label_20.set_pos(int(6),int(5))
error_label_20.set_size(86,11)
error_label_20.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
error_label_20.set_text("错误信息提示区域")
error_label_20.set_long_mode(lv.label.LONG.WRAP)
# create style style_error_label_20_main_main_default
style_error_label_20_main_main_default = lv.style_t()
style_error_label_20_main_main_default.init()
style_error_label_20_main_main_default.set_radius(0)
style_error_label_20_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_20_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_20_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_label_20_main_main_default.set_bg_opa(0)
style_error_label_20_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_error_label_20_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_error_label_20_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_error_label_20_main_main_default.set_text_font(lv.font_montserrat_16)
style_error_label_20_main_main_default.set_text_letter_space(0)
style_error_label_20_main_main_default.set_text_line_space(0)
style_error_label_20_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_error_label_20_main_main_default.set_pad_left(0)
style_error_label_20_main_main_default.set_pad_right(0)
style_error_label_20_main_main_default.set_pad_top(1)
style_error_label_20_main_main_default.set_pad_bottom(0)

# add style for error_label_20
error_label_20.add_style(style_error_label_20_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

error_btn_2 = lv.btn(error)
error_btn_2.set_pos(int(0),int(0))
error_btn_2.set_size(284,100)
error_btn_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_error_btn_2_main_main_default
style_error_btn_2_main_main_default = lv.style_t()
style_error_btn_2_main_main_default.init()
style_error_btn_2_main_main_default.set_radius(5)
style_error_btn_2_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_btn_2_main_main_default.set_bg_opa(0)
style_error_btn_2_main_main_default.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_default.set_border_width(0)
style_error_btn_2_main_main_default.set_border_opa(0)
style_error_btn_2_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_error_btn_2_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_error_btn_2_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_error_btn_2_main_main_default.set_text_font(lv.font_montserrat_16)
style_error_btn_2_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for error_btn_2
error_btn_2.add_style(style_error_btn_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_error_btn_2_main_main_focused
style_error_btn_2_main_main_focused = lv.style_t()
style_error_btn_2_main_main_focused.init()
style_error_btn_2_main_main_focused.set_radius(5)
style_error_btn_2_main_main_focused.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_focused.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_focused.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_btn_2_main_main_focused.set_bg_opa(0)
style_error_btn_2_main_main_focused.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_focused.set_border_width(0)
style_error_btn_2_main_main_focused.set_border_opa(0)
style_error_btn_2_main_main_focused.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_error_btn_2_main_main_focused.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_error_btn_2_main_main_focused.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_error_btn_2_main_main_focused.set_text_font(lv.font_montserrat_16)

# add style for error_btn_2
error_btn_2.add_style(style_error_btn_2_main_main_focused, lv.PART.MAIN|lv.STATE.FOCUSED)

# create style style_error_btn_2_main_main_pressed
style_error_btn_2_main_main_pressed = lv.style_t()
style_error_btn_2_main_main_pressed.init()
style_error_btn_2_main_main_pressed.set_radius(5)
style_error_btn_2_main_main_pressed.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_pressed.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_pressed.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_btn_2_main_main_pressed.set_bg_opa(0)
style_error_btn_2_main_main_pressed.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_pressed.set_border_width(0)
style_error_btn_2_main_main_pressed.set_border_opa(0)
style_error_btn_2_main_main_pressed.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_error_btn_2_main_main_pressed.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_error_btn_2_main_main_pressed.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_error_btn_2_main_main_pressed.set_text_font(lv.font_montserrat_16)

# add style for error_btn_2
error_btn_2.add_style(style_error_btn_2_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_error_btn_2_main_main_checked
style_error_btn_2_main_main_checked = lv.style_t()
style_error_btn_2_main_main_checked.init()
style_error_btn_2_main_main_checked.set_radius(5)
style_error_btn_2_main_main_checked.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_checked.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_checked.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_btn_2_main_main_checked.set_bg_opa(0)
style_error_btn_2_main_main_checked.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_checked.set_border_width(0)
style_error_btn_2_main_main_checked.set_border_opa(0)
style_error_btn_2_main_main_checked.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_error_btn_2_main_main_checked.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_error_btn_2_main_main_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_error_btn_2_main_main_checked.set_text_font(lv.font_montserrat_16)

# add style for error_btn_2
error_btn_2.add_style(style_error_btn_2_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

# create style style_error_btn_2_main_main_disabled
style_error_btn_2_main_main_disabled = lv.style_t()
style_error_btn_2_main_main_disabled.init()
style_error_btn_2_main_main_disabled.set_radius(5)
style_error_btn_2_main_main_disabled.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_disabled.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_disabled.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_btn_2_main_main_disabled.set_bg_opa(0)
style_error_btn_2_main_main_disabled.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_error_btn_2_main_main_disabled.set_border_width(0)
style_error_btn_2_main_main_disabled.set_border_opa(0)
style_error_btn_2_main_main_disabled.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_error_btn_2_main_main_disabled.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_error_btn_2_main_main_disabled.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_error_btn_2_main_main_disabled.set_text_font(lv.font_montserrat_16)

# add style for error_btn_2
error_btn_2.add_style(style_error_btn_2_main_main_disabled, lv.PART.MAIN|lv.STATE.DISABLED)

error_label_22 = lv.label(error)
error_label_22.set_pos(int(102),int(7))
error_label_22.set_size(81,11)
error_label_22.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
error_label_22.set_text("12:09")
error_label_22.set_long_mode(lv.label.LONG.WRAP)
# create style style_error_label_22_main_main_default
style_error_label_22_main_main_default = lv.style_t()
style_error_label_22_main_main_default.init()
style_error_label_22_main_main_default.set_radius(0)
style_error_label_22_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_22_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_22_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_label_22_main_main_default.set_bg_opa(0)
style_error_label_22_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_error_label_22_main_main_default.set_text_font(lv.font_simsun_11)
except AttributeError:
    try:
        style_error_label_22_main_main_default.set_text_font(lv.font_montserrat_11)
    except AttributeError:
        style_error_label_22_main_main_default.set_text_font(lv.font_montserrat_16)
style_error_label_22_main_main_default.set_text_letter_space(0)
style_error_label_22_main_main_default.set_text_line_space(0)
style_error_label_22_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_error_label_22_main_main_default.set_pad_left(0)
style_error_label_22_main_main_default.set_pad_right(0)
style_error_label_22_main_main_default.set_pad_top(0)
style_error_label_22_main_main_default.set_pad_bottom(0)

# add style for error_label_22
error_label_22.add_style(style_error_label_22_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

error_label_23 = lv.label(error)
error_label_23.set_pos(int(210),int(7))
error_label_23.set_size(81,11)
error_label_23.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
error_label_23.set_text("2025.12.31")
error_label_23.set_long_mode(lv.label.LONG.WRAP)
# create style style_error_label_23_main_main_default
style_error_label_23_main_main_default = lv.style_t()
style_error_label_23_main_main_default.init()
style_error_label_23_main_main_default.set_radius(0)
style_error_label_23_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_23_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_error_label_23_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_error_label_23_main_main_default.set_bg_opa(0)
style_error_label_23_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_error_label_23_main_main_default.set_text_font(lv.font_simsun_11)
except AttributeError:
    try:
        style_error_label_23_main_main_default.set_text_font(lv.font_montserrat_11)
    except AttributeError:
        style_error_label_23_main_main_default.set_text_font(lv.font_montserrat_16)
style_error_label_23_main_main_default.set_text_letter_space(0)
style_error_label_23_main_main_default.set_text_line_space(0)
style_error_label_23_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_error_label_23_main_main_default.set_pad_left(0)
style_error_label_23_main_main_default.set_pad_right(0)
style_error_label_23_main_main_default.set_pad_top(0)
style_error_label_23_main_main_default.set_pad_bottom(0)

# add style for error_label_23
error_label_23.add_style(style_error_label_23_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9 = lv.obj()
label_9.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_label_9_main_main_default
style_label_9_main_main_default = lv.style_t()
style_label_9_main_main_default.init()
style_label_9_main_main_default.set_radius(0)
style_label_9_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_main_main_default.set_bg_opa(0)
style_label_9_main_main_default.set_text_color(lv.color_make(0x99,0x96,0xab))
try:
    style_label_9_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_label_9_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_label_9_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_main_main_default.set_text_letter_space(0)
style_label_9_main_main_default.set_text_line_space(0)
style_label_9_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_main_main_default.set_pad_left(0)
style_label_9_main_main_default.set_pad_right(0)
style_label_9_main_main_default.set_pad_top(0)
style_label_9_main_main_default.set_pad_bottom(0)

# add style for label_9
label_9.add_style(style_label_9_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_Four_page = lv.label(label_9)
label_9_Four_page.set_pos(int(0),int(0))
label_9_Four_page.set_size(284,76)
label_9_Four_page.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_label_9_four_page_main_main_default
style_label_9_four_page_main_main_default = lv.style_t()
style_label_9_four_page_main_main_default.init()
style_label_9_four_page_main_main_default.set_radius(0)
style_label_9_four_page_main_main_default.set_bg_color(lv.color_make(0x00,0x00,0x00))
style_label_9_four_page_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_four_page_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_four_page_main_main_default.set_bg_opa(255)
style_label_9_four_page_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_label_9_four_page_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_label_9_four_page_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_label_9_four_page_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_four_page_main_main_default.set_text_letter_space(2)
style_label_9_four_page_main_main_default.set_text_line_space(0)
style_label_9_four_page_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_four_page_main_main_default.set_pad_left(0)
style_label_9_four_page_main_main_default.set_pad_right(0)
style_label_9_four_page_main_main_default.set_pad_top(8)
style_label_9_four_page_main_main_default.set_pad_bottom(0)

# add style for label_9_Four_page
label_9_Four_page.add_style(style_label_9_four_page_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_label_1 = lv.label(label_9)
label_9_label_1.set_pos(int(7),int(6))
label_9_label_1.set_size(111,65)
label_9_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_label_9_label_1_main_main_default
style_label_9_label_1_main_main_default = lv.style_t()
style_label_9_label_1_main_main_default.init()
style_label_9_label_1_main_main_default.set_radius(0)
style_label_9_label_1_main_main_default.set_bg_color(lv.color_make(0x14,0x11,0x26))
style_label_9_label_1_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_label_1_main_main_default.set_bg_opa(255)
style_label_9_label_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_label_9_label_1_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_label_9_label_1_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_label_9_label_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_label_1_main_main_default.set_text_letter_space(2)
style_label_9_label_1_main_main_default.set_text_line_space(0)
style_label_9_label_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_label_1_main_main_default.set_pad_left(0)
style_label_9_label_1_main_main_default.set_pad_right(0)
style_label_9_label_1_main_main_default.set_pad_top(8)
style_label_9_label_1_main_main_default.set_pad_bottom(0)

# add style for label_9_label_1
label_9_label_1.add_style(style_label_9_label_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_label_2 = lv.label(label_9)
label_9_label_2.set_pos(int(125),int(6))
label_9_label_2.set_size(152,65)
label_9_label_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_label_9_label_2_main_main_default
style_label_9_label_2_main_main_default = lv.style_t()
style_label_9_label_2_main_main_default.init()
style_label_9_label_2_main_main_default.set_radius(0)
style_label_9_label_2_main_main_default.set_bg_color(lv.color_make(0x14,0x11,0x26))
style_label_9_label_2_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_label_2_main_main_default.set_bg_opa(255)
style_label_9_label_2_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_label_9_label_2_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_label_9_label_2_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_label_9_label_2_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_label_2_main_main_default.set_text_letter_space(2)
style_label_9_label_2_main_main_default.set_text_line_space(0)
style_label_9_label_2_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_label_2_main_main_default.set_pad_left(0)
style_label_9_label_2_main_main_default.set_pad_right(0)
style_label_9_label_2_main_main_default.set_pad_top(8)
style_label_9_label_2_main_main_default.set_pad_bottom(0)

# add style for label_9_label_2
label_9_label_2.add_style(style_label_9_label_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_arc_2 = lv.arc(label_9)
label_9_arc_2.set_pos(int(52),int(6))
label_9_arc_2.set_size(79,100)
label_9_arc_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_arc_2.set_mode(lv.arc.MODE.NORMAL)
label_9_arc_2.set_range(0, 100)
label_9_arc_2.set_bg_angles(0, 360)
label_9_arc_2.set_angles(270, 90)
label_9_arc_2.set_rotation(0)
label_9_arc_2.set_style_arc_rounded(False, lv.PART.INDICATOR | lv.STATE.DEFAULT)
label_9_arc_2.set_style_arc_rounded(False, lv.PART.MAIN | lv.STATE.DEFAULT)
# create style style_label_9_arc_2_main_main_default
style_label_9_arc_2_main_main_default = lv.style_t()
style_label_9_arc_2_main_main_default.init()
style_label_9_arc_2_main_main_default.set_radius(6)
style_label_9_arc_2_main_main_default.set_bg_color(lv.color_make(0xf6,0xf6,0xf6))
style_label_9_arc_2_main_main_default.set_bg_grad_color(lv.color_make(0xf6,0xf6,0xf6))
style_label_9_arc_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_arc_2_main_main_default.set_bg_opa(0)
style_label_9_arc_2_main_main_default.set_border_width(0)
style_label_9_arc_2_main_main_default.set_pad_left(20)
style_label_9_arc_2_main_main_default.set_pad_right(20)
style_label_9_arc_2_main_main_default.set_pad_top(20)
style_label_9_arc_2_main_main_default.set_pad_bottom(20)
style_label_9_arc_2_main_main_default.set_arc_color(lv.color_make(0x75,0x73,0x80))
style_label_9_arc_2_main_main_default.set_arc_width(4)

# add style for label_9_arc_2
label_9_arc_2.add_style(style_label_9_arc_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_label_9_arc_2_main_indicator_default
style_label_9_arc_2_main_indicator_default = lv.style_t()
style_label_9_arc_2_main_indicator_default.init()
style_label_9_arc_2_main_indicator_default.set_arc_color(lv.color_make(0x39,0xbb,0x8d))
style_label_9_arc_2_main_indicator_default.set_arc_width(4)

# add style for label_9_arc_2
label_9_arc_2.add_style(style_label_9_arc_2_main_indicator_default, lv.PART.INDICATOR|lv.STATE.DEFAULT)

# create style style_label_9_arc_2_main_knob_default
style_label_9_arc_2_main_knob_default = lv.style_t()
style_label_9_arc_2_main_knob_default.init()
style_label_9_arc_2_main_knob_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_arc_2_main_knob_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_arc_2_main_knob_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_arc_2_main_knob_default.set_bg_opa(0)
style_label_9_arc_2_main_knob_default.set_pad_all(0)

# add style for label_9_arc_2
label_9_arc_2.add_style(style_label_9_arc_2_main_knob_default, lv.PART.KNOB|lv.STATE.DEFAULT)

label_9_label_4 = lv.label(label_9)
label_9_label_4.set_pos(int(64),int(3))
label_9_label_4.set_size(56,25)
label_9_label_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_label_4.set_text("温度")
label_9_label_4.set_long_mode(lv.label.LONG.WRAP)
# create style style_label_9_label_4_main_main_default
style_label_9_label_4_main_main_default = lv.style_t()
style_label_9_label_4_main_main_default.init()
style_label_9_label_4_main_main_default.set_radius(0)
style_label_9_label_4_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_4_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_4_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_label_4_main_main_default.set_bg_opa(0)
style_label_9_label_4_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_label_9_label_4_main_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_label_9_label_4_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_label_9_label_4_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_label_4_main_main_default.set_text_letter_space(0)
style_label_9_label_4_main_main_default.set_text_line_space(0)
style_label_9_label_4_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_label_4_main_main_default.set_pad_left(0)
style_label_9_label_4_main_main_default.set_pad_right(0)
style_label_9_label_4_main_main_default.set_pad_top(8)
style_label_9_label_4_main_main_default.set_pad_bottom(0)

# add style for label_9_label_4
label_9_label_4.add_style(style_label_9_label_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_label_6 = lv.label(label_9)
label_9_label_6.set_pos(int(80),int(33))
label_9_label_6.set_size(25,25)
label_9_label_6.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_label_6.set_text("45℃")
label_9_label_6.set_long_mode(lv.label.LONG.WRAP)
# create style style_label_9_label_6_main_main_default
style_label_9_label_6_main_main_default = lv.style_t()
style_label_9_label_6_main_main_default.init()
style_label_9_label_6_main_main_default.set_radius(0)
style_label_9_label_6_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_6_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_6_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_label_6_main_main_default.set_bg_opa(0)
style_label_9_label_6_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_label_9_label_6_main_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_label_9_label_6_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_label_9_label_6_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_label_6_main_main_default.set_text_letter_space(0)
style_label_9_label_6_main_main_default.set_text_line_space(0)
style_label_9_label_6_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_label_6_main_main_default.set_pad_left(0)
style_label_9_label_6_main_main_default.set_pad_right(0)
style_label_9_label_6_main_main_default.set_pad_top(8)
style_label_9_label_6_main_main_default.set_pad_bottom(0)

# add style for label_9_label_6
label_9_label_6.add_style(style_label_9_label_6_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_label_7 = lv.label(label_9)
label_9_label_7.set_pos(int(127),int(12))
label_9_label_7.set_size(44,11)
label_9_label_7.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_label_7.set_text("硬盘1:")
label_9_label_7.set_long_mode(lv.label.LONG.WRAP)
# create style style_label_9_label_7_main_main_default
style_label_9_label_7_main_main_default = lv.style_t()
style_label_9_label_7_main_main_default.init()
style_label_9_label_7_main_main_default.set_radius(0)
style_label_9_label_7_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_7_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_7_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_label_7_main_main_default.set_bg_opa(0)
style_label_9_label_7_main_main_default.set_text_color(lv.color_make(0x99,0x96,0xab))
try:
    style_label_9_label_7_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_label_9_label_7_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_label_9_label_7_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_label_7_main_main_default.set_text_letter_space(0)
style_label_9_label_7_main_main_default.set_text_line_space(0)
style_label_9_label_7_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_label_7_main_main_default.set_pad_left(0)
style_label_9_label_7_main_main_default.set_pad_right(0)
style_label_9_label_7_main_main_default.set_pad_top(0)
style_label_9_label_7_main_main_default.set_pad_bottom(0)

# add style for label_9_label_7
label_9_label_7.add_style(style_label_9_label_7_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_arc_3 = lv.arc(label_9)
label_9_arc_3.set_pos(int(-7),int(6))
label_9_arc_3.set_size(79,100)
label_9_arc_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_arc_3.set_mode(lv.arc.MODE.NORMAL)
label_9_arc_3.set_range(0, 100)
label_9_arc_3.set_bg_angles(0, 360)
label_9_arc_3.set_angles(270, 180)
label_9_arc_3.set_rotation(0)
label_9_arc_3.set_style_arc_rounded(False, lv.PART.INDICATOR | lv.STATE.DEFAULT)
label_9_arc_3.set_style_arc_rounded(False, lv.PART.MAIN | lv.STATE.DEFAULT)
# create style style_label_9_arc_3_main_main_default
style_label_9_arc_3_main_main_default = lv.style_t()
style_label_9_arc_3_main_main_default.init()
style_label_9_arc_3_main_main_default.set_radius(6)
style_label_9_arc_3_main_main_default.set_bg_color(lv.color_make(0xf6,0xf6,0xf6))
style_label_9_arc_3_main_main_default.set_bg_grad_color(lv.color_make(0xf6,0xf6,0xf6))
style_label_9_arc_3_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_arc_3_main_main_default.set_bg_opa(0)
style_label_9_arc_3_main_main_default.set_border_width(0)
style_label_9_arc_3_main_main_default.set_pad_left(20)
style_label_9_arc_3_main_main_default.set_pad_right(20)
style_label_9_arc_3_main_main_default.set_pad_top(20)
style_label_9_arc_3_main_main_default.set_pad_bottom(20)
style_label_9_arc_3_main_main_default.set_arc_color(lv.color_make(0x75,0x73,0x80))
style_label_9_arc_3_main_main_default.set_arc_width(4)

# add style for label_9_arc_3
label_9_arc_3.add_style(style_label_9_arc_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_label_9_arc_3_main_indicator_default
style_label_9_arc_3_main_indicator_default = lv.style_t()
style_label_9_arc_3_main_indicator_default.init()
style_label_9_arc_3_main_indicator_default.set_arc_color(lv.color_make(0xf2,0x7e,0x05))
style_label_9_arc_3_main_indicator_default.set_arc_width(4)

# add style for label_9_arc_3
label_9_arc_3.add_style(style_label_9_arc_3_main_indicator_default, lv.PART.INDICATOR|lv.STATE.DEFAULT)

# create style style_label_9_arc_3_main_knob_default
style_label_9_arc_3_main_knob_default = lv.style_t()
style_label_9_arc_3_main_knob_default.init()
style_label_9_arc_3_main_knob_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_arc_3_main_knob_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_arc_3_main_knob_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_arc_3_main_knob_default.set_bg_opa(0)
style_label_9_arc_3_main_knob_default.set_pad_all(0)

# add style for label_9_arc_3
label_9_arc_3.add_style(style_label_9_arc_3_main_knob_default, lv.PART.KNOB|lv.STATE.DEFAULT)

label_9_label_8 = lv.label(label_9)
label_9_label_8.set_pos(int(127),int(32))
label_9_label_8.set_size(42,11)
label_9_label_8.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_label_8.set_text("硬盘2:")
label_9_label_8.set_long_mode(lv.label.LONG.WRAP)
# create style style_label_9_label_8_main_main_default
style_label_9_label_8_main_main_default = lv.style_t()
style_label_9_label_8_main_main_default.init()
style_label_9_label_8_main_main_default.set_radius(0)
style_label_9_label_8_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_8_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_8_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_label_8_main_main_default.set_bg_opa(0)
style_label_9_label_8_main_main_default.set_text_color(lv.color_make(0x99,0x96,0xab))
try:
    style_label_9_label_8_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_label_9_label_8_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_label_9_label_8_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_label_8_main_main_default.set_text_letter_space(0)
style_label_9_label_8_main_main_default.set_text_line_space(0)
style_label_9_label_8_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_label_8_main_main_default.set_pad_left(0)
style_label_9_label_8_main_main_default.set_pad_right(0)
style_label_9_label_8_main_main_default.set_pad_top(0)
style_label_9_label_8_main_main_default.set_pad_bottom(0)

# add style for label_9_label_8
label_9_label_8.add_style(style_label_9_label_8_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_label_3 = lv.label(label_9)
label_9_label_3.set_pos(int(5),int(3))
label_9_label_3.set_size(56,25)
label_9_label_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_label_3.set_text("CPU")
label_9_label_3.set_long_mode(lv.label.LONG.WRAP)
# create style style_label_9_label_3_main_main_default
style_label_9_label_3_main_main_default = lv.style_t()
style_label_9_label_3_main_main_default.init()
style_label_9_label_3_main_main_default.set_radius(0)
style_label_9_label_3_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_3_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_3_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_label_3_main_main_default.set_bg_opa(0)
style_label_9_label_3_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_label_9_label_3_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_label_9_label_3_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_label_9_label_3_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_label_3_main_main_default.set_text_letter_space(0)
style_label_9_label_3_main_main_default.set_text_line_space(0)
style_label_9_label_3_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_label_3_main_main_default.set_pad_left(0)
style_label_9_label_3_main_main_default.set_pad_right(0)
style_label_9_label_3_main_main_default.set_pad_top(8)
style_label_9_label_3_main_main_default.set_pad_bottom(0)

# add style for label_9_label_3
label_9_label_3.add_style(style_label_9_label_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_label_9 = lv.label(label_9)
label_9_label_9.set_pos(int(127),int(52))
label_9_label_9.set_size(42,11)
label_9_label_9.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_label_9.set_text("硬盘1:")
label_9_label_9.set_long_mode(lv.label.LONG.WRAP)
# create style style_label_9_label_9_main_main_default
style_label_9_label_9_main_main_default = lv.style_t()
style_label_9_label_9_main_main_default.init()
style_label_9_label_9_main_main_default.set_radius(0)
style_label_9_label_9_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_9_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_9_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_label_9_main_main_default.set_bg_opa(0)
style_label_9_label_9_main_main_default.set_text_color(lv.color_make(0x99,0x96,0xab))
try:
    style_label_9_label_9_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_label_9_label_9_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_label_9_label_9_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_label_9_main_main_default.set_text_letter_space(0)
style_label_9_label_9_main_main_default.set_text_line_space(0)
style_label_9_label_9_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_label_9_main_main_default.set_pad_left(0)
style_label_9_label_9_main_main_default.set_pad_right(0)
style_label_9_label_9_main_main_default.set_pad_top(0)
style_label_9_label_9_main_main_default.set_pad_bottom(0)

# add style for label_9_label_9
label_9_label_9.add_style(style_label_9_label_9_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_bar_1 = lv.bar(label_9)
label_9_bar_1.set_pos(int(169),int(13))
label_9_bar_1.set_size(45,10)
label_9_bar_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_bar_1.set_style_anim_time(1000, 0)
label_9_bar_1.set_mode(lv.bar.MODE.NORMAL)
label_9_bar_1.set_value(50, lv.ANIM.OFF)
# create style style_label_9_bar_1_main_main_default
style_label_9_bar_1_main_main_default = lv.style_t()
style_label_9_bar_1_main_main_default.init()
style_label_9_bar_1_main_main_default.set_radius(10)
style_label_9_bar_1_main_main_default.set_bg_color(lv.color_make(0x2a,0x29,0x39))
style_label_9_bar_1_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_bar_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_bar_1_main_main_default.set_bg_opa(255)

# add style for label_9_bar_1
label_9_bar_1.add_style(style_label_9_bar_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_label_9_bar_1_main_indicator_default
style_label_9_bar_1_main_indicator_default = lv.style_t()
style_label_9_bar_1_main_indicator_default.init()
style_label_9_bar_1_main_indicator_default.set_radius(10)
style_label_9_bar_1_main_indicator_default.set_bg_color(lv.color_make(0x60,0xe4,0xb3))
style_label_9_bar_1_main_indicator_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_bar_1_main_indicator_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_bar_1_main_indicator_default.set_bg_opa(255)

# add style for label_9_bar_1
label_9_bar_1.add_style(style_label_9_bar_1_main_indicator_default, lv.PART.INDICATOR|lv.STATE.DEFAULT)

label_9_label_5 = lv.label(label_9)
label_9_label_5.set_pos(int(20),int(33))
label_9_label_5.set_size(25,25)
label_9_label_5.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_label_5.set_text("90%")
label_9_label_5.set_long_mode(lv.label.LONG.WRAP)
# create style style_label_9_label_5_main_main_default
style_label_9_label_5_main_main_default = lv.style_t()
style_label_9_label_5_main_main_default.init()
style_label_9_label_5_main_main_default.set_radius(0)
style_label_9_label_5_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_5_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_5_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_label_5_main_main_default.set_bg_opa(0)
style_label_9_label_5_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_label_9_label_5_main_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_label_9_label_5_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_label_9_label_5_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_label_5_main_main_default.set_text_letter_space(0)
style_label_9_label_5_main_main_default.set_text_line_space(0)
style_label_9_label_5_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_label_5_main_main_default.set_pad_left(0)
style_label_9_label_5_main_main_default.set_pad_right(0)
style_label_9_label_5_main_main_default.set_pad_top(8)
style_label_9_label_5_main_main_default.set_pad_bottom(0)

# add style for label_9_label_5
label_9_label_5.add_style(style_label_9_label_5_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_bar_2 = lv.bar(label_9)
label_9_bar_2.set_pos(int(169),int(33))
label_9_bar_2.set_size(45,10)
label_9_bar_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_bar_2.set_style_anim_time(1000, 0)
label_9_bar_2.set_mode(lv.bar.MODE.NORMAL)
label_9_bar_2.set_value(70, lv.ANIM.OFF)
# create style style_label_9_bar_2_main_main_default
style_label_9_bar_2_main_main_default = lv.style_t()
style_label_9_bar_2_main_main_default.init()
style_label_9_bar_2_main_main_default.set_radius(10)
style_label_9_bar_2_main_main_default.set_bg_color(lv.color_make(0x2a,0x29,0x39))
style_label_9_bar_2_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_bar_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_bar_2_main_main_default.set_bg_opa(255)

# add style for label_9_bar_2
label_9_bar_2.add_style(style_label_9_bar_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_label_9_bar_2_main_indicator_default
style_label_9_bar_2_main_indicator_default = lv.style_t()
style_label_9_bar_2_main_indicator_default.init()
style_label_9_bar_2_main_indicator_default.set_radius(10)
style_label_9_bar_2_main_indicator_default.set_bg_color(lv.color_make(0xf5,0x91,0x1f))
style_label_9_bar_2_main_indicator_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_bar_2_main_indicator_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_bar_2_main_indicator_default.set_bg_opa(255)

# add style for label_9_bar_2
label_9_bar_2.add_style(style_label_9_bar_2_main_indicator_default, lv.PART.INDICATOR|lv.STATE.DEFAULT)

label_9_bar_3 = lv.bar(label_9)
label_9_bar_3.set_pos(int(169),int(53))
label_9_bar_3.set_size(45,10)
label_9_bar_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_bar_3.set_style_anim_time(1000, 0)
label_9_bar_3.set_mode(lv.bar.MODE.NORMAL)
label_9_bar_3.set_value(0, lv.ANIM.OFF)
# create style style_label_9_bar_3_main_main_default
style_label_9_bar_3_main_main_default = lv.style_t()
style_label_9_bar_3_main_main_default.init()
style_label_9_bar_3_main_main_default.set_radius(10)
style_label_9_bar_3_main_main_default.set_bg_color(lv.color_make(0x2a,0x29,0x39))
style_label_9_bar_3_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_bar_3_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_bar_3_main_main_default.set_bg_opa(255)

# add style for label_9_bar_3
label_9_bar_3.add_style(style_label_9_bar_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_label_9_bar_3_main_indicator_default
style_label_9_bar_3_main_indicator_default = lv.style_t()
style_label_9_bar_3_main_indicator_default.init()
style_label_9_bar_3_main_indicator_default.set_radius(10)
style_label_9_bar_3_main_indicator_default.set_bg_color(lv.color_make(0xf6,0xef,0x23))
style_label_9_bar_3_main_indicator_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_bar_3_main_indicator_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_bar_3_main_indicator_default.set_bg_opa(255)

# add style for label_9_bar_3
label_9_bar_3.add_style(style_label_9_bar_3_main_indicator_default, lv.PART.INDICATOR|lv.STATE.DEFAULT)

label_9_label_10 = lv.label(label_9)
label_9_label_10.set_pos(int(222),int(12))
label_9_label_10.set_size(45,11)
label_9_label_10.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_label_10.set_text("134G/848G")
label_9_label_10.set_long_mode(lv.label.LONG.WRAP)
# create style style_label_9_label_10_main_main_default
style_label_9_label_10_main_main_default = lv.style_t()
style_label_9_label_10_main_main_default.init()
style_label_9_label_10_main_main_default.set_radius(0)
style_label_9_label_10_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_10_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_10_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_label_10_main_main_default.set_bg_opa(0)
style_label_9_label_10_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_label_9_label_10_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_label_9_label_10_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_label_9_label_10_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_label_10_main_main_default.set_text_letter_space(0)
style_label_9_label_10_main_main_default.set_text_line_space(0)
style_label_9_label_10_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_label_10_main_main_default.set_pad_left(0)
style_label_9_label_10_main_main_default.set_pad_right(0)
style_label_9_label_10_main_main_default.set_pad_top(0)
style_label_9_label_10_main_main_default.set_pad_bottom(0)

# add style for label_9_label_10
label_9_label_10.add_style(style_label_9_label_10_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_label_11 = lv.label(label_9)
label_9_label_11.set_pos(int(222),int(32))
label_9_label_11.set_size(45,11)
label_9_label_11.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_label_11.set_text("734G/848G")
label_9_label_11.set_long_mode(lv.label.LONG.WRAP)
# create style style_label_9_label_11_main_main_default
style_label_9_label_11_main_main_default = lv.style_t()
style_label_9_label_11_main_main_default.init()
style_label_9_label_11_main_main_default.set_radius(0)
style_label_9_label_11_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_11_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_11_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_label_11_main_main_default.set_bg_opa(0)
style_label_9_label_11_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_label_9_label_11_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_label_9_label_11_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_label_9_label_11_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_label_11_main_main_default.set_text_letter_space(0)
style_label_9_label_11_main_main_default.set_text_line_space(0)
style_label_9_label_11_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_label_11_main_main_default.set_pad_left(0)
style_label_9_label_11_main_main_default.set_pad_right(0)
style_label_9_label_11_main_main_default.set_pad_top(0)
style_label_9_label_11_main_main_default.set_pad_bottom(0)

# add style for label_9_label_11
label_9_label_11.add_style(style_label_9_label_11_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_label_12 = lv.label(label_9)
label_9_label_12.set_pos(int(222),int(52))
label_9_label_12.set_size(45,11)
label_9_label_12.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_label_12.set_text("--/--")
label_9_label_12.set_long_mode(lv.label.LONG.WRAP)
# create style style_label_9_label_12_main_main_default
style_label_9_label_12_main_main_default = lv.style_t()
style_label_9_label_12_main_main_default.init()
style_label_9_label_12_main_main_default.set_radius(0)
style_label_9_label_12_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_12_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_12_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_label_12_main_main_default.set_bg_opa(0)
style_label_9_label_12_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_label_9_label_12_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_label_9_label_12_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_label_9_label_12_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_label_12_main_main_default.set_text_letter_space(0)
style_label_9_label_12_main_main_default.set_text_line_space(0)
style_label_9_label_12_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_label_12_main_main_default.set_pad_left(0)
style_label_9_label_12_main_main_default.set_pad_right(0)
style_label_9_label_12_main_main_default.set_pad_top(0)
style_label_9_label_12_main_main_default.set_pad_bottom(0)

# add style for label_9_label_12
label_9_label_12.add_style(style_label_9_label_12_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_label_13 = lv.label(label_9)
label_9_label_13.set_pos(int(127),int(52))
label_9_label_13.set_size(42,11)
label_9_label_13.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
label_9_label_13.set_text("硬盘3:")
label_9_label_13.set_long_mode(lv.label.LONG.WRAP)
# create style style_label_9_label_13_main_main_default
style_label_9_label_13_main_main_default = lv.style_t()
style_label_9_label_13_main_main_default.init()
style_label_9_label_13_main_main_default.set_radius(0)
style_label_9_label_13_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_13_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_label_13_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_label_13_main_main_default.set_bg_opa(0)
style_label_9_label_13_main_main_default.set_text_color(lv.color_make(0x99,0x96,0xab))
try:
    style_label_9_label_13_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_label_9_label_13_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_label_9_label_13_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_label_13_main_main_default.set_text_letter_space(0)
style_label_9_label_13_main_main_default.set_text_line_space(0)
style_label_9_label_13_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_label_9_label_13_main_main_default.set_pad_left(0)
style_label_9_label_13_main_main_default.set_pad_right(0)
style_label_9_label_13_main_main_default.set_pad_top(0)
style_label_9_label_13_main_main_default.set_pad_bottom(0)

# add style for label_9_label_13
label_9_label_13.add_style(style_label_9_label_13_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

label_9_btn_1 = lv.btn(label_9)
label_9_btn_1.set_pos(int(0),int(0))
label_9_btn_1.set_size(284,76)
label_9_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_label_9_btn_1_main_main_default
style_label_9_btn_1_main_main_default = lv.style_t()
style_label_9_btn_1_main_main_default.init()
style_label_9_btn_1_main_main_default.set_radius(5)
style_label_9_btn_1_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_btn_1_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_btn_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_label_9_btn_1_main_main_default.set_bg_opa(0)
style_label_9_btn_1_main_main_default.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_label_9_btn_1_main_main_default.set_border_width(0)
style_label_9_btn_1_main_main_default.set_border_opa(255)
style_label_9_btn_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_label_9_btn_1_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_label_9_btn_1_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_label_9_btn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_label_9_btn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for label_9_btn_1
label_9_btn_1.add_style(style_label_9_btn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1 = lv.obj()
screen_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_screen_1_main_main_default
style_screen_1_main_main_default = lv.style_t()
style_screen_1_main_main_default.init()
style_screen_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_1_main_main_default.set_bg_opa(255)

# add style for screen_1
screen_1.add_style(style_screen_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_label_11 = lv.label(screen_1)
screen_1_label_11.set_pos(int(0),int(0))
screen_1_label_11.set_size(284,76)
screen_1_label_11.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_1_label_11.set_text("Label")
screen_1_label_11.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_1_label_11_main_main_default
style_screen_1_label_11_main_main_default = lv.style_t()
style_screen_1_label_11_main_main_default.init()
style_screen_1_label_11_main_main_default.set_radius(0)
style_screen_1_label_11_main_main_default.set_bg_color(lv.color_make(0x00,0x00,0x00))
style_screen_1_label_11_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_label_11_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_1_label_11_main_main_default.set_bg_opa(255)
style_screen_1_label_11_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_1_label_11_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_screen_1_label_11_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_screen_1_label_11_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_1_label_11_main_main_default.set_text_letter_space(2)
style_screen_1_label_11_main_main_default.set_text_line_space(0)
style_screen_1_label_11_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_1_label_11_main_main_default.set_pad_left(0)
style_screen_1_label_11_main_main_default.set_pad_right(0)
style_screen_1_label_11_main_main_default.set_pad_top(8)
style_screen_1_label_11_main_main_default.set_pad_bottom(0)

# add style for screen_1_label_11
screen_1_label_11.add_style(style_screen_1_label_11_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_img_9 = lv.img(screen_1)
screen_1_img_9.set_pos(int(6),int(8))
screen_1_img_9.set_size(273,64)
screen_1_img_9.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_1_img_9.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp-1327084711.png','rb') as f:
        screen_1_img_9_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp-1327084711.png')
    sys.exit()

screen_1_img_9_img = lv.img_dsc_t({
  'data_size': len(screen_1_img_9_img_data),
  'header': {'always_zero': 0, 'w': 273, 'h': 64, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_1_img_9_img_data
})

screen_1_img_9.set_src(screen_1_img_9_img)
screen_1_img_9.set_pivot(50,50)
screen_1_img_9.set_angle(0)
# create style style_screen_1_img_9_main_main_default
style_screen_1_img_9_main_main_default = lv.style_t()
style_screen_1_img_9_main_main_default.init()
style_screen_1_img_9_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_1_img_9_main_main_default.set_img_recolor_opa(0)
style_screen_1_img_9_main_main_default.set_img_opa(255)

# add style for screen_1_img_9
screen_1_img_9.add_style(style_screen_1_img_9_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_img_14 = lv.img(screen_1)
screen_1_img_14.set_pos(int(222),int(38))
screen_1_img_14.set_size(57,34)
screen_1_img_14.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_1_img_14.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png','rb') as f:
        screen_1_img_14_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png')
    sys.exit()

screen_1_img_14_img = lv.img_dsc_t({
  'data_size': len(screen_1_img_14_img_data),
  'header': {'always_zero': 0, 'w': 57, 'h': 34, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_1_img_14_img_data
})

screen_1_img_14.set_src(screen_1_img_14_img)
screen_1_img_14.set_pivot(50,50)
screen_1_img_14.set_angle(0)
# create style style_screen_1_img_14_main_main_default
style_screen_1_img_14_main_main_default = lv.style_t()
style_screen_1_img_14_main_main_default.init()
style_screen_1_img_14_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_1_img_14_main_main_default.set_img_recolor_opa(0)
style_screen_1_img_14_main_main_default.set_img_opa(255)

# add style for screen_1_img_14
screen_1_img_14.add_style(style_screen_1_img_14_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_img_13 = lv.img(screen_1)
screen_1_img_13.set_pos(int(6),int(38))
screen_1_img_13.set_size(57,34)
screen_1_img_13.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_1_img_13.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png','rb') as f:
        screen_1_img_13_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png')
    sys.exit()

screen_1_img_13_img = lv.img_dsc_t({
  'data_size': len(screen_1_img_13_img_data),
  'header': {'always_zero': 0, 'w': 57, 'h': 34, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_1_img_13_img_data
})

screen_1_img_13.set_src(screen_1_img_13_img)
screen_1_img_13.set_pivot(50,50)
screen_1_img_13.set_angle(0)
# create style style_screen_1_img_13_main_main_default
style_screen_1_img_13_main_main_default = lv.style_t()
style_screen_1_img_13_main_main_default.init()
style_screen_1_img_13_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_1_img_13_main_main_default.set_img_recolor_opa(0)
style_screen_1_img_13_main_main_default.set_img_opa(255)

# add style for screen_1_img_13
screen_1_img_13.add_style(style_screen_1_img_13_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_img_16 = lv.img(screen_1)
screen_1_img_16.set_pos(int(6),int(8))
screen_1_img_16.set_size(57,34)
screen_1_img_16.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_1_img_16.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png','rb') as f:
        screen_1_img_16_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png')
    sys.exit()

screen_1_img_16_img = lv.img_dsc_t({
  'data_size': len(screen_1_img_16_img_data),
  'header': {'always_zero': 0, 'w': 57, 'h': 34, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_1_img_16_img_data
})

screen_1_img_16.set_src(screen_1_img_16_img)
screen_1_img_16.set_pivot(50,50)
screen_1_img_16.set_angle(0)
# create style style_screen_1_img_16_main_main_default
style_screen_1_img_16_main_main_default = lv.style_t()
style_screen_1_img_16_main_main_default.init()
style_screen_1_img_16_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_1_img_16_main_main_default.set_img_recolor_opa(0)
style_screen_1_img_16_main_main_default.set_img_opa(255)

# add style for screen_1_img_16
screen_1_img_16.add_style(style_screen_1_img_16_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_img_17 = lv.img(screen_1)
screen_1_img_17.set_pos(int(222),int(8))
screen_1_img_17.set_size(57,34)
screen_1_img_17.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_1_img_17.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png','rb') as f:
        screen_1_img_17_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png')
    sys.exit()

screen_1_img_17_img = lv.img_dsc_t({
  'data_size': len(screen_1_img_17_img_data),
  'header': {'always_zero': 0, 'w': 57, 'h': 34, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_1_img_17_img_data
})

screen_1_img_17.set_src(screen_1_img_17_img)
screen_1_img_17.set_pivot(50,50)
screen_1_img_17.set_angle(0)
# create style style_screen_1_img_17_main_main_default
style_screen_1_img_17_main_main_default = lv.style_t()
style_screen_1_img_17_main_main_default.init()
style_screen_1_img_17_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_1_img_17_main_main_default.set_img_recolor_opa(0)
style_screen_1_img_17_main_main_default.set_img_opa(255)

# add style for screen_1_img_17
screen_1_img_17.add_style(style_screen_1_img_17_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_label_10 = lv.label(screen_1)
screen_1_label_10.set_pos(int(7),int(23))
screen_1_label_10.set_size(271,45)
screen_1_label_10.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_screen_1_label_10_main_main_default
style_screen_1_label_10_main_main_default = lv.style_t()
style_screen_1_label_10_main_main_default.init()
style_screen_1_label_10_main_main_default.set_radius(0)
style_screen_1_label_10_main_main_default.set_bg_color(lv.color_make(0x14,0x11,0x26))
style_screen_1_label_10_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_label_10_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_1_label_10_main_main_default.set_bg_opa(255)
style_screen_1_label_10_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_1_label_10_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_screen_1_label_10_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_screen_1_label_10_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_1_label_10_main_main_default.set_text_letter_space(0)
style_screen_1_label_10_main_main_default.set_text_line_space(0)
style_screen_1_label_10_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_screen_1_label_10_main_main_default.set_pad_left(0)
style_screen_1_label_10_main_main_default.set_pad_right(7)
style_screen_1_label_10_main_main_default.set_pad_top(0)
style_screen_1_label_10_main_main_default.set_pad_bottom(0)

# add style for screen_1_label_10
screen_1_label_10.add_style(style_screen_1_label_10_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_img_10 = lv.img(screen_1)
screen_1_img_10.set_pos(int(7),int(35))
screen_1_img_10.set_size(57,36)
screen_1_img_10.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_1_img_10.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp477530338.png','rb') as f:
        screen_1_img_10_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp477530338.png')
    sys.exit()

screen_1_img_10_img = lv.img_dsc_t({
  'data_size': len(screen_1_img_10_img_data),
  'header': {'always_zero': 0, 'w': 57, 'h': 36, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_1_img_10_img_data
})

screen_1_img_10.set_src(screen_1_img_10_img)
screen_1_img_10.set_pivot(50,50)
screen_1_img_10.set_angle(0)
# create style style_screen_1_img_10_main_main_default
style_screen_1_img_10_main_main_default = lv.style_t()
style_screen_1_img_10_main_main_default.init()
style_screen_1_img_10_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_1_img_10_main_main_default.set_img_recolor_opa(0)
style_screen_1_img_10_main_main_default.set_img_opa(255)

# add style for screen_1_img_10
screen_1_img_10.add_style(style_screen_1_img_10_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_img_11 = lv.img(screen_1)
screen_1_img_11.set_pos(int(42),int(35))
screen_1_img_11.set_size(200,36)
screen_1_img_11.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_1_img_11.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp-296662622.png','rb') as f:
        screen_1_img_11_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp-296662622.png')
    sys.exit()

screen_1_img_11_img = lv.img_dsc_t({
  'data_size': len(screen_1_img_11_img_data),
  'header': {'always_zero': 0, 'w': 200, 'h': 36, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_1_img_11_img_data
})

screen_1_img_11.set_src(screen_1_img_11_img)
screen_1_img_11.set_pivot(50,50)
screen_1_img_11.set_angle(0)
# create style style_screen_1_img_11_main_main_default
style_screen_1_img_11_main_main_default = lv.style_t()
style_screen_1_img_11_main_main_default.init()
style_screen_1_img_11_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_1_img_11_main_main_default.set_img_recolor_opa(0)
style_screen_1_img_11_main_main_default.set_img_opa(255)

# add style for screen_1_img_11
screen_1_img_11.add_style(style_screen_1_img_11_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_img_15 = lv.img(screen_1)
screen_1_img_15.set_pos(int(221),int(35))
screen_1_img_15.set_size(57,36)
screen_1_img_15.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_1_img_15.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp477530338.png','rb') as f:
        screen_1_img_15_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp477530338.png')
    sys.exit()

screen_1_img_15_img = lv.img_dsc_t({
  'data_size': len(screen_1_img_15_img_data),
  'header': {'always_zero': 0, 'w': 57, 'h': 36, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_1_img_15_img_data
})

screen_1_img_15.set_src(screen_1_img_15_img)
screen_1_img_15.set_pivot(50,50)
screen_1_img_15.set_angle(0)
# create style style_screen_1_img_15_main_main_default
style_screen_1_img_15_main_main_default = lv.style_t()
style_screen_1_img_15_main_main_default.init()
style_screen_1_img_15_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_1_img_15_main_main_default.set_img_recolor_opa(0)
style_screen_1_img_15_main_main_default.set_img_opa(255)

# add style for screen_1_img_15
screen_1_img_15.add_style(style_screen_1_img_15_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_label_12 = lv.label(screen_1)
screen_1_label_12.set_pos(int(8),int(7))
screen_1_label_12.set_size(45,18)
screen_1_label_12.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_1_label_12.set_text("IP地址")
screen_1_label_12.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_1_label_12_main_main_default
style_screen_1_label_12_main_main_default = lv.style_t()
style_screen_1_label_12_main_main_default.init()
style_screen_1_label_12_main_main_default.set_radius(0)
style_screen_1_label_12_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_label_12_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_label_12_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_1_label_12_main_main_default.set_bg_opa(0)
style_screen_1_label_12_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_1_label_12_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_screen_1_label_12_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_1_label_12_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_1_label_12_main_main_default.set_text_letter_space(2)
style_screen_1_label_12_main_main_default.set_text_line_space(0)
style_screen_1_label_12_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_1_label_12_main_main_default.set_pad_left(0)
style_screen_1_label_12_main_main_default.set_pad_right(0)
style_screen_1_label_12_main_main_default.set_pad_top(3)
style_screen_1_label_12_main_main_default.set_pad_bottom(0)

# add style for screen_1_label_12
screen_1_label_12.add_style(style_screen_1_label_12_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_label_9 = lv.label(screen_1)
screen_1_label_9.set_pos(int(18),int(51))
screen_1_label_9.set_size(284,11)
screen_1_label_9.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_1_label_9.set_text("IPv6 : xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx")
screen_1_label_9.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_1_label_9_main_main_default
style_screen_1_label_9_main_main_default = lv.style_t()
style_screen_1_label_9_main_main_default.init()
style_screen_1_label_9_main_main_default.set_radius(0)
style_screen_1_label_9_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_label_9_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_label_9_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_1_label_9_main_main_default.set_bg_opa(0)
style_screen_1_label_9_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_1_label_9_main_main_default.set_text_font(lv.font_arial_10)
except AttributeError:
    try:
        style_screen_1_label_9_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_1_label_9_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_1_label_9_main_main_default.set_text_letter_space(0)
style_screen_1_label_9_main_main_default.set_text_line_space(0)
style_screen_1_label_9_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_screen_1_label_9_main_main_default.set_pad_left(0)
style_screen_1_label_9_main_main_default.set_pad_right(0)
style_screen_1_label_9_main_main_default.set_pad_top(0)
style_screen_1_label_9_main_main_default.set_pad_bottom(0)

# add style for screen_1_label_9
screen_1_label_9.add_style(style_screen_1_label_9_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_label_8 = lv.label(screen_1)
screen_1_label_8.set_pos(int(141),int(33))
screen_1_label_8.set_size(128,9)
screen_1_label_8.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_1_label_8.set_text("DNS : 192.168.100.1")
screen_1_label_8.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_1_label_8_main_main_default
style_screen_1_label_8_main_main_default = lv.style_t()
style_screen_1_label_8_main_main_default.init()
style_screen_1_label_8_main_main_default.set_radius(0)
style_screen_1_label_8_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_label_8_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_label_8_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_1_label_8_main_main_default.set_bg_opa(0)
style_screen_1_label_8_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_1_label_8_main_main_default.set_text_font(lv.font_arial_10)
except AttributeError:
    try:
        style_screen_1_label_8_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_1_label_8_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_1_label_8_main_main_default.set_text_letter_space(0)
style_screen_1_label_8_main_main_default.set_text_line_space(0)
style_screen_1_label_8_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_1_label_8_main_main_default.set_pad_left(0)
style_screen_1_label_8_main_main_default.set_pad_right(0)
style_screen_1_label_8_main_main_default.set_pad_top(0)
style_screen_1_label_8_main_main_default.set_pad_bottom(0)

# add style for screen_1_label_8
screen_1_label_8.add_style(style_screen_1_label_8_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_label_7 = lv.label(screen_1)
screen_1_label_7.set_pos(int(18),int(33))
screen_1_label_7.set_size(128,9)
screen_1_label_7.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_1_label_7.set_text("IPv4 : 192.168.100.1")
screen_1_label_7.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_1_label_7_main_main_default
style_screen_1_label_7_main_main_default = lv.style_t()
style_screen_1_label_7_main_main_default.init()
style_screen_1_label_7_main_main_default.set_radius(0)
style_screen_1_label_7_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_label_7_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_label_7_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_1_label_7_main_main_default.set_bg_opa(0)
style_screen_1_label_7_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_1_label_7_main_main_default.set_text_font(lv.font_arial_10)
except AttributeError:
    try:
        style_screen_1_label_7_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_1_label_7_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_1_label_7_main_main_default.set_text_letter_space(0)
style_screen_1_label_7_main_main_default.set_text_line_space(0)
style_screen_1_label_7_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_screen_1_label_7_main_main_default.set_pad_left(0)
style_screen_1_label_7_main_main_default.set_pad_right(0)
style_screen_1_label_7_main_main_default.set_pad_top(0)
style_screen_1_label_7_main_main_default.set_pad_bottom(0)

# add style for screen_1_label_7
screen_1_label_7.add_style(style_screen_1_label_7_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1_btn_1 = lv.btn(screen_1)
screen_1_btn_1.set_pos(int(0),int(85))
screen_1_btn_1.set_size(284,100)
screen_1_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_screen_1_btn_1_main_main_default
style_screen_1_btn_1_main_main_default = lv.style_t()
style_screen_1_btn_1_main_main_default.init()
style_screen_1_btn_1_main_main_default.set_radius(5)
style_screen_1_btn_1_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_1_btn_1_main_main_default.set_bg_opa(0)
style_screen_1_btn_1_main_main_default.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_default.set_border_width(0)
style_screen_1_btn_1_main_main_default.set_border_opa(0)
style_screen_1_btn_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_1_btn_1_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_screen_1_btn_1_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_screen_1_btn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_1_btn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for screen_1_btn_1
screen_1_btn_1.add_style(style_screen_1_btn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_screen_1_btn_1_main_main_focused
style_screen_1_btn_1_main_main_focused = lv.style_t()
style_screen_1_btn_1_main_main_focused.init()
style_screen_1_btn_1_main_main_focused.set_radius(5)
style_screen_1_btn_1_main_main_focused.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_focused.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_focused.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_1_btn_1_main_main_focused.set_bg_opa(0)
style_screen_1_btn_1_main_main_focused.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_focused.set_border_width(0)
style_screen_1_btn_1_main_main_focused.set_border_opa(0)
style_screen_1_btn_1_main_main_focused.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_1_btn_1_main_main_focused.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_screen_1_btn_1_main_main_focused.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_screen_1_btn_1_main_main_focused.set_text_font(lv.font_montserrat_16)

# add style for screen_1_btn_1
screen_1_btn_1.add_style(style_screen_1_btn_1_main_main_focused, lv.PART.MAIN|lv.STATE.FOCUSED)

# create style style_screen_1_btn_1_main_main_pressed
style_screen_1_btn_1_main_main_pressed = lv.style_t()
style_screen_1_btn_1_main_main_pressed.init()
style_screen_1_btn_1_main_main_pressed.set_radius(5)
style_screen_1_btn_1_main_main_pressed.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_pressed.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_pressed.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_1_btn_1_main_main_pressed.set_bg_opa(0)
style_screen_1_btn_1_main_main_pressed.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_pressed.set_border_width(0)
style_screen_1_btn_1_main_main_pressed.set_border_opa(0)
style_screen_1_btn_1_main_main_pressed.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_1_btn_1_main_main_pressed.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_screen_1_btn_1_main_main_pressed.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_screen_1_btn_1_main_main_pressed.set_text_font(lv.font_montserrat_16)

# add style for screen_1_btn_1
screen_1_btn_1.add_style(style_screen_1_btn_1_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_screen_1_btn_1_main_main_checked
style_screen_1_btn_1_main_main_checked = lv.style_t()
style_screen_1_btn_1_main_main_checked.init()
style_screen_1_btn_1_main_main_checked.set_radius(5)
style_screen_1_btn_1_main_main_checked.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_checked.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_checked.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_1_btn_1_main_main_checked.set_bg_opa(0)
style_screen_1_btn_1_main_main_checked.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_checked.set_border_width(0)
style_screen_1_btn_1_main_main_checked.set_border_opa(0)
style_screen_1_btn_1_main_main_checked.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_1_btn_1_main_main_checked.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_screen_1_btn_1_main_main_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_screen_1_btn_1_main_main_checked.set_text_font(lv.font_montserrat_16)

# add style for screen_1_btn_1
screen_1_btn_1.add_style(style_screen_1_btn_1_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

# create style style_screen_1_btn_1_main_main_disabled
style_screen_1_btn_1_main_main_disabled = lv.style_t()
style_screen_1_btn_1_main_main_disabled.init()
style_screen_1_btn_1_main_main_disabled.set_radius(5)
style_screen_1_btn_1_main_main_disabled.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_disabled.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_disabled.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_1_btn_1_main_main_disabled.set_bg_opa(0)
style_screen_1_btn_1_main_main_disabled.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_screen_1_btn_1_main_main_disabled.set_border_width(0)
style_screen_1_btn_1_main_main_disabled.set_border_opa(0)
style_screen_1_btn_1_main_main_disabled.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_1_btn_1_main_main_disabled.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_screen_1_btn_1_main_main_disabled.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_screen_1_btn_1_main_main_disabled.set_text_font(lv.font_montserrat_16)

# add style for screen_1_btn_1
screen_1_btn_1.add_style(style_screen_1_btn_1_main_main_disabled, lv.PART.MAIN|lv.STATE.DISABLED)

screen_3 = lv.obj()
screen_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_screen_3_main_main_default
style_screen_3_main_main_default = lv.style_t()
style_screen_3_main_main_default.init()
style_screen_3_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_3_main_main_default.set_bg_opa(255)

# add style for screen_3
screen_3.add_style(style_screen_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_11 = lv.label(screen_3)
screen_3_label_11.set_pos(int(0),int(0))
screen_3_label_11.set_size(284,76)
screen_3_label_11.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_label_11.set_text("Label")
screen_3_label_11.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_3_label_11_main_main_default
style_screen_3_label_11_main_main_default = lv.style_t()
style_screen_3_label_11_main_main_default.init()
style_screen_3_label_11_main_main_default.set_radius(0)
style_screen_3_label_11_main_main_default.set_bg_color(lv.color_make(0x00,0x00,0x00))
style_screen_3_label_11_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_11_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_11_main_main_default.set_bg_opa(255)
style_screen_3_label_11_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_3_label_11_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_screen_3_label_11_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_screen_3_label_11_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_11_main_main_default.set_text_letter_space(2)
style_screen_3_label_11_main_main_default.set_text_line_space(0)
style_screen_3_label_11_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_3_label_11_main_main_default.set_pad_left(0)
style_screen_3_label_11_main_main_default.set_pad_right(0)
style_screen_3_label_11_main_main_default.set_pad_top(8)
style_screen_3_label_11_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_11
screen_3_label_11.add_style(style_screen_3_label_11_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_img_9 = lv.img(screen_3)
screen_3_img_9.set_pos(int(6),int(8))
screen_3_img_9.set_size(273,64)
screen_3_img_9.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_img_9.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp-1327084711.png','rb') as f:
        screen_3_img_9_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp-1327084711.png')
    sys.exit()

screen_3_img_9_img = lv.img_dsc_t({
  'data_size': len(screen_3_img_9_img_data),
  'header': {'always_zero': 0, 'w': 273, 'h': 64, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_3_img_9_img_data
})

screen_3_img_9.set_src(screen_3_img_9_img)
screen_3_img_9.set_pivot(50,50)
screen_3_img_9.set_angle(0)
# create style style_screen_3_img_9_main_main_default
style_screen_3_img_9_main_main_default = lv.style_t()
style_screen_3_img_9_main_main_default.init()
style_screen_3_img_9_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_3_img_9_main_main_default.set_img_recolor_opa(0)
style_screen_3_img_9_main_main_default.set_img_opa(255)

# add style for screen_3_img_9
screen_3_img_9.add_style(style_screen_3_img_9_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_img_14 = lv.img(screen_3)
screen_3_img_14.set_pos(int(222),int(38))
screen_3_img_14.set_size(57,34)
screen_3_img_14.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_img_14.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png','rb') as f:
        screen_3_img_14_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png')
    sys.exit()

screen_3_img_14_img = lv.img_dsc_t({
  'data_size': len(screen_3_img_14_img_data),
  'header': {'always_zero': 0, 'w': 57, 'h': 34, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_3_img_14_img_data
})

screen_3_img_14.set_src(screen_3_img_14_img)
screen_3_img_14.set_pivot(50,50)
screen_3_img_14.set_angle(0)
# create style style_screen_3_img_14_main_main_default
style_screen_3_img_14_main_main_default = lv.style_t()
style_screen_3_img_14_main_main_default.init()
style_screen_3_img_14_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_3_img_14_main_main_default.set_img_recolor_opa(0)
style_screen_3_img_14_main_main_default.set_img_opa(255)

# add style for screen_3_img_14
screen_3_img_14.add_style(style_screen_3_img_14_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_img_13 = lv.img(screen_3)
screen_3_img_13.set_pos(int(6),int(38))
screen_3_img_13.set_size(57,34)
screen_3_img_13.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_img_13.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png','rb') as f:
        screen_3_img_13_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png')
    sys.exit()

screen_3_img_13_img = lv.img_dsc_t({
  'data_size': len(screen_3_img_13_img_data),
  'header': {'always_zero': 0, 'w': 57, 'h': 34, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_3_img_13_img_data
})

screen_3_img_13.set_src(screen_3_img_13_img)
screen_3_img_13.set_pivot(50,50)
screen_3_img_13.set_angle(0)
# create style style_screen_3_img_13_main_main_default
style_screen_3_img_13_main_main_default = lv.style_t()
style_screen_3_img_13_main_main_default.init()
style_screen_3_img_13_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_3_img_13_main_main_default.set_img_recolor_opa(0)
style_screen_3_img_13_main_main_default.set_img_opa(255)

# add style for screen_3_img_13
screen_3_img_13.add_style(style_screen_3_img_13_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_img_16 = lv.img(screen_3)
screen_3_img_16.set_pos(int(6),int(8))
screen_3_img_16.set_size(57,34)
screen_3_img_16.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_img_16.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png','rb') as f:
        screen_3_img_16_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png')
    sys.exit()

screen_3_img_16_img = lv.img_dsc_t({
  'data_size': len(screen_3_img_16_img_data),
  'header': {'always_zero': 0, 'w': 57, 'h': 34, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_3_img_16_img_data
})

screen_3_img_16.set_src(screen_3_img_16_img)
screen_3_img_16.set_pivot(50,50)
screen_3_img_16.set_angle(0)
# create style style_screen_3_img_16_main_main_default
style_screen_3_img_16_main_main_default = lv.style_t()
style_screen_3_img_16_main_main_default.init()
style_screen_3_img_16_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_3_img_16_main_main_default.set_img_recolor_opa(0)
style_screen_3_img_16_main_main_default.set_img_opa(255)

# add style for screen_3_img_16
screen_3_img_16.add_style(style_screen_3_img_16_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_img_17 = lv.img(screen_3)
screen_3_img_17.set_pos(int(222),int(8))
screen_3_img_17.set_size(57,34)
screen_3_img_17.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_img_17.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png','rb') as f:
        screen_3_img_17_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp727910240.png')
    sys.exit()

screen_3_img_17_img = lv.img_dsc_t({
  'data_size': len(screen_3_img_17_img_data),
  'header': {'always_zero': 0, 'w': 57, 'h': 34, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_3_img_17_img_data
})

screen_3_img_17.set_src(screen_3_img_17_img)
screen_3_img_17.set_pivot(50,50)
screen_3_img_17.set_angle(0)
# create style style_screen_3_img_17_main_main_default
style_screen_3_img_17_main_main_default = lv.style_t()
style_screen_3_img_17_main_main_default.init()
style_screen_3_img_17_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_3_img_17_main_main_default.set_img_recolor_opa(0)
style_screen_3_img_17_main_main_default.set_img_opa(255)

# add style for screen_3_img_17
screen_3_img_17.add_style(style_screen_3_img_17_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_10 = lv.label(screen_3)
screen_3_label_10.set_pos(int(7),int(23))
screen_3_label_10.set_size(271,45)
screen_3_label_10.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_screen_3_label_10_main_main_default
style_screen_3_label_10_main_main_default = lv.style_t()
style_screen_3_label_10_main_main_default.init()
style_screen_3_label_10_main_main_default.set_radius(0)
style_screen_3_label_10_main_main_default.set_bg_color(lv.color_make(0x14,0x11,0x26))
style_screen_3_label_10_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_10_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_10_main_main_default.set_bg_opa(255)
style_screen_3_label_10_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_3_label_10_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_screen_3_label_10_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_screen_3_label_10_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_10_main_main_default.set_text_letter_space(0)
style_screen_3_label_10_main_main_default.set_text_line_space(0)
style_screen_3_label_10_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_screen_3_label_10_main_main_default.set_pad_left(0)
style_screen_3_label_10_main_main_default.set_pad_right(7)
style_screen_3_label_10_main_main_default.set_pad_top(0)
style_screen_3_label_10_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_10
screen_3_label_10.add_style(style_screen_3_label_10_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_img_10 = lv.img(screen_3)
screen_3_img_10.set_pos(int(7),int(35))
screen_3_img_10.set_size(57,36)
screen_3_img_10.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_img_10.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp477530338.png','rb') as f:
        screen_3_img_10_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp477530338.png')
    sys.exit()

screen_3_img_10_img = lv.img_dsc_t({
  'data_size': len(screen_3_img_10_img_data),
  'header': {'always_zero': 0, 'w': 57, 'h': 36, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_3_img_10_img_data
})

screen_3_img_10.set_src(screen_3_img_10_img)
screen_3_img_10.set_pivot(50,50)
screen_3_img_10.set_angle(0)
# create style style_screen_3_img_10_main_main_default
style_screen_3_img_10_main_main_default = lv.style_t()
style_screen_3_img_10_main_main_default.init()
style_screen_3_img_10_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_3_img_10_main_main_default.set_img_recolor_opa(0)
style_screen_3_img_10_main_main_default.set_img_opa(255)

# add style for screen_3_img_10
screen_3_img_10.add_style(style_screen_3_img_10_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_img_11 = lv.img(screen_3)
screen_3_img_11.set_pos(int(42),int(35))
screen_3_img_11.set_size(200,36)
screen_3_img_11.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_img_11.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp-296662622.png','rb') as f:
        screen_3_img_11_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp-296662622.png')
    sys.exit()

screen_3_img_11_img = lv.img_dsc_t({
  'data_size': len(screen_3_img_11_img_data),
  'header': {'always_zero': 0, 'w': 200, 'h': 36, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_3_img_11_img_data
})

screen_3_img_11.set_src(screen_3_img_11_img)
screen_3_img_11.set_pivot(50,50)
screen_3_img_11.set_angle(0)
# create style style_screen_3_img_11_main_main_default
style_screen_3_img_11_main_main_default = lv.style_t()
style_screen_3_img_11_main_main_default.init()
style_screen_3_img_11_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_3_img_11_main_main_default.set_img_recolor_opa(0)
style_screen_3_img_11_main_main_default.set_img_opa(255)

# add style for screen_3_img_11
screen_3_img_11.add_style(style_screen_3_img_11_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_img_15 = lv.img(screen_3)
screen_3_img_15.set_pos(int(221),int(35))
screen_3_img_15.set_size(57,36)
screen_3_img_15.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_img_15.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp477530338.png','rb') as f:
        screen_3_img_15_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp477530338.png')
    sys.exit()

screen_3_img_15_img = lv.img_dsc_t({
  'data_size': len(screen_3_img_15_img_data),
  'header': {'always_zero': 0, 'w': 57, 'h': 36, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_3_img_15_img_data
})

screen_3_img_15.set_src(screen_3_img_15_img)
screen_3_img_15.set_pivot(50,50)
screen_3_img_15.set_angle(0)
# create style style_screen_3_img_15_main_main_default
style_screen_3_img_15_main_main_default = lv.style_t()
style_screen_3_img_15_main_main_default.init()
style_screen_3_img_15_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_3_img_15_main_main_default.set_img_recolor_opa(0)
style_screen_3_img_15_main_main_default.set_img_opa(255)

# add style for screen_3_img_15
screen_3_img_15.add_style(style_screen_3_img_15_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_12 = lv.label(screen_3)
screen_3_label_12.set_pos(int(8),int(7))
screen_3_label_12.set_size(80,18)
screen_3_label_12.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_label_12.set_text("外网网络状态")
screen_3_label_12.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_3_label_12_main_main_default
style_screen_3_label_12_main_main_default = lv.style_t()
style_screen_3_label_12_main_main_default.init()
style_screen_3_label_12_main_main_default.set_radius(0)
style_screen_3_label_12_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_12_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_12_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_12_main_main_default.set_bg_opa(0)
style_screen_3_label_12_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_3_label_12_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_screen_3_label_12_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_3_label_12_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_12_main_main_default.set_text_letter_space(2)
style_screen_3_label_12_main_main_default.set_text_line_space(0)
style_screen_3_label_12_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_3_label_12_main_main_default.set_pad_left(0)
style_screen_3_label_12_main_main_default.set_pad_right(0)
style_screen_3_label_12_main_main_default.set_pad_top(3)
style_screen_3_label_12_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_12
screen_3_label_12.add_style(style_screen_3_label_12_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_9 = lv.label(screen_3)
screen_3_label_9.set_pos(int(18),int(51))
screen_3_label_9.set_size(30,11)
screen_3_label_9.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_label_9.set_text("域名 :")
screen_3_label_9.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_3_label_9_main_main_default
style_screen_3_label_9_main_main_default = lv.style_t()
style_screen_3_label_9_main_main_default.init()
style_screen_3_label_9_main_main_default.set_radius(0)
style_screen_3_label_9_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_9_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_9_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_9_main_main_default.set_bg_opa(0)
style_screen_3_label_9_main_main_default.set_text_color(lv.color_make(0xb7,0xb5,0xc3))
try:
    style_screen_3_label_9_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_screen_3_label_9_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_3_label_9_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_9_main_main_default.set_text_letter_space(0)
style_screen_3_label_9_main_main_default.set_text_line_space(0)
style_screen_3_label_9_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_screen_3_label_9_main_main_default.set_pad_left(0)
style_screen_3_label_9_main_main_default.set_pad_right(0)
style_screen_3_label_9_main_main_default.set_pad_top(0)
style_screen_3_label_9_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_9
screen_3_label_9.add_style(style_screen_3_label_9_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_8 = lv.label(screen_3)
screen_3_label_8.set_pos(int(202),int(34))
screen_3_label_8.set_size(50,9)
screen_3_label_8.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_label_8.set_text("1 KB/s")
screen_3_label_8.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_3_label_8_main_main_default
style_screen_3_label_8_main_main_default = lv.style_t()
style_screen_3_label_8_main_main_default.init()
style_screen_3_label_8_main_main_default.set_radius(0)
style_screen_3_label_8_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_8_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_8_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_8_main_main_default.set_bg_opa(0)
style_screen_3_label_8_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_3_label_8_main_main_default.set_text_font(lv.font_arial_10)
except AttributeError:
    try:
        style_screen_3_label_8_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_3_label_8_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_8_main_main_default.set_text_letter_space(0)
style_screen_3_label_8_main_main_default.set_text_line_space(0)
style_screen_3_label_8_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_3_label_8_main_main_default.set_pad_left(0)
style_screen_3_label_8_main_main_default.set_pad_right(0)
style_screen_3_label_8_main_main_default.set_pad_top(0)
style_screen_3_label_8_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_8
screen_3_label_8.add_style(style_screen_3_label_8_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_7 = lv.label(screen_3)
screen_3_label_7.set_pos(int(18),int(33))
screen_3_label_7.set_size(30,9)
screen_3_label_7.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_label_7.set_text("IP :")
screen_3_label_7.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_3_label_7_main_main_default
style_screen_3_label_7_main_main_default = lv.style_t()
style_screen_3_label_7_main_main_default.init()
style_screen_3_label_7_main_main_default.set_radius(0)
style_screen_3_label_7_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_7_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_7_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_7_main_main_default.set_bg_opa(0)
style_screen_3_label_7_main_main_default.set_text_color(lv.color_make(0xb7,0xb5,0xc3))
try:
    style_screen_3_label_7_main_main_default.set_text_font(lv.font_arial_10)
except AttributeError:
    try:
        style_screen_3_label_7_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_3_label_7_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_7_main_main_default.set_text_letter_space(0)
style_screen_3_label_7_main_main_default.set_text_line_space(0)
style_screen_3_label_7_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_screen_3_label_7_main_main_default.set_pad_left(0)
style_screen_3_label_7_main_main_default.set_pad_right(0)
style_screen_3_label_7_main_main_default.set_pad_top(0)
style_screen_3_label_7_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_7
screen_3_label_7.add_style(style_screen_3_label_7_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_13 = lv.label(screen_3)
screen_3_label_13.set_pos(int(150),int(12))
screen_3_label_13.set_size(7,1)
screen_3_label_13.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_screen_3_label_13_main_main_default
style_screen_3_label_13_main_main_default = lv.style_t()
style_screen_3_label_13_main_main_default.init()
style_screen_3_label_13_main_main_default.set_radius(0)
style_screen_3_label_13_main_main_default.set_bg_color(lv.color_make(0x5e,0xd7,0xa2))
style_screen_3_label_13_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_13_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_13_main_main_default.set_bg_opa(255)
style_screen_3_label_13_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_3_label_13_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_screen_3_label_13_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_screen_3_label_13_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_13_main_main_default.set_text_letter_space(2)
style_screen_3_label_13_main_main_default.set_text_line_space(0)
style_screen_3_label_13_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_3_label_13_main_main_default.set_pad_left(0)
style_screen_3_label_13_main_main_default.set_pad_right(0)
style_screen_3_label_13_main_main_default.set_pad_top(8)
style_screen_3_label_13_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_13
screen_3_label_13.add_style(style_screen_3_label_13_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_16 = lv.label(screen_3)
screen_3_label_16.set_pos(int(216),int(12))
screen_3_label_16.set_size(7,1)
screen_3_label_16.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_screen_3_label_16_main_main_default
style_screen_3_label_16_main_main_default = lv.style_t()
style_screen_3_label_16_main_main_default.init()
style_screen_3_label_16_main_main_default.set_radius(0)
style_screen_3_label_16_main_main_default.set_bg_color(lv.color_make(0x5e,0xd7,0xa2))
style_screen_3_label_16_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_16_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_16_main_main_default.set_bg_opa(255)
style_screen_3_label_16_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_3_label_16_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_screen_3_label_16_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_screen_3_label_16_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_16_main_main_default.set_text_letter_space(2)
style_screen_3_label_16_main_main_default.set_text_line_space(0)
style_screen_3_label_16_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_3_label_16_main_main_default.set_pad_left(0)
style_screen_3_label_16_main_main_default.set_pad_right(0)
style_screen_3_label_16_main_main_default.set_pad_top(8)
style_screen_3_label_16_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_16
screen_3_label_16.add_style(style_screen_3_label_16_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_14 = lv.label(screen_3)
screen_3_label_14.set_pos(int(162),int(7))
screen_3_label_14.set_size(40,18)
screen_3_label_14.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_label_14.set_text("百度连接")
screen_3_label_14.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_3_label_14_main_main_default
style_screen_3_label_14_main_main_default = lv.style_t()
style_screen_3_label_14_main_main_default.init()
style_screen_3_label_14_main_main_default.set_radius(0)
style_screen_3_label_14_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_14_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_14_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_14_main_main_default.set_bg_opa(0)
style_screen_3_label_14_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_3_label_14_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_screen_3_label_14_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_3_label_14_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_14_main_main_default.set_text_letter_space(0)
style_screen_3_label_14_main_main_default.set_text_line_space(0)
style_screen_3_label_14_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_3_label_14_main_main_default.set_pad_left(0)
style_screen_3_label_14_main_main_default.set_pad_right(0)
style_screen_3_label_14_main_main_default.set_pad_top(3)
style_screen_3_label_14_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_14
screen_3_label_14.add_style(style_screen_3_label_14_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_img_19 = lv.img(screen_3)
screen_3_img_19.set_pos(int(213),int(9))
screen_3_img_19.set_size(13,13)
screen_3_img_19.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_img_19.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp-1106748526.png','rb') as f:
        screen_3_img_19_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp-1106748526.png')
    sys.exit()

screen_3_img_19_img = lv.img_dsc_t({
  'data_size': len(screen_3_img_19_img_data),
  'header': {'always_zero': 0, 'w': 13, 'h': 13, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_3_img_19_img_data
})

screen_3_img_19.set_src(screen_3_img_19_img)
screen_3_img_19.set_pivot(50,50)
screen_3_img_19.set_angle(0)
# create style style_screen_3_img_19_main_main_default
style_screen_3_img_19_main_main_default = lv.style_t()
style_screen_3_img_19_main_main_default.init()
style_screen_3_img_19_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_3_img_19_main_main_default.set_img_recolor_opa(0)
style_screen_3_img_19_main_main_default.set_img_opa(255)

# add style for screen_3_img_19
screen_3_img_19.add_style(style_screen_3_img_19_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_15 = lv.label(screen_3)
screen_3_label_15.set_pos(int(229),int(7))
screen_3_label_15.set_size(40,16)
screen_3_label_15.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_label_15.set_text("谷歌连接")
screen_3_label_15.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_3_label_15_main_main_default
style_screen_3_label_15_main_main_default = lv.style_t()
style_screen_3_label_15_main_main_default.init()
style_screen_3_label_15_main_main_default.set_radius(0)
style_screen_3_label_15_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_15_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_15_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_15_main_main_default.set_bg_opa(0)
style_screen_3_label_15_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_3_label_15_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_screen_3_label_15_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_3_label_15_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_15_main_main_default.set_text_letter_space(0)
style_screen_3_label_15_main_main_default.set_text_line_space(0)
style_screen_3_label_15_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_3_label_15_main_main_default.set_pad_left(0)
style_screen_3_label_15_main_main_default.set_pad_right(0)
style_screen_3_label_15_main_main_default.set_pad_top(3)
style_screen_3_label_15_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_15
screen_3_label_15.add_style(style_screen_3_label_15_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_img_18 = lv.img(screen_3)
screen_3_img_18.set_pos(int(147),int(9))
screen_3_img_18.set_size(13,13)
screen_3_img_18.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_img_18.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp-1106748526.png','rb') as f:
        screen_3_img_18_img_data = f.read()
except:
    print('Could not open D:\\Gui_8_2_Project\\Over_Version\\generated\\mPythonImages\\mp-1106748526.png')
    sys.exit()

screen_3_img_18_img = lv.img_dsc_t({
  'data_size': len(screen_3_img_18_img_data),
  'header': {'always_zero': 0, 'w': 13, 'h': 13, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_3_img_18_img_data
})

screen_3_img_18.set_src(screen_3_img_18_img)
screen_3_img_18.set_pivot(50,50)
screen_3_img_18.set_angle(0)
# create style style_screen_3_img_18_main_main_default
style_screen_3_img_18_main_main_default = lv.style_t()
style_screen_3_img_18_main_main_default.init()
style_screen_3_img_18_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_3_img_18_main_main_default.set_img_recolor_opa(0)
style_screen_3_img_18_main_main_default.set_img_opa(255)

# add style for screen_3_img_18
screen_3_img_18.add_style(style_screen_3_img_18_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_17 = lv.label(screen_3)
screen_3_label_17.set_pos(int(53),int(33))
screen_3_label_17.set_size(80,9)
screen_3_label_17.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_label_17.set_text("41.164.11.44")
screen_3_label_17.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_3_label_17_main_main_default
style_screen_3_label_17_main_main_default = lv.style_t()
style_screen_3_label_17_main_main_default.init()
style_screen_3_label_17_main_main_default.set_radius(0)
style_screen_3_label_17_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_17_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_17_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_17_main_main_default.set_bg_opa(0)
style_screen_3_label_17_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_3_label_17_main_main_default.set_text_font(lv.font_arial_10)
except AttributeError:
    try:
        style_screen_3_label_17_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_3_label_17_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_17_main_main_default.set_text_letter_space(0)
style_screen_3_label_17_main_main_default.set_text_line_space(0)
style_screen_3_label_17_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_screen_3_label_17_main_main_default.set_pad_left(0)
style_screen_3_label_17_main_main_default.set_pad_right(0)
style_screen_3_label_17_main_main_default.set_pad_top(0)
style_screen_3_label_17_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_17
screen_3_label_17.add_style(style_screen_3_label_17_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_18 = lv.label(screen_3)
screen_3_label_18.set_pos(int(54),int(52))
screen_3_label_18.set_size(80,9)
screen_3_label_18.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_label_18.set_text("default.com")
screen_3_label_18.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_3_label_18_main_main_default
style_screen_3_label_18_main_main_default = lv.style_t()
style_screen_3_label_18_main_main_default.init()
style_screen_3_label_18_main_main_default.set_radius(0)
style_screen_3_label_18_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_18_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_18_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_18_main_main_default.set_bg_opa(0)
style_screen_3_label_18_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_3_label_18_main_main_default.set_text_font(lv.font_arial_10)
except AttributeError:
    try:
        style_screen_3_label_18_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_3_label_18_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_18_main_main_default.set_text_letter_space(0)
style_screen_3_label_18_main_main_default.set_text_line_space(0)
style_screen_3_label_18_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_screen_3_label_18_main_main_default.set_pad_left(0)
style_screen_3_label_18_main_main_default.set_pad_right(0)
style_screen_3_label_18_main_main_default.set_pad_top(0)
style_screen_3_label_18_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_18
screen_3_label_18.add_style(style_screen_3_label_18_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_19 = lv.label(screen_3)
screen_3_label_19.set_pos(int(178),int(33))
screen_3_label_19.set_size(29,13)
screen_3_label_19.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_label_19.set_text("下载")
screen_3_label_19.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_3_label_19_main_main_default
style_screen_3_label_19_main_main_default = lv.style_t()
style_screen_3_label_19_main_main_default.init()
style_screen_3_label_19_main_main_default.set_radius(0)
style_screen_3_label_19_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_19_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_19_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_19_main_main_default.set_bg_opa(0)
style_screen_3_label_19_main_main_default.set_text_color(lv.color_make(0xb7,0xb5,0xc3))
try:
    style_screen_3_label_19_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_screen_3_label_19_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_3_label_19_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_19_main_main_default.set_text_letter_space(0)
style_screen_3_label_19_main_main_default.set_text_line_space(0)
style_screen_3_label_19_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_screen_3_label_19_main_main_default.set_pad_left(0)
style_screen_3_label_19_main_main_default.set_pad_right(0)
style_screen_3_label_19_main_main_default.set_pad_top(0)
style_screen_3_label_19_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_19
screen_3_label_19.add_style(style_screen_3_label_19_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_20 = lv.label(screen_3)
screen_3_label_20.set_pos(int(178),int(51))
screen_3_label_20.set_size(29,13)
screen_3_label_20.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_label_20.set_text("上传")
screen_3_label_20.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_3_label_20_main_main_default
style_screen_3_label_20_main_main_default = lv.style_t()
style_screen_3_label_20_main_main_default.init()
style_screen_3_label_20_main_main_default.set_radius(0)
style_screen_3_label_20_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_20_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_20_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_20_main_main_default.set_bg_opa(0)
style_screen_3_label_20_main_main_default.set_text_color(lv.color_make(0xb7,0xb5,0xc3))
try:
    style_screen_3_label_20_main_main_default.set_text_font(lv.font_simsun_10)
except AttributeError:
    try:
        style_screen_3_label_20_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_3_label_20_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_20_main_main_default.set_text_letter_space(0)
style_screen_3_label_20_main_main_default.set_text_line_space(0)
style_screen_3_label_20_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_screen_3_label_20_main_main_default.set_pad_left(0)
style_screen_3_label_20_main_main_default.set_pad_right(0)
style_screen_3_label_20_main_main_default.set_pad_top(0)
style_screen_3_label_20_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_20
screen_3_label_20.add_style(style_screen_3_label_20_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_label_21 = lv.label(screen_3)
screen_3_label_21.set_pos(int(202),int(52))
screen_3_label_21.set_size(50,9)
screen_3_label_21.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_3_label_21.set_text("1 KB/s")
screen_3_label_21.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_3_label_21_main_main_default
style_screen_3_label_21_main_main_default = lv.style_t()
style_screen_3_label_21_main_main_default.init()
style_screen_3_label_21_main_main_default.set_radius(0)
style_screen_3_label_21_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_21_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_label_21_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_label_21_main_main_default.set_bg_opa(0)
style_screen_3_label_21_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_3_label_21_main_main_default.set_text_font(lv.font_arial_10)
except AttributeError:
    try:
        style_screen_3_label_21_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_3_label_21_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_label_21_main_main_default.set_text_letter_space(0)
style_screen_3_label_21_main_main_default.set_text_line_space(0)
style_screen_3_label_21_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_3_label_21_main_main_default.set_pad_left(0)
style_screen_3_label_21_main_main_default.set_pad_right(0)
style_screen_3_label_21_main_main_default.set_pad_top(0)
style_screen_3_label_21_main_main_default.set_pad_bottom(0)

# add style for screen_3_label_21
screen_3_label_21.add_style(style_screen_3_label_21_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3_btn_1 = lv.btn(screen_3)
screen_3_btn_1.set_pos(int(0),int(0))
screen_3_btn_1.set_size(284,76)
screen_3_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_screen_3_btn_1_main_main_default
style_screen_3_btn_1_main_main_default = lv.style_t()
style_screen_3_btn_1_main_main_default.init()
style_screen_3_btn_1_main_main_default.set_radius(5)
style_screen_3_btn_1_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_btn_1_main_main_default.set_bg_opa(0)
style_screen_3_btn_1_main_main_default.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_default.set_border_width(0)
style_screen_3_btn_1_main_main_default.set_border_opa(0)
style_screen_3_btn_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_3_btn_1_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_screen_3_btn_1_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_screen_3_btn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_3_btn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for screen_3_btn_1
screen_3_btn_1.add_style(style_screen_3_btn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_screen_3_btn_1_main_main_focused
style_screen_3_btn_1_main_main_focused = lv.style_t()
style_screen_3_btn_1_main_main_focused.init()
style_screen_3_btn_1_main_main_focused.set_radius(5)
style_screen_3_btn_1_main_main_focused.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_focused.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_focused.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_btn_1_main_main_focused.set_bg_opa(0)
style_screen_3_btn_1_main_main_focused.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_focused.set_border_width(0)
style_screen_3_btn_1_main_main_focused.set_border_opa(0)
style_screen_3_btn_1_main_main_focused.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_3_btn_1_main_main_focused.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_screen_3_btn_1_main_main_focused.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_screen_3_btn_1_main_main_focused.set_text_font(lv.font_montserrat_16)

# add style for screen_3_btn_1
screen_3_btn_1.add_style(style_screen_3_btn_1_main_main_focused, lv.PART.MAIN|lv.STATE.FOCUSED)

# create style style_screen_3_btn_1_main_main_pressed
style_screen_3_btn_1_main_main_pressed = lv.style_t()
style_screen_3_btn_1_main_main_pressed.init()
style_screen_3_btn_1_main_main_pressed.set_radius(5)
style_screen_3_btn_1_main_main_pressed.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_pressed.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_pressed.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_btn_1_main_main_pressed.set_bg_opa(0)
style_screen_3_btn_1_main_main_pressed.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_pressed.set_border_width(0)
style_screen_3_btn_1_main_main_pressed.set_border_opa(0)
style_screen_3_btn_1_main_main_pressed.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_3_btn_1_main_main_pressed.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_screen_3_btn_1_main_main_pressed.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_screen_3_btn_1_main_main_pressed.set_text_font(lv.font_montserrat_16)

# add style for screen_3_btn_1
screen_3_btn_1.add_style(style_screen_3_btn_1_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_screen_3_btn_1_main_main_checked
style_screen_3_btn_1_main_main_checked = lv.style_t()
style_screen_3_btn_1_main_main_checked.init()
style_screen_3_btn_1_main_main_checked.set_radius(5)
style_screen_3_btn_1_main_main_checked.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_checked.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_checked.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_btn_1_main_main_checked.set_bg_opa(0)
style_screen_3_btn_1_main_main_checked.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_checked.set_border_width(0)
style_screen_3_btn_1_main_main_checked.set_border_opa(0)
style_screen_3_btn_1_main_main_checked.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_3_btn_1_main_main_checked.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_screen_3_btn_1_main_main_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_screen_3_btn_1_main_main_checked.set_text_font(lv.font_montserrat_16)

# add style for screen_3_btn_1
screen_3_btn_1.add_style(style_screen_3_btn_1_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

# create style style_screen_3_btn_1_main_main_disabled
style_screen_3_btn_1_main_main_disabled = lv.style_t()
style_screen_3_btn_1_main_main_disabled.init()
style_screen_3_btn_1_main_main_disabled.set_radius(5)
style_screen_3_btn_1_main_main_disabled.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_disabled.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_disabled.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_3_btn_1_main_main_disabled.set_bg_opa(0)
style_screen_3_btn_1_main_main_disabled.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_screen_3_btn_1_main_main_disabled.set_border_width(0)
style_screen_3_btn_1_main_main_disabled.set_border_opa(0)
style_screen_3_btn_1_main_main_disabled.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_3_btn_1_main_main_disabled.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_screen_3_btn_1_main_main_disabled.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_screen_3_btn_1_main_main_disabled.set_text_font(lv.font_montserrat_16)

# add style for screen_3_btn_1
screen_3_btn_1.add_style(style_screen_3_btn_1_main_main_disabled, lv.PART.MAIN|lv.STATE.DISABLED)

screen_4 = lv.obj()
screen_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_screen_4_main_main_default
style_screen_4_main_main_default = lv.style_t()
style_screen_4_main_main_default.init()
style_screen_4_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_4_main_main_default.set_bg_opa(0)

# add style for screen_4
screen_4.add_style(style_screen_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_4_label_1 = lv.label(screen_4)
screen_4_label_1.set_pos(int(117),int(18))
screen_4_label_1.set_size(100,32)
screen_4_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_4_label_1.set_text("Label")
screen_4_label_1.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_4_label_1_main_main_default
style_screen_4_label_1_main_main_default = lv.style_t()
style_screen_4_label_1_main_main_default.init()
style_screen_4_label_1_main_main_default.set_radius(0)
style_screen_4_label_1_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_4_label_1_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_4_label_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_4_label_1_main_main_default.set_bg_opa(255)
style_screen_4_label_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_screen_4_label_1_main_main_default.set_text_font(lv.font_simsun_16)
except AttributeError:
    try:
        style_screen_4_label_1_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_screen_4_label_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_4_label_1_main_main_default.set_text_letter_space(2)
style_screen_4_label_1_main_main_default.set_text_line_space(0)
style_screen_4_label_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_4_label_1_main_main_default.set_pad_left(0)
style_screen_4_label_1_main_main_default.set_pad_right(0)
style_screen_4_label_1_main_main_default.set_pad_top(8)
style_screen_4_label_1_main_main_default.set_pad_bottom(0)

# add style for screen_4_label_1
screen_4_label_1.add_style(style_screen_4_label_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)



def error_btn_2_clicked_1_event_cb(e,screen_1):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(screen_1, lv.SCR_LOAD_ANIM.OVER_TOP, 0, 0, False)
error_btn_2.add_event_cb(lambda e: error_btn_2_clicked_1_event_cb(e,screen_1), lv.EVENT.CLICKED, None)


def screen_1_btn_1_clicked_1_event_cb(e,screen_1):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(screen_1, lv.SCR_LOAD_ANIM.OVER_TOP, 0, 0, False)
screen_1_btn_1.add_event_cb(lambda e: screen_1_btn_1_clicked_1_event_cb(e,screen_1), lv.EVENT.CLICKED, None)


def screen_3_btn_1_clicked_1_event_cb(e,screen_4):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(screen_4, lv.SCR_LOAD_ANIM.OVER_TOP, 0, 0, False)
screen_3_btn_1.add_event_cb(lambda e: screen_3_btn_1_clicked_1_event_cb(e,screen_4), lv.EVENT.CLICKED, None)


def label_9_btn_1_clicked_1_event_cb(e,screen_1):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(screen_1, lv.SCR_LOAD_ANIM.OVER_TOP, 0, 0, False)
label_9_btn_1.add_event_cb(lambda e: label_9_btn_1_clicked_1_event_cb(e,screen_1), lv.EVENT.CLICKED, None)



# content from custom.py

# Load the default screen
lv.scr_load(error)

while SDL.check():
    time.sleep_ms(5)
