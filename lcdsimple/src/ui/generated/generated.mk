# images

PRJ_DIR=/home/build/istoreos-build/idisk-rk35xx/openwrt/build_dir/target-aarch64_cortex-a53_musl/lcdsimple-1.0/ui

include $(PRJ_DIR)/generated/images/images.mk

# GUI Guider fonts
include $(PRJ_DIR)/generated/guider_fonts/guider_fonts.mk

# GUI Guider customer fonts
include $(PRJ_DIR)/generated/guider_customer_fonts/guider_customer_fonts.mk


GEN_CSRCS += $(notdir $(wildcard $(PRJ_DIR)/generated/*.c))

DEPPATH += --dep-path $(PRJ_DIR)/generated
VPATH += :$(PRJ_DIR)/generated

CFLAGS2 += "-I$(PRJ_DIR)/generated"
