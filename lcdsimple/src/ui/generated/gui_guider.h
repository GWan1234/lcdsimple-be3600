/*
 * Copyright 2025 NXP
 * SPDX-License-Identifier: MIT
 * The auto-generated can only be used on NXP devices
 */

#ifndef GUI_GUIDER_H
#define GUI_GUIDER_H
#ifdef __cplusplus
extern "C" {
#endif

#include "lvgl/lvgl.h"
#include "guider_fonts.h"

typedef struct
{
	lv_obj_t *error;
	bool error_del;
	lv_obj_t *error_label_21;
	lv_obj_t *error_label_19;
	lv_obj_t *error_label_17;
	lv_obj_t *error_label_13;
	lv_obj_t *error_img_12;
	lv_obj_t *error_label_16;
	lv_obj_t *error_label_18;
	lv_obj_t *error_img_15;
	lv_obj_t *error_img_13;
	lv_obj_t *error_label_20;
	lv_obj_t *error_btn_2;
	lv_obj_t *error_btn_2_label;
	lv_obj_t *error_label_22;
	lv_obj_t *error_label_23;
	lv_obj_t *label_9;
	bool label_9_del;
	lv_obj_t *label_9_Four_page;
	lv_obj_t *label_9_label_1;
	lv_obj_t *label_9_label_2;
	lv_obj_t *label_9_arc_2;
	lv_obj_t *label_9_label_4;
	lv_obj_t *label_9_label_6;
	lv_obj_t *label_9_label_7;
	lv_obj_t *label_9_arc_3;
	lv_obj_t *label_9_label_8;
	lv_obj_t *label_9_label_3;
	lv_obj_t *label_9_label_9;
	lv_obj_t *label_9_bar_1;
	lv_obj_t *label_9_label_5;
	lv_obj_t *label_9_bar_2;
	lv_obj_t *label_9_bar_3;
	lv_obj_t *label_9_label_10;
	lv_obj_t *label_9_label_11;
	lv_obj_t *label_9_label_12;
	lv_obj_t *label_9_label_13;
	lv_obj_t *label_9_btn_1;
	lv_obj_t *label_9_btn_1_label;
	lv_obj_t *screen_1;
	bool screen_1_del;
	lv_obj_t *screen_1_label_11;
	lv_obj_t *screen_1_img_9;
	lv_obj_t *screen_1_img_14;
	lv_obj_t *screen_1_img_13;
	lv_obj_t *screen_1_img_16;
	lv_obj_t *screen_1_img_17;
	lv_obj_t *screen_1_label_10;
	lv_obj_t *screen_1_img_10;
	lv_obj_t *screen_1_img_11;
	lv_obj_t *screen_1_img_15;
	lv_obj_t *screen_1_label_12;
	lv_obj_t *screen_1_label_9;
	lv_obj_t *screen_1_label_8;
	lv_obj_t *screen_1_label_7;
	lv_obj_t *screen_1_btn_1;
	lv_obj_t *screen_1_btn_1_label;
	lv_obj_t *screen_3;
	bool screen_3_del;
	lv_obj_t *screen_3_label_11;
	lv_obj_t *screen_3_img_9;
	lv_obj_t *screen_3_img_14;
	lv_obj_t *screen_3_img_13;
	lv_obj_t *screen_3_img_16;
	lv_obj_t *screen_3_img_17;
	lv_obj_t *screen_3_label_10;
	lv_obj_t *screen_3_img_10;
	lv_obj_t *screen_3_img_11;
	lv_obj_t *screen_3_img_15;
	lv_obj_t *screen_3_label_12;
	lv_obj_t *screen_3_label_9;
	lv_obj_t *screen_3_label_8;
	lv_obj_t *screen_3_label_7;
	lv_obj_t *screen_3_label_13;
	lv_obj_t *screen_3_label_16;
	lv_obj_t *screen_3_label_14;
	lv_obj_t *screen_3_img_19;
	lv_obj_t *screen_3_label_15;
	lv_obj_t *screen_3_img_18;
	lv_obj_t *screen_3_label_17;
	lv_obj_t *screen_3_label_18;
	lv_obj_t *screen_3_label_19;
	lv_obj_t *screen_3_label_20;
	lv_obj_t *screen_3_label_21;
	lv_obj_t *screen_3_btn_1;
	lv_obj_t *screen_3_btn_1_label;
	lv_obj_t *screen_4;
	bool screen_4_del;
	lv_obj_t *screen_4_label_1;
}lv_ui;

void init_scr_del_flag(lv_ui *ui);
void setup_ui(lv_ui *ui);
extern lv_ui guider_ui;
void setup_scr_error(lv_ui *ui);
void setup_scr_label_9(lv_ui *ui);
void setup_scr_screen_1(lv_ui *ui);
void setup_scr_screen_3(lv_ui *ui);
void setup_scr_screen_4(lv_ui *ui);
LV_IMG_DECLARE(_xuenze_15x15);
LV_IMG_DECLARE(_rect_57x34);
LV_IMG_DECLARE(_cirle_back_20x20);
LV_IMG_DECLARE(_file_12x12);
LV_IMG_DECLARE(_rect_273x64);
LV_IMG_DECLARE(_black_rect_57x36);
LV_IMG_DECLARE(_black_xuanze_13x13);
LV_IMG_DECLARE(_black_rect_200x36);

#ifdef __cplusplus
}
#endif
#endif
