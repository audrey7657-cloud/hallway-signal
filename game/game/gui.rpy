################################################################################
## 초기화
################################################################################

init offset = -2

init python:
    gui.init(1280, 720)

define config.check_conflicting_properties = True


################################################################################
## GUI 설정 변수
################################################################################


## Colors ######################################################################
## 빈티지 앤티크 아이보리 톤

define gui.accent_color = '#2C3E50'        # 네이비 (메인 강조)
define gui.idle_color = '#888888'          # 비활성 텍스트
define gui.idle_small_color = '#AAAAAA'    # 비활성 작은 텍스트
define gui.hover_color = '#E8736C'         # 코랄 (호버)
define gui.selected_color = '#2C3E50'      # 선택됨 (네이비)
define gui.insensitive_color = '#CCCCCC'   # 클릭 불가
define gui.muted_color = '#D5C5A8'         # 약한 강조 (베이지)
define gui.hover_muted_color = '#E8736C'   # 호버 약한 강조
define gui.text_color = '#3A3A3A'          # 본문 텍스트
define gui.interface_text_color = '#3A3A3A' # 인터페이스 텍스트


## Fonts and Font Sizes ########################################################

define gui.text_font = "kangwon2.ttf"
define gui.name_text_font = "kangwon2.ttf"
define gui.interface_text_font = "kangwon2.ttf"

define gui.text_size = 28
define gui.name_text_size = 32
define gui.interface_text_size = 24
define gui.label_text_size = 32
define gui.notify_text_size = 20
define gui.title_text_size = 80


## Main and Game Menus #########################################################

define gui.main_menu_background = "gui/overlay/main_menu.jpg"
define gui.game_menu_background = "gui/overlay/game_menu.jpg"



## Dialogue ####################################################################

define gui.textbox_height = 220
define gui.textbox_yalign = 1.0

# 이름표: 더 왼쪽, 더 상단
define gui.name_xpos = 90
define gui.name_ypos = 18
define gui.name_xalign = 0.0

define gui.namebox_width = 300
define gui.namebox_height = 68
define gui.namebox_borders = Borders(8, 8, 8, 8)
define gui.namebox_tile = False

# 본문: 더 위로, 넓게
define gui.dialogue_xpos = 125
define gui.dialogue_ypos = 82
define gui.dialogue_width = 1050

define gui.dialogue_text_xalign = 0.0


## Buttons #####################################################################

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size

define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

define gui.button_text_xalign = 0.0


## Radio / Check buttons #######################################################

define gui.radio_button_borders = Borders(40, 8, 8, 8)
define gui.check_button_borders = Borders(40, 8, 8, 8)


## Confirm button ##############################################################

define gui.confirm_button_text_xalign = 0.5


## Page button #################################################################

define gui.page_button_borders = Borders(15, 6, 15, 6)


## Quick button ################################################################

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 18
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color


## Choice buttons ##############################################################

define gui.choice_button_width = 800
define gui.choice_button_height = 436
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(40, 30, 40, 30)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = 30
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#3A3A3A'
define gui.choice_button_text_hover_color = '#E8736C'
define gui.choice_button_text_insensitive_color = '#888888'


define gui.slot_button_width = 270
define gui.slot_button_height = 230
define gui.slot_button_borders = Borders(0, 0, 0, 0)
define gui.slot_button_text_size = 18

define config.thumbnail_width = 140
define config.thumbnail_height = 79

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2
define gui.slot_spacing = 16

## Positioning and Spacing #####################################################

define gui.navigation_xpos = 70
define gui.skip_ypos = 15
define gui.notify_ypos = 68
define gui.choice_spacing = 22
define gui.navigation_spacing = 6
define gui.pref_spacing = 15
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.main_menu_text_xalign = 1.0


## Frames ######################################################################

define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.skip_frame_borders = Borders(24, 8, 75, 8)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)
define gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################
## 만든 이미지에 맞춘 크기

define gui.bar_size = 20
define gui.scrollbar_size = 12
define gui.slider_size = 30

define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(6, 0, 6, 0)
define gui.scrollbar_borders = Borders(0, 0, 0, 0)
define gui.slider_borders = Borders(6, 0, 6, 0)

define gui.vbar_borders = Borders(0, 6, 0, 6)
define gui.vscrollbar_borders = Borders(0, 0, 0, 0)
define gui.vslider_borders = Borders(0, 6, 0, 6)

define gui.unscrollable = "hide"


## History #####################################################################

define config.history_length = 250
define gui.history_height = 180
define gui.history_spacing = 0

define gui.history_name_xpos = 200
define gui.history_name_ypos = 0
define gui.history_name_width = 200
define gui.history_name_xalign = 1.0

define gui.history_text_xpos = 220
define gui.history_text_ypos = 3
define gui.history_text_width = 950
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################

define gui.nvl_borders = Borders(0, 15, 0, 30)
define gui.nvl_list_length = 6
define gui.nvl_height = 173
define gui.nvl_spacing = 15

define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Localization ################################################################

define gui.language = "unicode"


################################################################################
## 모바일 기기 (small variant)
################################################################################

init python:

    @gui.variant
    def touch():
        gui.quick_button_borders = Borders(60, 21, 60, 0)

    @gui.variant
    def small():

        # 글자 크기들
        gui.text_size = 28
        gui.name_text_size = 32
        gui.notify_text_size = 22
        gui.interface_text_size = 24
        gui.button_text_size = 24
        gui.label_text_size = 32

        gui.textbox_height = 240
        gui.name_xpos = 90
        gui.name_ypos = 18
        gui.namebox_width = 300
        gui.namebox_height = 68

        gui.dialogue_xpos = 125
        gui.dialogue_ypos = 82
        gui.dialogue_width = 1050

        # 슬라이더 등
        gui.slider_size = 50

        # 선택지
        gui.choice_button_width = 1500
        gui.choice_button_text_size = 38

        # 메뉴 간격
        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        # 대사록
        gui.history_height = 220
        gui.history_text_width = 1100

        # 퀵메뉴
        gui.quick_button_text_size = 28

        # 파일 슬롯
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        # NVL
        gui.nvl_height = 255
        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488
        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8
        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30
        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30