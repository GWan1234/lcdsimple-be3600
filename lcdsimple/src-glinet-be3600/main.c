#include "lvgl/lvgl.h"
//#include "lvgl/demos/lv_demos.h"
#include <unistd.h>
#include <pthread.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include "gui_guider.h"

#define DISP_BUF_SIZE (76*284)

lv_ui guider_ui = {0};

static const char *getenv_default(const char *name, const char *dflt)
{
    return getenv(name) ? : dflt;
}

#if LV_USE_LINUX_FBDEV
static void lv_linux_disp_init(void)
{
    const char *device = getenv_default("LV_LINUX_FBDEV_DEVICE", "/dev/fb0");
    lv_display_t * disp = lv_linux_fbdev_create();

    static lv_color_t sbuf0[DISP_BUF_SIZE], sbuf1[DISP_BUF_SIZE];
    lv_display_set_buffers(disp,
         sbuf0,
         sbuf1,
         DISP_BUF_SIZE*sizeof(lv_color_t), 
         LV_DISPLAY_RENDER_MODE_PARTIAL);

    lv_display_set_physical_resolution(disp, 76, 284);
    lv_linux_fbdev_set_file(disp, device);
    lv_display_set_rotation(disp, LV_DISPLAY_ROTATION_90);
    //lv_linux_fbdev_set_unblank(disp);
    //lv_linux_fbdev_set_display(disp);
}
#elif LV_USE_LINUX_DRM
static void lv_linux_disp_init(void)
{
    const char *device = getenv_default("LV_LINUX_DRM_CARD", "/dev/dri/card0");
    lv_display_t * disp = lv_linux_drm_create();

    lv_linux_drm_set_file(disp, device, -1);
}
#elif LV_USE_SDL
static void lv_linux_disp_init(void)
{
    const int width = atoi(getenv("LV_SDL_VIDEO_WIDTH") ? : "800");
    const int height = atoi(getenv("LV_SDL_VIDEO_HEIGHT") ? : "480");

    lv_sdl_window_create(width, height);
}
#else
#error Unsupported configuration
#endif

static void lv_indev_init(void)
{
#if LV_USE_EVDEV
    lv_indev_t * indev = lv_evdev_create(LV_INDEV_TYPE_POINTER, "/dev/input/event0");
    lv_evdev_set_swap_axes(indev, true);
    lv_evdev_set_calibration(indev, 283, 0, 0, 75);
#endif
}

int main(void)
{
    lv_init();
    
    /*Linux display device init*/
    lv_linux_disp_init();
    lv_indev_init();

    setup_ui(&guider_ui);

    /*Handle LVGL tasks*/
    while(1) {
        lv_timer_handler();
        usleep(5000);
    }

    return 0;
}
