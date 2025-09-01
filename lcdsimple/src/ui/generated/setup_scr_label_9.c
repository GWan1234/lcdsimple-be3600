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


void setup_scr_label_9(lv_ui *ui){

	//Write codes label_9
	ui->label_9 = lv_obj_create(NULL);
	lv_obj_set_scrollbar_mode(ui->label_9, LV_SCROLLBAR_MODE_OFF);
	lv_obj_clear_flag(ui->label_9, LV_OBJ_FLAG_SCROLLABLE);  // [2,6](@ref)

	//Write style state: LV_STATE_DEFAULT for style_label_9_main_main_default
	static lv_style_t style_label_9_main_main_default;
	if (style_label_9_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_main_main_default);
	else
		lv_style_init(&style_label_9_main_main_default);
	lv_style_set_radius(&style_label_9_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_main_main_default, 0);
	lv_style_set_text_color(&style_label_9_main_main_default, lv_color_make(0x99, 0x96, 0xab));
	lv_style_set_text_letter_space(&style_label_9_main_main_default, 0);
	lv_style_set_text_line_space(&style_label_9_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_main_main_default, 0);
	lv_style_set_pad_bottom(&style_label_9_main_main_default, 0);
	lv_obj_add_style(ui->label_9, &style_label_9_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_Four_page
	ui->label_9_Four_page = lv_label_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_Four_page, 0, 0);
	lv_obj_set_size(ui->label_9_Four_page, 284, 76);
	lv_obj_set_scrollbar_mode(ui->label_9_Four_page, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->label_9_Four_page, "");
	lv_label_set_long_mode(ui->label_9_Four_page, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_label_9_four_page_main_main_default
	static lv_style_t style_label_9_four_page_main_main_default;
	if (style_label_9_four_page_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_four_page_main_main_default);
	else
		lv_style_init(&style_label_9_four_page_main_main_default);
	lv_style_set_radius(&style_label_9_four_page_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_four_page_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_bg_grad_color(&style_label_9_four_page_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_four_page_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_four_page_main_main_default, 255);
	lv_style_set_text_color(&style_label_9_four_page_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_letter_space(&style_label_9_four_page_main_main_default, 2);
	lv_style_set_text_line_space(&style_label_9_four_page_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_four_page_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_four_page_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_four_page_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_four_page_main_main_default, 8);
	lv_style_set_pad_bottom(&style_label_9_four_page_main_main_default, 0);
	lv_obj_add_style(ui->label_9_Four_page, &style_label_9_four_page_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_label_1
	ui->label_9_label_1 = lv_label_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_label_1, 7, 6);
	lv_obj_set_size(ui->label_9_label_1, 111, 65);
	lv_obj_set_scrollbar_mode(ui->label_9_label_1, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->label_9_label_1, "");
	lv_label_set_long_mode(ui->label_9_label_1, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_label_9_label_1_main_main_default
	static lv_style_t style_label_9_label_1_main_main_default;
	if (style_label_9_label_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_label_1_main_main_default);
	else
		lv_style_init(&style_label_9_label_1_main_main_default);
	lv_style_set_radius(&style_label_9_label_1_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_label_1_main_main_default, lv_color_make(0x14, 0x11, 0x26));
	lv_style_set_bg_grad_color(&style_label_9_label_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_label_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_label_1_main_main_default, 255);
	lv_style_set_text_color(&style_label_9_label_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_letter_space(&style_label_9_label_1_main_main_default, 2);
	lv_style_set_text_line_space(&style_label_9_label_1_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_label_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_label_1_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_label_1_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_label_1_main_main_default, 8);
	lv_style_set_pad_bottom(&style_label_9_label_1_main_main_default, 0);
	lv_obj_add_style(ui->label_9_label_1, &style_label_9_label_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_label_2
	ui->label_9_label_2 = lv_label_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_label_2, 125, 6);
	lv_obj_set_size(ui->label_9_label_2, 152, 65);
	lv_obj_set_scrollbar_mode(ui->label_9_label_2, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->label_9_label_2, "");
	lv_label_set_long_mode(ui->label_9_label_2, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_label_9_label_2_main_main_default
	static lv_style_t style_label_9_label_2_main_main_default;
	if (style_label_9_label_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_label_2_main_main_default);
	else
		lv_style_init(&style_label_9_label_2_main_main_default);
	lv_style_set_radius(&style_label_9_label_2_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_label_2_main_main_default, lv_color_make(0x14, 0x11, 0x26));
	lv_style_set_bg_grad_color(&style_label_9_label_2_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_label_2_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_label_2_main_main_default, 255);
	lv_style_set_text_color(&style_label_9_label_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_letter_space(&style_label_9_label_2_main_main_default, 2);
	lv_style_set_text_line_space(&style_label_9_label_2_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_label_2_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_label_2_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_label_2_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_label_2_main_main_default, 8);
	lv_style_set_pad_bottom(&style_label_9_label_2_main_main_default, 0);
	lv_obj_add_style(ui->label_9_label_2, &style_label_9_label_2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_arc_2
	ui->label_9_arc_2 = lv_arc_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_arc_2, 52, 6);
	lv_obj_set_size(ui->label_9_arc_2, 79, 100);
	lv_obj_set_scrollbar_mode(ui->label_9_arc_2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_label_9_arc_2_main_main_default
	static lv_style_t style_label_9_arc_2_main_main_default;
	if (style_label_9_arc_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_arc_2_main_main_default);
	else
		lv_style_init(&style_label_9_arc_2_main_main_default);
	lv_style_set_radius(&style_label_9_arc_2_main_main_default, 6);
	lv_style_set_bg_color(&style_label_9_arc_2_main_main_default, lv_color_make(0xf6, 0xf6, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_arc_2_main_main_default, lv_color_make(0xf6, 0xf6, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_arc_2_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_arc_2_main_main_default, 0);
	lv_style_set_border_width(&style_label_9_arc_2_main_main_default, 0);
	lv_style_set_pad_left(&style_label_9_arc_2_main_main_default, 20);
	lv_style_set_pad_right(&style_label_9_arc_2_main_main_default, 20);
	lv_style_set_pad_top(&style_label_9_arc_2_main_main_default, 20);
	lv_style_set_pad_bottom(&style_label_9_arc_2_main_main_default, 20);
	lv_style_set_arc_color(&style_label_9_arc_2_main_main_default, lv_color_make(0x75, 0x73, 0x80));
	lv_style_set_arc_width(&style_label_9_arc_2_main_main_default, 4);
	lv_obj_add_style(ui->label_9_arc_2, &style_label_9_arc_2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_label_9_arc_2_main_indicator_default
	static lv_style_t style_label_9_arc_2_main_indicator_default;
	if (style_label_9_arc_2_main_indicator_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_arc_2_main_indicator_default);
	else
		lv_style_init(&style_label_9_arc_2_main_indicator_default);
	lv_style_set_arc_color(&style_label_9_arc_2_main_indicator_default, lv_color_make(0x39, 0xbb, 0x8d));
	lv_style_set_arc_width(&style_label_9_arc_2_main_indicator_default, 4);
	lv_obj_add_style(ui->label_9_arc_2, &style_label_9_arc_2_main_indicator_default, LV_PART_INDICATOR|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_label_9_arc_2_main_knob_default
	static lv_style_t style_label_9_arc_2_main_knob_default;
	if (style_label_9_arc_2_main_knob_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_arc_2_main_knob_default);
	else
		lv_style_init(&style_label_9_arc_2_main_knob_default);
	lv_style_set_bg_color(&style_label_9_arc_2_main_knob_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_arc_2_main_knob_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_arc_2_main_knob_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_arc_2_main_knob_default, 0);
	lv_style_set_pad_all(&style_label_9_arc_2_main_knob_default, 0);
	lv_obj_add_style(ui->label_9_arc_2, &style_label_9_arc_2_main_knob_default, LV_PART_KNOB|LV_STATE_DEFAULT);
	lv_arc_set_mode(ui->label_9_arc_2, LV_ARC_MODE_NORMAL);
	lv_arc_set_range(ui->label_9_arc_2, 0, 100);
	lv_arc_set_bg_angles(ui->label_9_arc_2, 0, 360);
	lv_arc_set_angles(ui->label_9_arc_2, 270, 90);
	lv_arc_set_rotation(ui->label_9_arc_2, 0);
	lv_obj_set_style_arc_rounded(ui->label_9_arc_2, 0,  LV_PART_INDICATOR|LV_STATE_DEFAULT);
	lv_obj_set_style_arc_rounded(ui->label_9_arc_2, 0, LV_STATE_DEFAULT);

	//Write codes label_9_label_4
	ui->label_9_label_4 = lv_label_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_label_4, 64, 3);
	lv_obj_set_size(ui->label_9_label_4, 56, 25);
	lv_obj_set_scrollbar_mode(ui->label_9_label_4, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->label_9_label_4, "温度");
	lv_label_set_long_mode(ui->label_9_label_4, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_label_9_label_4_main_main_default
	static lv_style_t style_label_9_label_4_main_main_default;
	if (style_label_9_label_4_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_label_4_main_main_default);
	else
		lv_style_init(&style_label_9_label_4_main_main_default);
	lv_style_set_radius(&style_label_9_label_4_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_label_4_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_label_4_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_label_4_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_label_4_main_main_default, 0);
	lv_style_set_text_color(&style_label_9_label_4_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_label_9_label_4_main_main_default, &lv_font_simsun_12);
	lv_style_set_text_letter_space(&style_label_9_label_4_main_main_default, 0);
	lv_style_set_text_line_space(&style_label_9_label_4_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_label_4_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_label_4_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_label_4_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_label_4_main_main_default, 8);
	lv_style_set_pad_bottom(&style_label_9_label_4_main_main_default, 0);
	lv_obj_add_style(ui->label_9_label_4, &style_label_9_label_4_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_label_6
	ui->label_9_label_6 = lv_label_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_label_6, 80, 33);
	lv_obj_set_size(ui->label_9_label_6, 25, 25);
	lv_obj_set_scrollbar_mode(ui->label_9_label_6, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->label_9_label_6, "45℃");
	lv_label_set_long_mode(ui->label_9_label_6, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_label_9_label_6_main_main_default
	static lv_style_t style_label_9_label_6_main_main_default;
	if (style_label_9_label_6_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_label_6_main_main_default);
	else
		lv_style_init(&style_label_9_label_6_main_main_default);
	lv_style_set_radius(&style_label_9_label_6_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_label_6_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_label_6_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_label_6_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_label_6_main_main_default, 0);
	lv_style_set_text_color(&style_label_9_label_6_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_label_9_label_6_main_main_default, &lv_font_simsun_12);
	lv_style_set_text_letter_space(&style_label_9_label_6_main_main_default, 0);
	lv_style_set_text_line_space(&style_label_9_label_6_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_label_6_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_label_6_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_label_6_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_label_6_main_main_default, 8);
	lv_style_set_pad_bottom(&style_label_9_label_6_main_main_default, 0);
	lv_obj_add_style(ui->label_9_label_6, &style_label_9_label_6_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_label_7
	ui->label_9_label_7 = lv_label_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_label_7, 127, 12);
	lv_obj_set_size(ui->label_9_label_7, 44, 11);
	lv_obj_set_scrollbar_mode(ui->label_9_label_7, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->label_9_label_7, "硬盘1:");
	lv_label_set_long_mode(ui->label_9_label_7, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_label_9_label_7_main_main_default
	static lv_style_t style_label_9_label_7_main_main_default;
	if (style_label_9_label_7_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_label_7_main_main_default);
	else
		lv_style_init(&style_label_9_label_7_main_main_default);
	lv_style_set_radius(&style_label_9_label_7_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_label_7_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_label_7_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_label_7_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_label_7_main_main_default, 0);
	lv_style_set_text_color(&style_label_9_label_7_main_main_default, lv_color_make(0x99, 0x96, 0xab));
	lv_style_set_text_font(&style_label_9_label_7_main_main_default, &lv_font_simsun_10);
	lv_style_set_text_letter_space(&style_label_9_label_7_main_main_default, 0);
	lv_style_set_text_line_space(&style_label_9_label_7_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_label_7_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_label_7_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_label_7_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_label_7_main_main_default, 0);
	lv_style_set_pad_bottom(&style_label_9_label_7_main_main_default, 0);
	lv_obj_add_style(ui->label_9_label_7, &style_label_9_label_7_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_arc_3
	ui->label_9_arc_3 = lv_arc_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_arc_3, -7, 6);
	lv_obj_set_size(ui->label_9_arc_3, 79, 100);
	lv_obj_set_scrollbar_mode(ui->label_9_arc_3, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_label_9_arc_3_main_main_default
	static lv_style_t style_label_9_arc_3_main_main_default;
	if (style_label_9_arc_3_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_arc_3_main_main_default);
	else
		lv_style_init(&style_label_9_arc_3_main_main_default);
	lv_style_set_radius(&style_label_9_arc_3_main_main_default, 6);
	lv_style_set_bg_color(&style_label_9_arc_3_main_main_default, lv_color_make(0xf6, 0xf6, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_arc_3_main_main_default, lv_color_make(0xf6, 0xf6, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_arc_3_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_arc_3_main_main_default, 0);
	lv_style_set_border_width(&style_label_9_arc_3_main_main_default, 0);
	lv_style_set_pad_left(&style_label_9_arc_3_main_main_default, 20);
	lv_style_set_pad_right(&style_label_9_arc_3_main_main_default, 20);
	lv_style_set_pad_top(&style_label_9_arc_3_main_main_default, 20);
	lv_style_set_pad_bottom(&style_label_9_arc_3_main_main_default, 20);
	lv_style_set_arc_color(&style_label_9_arc_3_main_main_default, lv_color_make(0x75, 0x73, 0x80));
	lv_style_set_arc_width(&style_label_9_arc_3_main_main_default, 4);
	lv_obj_add_style(ui->label_9_arc_3, &style_label_9_arc_3_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_label_9_arc_3_main_indicator_default
	static lv_style_t style_label_9_arc_3_main_indicator_default;
	if (style_label_9_arc_3_main_indicator_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_arc_3_main_indicator_default);
	else
		lv_style_init(&style_label_9_arc_3_main_indicator_default);
	lv_style_set_arc_color(&style_label_9_arc_3_main_indicator_default, lv_color_make(0xf2, 0x7e, 0x05));
	lv_style_set_arc_width(&style_label_9_arc_3_main_indicator_default, 4);
	lv_obj_add_style(ui->label_9_arc_3, &style_label_9_arc_3_main_indicator_default, LV_PART_INDICATOR|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_label_9_arc_3_main_knob_default
	static lv_style_t style_label_9_arc_3_main_knob_default;
	if (style_label_9_arc_3_main_knob_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_arc_3_main_knob_default);
	else
		lv_style_init(&style_label_9_arc_3_main_knob_default);
	lv_style_set_bg_color(&style_label_9_arc_3_main_knob_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_arc_3_main_knob_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_arc_3_main_knob_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_arc_3_main_knob_default, 0);
	lv_style_set_pad_all(&style_label_9_arc_3_main_knob_default, 0);
	lv_obj_add_style(ui->label_9_arc_3, &style_label_9_arc_3_main_knob_default, LV_PART_KNOB|LV_STATE_DEFAULT);
	lv_arc_set_mode(ui->label_9_arc_3, LV_ARC_MODE_NORMAL);
	lv_arc_set_range(ui->label_9_arc_3, 0, 100);
	lv_arc_set_bg_angles(ui->label_9_arc_3, 0, 360);
	lv_arc_set_angles(ui->label_9_arc_3, 270, 180);
	lv_arc_set_rotation(ui->label_9_arc_3, 0);
	lv_obj_set_style_arc_rounded(ui->label_9_arc_3, 0,  LV_PART_INDICATOR|LV_STATE_DEFAULT);
	lv_obj_set_style_arc_rounded(ui->label_9_arc_3, 0, LV_STATE_DEFAULT);

	//Write codes label_9_label_8
	ui->label_9_label_8 = lv_label_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_label_8, 127, 32);
	lv_obj_set_size(ui->label_9_label_8, 42, 11);
	lv_obj_set_scrollbar_mode(ui->label_9_label_8, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->label_9_label_8, "硬盘2:");
	lv_label_set_long_mode(ui->label_9_label_8, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_label_9_label_8_main_main_default
	static lv_style_t style_label_9_label_8_main_main_default;
	if (style_label_9_label_8_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_label_8_main_main_default);
	else
		lv_style_init(&style_label_9_label_8_main_main_default);
	lv_style_set_radius(&style_label_9_label_8_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_label_8_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_label_8_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_label_8_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_label_8_main_main_default, 0);
	lv_style_set_text_color(&style_label_9_label_8_main_main_default, lv_color_make(0x99, 0x96, 0xab));
	lv_style_set_text_font(&style_label_9_label_8_main_main_default, &lv_font_simsun_10);
	lv_style_set_text_letter_space(&style_label_9_label_8_main_main_default, 0);
	lv_style_set_text_line_space(&style_label_9_label_8_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_label_8_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_label_8_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_label_8_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_label_8_main_main_default, 0);
	lv_style_set_pad_bottom(&style_label_9_label_8_main_main_default, 0);
	lv_obj_add_style(ui->label_9_label_8, &style_label_9_label_8_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_label_3
	ui->label_9_label_3 = lv_label_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_label_3, 5, 3);
	lv_obj_set_size(ui->label_9_label_3, 56, 25);
	lv_obj_set_scrollbar_mode(ui->label_9_label_3, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->label_9_label_3, "CPU");
	lv_label_set_long_mode(ui->label_9_label_3, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_label_9_label_3_main_main_default
	static lv_style_t style_label_9_label_3_main_main_default;
	if (style_label_9_label_3_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_label_3_main_main_default);
	else
		lv_style_init(&style_label_9_label_3_main_main_default);
	lv_style_set_radius(&style_label_9_label_3_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_label_3_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_label_3_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_label_3_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_label_3_main_main_default, 0);
	lv_style_set_text_color(&style_label_9_label_3_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_label_9_label_3_main_main_default, &lv_font_arial_12);
	lv_style_set_text_letter_space(&style_label_9_label_3_main_main_default, 0);
	lv_style_set_text_line_space(&style_label_9_label_3_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_label_3_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_label_3_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_label_3_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_label_3_main_main_default, 8);
	lv_style_set_pad_bottom(&style_label_9_label_3_main_main_default, 0);
	lv_obj_add_style(ui->label_9_label_3, &style_label_9_label_3_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_label_9
	ui->label_9_label_9 = lv_label_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_label_9, 127, 52);
	lv_obj_set_size(ui->label_9_label_9, 42, 11);
	lv_obj_set_scrollbar_mode(ui->label_9_label_9, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->label_9_label_9, "硬盘1:");
	lv_label_set_long_mode(ui->label_9_label_9, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_label_9_label_9_main_main_default
	static lv_style_t style_label_9_label_9_main_main_default;
	if (style_label_9_label_9_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_label_9_main_main_default);
	else
		lv_style_init(&style_label_9_label_9_main_main_default);
	lv_style_set_radius(&style_label_9_label_9_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_label_9_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_label_9_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_label_9_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_label_9_main_main_default, 0);
	lv_style_set_text_color(&style_label_9_label_9_main_main_default, lv_color_make(0x99, 0x96, 0xab));
	lv_style_set_text_font(&style_label_9_label_9_main_main_default, &lv_font_simsun_10);
	lv_style_set_text_letter_space(&style_label_9_label_9_main_main_default, 0);
	lv_style_set_text_line_space(&style_label_9_label_9_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_label_9_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_label_9_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_label_9_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_label_9_main_main_default, 0);
	lv_style_set_pad_bottom(&style_label_9_label_9_main_main_default, 0);
	lv_obj_add_style(ui->label_9_label_9, &style_label_9_label_9_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_bar_1
	ui->label_9_bar_1 = lv_bar_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_bar_1, 169, 13);
	lv_obj_set_size(ui->label_9_bar_1, 45, 10);
	lv_obj_set_scrollbar_mode(ui->label_9_bar_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_label_9_bar_1_main_main_default
	static lv_style_t style_label_9_bar_1_main_main_default;
	if (style_label_9_bar_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_bar_1_main_main_default);
	else
		lv_style_init(&style_label_9_bar_1_main_main_default);
	lv_style_set_radius(&style_label_9_bar_1_main_main_default, 10);
	lv_style_set_bg_color(&style_label_9_bar_1_main_main_default, lv_color_make(0x2a, 0x29, 0x39));
	lv_style_set_bg_grad_color(&style_label_9_bar_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_bar_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_bar_1_main_main_default, 255);
	lv_obj_add_style(ui->label_9_bar_1, &style_label_9_bar_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_label_9_bar_1_main_indicator_default
	static lv_style_t style_label_9_bar_1_main_indicator_default;
	if (style_label_9_bar_1_main_indicator_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_bar_1_main_indicator_default);
	else
		lv_style_init(&style_label_9_bar_1_main_indicator_default);
	lv_style_set_radius(&style_label_9_bar_1_main_indicator_default, 10);
	lv_style_set_bg_color(&style_label_9_bar_1_main_indicator_default, lv_color_make(0x60, 0xe4, 0xb3));
	lv_style_set_bg_grad_color(&style_label_9_bar_1_main_indicator_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_bar_1_main_indicator_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_bar_1_main_indicator_default, 255);
	lv_obj_add_style(ui->label_9_bar_1, &style_label_9_bar_1_main_indicator_default, LV_PART_INDICATOR|LV_STATE_DEFAULT);
	lv_obj_set_style_anim_time(ui->label_9_bar_1, 1000, 0);
	lv_bar_set_mode(ui->label_9_bar_1, LV_BAR_MODE_NORMAL);
	lv_bar_set_value(ui->label_9_bar_1, 50, LV_ANIM_OFF);

	//Write codes label_9_label_5
	ui->label_9_label_5 = lv_label_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_label_5, 20, 33);
	lv_obj_set_size(ui->label_9_label_5, 25, 25);
	lv_obj_set_scrollbar_mode(ui->label_9_label_5, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->label_9_label_5, "90%");
	lv_label_set_long_mode(ui->label_9_label_5, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_label_9_label_5_main_main_default
	static lv_style_t style_label_9_label_5_main_main_default;
	if (style_label_9_label_5_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_label_5_main_main_default);
	else
		lv_style_init(&style_label_9_label_5_main_main_default);
	lv_style_set_radius(&style_label_9_label_5_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_label_5_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_label_5_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_label_5_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_label_5_main_main_default, 0);
	lv_style_set_text_color(&style_label_9_label_5_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_label_9_label_5_main_main_default, &lv_font_simsun_12);
	lv_style_set_text_letter_space(&style_label_9_label_5_main_main_default, 0);
	lv_style_set_text_line_space(&style_label_9_label_5_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_label_5_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_label_5_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_label_5_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_label_5_main_main_default, 8);
	lv_style_set_pad_bottom(&style_label_9_label_5_main_main_default, 0);
	lv_obj_add_style(ui->label_9_label_5, &style_label_9_label_5_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_bar_2
	ui->label_9_bar_2 = lv_bar_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_bar_2, 169, 33);
	lv_obj_set_size(ui->label_9_bar_2, 45, 10);
	lv_obj_set_scrollbar_mode(ui->label_9_bar_2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_label_9_bar_2_main_main_default
	static lv_style_t style_label_9_bar_2_main_main_default;
	if (style_label_9_bar_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_bar_2_main_main_default);
	else
		lv_style_init(&style_label_9_bar_2_main_main_default);
	lv_style_set_radius(&style_label_9_bar_2_main_main_default, 10);
	lv_style_set_bg_color(&style_label_9_bar_2_main_main_default, lv_color_make(0x2a, 0x29, 0x39));
	lv_style_set_bg_grad_color(&style_label_9_bar_2_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_bar_2_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_bar_2_main_main_default, 255);
	lv_obj_add_style(ui->label_9_bar_2, &style_label_9_bar_2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_label_9_bar_2_main_indicator_default
	static lv_style_t style_label_9_bar_2_main_indicator_default;
	if (style_label_9_bar_2_main_indicator_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_bar_2_main_indicator_default);
	else
		lv_style_init(&style_label_9_bar_2_main_indicator_default);
	lv_style_set_radius(&style_label_9_bar_2_main_indicator_default, 10);
	lv_style_set_bg_color(&style_label_9_bar_2_main_indicator_default, lv_color_make(0xf5, 0x91, 0x1f));
	lv_style_set_bg_grad_color(&style_label_9_bar_2_main_indicator_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_bar_2_main_indicator_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_bar_2_main_indicator_default, 255);
	lv_obj_add_style(ui->label_9_bar_2, &style_label_9_bar_2_main_indicator_default, LV_PART_INDICATOR|LV_STATE_DEFAULT);
	lv_obj_set_style_anim_time(ui->label_9_bar_2, 1000, 0);
	lv_bar_set_mode(ui->label_9_bar_2, LV_BAR_MODE_NORMAL);
	lv_bar_set_value(ui->label_9_bar_2, 70, LV_ANIM_OFF);

	//Write codes label_9_bar_3
	ui->label_9_bar_3 = lv_bar_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_bar_3, 169, 53);
	lv_obj_set_size(ui->label_9_bar_3, 45, 10);
	lv_obj_set_scrollbar_mode(ui->label_9_bar_3, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_label_9_bar_3_main_main_default
	static lv_style_t style_label_9_bar_3_main_main_default;
	if (style_label_9_bar_3_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_bar_3_main_main_default);
	else
		lv_style_init(&style_label_9_bar_3_main_main_default);
	lv_style_set_radius(&style_label_9_bar_3_main_main_default, 10);
	lv_style_set_bg_color(&style_label_9_bar_3_main_main_default, lv_color_make(0x2a, 0x29, 0x39));
	lv_style_set_bg_grad_color(&style_label_9_bar_3_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_bar_3_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_bar_3_main_main_default, 255);
	lv_obj_add_style(ui->label_9_bar_3, &style_label_9_bar_3_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_label_9_bar_3_main_indicator_default
	static lv_style_t style_label_9_bar_3_main_indicator_default;
	if (style_label_9_bar_3_main_indicator_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_bar_3_main_indicator_default);
	else
		lv_style_init(&style_label_9_bar_3_main_indicator_default);
	lv_style_set_radius(&style_label_9_bar_3_main_indicator_default, 10);
	lv_style_set_bg_color(&style_label_9_bar_3_main_indicator_default, lv_color_make(0xf6, 0xef, 0x23));
	lv_style_set_bg_grad_color(&style_label_9_bar_3_main_indicator_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_bar_3_main_indicator_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_bar_3_main_indicator_default, 255);
	lv_obj_add_style(ui->label_9_bar_3, &style_label_9_bar_3_main_indicator_default, LV_PART_INDICATOR|LV_STATE_DEFAULT);
	lv_obj_set_style_anim_time(ui->label_9_bar_3, 1000, 0);
	lv_bar_set_mode(ui->label_9_bar_3, LV_BAR_MODE_NORMAL);
	lv_bar_set_value(ui->label_9_bar_3, 0, LV_ANIM_OFF);

	//Write codes label_9_label_10
	ui->label_9_label_10 = lv_label_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_label_10, 222, 12);
	lv_obj_set_size(ui->label_9_label_10, 45, 11);
	lv_obj_set_scrollbar_mode(ui->label_9_label_10, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->label_9_label_10, "134G/848G");
	lv_label_set_long_mode(ui->label_9_label_10, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_label_9_label_10_main_main_default
	static lv_style_t style_label_9_label_10_main_main_default;
	if (style_label_9_label_10_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_label_10_main_main_default);
	else
		lv_style_init(&style_label_9_label_10_main_main_default);
	lv_style_set_radius(&style_label_9_label_10_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_label_10_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_label_10_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_label_10_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_label_10_main_main_default, 0);
	lv_style_set_text_color(&style_label_9_label_10_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_label_9_label_10_main_main_default, &lv_font_simsun_10);
	lv_style_set_text_letter_space(&style_label_9_label_10_main_main_default, 0);
	lv_style_set_text_line_space(&style_label_9_label_10_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_label_10_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_label_10_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_label_10_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_label_10_main_main_default, 0);
	lv_style_set_pad_bottom(&style_label_9_label_10_main_main_default, 0);
	lv_obj_add_style(ui->label_9_label_10, &style_label_9_label_10_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_label_11
	ui->label_9_label_11 = lv_label_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_label_11, 222, 32);
	lv_obj_set_size(ui->label_9_label_11, 45, 11);
	lv_obj_set_scrollbar_mode(ui->label_9_label_11, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->label_9_label_11, "734G/848G");
	lv_label_set_long_mode(ui->label_9_label_11, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_label_9_label_11_main_main_default
	static lv_style_t style_label_9_label_11_main_main_default;
	if (style_label_9_label_11_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_label_11_main_main_default);
	else
		lv_style_init(&style_label_9_label_11_main_main_default);
	lv_style_set_radius(&style_label_9_label_11_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_label_11_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_label_11_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_label_11_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_label_11_main_main_default, 0);
	lv_style_set_text_color(&style_label_9_label_11_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_label_9_label_11_main_main_default, &lv_font_simsun_10);
	lv_style_set_text_letter_space(&style_label_9_label_11_main_main_default, 0);
	lv_style_set_text_line_space(&style_label_9_label_11_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_label_11_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_label_11_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_label_11_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_label_11_main_main_default, 0);
	lv_style_set_pad_bottom(&style_label_9_label_11_main_main_default, 0);
	lv_obj_add_style(ui->label_9_label_11, &style_label_9_label_11_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_label_12
	ui->label_9_label_12 = lv_label_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_label_12, 222, 52);
	lv_obj_set_size(ui->label_9_label_12, 45, 11);
	lv_obj_set_scrollbar_mode(ui->label_9_label_12, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->label_9_label_12, "--/--");
	lv_label_set_long_mode(ui->label_9_label_12, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_label_9_label_12_main_main_default
	static lv_style_t style_label_9_label_12_main_main_default;
	if (style_label_9_label_12_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_label_12_main_main_default);
	else
		lv_style_init(&style_label_9_label_12_main_main_default);
	lv_style_set_radius(&style_label_9_label_12_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_label_12_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_label_12_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_label_12_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_label_12_main_main_default, 0);
	lv_style_set_text_color(&style_label_9_label_12_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_label_9_label_12_main_main_default, &lv_font_simsun_10);
	lv_style_set_text_letter_space(&style_label_9_label_12_main_main_default, 0);
	lv_style_set_text_line_space(&style_label_9_label_12_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_label_12_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_label_12_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_label_12_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_label_12_main_main_default, 0);
	lv_style_set_pad_bottom(&style_label_9_label_12_main_main_default, 0);
	lv_obj_add_style(ui->label_9_label_12, &style_label_9_label_12_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_label_13
	ui->label_9_label_13 = lv_label_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_label_13, 127, 52);
	lv_obj_set_size(ui->label_9_label_13, 42, 11);
	lv_obj_set_scrollbar_mode(ui->label_9_label_13, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->label_9_label_13, "硬盘3:");
	lv_label_set_long_mode(ui->label_9_label_13, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_label_9_label_13_main_main_default
	static lv_style_t style_label_9_label_13_main_main_default;
	if (style_label_9_label_13_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_label_13_main_main_default);
	else
		lv_style_init(&style_label_9_label_13_main_main_default);
	lv_style_set_radius(&style_label_9_label_13_main_main_default, 0);
	lv_style_set_bg_color(&style_label_9_label_13_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_label_13_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_label_13_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_label_13_main_main_default, 0);
	lv_style_set_text_color(&style_label_9_label_13_main_main_default, lv_color_make(0x99, 0x96, 0xab));
	lv_style_set_text_font(&style_label_9_label_13_main_main_default, &lv_font_simsun_10);
	lv_style_set_text_letter_space(&style_label_9_label_13_main_main_default, 0);
	lv_style_set_text_line_space(&style_label_9_label_13_main_main_default, 0);
	lv_style_set_text_align(&style_label_9_label_13_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_label_9_label_13_main_main_default, 0);
	lv_style_set_pad_right(&style_label_9_label_13_main_main_default, 0);
	lv_style_set_pad_top(&style_label_9_label_13_main_main_default, 0);
	lv_style_set_pad_bottom(&style_label_9_label_13_main_main_default, 0);
	lv_obj_add_style(ui->label_9_label_13, &style_label_9_label_13_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes label_9_btn_1
	ui->label_9_btn_1 = lv_btn_create(ui->label_9);
	lv_obj_set_pos(ui->label_9_btn_1, 0, 0);
	lv_obj_set_size(ui->label_9_btn_1, 284, 76);
	lv_obj_set_scrollbar_mode(ui->label_9_btn_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_label_9_btn_1_main_main_default
	static lv_style_t style_label_9_btn_1_main_main_default;
	if (style_label_9_btn_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_label_9_btn_1_main_main_default);
	else
		lv_style_init(&style_label_9_btn_1_main_main_default);
	lv_style_set_radius(&style_label_9_btn_1_main_main_default, 5);
	lv_style_set_bg_color(&style_label_9_btn_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_label_9_btn_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_label_9_btn_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_label_9_btn_1_main_main_default, 0);
	lv_style_set_border_color(&style_label_9_btn_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_label_9_btn_1_main_main_default, 0);
	lv_style_set_border_opa(&style_label_9_btn_1_main_main_default, 255);
	lv_style_set_text_color(&style_label_9_btn_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_align(&style_label_9_btn_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_obj_add_style(ui->label_9_btn_1, &style_label_9_btn_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	ui->label_9_btn_1_label = lv_label_create(ui->label_9_btn_1);
	lv_label_set_text(ui->label_9_btn_1_label, "");
	lv_obj_set_style_pad_all(ui->label_9_btn_1, 0, LV_STATE_DEFAULT);
	lv_obj_align(ui->label_9_btn_1_label, LV_ALIGN_CENTER, 0, 0);

	//Init events for screen
	events_init_label_9(ui);
}