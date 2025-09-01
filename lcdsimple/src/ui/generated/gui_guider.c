/*
 * Copyright 2025 NXP
 * SPDX-License-Identifier: MIT
 * The auto-generated can only be used on NXP devices
 */

#include "lvgl.h"
#include <stdio.h>
#include "gui_guider.h"


void init_scr_del_flag(lv_ui *ui){
	ui->error_del = true;
	ui->label_9_del = true;
	ui->screen_1_del = true;
	ui->screen_3_del = true;
	ui->screen_4_del = true;
}

void setup_ui(lv_ui *ui){
	init_scr_del_flag(ui);
	setup_scr_error(ui);
	lv_scr_load(ui->error);
}
