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


void setup_scr_screen_1(lv_ui *ui){

	//Write codes screen_1
	ui->screen_1 = lv_obj_create(NULL);
	lv_obj_set_scrollbar_mode(ui->screen_1, LV_SCROLLBAR_MODE_OFF);
	lv_obj_clear_flag(ui->screen_1, LV_OBJ_FLAG_SCROLLABLE);  // [2,6](@ref)
	//Write style state: LV_STATE_DEFAULT for style_screen_1_main_main_default
	static lv_style_t style_screen_1_main_main_default;
	if (style_screen_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_main_main_default);
	else
		lv_style_init(&style_screen_1_main_main_default);
	lv_style_set_bg_color(&style_screen_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_opa(&style_screen_1_main_main_default, 255);
	lv_obj_add_style(ui->screen_1, &style_screen_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_1_label_11
	ui->screen_1_label_11 = lv_label_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_label_11, 0, 0);
	lv_obj_set_size(ui->screen_1_label_11, 284, 76);
	lv_obj_set_scrollbar_mode(ui->screen_1_label_11, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->screen_1_label_11, "Label");
	lv_label_set_long_mode(ui->screen_1_label_11, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_label_11_main_main_default
	static lv_style_t style_screen_1_label_11_main_main_default;
	if (style_screen_1_label_11_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_label_11_main_main_default);
	else
		lv_style_init(&style_screen_1_label_11_main_main_default);
	lv_style_set_radius(&style_screen_1_label_11_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_1_label_11_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_bg_grad_color(&style_screen_1_label_11_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_1_label_11_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_1_label_11_main_main_default, 255);
	lv_style_set_text_color(&style_screen_1_label_11_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_screen_1_label_11_main_main_default, &lv_font_simsun_16);
	lv_style_set_text_letter_space(&style_screen_1_label_11_main_main_default, 2);
	lv_style_set_text_line_space(&style_screen_1_label_11_main_main_default, 0);
	lv_style_set_text_align(&style_screen_1_label_11_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_screen_1_label_11_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_1_label_11_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_1_label_11_main_main_default, 8);
	lv_style_set_pad_bottom(&style_screen_1_label_11_main_main_default, 0);
	lv_obj_add_style(ui->screen_1_label_11, &style_screen_1_label_11_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_1_img_9
	ui->screen_1_img_9 = lv_img_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_img_9, 6, 8);
	lv_obj_set_size(ui->screen_1_img_9, 273, 64);
	lv_obj_set_scrollbar_mode(ui->screen_1_img_9, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_img_9_main_main_default
	static lv_style_t style_screen_1_img_9_main_main_default;
	if (style_screen_1_img_9_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_img_9_main_main_default);
	else
		lv_style_init(&style_screen_1_img_9_main_main_default);
	lv_style_set_img_recolor(&style_screen_1_img_9_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_1_img_9_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_1_img_9_main_main_default, 255);
	lv_obj_add_style(ui->screen_1_img_9, &style_screen_1_img_9_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_1_img_9, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_1_img_9,&_rect_273x64);
	lv_img_set_pivot(ui->screen_1_img_9, 50,50);
	lv_img_set_angle(ui->screen_1_img_9, 0);

	//Write codes screen_1_img_14
	ui->screen_1_img_14 = lv_img_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_img_14, 222, 38);
	lv_obj_set_size(ui->screen_1_img_14, 57, 34);
	lv_obj_set_scrollbar_mode(ui->screen_1_img_14, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_img_14_main_main_default
	static lv_style_t style_screen_1_img_14_main_main_default;
	if (style_screen_1_img_14_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_img_14_main_main_default);
	else
		lv_style_init(&style_screen_1_img_14_main_main_default);
	lv_style_set_img_recolor(&style_screen_1_img_14_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_1_img_14_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_1_img_14_main_main_default, 255);
	lv_obj_add_style(ui->screen_1_img_14, &style_screen_1_img_14_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_1_img_14, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_1_img_14,&_rect_57x34);
	lv_img_set_pivot(ui->screen_1_img_14, 50,50);
	lv_img_set_angle(ui->screen_1_img_14, 0);

	//Write codes screen_1_img_13
	ui->screen_1_img_13 = lv_img_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_img_13, 6, 38);
	lv_obj_set_size(ui->screen_1_img_13, 57, 34);
	lv_obj_set_scrollbar_mode(ui->screen_1_img_13, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_img_13_main_main_default
	static lv_style_t style_screen_1_img_13_main_main_default;
	if (style_screen_1_img_13_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_img_13_main_main_default);
	else
		lv_style_init(&style_screen_1_img_13_main_main_default);
	lv_style_set_img_recolor(&style_screen_1_img_13_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_1_img_13_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_1_img_13_main_main_default, 255);
	lv_obj_add_style(ui->screen_1_img_13, &style_screen_1_img_13_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_1_img_13, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_1_img_13,&_rect_57x34);
	lv_img_set_pivot(ui->screen_1_img_13, 50,50);
	lv_img_set_angle(ui->screen_1_img_13, 0);

	//Write codes screen_1_img_16
	ui->screen_1_img_16 = lv_img_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_img_16, 6, 8);
	lv_obj_set_size(ui->screen_1_img_16, 57, 34);
	lv_obj_set_scrollbar_mode(ui->screen_1_img_16, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_img_16_main_main_default
	static lv_style_t style_screen_1_img_16_main_main_default;
	if (style_screen_1_img_16_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_img_16_main_main_default);
	else
		lv_style_init(&style_screen_1_img_16_main_main_default);
	lv_style_set_img_recolor(&style_screen_1_img_16_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_1_img_16_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_1_img_16_main_main_default, 255);
	lv_obj_add_style(ui->screen_1_img_16, &style_screen_1_img_16_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_1_img_16, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_1_img_16,&_rect_57x34);
	lv_img_set_pivot(ui->screen_1_img_16, 50,50);
	lv_img_set_angle(ui->screen_1_img_16, 0);

	//Write codes screen_1_img_17
	ui->screen_1_img_17 = lv_img_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_img_17, 222, 8);
	lv_obj_set_size(ui->screen_1_img_17, 57, 34);
	lv_obj_set_scrollbar_mode(ui->screen_1_img_17, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_img_17_main_main_default
	static lv_style_t style_screen_1_img_17_main_main_default;
	if (style_screen_1_img_17_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_img_17_main_main_default);
	else
		lv_style_init(&style_screen_1_img_17_main_main_default);
	lv_style_set_img_recolor(&style_screen_1_img_17_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_1_img_17_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_1_img_17_main_main_default, 255);
	lv_obj_add_style(ui->screen_1_img_17, &style_screen_1_img_17_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_1_img_17, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_1_img_17,&_rect_57x34);
	lv_img_set_pivot(ui->screen_1_img_17, 50,50);
	lv_img_set_angle(ui->screen_1_img_17, 0);

	//Write codes screen_1_label_10
	ui->screen_1_label_10 = lv_label_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_label_10, 7, 23);
	lv_obj_set_size(ui->screen_1_label_10, 271, 45);
	lv_obj_set_scrollbar_mode(ui->screen_1_label_10, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->screen_1_label_10, "");
	lv_label_set_long_mode(ui->screen_1_label_10, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_label_10_main_main_default
	static lv_style_t style_screen_1_label_10_main_main_default;
	if (style_screen_1_label_10_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_label_10_main_main_default);
	else
		lv_style_init(&style_screen_1_label_10_main_main_default);
	lv_style_set_radius(&style_screen_1_label_10_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_1_label_10_main_main_default, lv_color_make(0x14, 0x11, 0x26));
	lv_style_set_bg_grad_color(&style_screen_1_label_10_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_1_label_10_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_1_label_10_main_main_default, 255);
	lv_style_set_text_color(&style_screen_1_label_10_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_letter_space(&style_screen_1_label_10_main_main_default, 0);
	lv_style_set_text_line_space(&style_screen_1_label_10_main_main_default, 0);
	lv_style_set_text_align(&style_screen_1_label_10_main_main_default, LV_TEXT_ALIGN_LEFT);
	lv_style_set_pad_left(&style_screen_1_label_10_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_1_label_10_main_main_default, 7);
	lv_style_set_pad_top(&style_screen_1_label_10_main_main_default, 0);
	lv_style_set_pad_bottom(&style_screen_1_label_10_main_main_default, 0);
	lv_obj_add_style(ui->screen_1_label_10, &style_screen_1_label_10_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_1_img_10
	ui->screen_1_img_10 = lv_img_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_img_10, 7, 35);
	lv_obj_set_size(ui->screen_1_img_10, 57, 36);
	lv_obj_set_scrollbar_mode(ui->screen_1_img_10, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_img_10_main_main_default
	static lv_style_t style_screen_1_img_10_main_main_default;
	if (style_screen_1_img_10_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_img_10_main_main_default);
	else
		lv_style_init(&style_screen_1_img_10_main_main_default);
	lv_style_set_img_recolor(&style_screen_1_img_10_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_1_img_10_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_1_img_10_main_main_default, 255);
	lv_obj_add_style(ui->screen_1_img_10, &style_screen_1_img_10_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_1_img_10, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_1_img_10,&_black_rect_57x36);
	lv_img_set_pivot(ui->screen_1_img_10, 50,50);
	lv_img_set_angle(ui->screen_1_img_10, 0);

	//Write codes screen_1_img_11
	ui->screen_1_img_11 = lv_img_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_img_11, 42, 35);
	lv_obj_set_size(ui->screen_1_img_11, 200, 36);
	lv_obj_set_scrollbar_mode(ui->screen_1_img_11, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_img_11_main_main_default
	static lv_style_t style_screen_1_img_11_main_main_default;
	if (style_screen_1_img_11_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_img_11_main_main_default);
	else
		lv_style_init(&style_screen_1_img_11_main_main_default);
	lv_style_set_img_recolor(&style_screen_1_img_11_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_1_img_11_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_1_img_11_main_main_default, 255);
	lv_obj_add_style(ui->screen_1_img_11, &style_screen_1_img_11_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_1_img_11, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_1_img_11,&_black_rect_200x36);
	lv_img_set_pivot(ui->screen_1_img_11, 50,50);
	lv_img_set_angle(ui->screen_1_img_11, 0);

	//Write codes screen_1_img_15
	ui->screen_1_img_15 = lv_img_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_img_15, 221, 35);
	lv_obj_set_size(ui->screen_1_img_15, 57, 36);
	lv_obj_set_scrollbar_mode(ui->screen_1_img_15, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_img_15_main_main_default
	static lv_style_t style_screen_1_img_15_main_main_default;
	if (style_screen_1_img_15_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_img_15_main_main_default);
	else
		lv_style_init(&style_screen_1_img_15_main_main_default);
	lv_style_set_img_recolor(&style_screen_1_img_15_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_1_img_15_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_1_img_15_main_main_default, 255);
	lv_obj_add_style(ui->screen_1_img_15, &style_screen_1_img_15_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_1_img_15, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_1_img_15,&_black_rect_57x36);
	lv_img_set_pivot(ui->screen_1_img_15, 50,50);
	lv_img_set_angle(ui->screen_1_img_15, 0);

	//Write codes screen_1_label_12
	ui->screen_1_label_12 = lv_label_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_label_12, 8, 7);
	lv_obj_set_size(ui->screen_1_label_12, 45, 18);
	lv_obj_set_scrollbar_mode(ui->screen_1_label_12, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->screen_1_label_12, "IP地址");
	lv_label_set_long_mode(ui->screen_1_label_12, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_label_12_main_main_default
	static lv_style_t style_screen_1_label_12_main_main_default;
	if (style_screen_1_label_12_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_label_12_main_main_default);
	else
		lv_style_init(&style_screen_1_label_12_main_main_default);
	lv_style_set_radius(&style_screen_1_label_12_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_1_label_12_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_screen_1_label_12_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_1_label_12_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_1_label_12_main_main_default, 0);
	lv_style_set_text_color(&style_screen_1_label_12_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_font(&style_screen_1_label_12_main_main_default, &lv_font_simsun_10);
	lv_style_set_text_letter_space(&style_screen_1_label_12_main_main_default, 2);
	lv_style_set_text_line_space(&style_screen_1_label_12_main_main_default, 0);
	lv_style_set_text_align(&style_screen_1_label_12_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_screen_1_label_12_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_1_label_12_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_1_label_12_main_main_default, 3);
	lv_style_set_pad_bottom(&style_screen_1_label_12_main_main_default, 0);
	lv_obj_add_style(ui->screen_1_label_12, &style_screen_1_label_12_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_1_label_9
	ui->screen_1_label_9 = lv_label_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_label_9, 18, 51);
	lv_obj_set_size(ui->screen_1_label_9, 284, 11);
	lv_obj_set_scrollbar_mode(ui->screen_1_label_9, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->screen_1_label_9, "IPv6 : xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx");
	lv_label_set_long_mode(ui->screen_1_label_9, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_label_9_main_main_default
	static lv_style_t style_screen_1_label_9_main_main_default;
	if (style_screen_1_label_9_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_label_9_main_main_default);
	else
		lv_style_init(&style_screen_1_label_9_main_main_default);
	lv_style_set_radius(&style_screen_1_label_9_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_1_label_9_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_screen_1_label_9_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_1_label_9_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_1_label_9_main_main_default, 0);
	lv_style_set_text_color(&style_screen_1_label_9_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_screen_1_label_9_main_main_default, &lv_font_arial_10);
	lv_style_set_text_letter_space(&style_screen_1_label_9_main_main_default, 0);
	lv_style_set_text_line_space(&style_screen_1_label_9_main_main_default, 0);
	lv_style_set_text_align(&style_screen_1_label_9_main_main_default, LV_TEXT_ALIGN_LEFT);
	lv_style_set_pad_left(&style_screen_1_label_9_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_1_label_9_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_1_label_9_main_main_default, 0);
	lv_style_set_pad_bottom(&style_screen_1_label_9_main_main_default, 0);
	lv_obj_add_style(ui->screen_1_label_9, &style_screen_1_label_9_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_1_label_8
	ui->screen_1_label_8 = lv_label_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_label_8, 141, 33);
	lv_obj_set_size(ui->screen_1_label_8, 128, 9);
	lv_obj_set_scrollbar_mode(ui->screen_1_label_8, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->screen_1_label_8, "DNS : 192.168.100.1");
	lv_label_set_long_mode(ui->screen_1_label_8, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_label_8_main_main_default
	static lv_style_t style_screen_1_label_8_main_main_default;
	if (style_screen_1_label_8_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_label_8_main_main_default);
	else
		lv_style_init(&style_screen_1_label_8_main_main_default);
	lv_style_set_radius(&style_screen_1_label_8_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_1_label_8_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_screen_1_label_8_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_1_label_8_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_1_label_8_main_main_default, 0);
	lv_style_set_text_color(&style_screen_1_label_8_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_screen_1_label_8_main_main_default, &lv_font_arial_10);
	lv_style_set_text_letter_space(&style_screen_1_label_8_main_main_default, 0);
	lv_style_set_text_line_space(&style_screen_1_label_8_main_main_default, 0);
	lv_style_set_text_align(&style_screen_1_label_8_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_screen_1_label_8_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_1_label_8_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_1_label_8_main_main_default, 0);
	lv_style_set_pad_bottom(&style_screen_1_label_8_main_main_default, 0);
	lv_obj_add_style(ui->screen_1_label_8, &style_screen_1_label_8_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_1_label_7
	ui->screen_1_label_7 = lv_label_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_label_7, 18, 33);
	lv_obj_set_size(ui->screen_1_label_7, 128, 9);
	lv_obj_set_scrollbar_mode(ui->screen_1_label_7, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->screen_1_label_7, "IPv4 : 192.168.100.1");
	lv_label_set_long_mode(ui->screen_1_label_7, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_label_7_main_main_default
	static lv_style_t style_screen_1_label_7_main_main_default;
	if (style_screen_1_label_7_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_label_7_main_main_default);
	else
		lv_style_init(&style_screen_1_label_7_main_main_default);
	lv_style_set_radius(&style_screen_1_label_7_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_1_label_7_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_screen_1_label_7_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_1_label_7_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_1_label_7_main_main_default, 0);
	lv_style_set_text_color(&style_screen_1_label_7_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_screen_1_label_7_main_main_default, &lv_font_arial_10);
	lv_style_set_text_letter_space(&style_screen_1_label_7_main_main_default, 0);
	lv_style_set_text_line_space(&style_screen_1_label_7_main_main_default, 0);
	lv_style_set_text_align(&style_screen_1_label_7_main_main_default, LV_TEXT_ALIGN_LEFT);
	lv_style_set_pad_left(&style_screen_1_label_7_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_1_label_7_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_1_label_7_main_main_default, 0);
	lv_style_set_pad_bottom(&style_screen_1_label_7_main_main_default, 0);
	lv_obj_add_style(ui->screen_1_label_7, &style_screen_1_label_7_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_1_btn_1
	ui->screen_1_btn_1 = lv_btn_create(ui->screen_1);
	lv_obj_set_pos(ui->screen_1_btn_1, 0, 0);
	lv_obj_set_size(ui->screen_1_btn_1, 284, 100);
	lv_obj_set_scrollbar_mode(ui->screen_1_btn_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_1_btn_1_main_main_default
	static lv_style_t style_screen_1_btn_1_main_main_default;
	if (style_screen_1_btn_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_1_btn_1_main_main_default);
	else
		lv_style_init(&style_screen_1_btn_1_main_main_default);
	lv_style_set_radius(&style_screen_1_btn_1_main_main_default, 5);
	lv_style_set_bg_color(&style_screen_1_btn_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_screen_1_btn_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_1_btn_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_1_btn_1_main_main_default, 0);
	lv_style_set_border_color(&style_screen_1_btn_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_screen_1_btn_1_main_main_default, 0);
	lv_style_set_border_opa(&style_screen_1_btn_1_main_main_default, 0);
	lv_style_set_text_color(&style_screen_1_btn_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_align(&style_screen_1_btn_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_obj_add_style(ui->screen_1_btn_1, &style_screen_1_btn_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_FOCUSED for style_screen_1_btn_1_main_main_focused
	static lv_style_t style_screen_1_btn_1_main_main_focused;
	if (style_screen_1_btn_1_main_main_focused.prop_cnt > 1)
		lv_style_reset(&style_screen_1_btn_1_main_main_focused);
	else
		lv_style_init(&style_screen_1_btn_1_main_main_focused);
	lv_style_set_radius(&style_screen_1_btn_1_main_main_focused, 5);
	lv_style_set_bg_color(&style_screen_1_btn_1_main_main_focused, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_screen_1_btn_1_main_main_focused, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_1_btn_1_main_main_focused, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_1_btn_1_main_main_focused, 0);
	lv_style_set_border_color(&style_screen_1_btn_1_main_main_focused, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_screen_1_btn_1_main_main_focused, 0);
	lv_style_set_border_opa(&style_screen_1_btn_1_main_main_focused, 0);
	lv_style_set_text_color(&style_screen_1_btn_1_main_main_focused, lv_color_make(0xff, 0xff, 0xff));
	lv_obj_add_style(ui->screen_1_btn_1, &style_screen_1_btn_1_main_main_focused, LV_PART_MAIN|LV_STATE_FOCUSED);

	//Write style state: LV_STATE_PRESSED for style_screen_1_btn_1_main_main_pressed
	static lv_style_t style_screen_1_btn_1_main_main_pressed;
	if (style_screen_1_btn_1_main_main_pressed.prop_cnt > 1)
		lv_style_reset(&style_screen_1_btn_1_main_main_pressed);
	else
		lv_style_init(&style_screen_1_btn_1_main_main_pressed);
	lv_style_set_radius(&style_screen_1_btn_1_main_main_pressed, 5);
	lv_style_set_bg_color(&style_screen_1_btn_1_main_main_pressed, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_screen_1_btn_1_main_main_pressed, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_1_btn_1_main_main_pressed, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_1_btn_1_main_main_pressed, 0);
	lv_style_set_border_color(&style_screen_1_btn_1_main_main_pressed, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_screen_1_btn_1_main_main_pressed, 0);
	lv_style_set_border_opa(&style_screen_1_btn_1_main_main_pressed, 0);
	lv_style_set_text_color(&style_screen_1_btn_1_main_main_pressed, lv_color_make(0xff, 0xff, 0xff));
	lv_obj_add_style(ui->screen_1_btn_1, &style_screen_1_btn_1_main_main_pressed, LV_PART_MAIN|LV_STATE_PRESSED);

	//Write style state: LV_STATE_CHECKED for style_screen_1_btn_1_main_main_checked
	static lv_style_t style_screen_1_btn_1_main_main_checked;
	if (style_screen_1_btn_1_main_main_checked.prop_cnt > 1)
		lv_style_reset(&style_screen_1_btn_1_main_main_checked);
	else
		lv_style_init(&style_screen_1_btn_1_main_main_checked);
	lv_style_set_radius(&style_screen_1_btn_1_main_main_checked, 5);
	lv_style_set_bg_color(&style_screen_1_btn_1_main_main_checked, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_screen_1_btn_1_main_main_checked, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_1_btn_1_main_main_checked, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_1_btn_1_main_main_checked, 0);
	lv_style_set_border_color(&style_screen_1_btn_1_main_main_checked, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_screen_1_btn_1_main_main_checked, 0);
	lv_style_set_border_opa(&style_screen_1_btn_1_main_main_checked, 0);
	lv_style_set_text_color(&style_screen_1_btn_1_main_main_checked, lv_color_make(0x00, 0x00, 0x00));
	lv_obj_add_style(ui->screen_1_btn_1, &style_screen_1_btn_1_main_main_checked, LV_PART_MAIN|LV_STATE_CHECKED);

	//Write style state: LV_STATE_DISABLED for style_screen_1_btn_1_main_main_disabled
	static lv_style_t style_screen_1_btn_1_main_main_disabled;
	if (style_screen_1_btn_1_main_main_disabled.prop_cnt > 1)
		lv_style_reset(&style_screen_1_btn_1_main_main_disabled);
	else
		lv_style_init(&style_screen_1_btn_1_main_main_disabled);
	lv_style_set_radius(&style_screen_1_btn_1_main_main_disabled, 5);
	lv_style_set_bg_color(&style_screen_1_btn_1_main_main_disabled, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_screen_1_btn_1_main_main_disabled, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_1_btn_1_main_main_disabled, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_1_btn_1_main_main_disabled, 0);
	lv_style_set_border_color(&style_screen_1_btn_1_main_main_disabled, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_screen_1_btn_1_main_main_disabled, 0);
	lv_style_set_border_opa(&style_screen_1_btn_1_main_main_disabled, 0);
	lv_style_set_text_color(&style_screen_1_btn_1_main_main_disabled, lv_color_make(0x00, 0x00, 0x00));
	lv_obj_add_style(ui->screen_1_btn_1, &style_screen_1_btn_1_main_main_disabled, LV_PART_MAIN|LV_STATE_DISABLED);
	ui->screen_1_btn_1_label = lv_label_create(ui->screen_1_btn_1);
	lv_label_set_text(ui->screen_1_btn_1_label, "");
	lv_obj_set_style_pad_all(ui->screen_1_btn_1, 0, LV_STATE_DEFAULT);
	lv_obj_align(ui->screen_1_btn_1_label, LV_ALIGN_CENTER, 0, 0);

	//Init events for screen
	events_init_screen_1(ui);
}