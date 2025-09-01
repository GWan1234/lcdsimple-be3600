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


void setup_scr_screen_4(lv_ui *ui){

	//Write codes screen_4
	ui->screen_4 = lv_obj_create(NULL);
	lv_obj_set_scrollbar_mode(ui->screen_4, LV_SCROLLBAR_MODE_OFF);
	lv_obj_clear_flag(ui->screen_4, LV_OBJ_FLAG_SCROLLABLE);  // [2,6](@ref)

	//Write style state: LV_STATE_DEFAULT for style_screen_4_main_main_default
	static lv_style_t style_screen_4_main_main_default;
	if (style_screen_4_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_4_main_main_default);
	else
		lv_style_init(&style_screen_4_main_main_default);
	lv_style_set_bg_color(&style_screen_4_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_opa(&style_screen_4_main_main_default, 0);
	lv_obj_add_style(ui->screen_4, &style_screen_4_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_4_label_1
	ui->screen_4_label_1 = lv_label_create(ui->screen_4);
	lv_obj_set_pos(ui->screen_4_label_1, 117, 18);
	lv_obj_set_size(ui->screen_4_label_1, 100, 32);
	lv_obj_set_scrollbar_mode(ui->screen_4_label_1, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->screen_4_label_1, "Label");
	lv_label_set_long_mode(ui->screen_4_label_1, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_screen_4_label_1_main_main_default
	static lv_style_t style_screen_4_label_1_main_main_default;
	if (style_screen_4_label_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_4_label_1_main_main_default);
	else
		lv_style_init(&style_screen_4_label_1_main_main_default);
	lv_style_set_radius(&style_screen_4_label_1_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_4_label_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_screen_4_label_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_4_label_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_4_label_1_main_main_default, 255);
	lv_style_set_text_color(&style_screen_4_label_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_screen_4_label_1_main_main_default, &lv_font_simsun_16);
	lv_style_set_text_letter_space(&style_screen_4_label_1_main_main_default, 2);
	lv_style_set_text_line_space(&style_screen_4_label_1_main_main_default, 0);
	lv_style_set_text_align(&style_screen_4_label_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_screen_4_label_1_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_4_label_1_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_4_label_1_main_main_default, 8);
	lv_style_set_pad_bottom(&style_screen_4_label_1_main_main_default, 0);
	lv_obj_add_style(ui->screen_4_label_1, &style_screen_4_label_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
}