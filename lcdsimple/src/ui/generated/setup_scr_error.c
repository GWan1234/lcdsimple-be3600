/*
 * Copyright 2025 NXP
 * SPDX-License-Identifier: MIT
 * The auto-generated can only be used on NXP devices
 */

#include "lvgl.h"
#include <stdio.h>
#include "gui_guider.h"
#include "events_init.h"
#include "custom.h"


void setup_scr_error(lv_ui *ui){

	//Write codes error
	ui->error = lv_obj_create(NULL);
	lv_obj_set_scrollbar_mode(ui->error, LV_SCROLLBAR_MODE_OFF);
	lv_obj_clear_flag(ui->error, LV_OBJ_FLAG_SCROLLABLE);  // [2,6](@ref)
	//Write style state: LV_STATE_DEFAULT for style_error_main_main_default
	static lv_style_t style_error_main_main_default;
	if (style_error_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_error_main_main_default);
	else
		lv_style_init(&style_error_main_main_default);
	lv_style_set_radius(&style_error_main_main_default, 5);
	lv_style_set_bg_color(&style_error_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_main_main_default, 0);
	lv_style_set_border_color(&style_error_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_error_main_main_default, 0);
	lv_style_set_border_opa(&style_error_main_main_default, 0);
	lv_style_set_text_color(&style_error_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_align(&style_error_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_obj_add_style(ui->error, &style_error_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_FOCUSED for style_error_main_main_focused
	static lv_style_t style_error_main_main_focused;
	if (style_error_main_main_focused.prop_cnt > 1)
		lv_style_reset(&style_error_main_main_focused);
	else
		lv_style_init(&style_error_main_main_focused);
	lv_style_set_radius(&style_error_main_main_focused, 5);
	lv_style_set_bg_color(&style_error_main_main_focused, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_main_main_focused, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_main_main_focused, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_main_main_focused, 0);
	lv_style_set_border_color(&style_error_main_main_focused, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_error_main_main_focused, 0);
	lv_style_set_border_opa(&style_error_main_main_focused, 0);
	lv_style_set_text_color(&style_error_main_main_focused, lv_color_make(0xff, 0xff, 0xff));
	lv_obj_add_style(ui->error, &style_error_main_main_focused, LV_PART_MAIN|LV_STATE_FOCUSED);

	//Write style state: LV_STATE_PRESSED for style_error_main_main_pressed
	static lv_style_t style_error_main_main_pressed;
	if (style_error_main_main_pressed.prop_cnt > 1)
		lv_style_reset(&style_error_main_main_pressed);
	else
		lv_style_init(&style_error_main_main_pressed);
	lv_style_set_radius(&style_error_main_main_pressed, 5);
	lv_style_set_bg_color(&style_error_main_main_pressed, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_main_main_pressed, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_main_main_pressed, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_main_main_pressed, 0);
	lv_style_set_border_color(&style_error_main_main_pressed, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_error_main_main_pressed, 0);
	lv_style_set_border_opa(&style_error_main_main_pressed, 0);
	lv_style_set_text_color(&style_error_main_main_pressed, lv_color_make(0xff, 0xff, 0xff));
	lv_obj_add_style(ui->error, &style_error_main_main_pressed, LV_PART_MAIN|LV_STATE_PRESSED);

	//Write style state: LV_STATE_CHECKED for style_error_main_main_checked
	static lv_style_t style_error_main_main_checked;
	if (style_error_main_main_checked.prop_cnt > 1)
		lv_style_reset(&style_error_main_main_checked);
	else
		lv_style_init(&style_error_main_main_checked);
	lv_style_set_radius(&style_error_main_main_checked, 5);
	lv_style_set_bg_color(&style_error_main_main_checked, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_main_main_checked, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_main_main_checked, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_main_main_checked, 0);
	lv_style_set_border_color(&style_error_main_main_checked, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_error_main_main_checked, 0);
	lv_style_set_border_opa(&style_error_main_main_checked, 0);
	lv_style_set_text_color(&style_error_main_main_checked, lv_color_make(0x00, 0x00, 0x00));
	lv_obj_add_style(ui->error, &style_error_main_main_checked, LV_PART_MAIN|LV_STATE_CHECKED);

	//Write style state: LV_STATE_DISABLED for style_error_main_main_disabled
	static lv_style_t style_error_main_main_disabled;
	if (style_error_main_main_disabled.prop_cnt > 1)
		lv_style_reset(&style_error_main_main_disabled);
	else
		lv_style_init(&style_error_main_main_disabled);
	lv_style_set_radius(&style_error_main_main_disabled, 5);
	lv_style_set_bg_color(&style_error_main_main_disabled, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_main_main_disabled, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_main_main_disabled, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_main_main_disabled, 0);
	lv_style_set_border_color(&style_error_main_main_disabled, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_error_main_main_disabled, 0);
	lv_style_set_border_opa(&style_error_main_main_disabled, 0);
	lv_style_set_text_color(&style_error_main_main_disabled, lv_color_make(0x00, 0x00, 0x00));
	lv_obj_add_style(ui->error, &style_error_main_main_disabled, LV_PART_MAIN|LV_STATE_DISABLED);

	//Write codes error_label_21
	ui->error_label_21 = lv_label_create(ui->error);
	lv_obj_set_pos(ui->error_label_21, 0, 0);
	lv_obj_set_size(ui->error_label_21, 284, 76);
	lv_obj_set_scrollbar_mode(ui->error_label_21, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->error_label_21, "");
	lv_label_set_long_mode(ui->error_label_21, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_error_label_21_main_main_default
	static lv_style_t style_error_label_21_main_main_default;
	if (style_error_label_21_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_error_label_21_main_main_default);
	else
		lv_style_init(&style_error_label_21_main_main_default);
	lv_style_set_radius(&style_error_label_21_main_main_default, 0);
	lv_style_set_bg_color(&style_error_label_21_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_bg_grad_color(&style_error_label_21_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_label_21_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_label_21_main_main_default, 255);
	lv_style_set_text_color(&style_error_label_21_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_letter_space(&style_error_label_21_main_main_default, 2);
	lv_style_set_text_line_space(&style_error_label_21_main_main_default, 0);
	lv_style_set_text_align(&style_error_label_21_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_error_label_21_main_main_default, 0);
	lv_style_set_pad_right(&style_error_label_21_main_main_default, 0);
	lv_style_set_pad_top(&style_error_label_21_main_main_default, 8);
	lv_style_set_pad_bottom(&style_error_label_21_main_main_default, 0);
	lv_obj_add_style(ui->error_label_21, &style_error_label_21_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes error_label_19
	ui->error_label_19 = lv_label_create(ui->error);
	lv_obj_set_pos(ui->error_label_19, 6, 22);
	lv_obj_set_size(ui->error_label_19, 272, 49);
	lv_obj_set_scrollbar_mode(ui->error_label_19, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->error_label_19, "");
	lv_label_set_long_mode(ui->error_label_19, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_error_label_19_main_main_default
	static lv_style_t style_error_label_19_main_main_default;
	if (style_error_label_19_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_error_label_19_main_main_default);
	else
		lv_style_init(&style_error_label_19_main_main_default);
	lv_style_set_radius(&style_error_label_19_main_main_default, 0);
	lv_style_set_bg_color(&style_error_label_19_main_main_default, lv_color_make(0x14, 0x11, 0x26));
	lv_style_set_bg_grad_color(&style_error_label_19_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_label_19_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_label_19_main_main_default, 255);
	lv_style_set_text_color(&style_error_label_19_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_letter_space(&style_error_label_19_main_main_default, 0);
	lv_style_set_text_line_space(&style_error_label_19_main_main_default, 0);
	lv_style_set_text_align(&style_error_label_19_main_main_default, LV_TEXT_ALIGN_LEFT);
	lv_style_set_pad_left(&style_error_label_19_main_main_default, 0);
	lv_style_set_pad_right(&style_error_label_19_main_main_default, 7);
	lv_style_set_pad_top(&style_error_label_19_main_main_default, 0);
	lv_style_set_pad_bottom(&style_error_label_19_main_main_default, 0);
	lv_obj_add_style(ui->error_label_19, &style_error_label_19_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes error_label_17
	ui->error_label_17 = lv_label_create(ui->error);
	lv_obj_set_pos(ui->error_label_17, 195, 21);
	lv_obj_set_size(ui->error_label_17, 16, 32);
	lv_obj_set_scrollbar_mode(ui->error_label_17, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->error_label_17, "4");
	lv_label_set_long_mode(ui->error_label_17, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_error_label_17_main_main_default
	static lv_style_t style_error_label_17_main_main_default;
	if (style_error_label_17_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_error_label_17_main_main_default);
	else
		lv_style_init(&style_error_label_17_main_main_default);
	lv_style_set_radius(&style_error_label_17_main_main_default, 0);
	lv_style_set_bg_color(&style_error_label_17_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_label_17_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_label_17_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_label_17_main_main_default, 0);
	lv_style_set_text_color(&style_error_label_17_main_main_default, lv_color_make(0xf9, 0xba, 0x2d));
	lv_style_set_text_font(&style_error_label_17_main_main_default, &lv_font_simsun_16);
	lv_style_set_text_letter_space(&style_error_label_17_main_main_default, 2);
	lv_style_set_text_line_space(&style_error_label_17_main_main_default, 0);
	lv_style_set_text_align(&style_error_label_17_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_error_label_17_main_main_default, 0);
	lv_style_set_pad_right(&style_error_label_17_main_main_default, 0);
	lv_style_set_pad_top(&style_error_label_17_main_main_default, 8);
	lv_style_set_pad_bottom(&style_error_label_17_main_main_default, 0);
	lv_obj_add_style(ui->error_label_17, &style_error_label_17_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes error_label_13
	ui->error_label_13 = lv_label_create(ui->error);
	lv_obj_set_pos(ui->error_label_13, 38, 21);
	lv_obj_set_size(ui->error_label_13, 48, 23);
	lv_obj_set_scrollbar_mode(ui->error_label_13, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->error_label_13, "已联网");
	lv_label_set_long_mode(ui->error_label_13, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_error_label_13_main_main_default
	static lv_style_t style_error_label_13_main_main_default;
	if (style_error_label_13_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_error_label_13_main_main_default);
	else
		lv_style_init(&style_error_label_13_main_main_default);
	lv_style_set_radius(&style_error_label_13_main_main_default, 0);
	lv_style_set_bg_color(&style_error_label_13_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_label_13_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_label_13_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_label_13_main_main_default, 0);
	lv_style_set_text_color(&style_error_label_13_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_error_label_13_main_main_default, &lv_font_simsun_13);
	lv_style_set_text_letter_space(&style_error_label_13_main_main_default, 2);
	lv_style_set_text_line_space(&style_error_label_13_main_main_default, 0);
	lv_style_set_text_align(&style_error_label_13_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_error_label_13_main_main_default, 0);
	lv_style_set_pad_right(&style_error_label_13_main_main_default, 0);
	lv_style_set_pad_top(&style_error_label_13_main_main_default, 8);
	lv_style_set_pad_bottom(&style_error_label_13_main_main_default, 0);
	lv_obj_add_style(ui->error_label_13, &style_error_label_13_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes error_img_12
	ui->error_img_12 = lv_img_create(ui->error);
	lv_obj_set_pos(ui->error_img_12, 15, 38);
	lv_obj_set_size(ui->error_img_12, 15, 15);
	lv_obj_set_scrollbar_mode(ui->error_img_12, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_error_img_12_main_main_default
	static lv_style_t style_error_img_12_main_main_default;
	if (style_error_img_12_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_error_img_12_main_main_default);
	else
		lv_style_init(&style_error_img_12_main_main_default);
	lv_style_set_img_recolor(&style_error_img_12_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_error_img_12_main_main_default, 0);
	lv_style_set_img_opa(&style_error_img_12_main_main_default, 255);
	lv_obj_add_style(ui->error_img_12, &style_error_img_12_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->error_img_12, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->error_img_12,&_xuenze_15x15);
	lv_img_set_pivot(ui->error_img_12, 50,50);
	lv_img_set_angle(ui->error_img_12, 0);

	//Write codes error_label_16
	ui->error_label_16 = lv_label_create(ui->error);
	lv_obj_set_pos(ui->error_label_16, 183, 42);
	lv_obj_set_size(ui->error_label_16, 89, 24);
	lv_obj_set_scrollbar_mode(ui->error_label_16, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->error_label_16, "已连接设备");
	lv_label_set_long_mode(ui->error_label_16, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_error_label_16_main_main_default
	static lv_style_t style_error_label_16_main_main_default;
	if (style_error_label_16_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_error_label_16_main_main_default);
	else
		lv_style_init(&style_error_label_16_main_main_default);
	lv_style_set_radius(&style_error_label_16_main_main_default, 0);
	lv_style_set_bg_color(&style_error_label_16_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_label_16_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_label_16_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_label_16_main_main_default, 0);
	lv_style_set_text_color(&style_error_label_16_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_error_label_16_main_main_default, &lv_font_simsun_11);
	lv_style_set_text_letter_space(&style_error_label_16_main_main_default, 2);
	lv_style_set_text_line_space(&style_error_label_16_main_main_default, 0);
	lv_style_set_text_align(&style_error_label_16_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_error_label_16_main_main_default, 0);
	lv_style_set_pad_right(&style_error_label_16_main_main_default, 0);
	lv_style_set_pad_top(&style_error_label_16_main_main_default, 8);
	lv_style_set_pad_bottom(&style_error_label_16_main_main_default, 0);
	lv_obj_add_style(ui->error_label_16, &style_error_label_16_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes error_label_18
	ui->error_label_18 = lv_label_create(ui->error);
	lv_obj_set_pos(ui->error_label_18, 36, 42);
	lv_obj_set_size(ui->error_label_18, 100, 32);
	lv_obj_set_scrollbar_mode(ui->error_label_18, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->error_label_18, "1小时28分51秒");
	lv_label_set_long_mode(ui->error_label_18, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_error_label_18_main_main_default
	static lv_style_t style_error_label_18_main_main_default;
	if (style_error_label_18_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_error_label_18_main_main_default);
	else
		lv_style_init(&style_error_label_18_main_main_default);
	lv_style_set_radius(&style_error_label_18_main_main_default, 0);
	lv_style_set_bg_color(&style_error_label_18_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_label_18_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_label_18_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_label_18_main_main_default, 0);
	lv_style_set_text_color(&style_error_label_18_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_error_label_18_main_main_default, &lv_font_simsun_11);
	lv_style_set_text_letter_space(&style_error_label_18_main_main_default, 2);
	lv_style_set_text_line_space(&style_error_label_18_main_main_default, 0);
	lv_style_set_text_align(&style_error_label_18_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_error_label_18_main_main_default, 0);
	lv_style_set_pad_right(&style_error_label_18_main_main_default, 0);
	lv_style_set_pad_top(&style_error_label_18_main_main_default, 8);
	lv_style_set_pad_bottom(&style_error_label_18_main_main_default, 0);
	lv_obj_add_style(ui->error_label_18, &style_error_label_18_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes error_img_15
	ui->error_img_15 = lv_img_create(ui->error);
	lv_obj_set_pos(ui->error_img_15, 172, 34);
	lv_obj_set_size(ui->error_img_15, 20, 20);
	lv_obj_set_scrollbar_mode(ui->error_img_15, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_error_img_15_main_main_default
	static lv_style_t style_error_img_15_main_main_default;
	if (style_error_img_15_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_error_img_15_main_main_default);
	else
		lv_style_init(&style_error_img_15_main_main_default);
	lv_style_set_img_recolor(&style_error_img_15_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_error_img_15_main_main_default, 0);
	lv_style_set_img_opa(&style_error_img_15_main_main_default, 255);
	lv_obj_add_style(ui->error_img_15, &style_error_img_15_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->error_img_15, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->error_img_15,&_cirle_back_20x20);
	lv_img_set_pivot(ui->error_img_15, 50,50);
	lv_img_set_angle(ui->error_img_15, 0);

	//Write codes error_img_13
	ui->error_img_13 = lv_img_create(ui->error);
	lv_obj_set_pos(ui->error_img_13, 176, 38);
	lv_obj_set_size(ui->error_img_13, 12, 12);
	lv_obj_set_scrollbar_mode(ui->error_img_13, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_error_img_13_main_main_default
	static lv_style_t style_error_img_13_main_main_default;
	if (style_error_img_13_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_error_img_13_main_main_default);
	else
		lv_style_init(&style_error_img_13_main_main_default);
	lv_style_set_img_recolor(&style_error_img_13_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_error_img_13_main_main_default, 0);
	lv_style_set_img_opa(&style_error_img_13_main_main_default, 255);
	lv_obj_add_style(ui->error_img_13, &style_error_img_13_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->error_img_13, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->error_img_13,&_file_12x12);
	lv_img_set_pivot(ui->error_img_13, 50,50);
	lv_img_set_angle(ui->error_img_13, 0);

	//Write codes error_label_20
	ui->error_label_20 = lv_label_create(ui->error);
	lv_obj_set_pos(ui->error_label_20, 6, 5);
	lv_obj_set_size(ui->error_label_20, 90, 11);
	lv_obj_set_scrollbar_mode(ui->error_label_20, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->error_label_20, "错误信息提示区域");
	lv_label_set_long_mode(ui->error_label_20, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_error_label_20_main_main_default
	static lv_style_t style_error_label_20_main_main_default;
	if (style_error_label_20_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_error_label_20_main_main_default);
	else
		lv_style_init(&style_error_label_20_main_main_default);
	lv_style_set_radius(&style_error_label_20_main_main_default, 0);
	lv_style_set_bg_color(&style_error_label_20_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_label_20_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_label_20_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_label_20_main_main_default, 0);
	lv_style_set_text_color(&style_error_label_20_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_error_label_20_main_main_default, &lv_font_simsun_11);
	lv_style_set_text_letter_space(&style_error_label_20_main_main_default, 0);
	lv_style_set_text_line_space(&style_error_label_20_main_main_default, 0);
	lv_style_set_text_align(&style_error_label_20_main_main_default, LV_TEXT_ALIGN_LEFT);
	lv_style_set_pad_left(&style_error_label_20_main_main_default, 0);
	lv_style_set_pad_right(&style_error_label_20_main_main_default, 0);
	lv_style_set_pad_top(&style_error_label_20_main_main_default, 1);
	lv_style_set_pad_bottom(&style_error_label_20_main_main_default, 0);
	lv_obj_add_style(ui->error_label_20, &style_error_label_20_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes error_btn_2
	ui->error_btn_2 = lv_btn_create(ui->error);
	lv_obj_set_pos(ui->error_btn_2, 0, 0);
	lv_obj_set_size(ui->error_btn_2, 284, 100);
	lv_obj_set_scrollbar_mode(ui->error_btn_2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_error_btn_2_main_main_default
	static lv_style_t style_error_btn_2_main_main_default;
	if (style_error_btn_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_error_btn_2_main_main_default);
	else
		lv_style_init(&style_error_btn_2_main_main_default);
	lv_style_set_radius(&style_error_btn_2_main_main_default, 5);
	lv_style_set_bg_color(&style_error_btn_2_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_btn_2_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_btn_2_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_btn_2_main_main_default, 0);
	lv_style_set_border_color(&style_error_btn_2_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_error_btn_2_main_main_default, 0);
	lv_style_set_border_opa(&style_error_btn_2_main_main_default, 0);
	lv_style_set_text_color(&style_error_btn_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_align(&style_error_btn_2_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_obj_add_style(ui->error_btn_2, &style_error_btn_2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_FOCUSED for style_error_btn_2_main_main_focused
	static lv_style_t style_error_btn_2_main_main_focused;
	if (style_error_btn_2_main_main_focused.prop_cnt > 1)
		lv_style_reset(&style_error_btn_2_main_main_focused);
	else
		lv_style_init(&style_error_btn_2_main_main_focused);
	lv_style_set_radius(&style_error_btn_2_main_main_focused, 5);
	lv_style_set_bg_color(&style_error_btn_2_main_main_focused, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_btn_2_main_main_focused, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_btn_2_main_main_focused, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_btn_2_main_main_focused, 0);
	lv_style_set_border_color(&style_error_btn_2_main_main_focused, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_error_btn_2_main_main_focused, 0);
	lv_style_set_border_opa(&style_error_btn_2_main_main_focused, 0);
	lv_style_set_text_color(&style_error_btn_2_main_main_focused, lv_color_make(0xff, 0xff, 0xff));
	lv_obj_add_style(ui->error_btn_2, &style_error_btn_2_main_main_focused, LV_PART_MAIN|LV_STATE_FOCUSED);

	//Write style state: LV_STATE_PRESSED for style_error_btn_2_main_main_pressed
	static lv_style_t style_error_btn_2_main_main_pressed;
	if (style_error_btn_2_main_main_pressed.prop_cnt > 1)
		lv_style_reset(&style_error_btn_2_main_main_pressed);
	else
		lv_style_init(&style_error_btn_2_main_main_pressed);
	lv_style_set_radius(&style_error_btn_2_main_main_pressed, 5);
	lv_style_set_bg_color(&style_error_btn_2_main_main_pressed, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_btn_2_main_main_pressed, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_btn_2_main_main_pressed, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_btn_2_main_main_pressed, 0);
	lv_style_set_border_color(&style_error_btn_2_main_main_pressed, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_error_btn_2_main_main_pressed, 0);
	lv_style_set_border_opa(&style_error_btn_2_main_main_pressed, 0);
	lv_style_set_text_color(&style_error_btn_2_main_main_pressed, lv_color_make(0xff, 0xff, 0xff));
	lv_obj_add_style(ui->error_btn_2, &style_error_btn_2_main_main_pressed, LV_PART_MAIN|LV_STATE_PRESSED);

	//Write style state: LV_STATE_CHECKED for style_error_btn_2_main_main_checked
	static lv_style_t style_error_btn_2_main_main_checked;
	if (style_error_btn_2_main_main_checked.prop_cnt > 1)
		lv_style_reset(&style_error_btn_2_main_main_checked);
	else
		lv_style_init(&style_error_btn_2_main_main_checked);
	lv_style_set_radius(&style_error_btn_2_main_main_checked, 5);
	lv_style_set_bg_color(&style_error_btn_2_main_main_checked, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_btn_2_main_main_checked, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_btn_2_main_main_checked, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_btn_2_main_main_checked, 0);
	lv_style_set_border_color(&style_error_btn_2_main_main_checked, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_error_btn_2_main_main_checked, 0);
	lv_style_set_border_opa(&style_error_btn_2_main_main_checked, 0);
	lv_style_set_text_color(&style_error_btn_2_main_main_checked, lv_color_make(0x00, 0x00, 0x00));
	lv_obj_add_style(ui->error_btn_2, &style_error_btn_2_main_main_checked, LV_PART_MAIN|LV_STATE_CHECKED);

	//Write style state: LV_STATE_DISABLED for style_error_btn_2_main_main_disabled
	static lv_style_t style_error_btn_2_main_main_disabled;
	if (style_error_btn_2_main_main_disabled.prop_cnt > 1)
		lv_style_reset(&style_error_btn_2_main_main_disabled);
	else
		lv_style_init(&style_error_btn_2_main_main_disabled);
	lv_style_set_radius(&style_error_btn_2_main_main_disabled, 5);
	lv_style_set_bg_color(&style_error_btn_2_main_main_disabled, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_btn_2_main_main_disabled, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_btn_2_main_main_disabled, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_btn_2_main_main_disabled, 0);
	lv_style_set_border_color(&style_error_btn_2_main_main_disabled, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_error_btn_2_main_main_disabled, 0);
	lv_style_set_border_opa(&style_error_btn_2_main_main_disabled, 0);
	lv_style_set_text_color(&style_error_btn_2_main_main_disabled, lv_color_make(0x00, 0x00, 0x00));
	lv_obj_add_style(ui->error_btn_2, &style_error_btn_2_main_main_disabled, LV_PART_MAIN|LV_STATE_DISABLED);
	ui->error_btn_2_label = lv_label_create(ui->error_btn_2);
	lv_label_set_text(ui->error_btn_2_label, "");
	lv_obj_set_style_pad_all(ui->error_btn_2, 0, LV_STATE_DEFAULT);
	lv_obj_align(ui->error_btn_2_label, LV_ALIGN_CENTER, 0, 0);

	//Write codes error_label_22
	ui->error_label_22 = lv_label_create(ui->error);
	lv_obj_set_pos(ui->error_label_22, 102, 6);
	lv_obj_set_size(ui->error_label_22, 81, 11);
	lv_obj_set_scrollbar_mode(ui->error_label_22, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->error_label_22, "12:09");
	lv_label_set_long_mode(ui->error_label_22, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_error_label_22_main_main_default
	static lv_style_t style_error_label_22_main_main_default;
	if (style_error_label_22_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_error_label_22_main_main_default);
	else
		lv_style_init(&style_error_label_22_main_main_default);
	lv_style_set_radius(&style_error_label_22_main_main_default, 0);
	lv_style_set_bg_color(&style_error_label_22_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_label_22_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_label_22_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_label_22_main_main_default, 0);
	lv_style_set_text_color(&style_error_label_22_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_error_label_22_main_main_default, &lv_font_simsun_11);
	lv_style_set_text_letter_space(&style_error_label_22_main_main_default, 0);
	lv_style_set_text_line_space(&style_error_label_22_main_main_default, 0);
	lv_style_set_text_align(&style_error_label_22_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_error_label_22_main_main_default, 0);
	lv_style_set_pad_right(&style_error_label_22_main_main_default, 0);
	lv_style_set_pad_top(&style_error_label_22_main_main_default, 0);
	lv_style_set_pad_bottom(&style_error_label_22_main_main_default, 0);
	lv_obj_add_style(ui->error_label_22, &style_error_label_22_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes error_label_23
	ui->error_label_23 = lv_label_create(ui->error);
	lv_obj_set_pos(ui->error_label_23, 210, 7);
	lv_obj_set_size(ui->error_label_23, 81, 11);
	lv_obj_set_scrollbar_mode(ui->error_label_23, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->error_label_23, "2025.12.31");
	lv_label_set_long_mode(ui->error_label_23, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_error_label_23_main_main_default
	static lv_style_t style_error_label_23_main_main_default;
	if (style_error_label_23_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_error_label_23_main_main_default);
	else
		lv_style_init(&style_error_label_23_main_main_default);
	lv_style_set_radius(&style_error_label_23_main_main_default, 0);
	lv_style_set_bg_color(&style_error_label_23_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_error_label_23_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_error_label_23_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_error_label_23_main_main_default, 0);
	lv_style_set_text_color(&style_error_label_23_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_error_label_23_main_main_default, &lv_font_simsun_11);
	lv_style_set_text_letter_space(&style_error_label_23_main_main_default, 0);
	lv_style_set_text_line_space(&style_error_label_23_main_main_default, 0);
	lv_style_set_text_align(&style_error_label_23_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_error_label_23_main_main_default, 0);
	lv_style_set_pad_right(&style_error_label_23_main_main_default, 0);
	lv_style_set_pad_top(&style_error_label_23_main_main_default, 0);
	lv_style_set_pad_bottom(&style_error_label_23_main_main_default, 0);
	lv_obj_add_style(ui->error_label_23, &style_error_label_23_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Init events for screen
	events_init_error(ui);
}