/*
 * Copyright 2025 NXP
 * SPDX-License-Identifier: MIT
 * The auto-generated can only be used on NXP devices
 */

#include "events_init.h"
#include <stdio.h>
#include "lvgl.h"

void events_init(lv_ui *ui)
{
}

static void error_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_disp_t * d = lv_obj_get_disp(lv_scr_act());
		if (d->prev_scr == NULL && d->scr_to_load == NULL)
		{
			if (guider_ui.screen_1_del == true)
				setup_scr_screen_1(&guider_ui);
			lv_scr_load_anim(guider_ui.screen_1, LV_SCR_LOAD_ANIM_OVER_TOP, 0, 0, true);
		}
		guider_ui.error_del = true;
	}
		break;
	default:
		break;
	}
}

void events_init_error(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->error_btn_2, error_btn_2_event_handler, LV_EVENT_ALL, NULL);
}

static void label_9_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_disp_t * d = lv_obj_get_disp(lv_scr_act());
		if (d->prev_scr == NULL && d->scr_to_load == NULL)
		{
			if (guider_ui.error_del == true)
				setup_scr_error(&guider_ui);
			lv_scr_load_anim(guider_ui.error, LV_SCR_LOAD_ANIM_OVER_TOP, 0, 0, true);
		}
		guider_ui.label_9_del = true;
	}
		break;
	default:
		break;
	}
}

void events_init_label_9(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->label_9_btn_1, label_9_btn_1_event_handler, LV_EVENT_ALL, NULL);
}

static void screen_1_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_disp_t * d = lv_obj_get_disp(lv_scr_act());
		if (d->prev_scr == NULL && d->scr_to_load == NULL)
		{
			if (guider_ui.screen_3_del == true)
				setup_scr_screen_3(&guider_ui);
			lv_scr_load_anim(guider_ui.screen_3, LV_SCR_LOAD_ANIM_OVER_TOP, 0, 0, true);
		}
		guider_ui.screen_1_del = true;
	}
		break;
	default:
		break;
	}
}

void events_init_screen_1(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->screen_1_btn_1, screen_1_btn_1_event_handler, LV_EVENT_ALL, NULL);
}

static void screen_3_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_disp_t * d = lv_obj_get_disp(lv_scr_act());
		if (d->prev_scr == NULL && d->scr_to_load == NULL)
		{
			if (guider_ui.label_9_del == true)
				setup_scr_label_9(&guider_ui);
			lv_scr_load_anim(guider_ui.label_9, LV_SCR_LOAD_ANIM_OVER_TOP, 0, 0, true);
		}
		guider_ui.screen_3_del = true;
	}
		break;
	default:
		break;
	}
}

void events_init_screen_3(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->screen_3_btn_1, screen_3_btn_1_event_handler, LV_EVENT_ALL, NULL);
}
