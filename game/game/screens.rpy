################################################################################
## 초기화
################################################################################

init offset = -1





################################################################################
## 기본 스타일
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


################################################################################
## 막대 / 슬라이더 - 만든 이미지 사용
################################################################################

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/left.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/right.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Solid("#D5C5A8")
    thumb Solid("#2C3E50")

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Solid("#D5C5A8")
    thumb Solid("#2C3E50")

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_idle_bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_idle_thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/horizontal_idle_bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_idle_thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


################################################################################
## Say 스크린
################################################################################

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"

                text who:
                    id "who"
                    style "namebox_label"
                    xalign 0.5
                    yalign 0.5
                    textalign 0.5

        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile)
    padding (0, 0)

style namebox_label:
    properties gui.text_properties("name", accent=True)
    bold True
    size 34
    color "#2C3E50"
    outlines [(1, "#FFF8E8", 0, 0)]
    xalign 0.5
    yalign 0.5
    textalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    color "#3A3A3A"
    line_leading 4
    line_spacing 6

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

style say_label:
    properties gui.text_properties("name", accent=True)
    color "#2C3E50"
    bold True
    xalign 0.5
    yalign 0.5
    textalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    color "#3A3A3A"
    line_leading 4
    line_spacing 6

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False


################################################################################
## Input 스크린
################################################################################

screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


################################################################################
## Choice 스크린
################################################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

screen choice_hint(message):
    zorder 90

    text message:
        xalign 0.5
        ypos 105
        size 28
        color "#2F2A26"
        text_align 0.5
        outlines [(3, "#FFF8E8", 0, 0)]

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 360
    yanchor 0.5
    spacing 12

style choice_button:
    background "gui/button/choice_idle_background.png"
    hover_background "gui/button/choice_hover_background.png"
    xsize 800
    ysize 120
    padding (0, 0)

style choice_button_text:
    properties gui.text_properties("choice_button")
    color "#2F2A26"
    hover_color "#2F2A26"
    size 27
    bold False
    xalign 0.5
    yalign 0.5
    text_align 0.5
    outlines [(1, "#FFF8E8", 0, 0)]



################################################################################
## Quick Menu 스크린
################################################################################

screen quick_menu():

    zorder 100

    if quick_menu:

        frame:
            xalign 0.5
            yalign 1.0
            yoffset -2
            background Solid("#000000AA")
            padding (16, 3)

            hbox:
                style_prefix "quick"
                style "quick_menu"

                textbutton _("되감기") action Rollback()
                textbutton _("대사록") action ShowMenu('history')
                textbutton _("넘기기") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("자동진행") action Preference("auto-forward", "toggle")
                textbutton _("저장하기") action ShowMenu('save')
                textbutton _("Q.저장하기") action QuickSave()
                textbutton _("Q.불러오기") action QuickLoad()
                textbutton _("설정") action ShowMenu('preferences')


init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0
    spacing 16

style quick_button:
    properties gui.button_properties("quick_button")
    padding (2, 0)

style quick_button_text:
    properties gui.text_properties("quick_button")
    color "#FFF8E8"
    hover_color "#FFD6A0"
    selected_color "#2C3E50"
    size 20
    outlines [(2, "#000000", 0, 0)]


################################################################################
## Navigation 스크린
################################################################################

screen navigation():

    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("시작하기") action Start()
        else:
            textbutton _("대사록") action ShowMenu("history")
            textbutton _("저장하기") action ShowMenu("save")

        textbutton _("불러오기") action ShowMenu("load")
        textbutton _("환경설정") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("리플레이 끝내기") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("메인 메뉴") action MainMenu()

        textbutton _("버전정보") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("조작방법") action ShowMenu("help")

        if renpy.variant("pc"):
            textbutton _("종료하기") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")
    color "#FFF4DD"
    hover_color "#FFD6A0"
    selected_color "#FF8A7A"
    size 28
    outlines [(2, "#1E2D3A", 0, 0)]


################################################################################
## Main Menu 스크린
################################################################################

screen main_menu():

    tag menu

    add gui.main_menu_background

    frame:
        style "main_menu_frame"

    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"
            spacing 12

            text "[config.name!t]":
                style "main_menu_title"
                size 80
                color "#2C3E50"
                outlines [(3, "#FFFCF5", 0, 0)]

            text "복도 끝의 신호":
                size 24
                color "#3A3A3A"
                outlines [(2, "#FFFCF5", 0, 0)]

            null height 15

            text "[config.version]":
                style "main_menu_version"
                color "#888888"
                size 18

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True
    background "gui/overlay/main_menu.jpg"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


################################################################################
## Game Menu 스크린
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        vbox:
                            spacing spacing
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        spacing spacing
                        transclude

                else:
                    transclude

    use navigation

    textbutton _("돌아가기"):
        style "return_button"
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 35
    top_padding 145
    background Solid("#00000033")

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 20
    right_margin 20
    top_margin 0

style game_menu_viewport:
    xsize 900

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 60
    color "#2C3E50"
    yalign 0.5
    outlines [(2, "#FFFCF5", 0, 0)]

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


################################################################################
## About 스크린
################################################################################

screen about():

    tag menu

    use game_menu(_("버전정보"), scroll="viewport"):

        style_prefix "about"

        vbox:
            xpos 40
            ypos 0
            xsize 820
            spacing 12

            label "[config.name!t]"
            text _("버전 [config.version!t]\n")

            if gui.about:
                text "[gui.about!t]\n"

            text _("{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 으로 만들어진 게임.\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size 34
    color "#FFD6A0"
    bold True
    outlines [(2, "#000000", 0, 0)]

style about_text:
    color "#FFF4DD"
    size 24
    line_spacing 8
    outlines [(2, "#000000", 0, 0)]

style about_hyperlink_text:
    color "#FFD6A0"
    hover_color "#FF8A7A"
    underline True
    outlines [(2, "#000000", 0, 0)]


################################################################################
## Save / Load 스크린
################################################################################

screen save():
    tag menu
    use file_slots(_("저장하기"))


screen load():
    tag menu
    use file_slots(_("불러오기"))


screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("{} 페이지"), auto=_("자동 세이브"), quick=_("퀵세이브"))

    use game_menu(title):
        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5
            yoffset -55

            button:
                style "page_label"
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                spacing gui.slot_spacing
                xalign 0.5

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1

                 
                    button:
                        action FileAction(slot)
                        xsize gui.slot_button_width
                        ysize gui.slot_button_height
                        background Transform("gui/button/slot_idle_background.png", size=(270, 230))
                        hover_background Transform("gui/button/slot_hover_background.png", size=(270, 230))

                        fixed:
                            xsize gui.slot_button_width
                            ysize gui.slot_button_height

                            add FileScreenshot(slot):
                                xpos 65
                                ypos 67
                                xsize 140
                                ysize 79
                                fit "contain"

                            text FileTime(slot, format=_("%Y-%m-%d %H:%M"), empty=_("빈 슬롯")):
                                color "#2C3E50"
                                size 18
                                bold True
                                xalign 0.5
                                ypos 166

                            key "save_delete" action FileDelete(slot)

            hbox:
                style_prefix "page"
                xalign 0.5
                yoffset -30
                spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious()
                if config.has_autosave:
                    textbutton _("자동") action FilePage("auto")
                if config.has_quicksave:
                    textbutton _("퀵") action FilePage("quick")
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()

                if config.has_sync:
                    null height 10
                    if CurrentScreenName() == "save":
                        textbutton _("동기화 업로드") action UploadSync() xalign 0.5
                    else:
                        textbutton _("동기화 다운로드") action DownloadSync() xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    color "#1F3C5A"
    outlines [(2, "#FFFFFFCC", 0, 0)]
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")
    color "#2C3E50"
    hover_color "#7A4A42"
    outlines [(2, "#FFFFFFCC", 0, 0)]

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")

    
################################################################################
## Preferences 스크린 - 라디오/체크 이미지 사용
################################################################################

screen preferences():

    tag menu

    use game_menu(_("환경설정")):

        fixed:
            xpos 0
            ypos 0
            xsize 900
            ysize 500

            vbox:
                style_prefix "radio"
                xpos 40
                ypos 0
                xsize 300

                label _("화면 모드")
                textbutton _("창 화면") action Preference("display", "window")
                textbutton _("전체 화면") action Preference("display", "fullscreen")

            vbox:
                style_prefix "check"
                xpos 480
                ypos 0
                xsize 360

                label _("넘기기")
                textbutton _("읽지 않은 지문") action Preference("skip", "toggle")
                textbutton _("선택지 이후") action Preference("after choices", "toggle")
                textbutton _("화면 전환 효과") action InvertSelected(Preference("transitions", "toggle"))

            vbox:
                style_prefix "slider"
                xpos 40
                ypos 220
                xsize 360

                label _("텍스트 속도")
                bar value Preference("text speed") xsize 340

                label _("자동 진행 시간")
                bar value Preference("auto-forward time") xsize 340

            vbox:
                style_prefix "slider"
                xpos 480
                ypos 220
                xsize 360

                if config.has_music:
                    label _("배경음 음량")
                    bar value Preference("music volume") xsize 340

                if config.has_sound:
                    label _("효과음 음량")
                    bar value Preference("sound volume") xsize 340

                if config.has_voice:
                    label _("음성 음량")
                    bar value Preference("voice volume") xsize 340

                if config.has_music or config.has_sound or config.has_voice:
                    null height 10

                    textbutton _("모두 음소거"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0
    color "#FFF4DD"
    size 24
    bold True
    outlines [(2, "#2C3E50", 0, 0)]

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_foreground.png"
    left_padding 45

style radio_button_text:
    properties gui.text_properties("radio_button")
    color "#F8F1E4"
    hover_color "#FFD6A0"
    selected_color "#FF8A7A"
    outlines [(2, "#1E2D3A", 0, 0)]

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_foreground.png"
    left_padding 45

style check_button_text:
    properties gui.text_properties("check_button")
    color "#F8F1E4"
    hover_color "#FFD6A0"
    selected_color "#FF8A7A"
    outlines [(2, "#1E2D3A", 0, 0)]

style slider_slider:
    xsize 340

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")
    color "#F8F1E4"
    hover_color "#FFD6A0"
    outlines [(2, "#1E2D3A", 0, 0)]

style slider_vbox:
    xsize 360

################################################################################
## 환경설정 슬라이더 색상 보정
################################################################################

style slider_slider:
    xsize 340
    ysize 24

    left_bar Frame(Solid("#F08A7A"), 6, 6)
    right_bar Frame(Solid("#F4EBDD"), 6, 6)

    hover_left_bar Frame(Solid("#FFAA98"), 6, 6)
    hover_right_bar Frame(Solid("#FFF4E8"), 6, 6)

    thumb Transform(Solid("#2F4E79"), xysize=(22, 22))
    hover_thumb Transform(Solid("#4C6FA3"), xysize=(24, 24))

################################################################################
## History 스크린
################################################################################

screen history():

    tag menu

    predict False

    use game_menu(_("대사록"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("대사가 없습니다.")


define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height
    background Solid("#00000055")

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign
    color "#FFD6A0"
    bold True
    size 24
    outlines [(2, "#000000", 0, 0)]

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    color "#FFF4DD"
    size 24
    outlines [(2, "#000000", 0, 0)]

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
    color "#FFF4DD"
    size 28
    bold True
    outlines [(2, "#000000", 0, 0)]


################################################################################
## Help 스크린
################################################################################

screen help():
    tag menu
    default device = "keyboard"

    use game_menu(_("조작방법"), scroll="viewport"):
        style_prefix "help"

        vbox:
            spacing 23
            hbox:
                textbutton _("키보드") action SetScreenVariable("device", "keyboard")
                textbutton _("마우스") action SetScreenVariable("device", "mouse")
                if GamepadExists():
                    textbutton _("게임패드") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():
    hbox:
        label _("엔터(Enter)")
        text _("대사 진행 및 UI (선택지 포함) 선택.")
    hbox:
        label _("스페이스(Space)")
        text _("대사를 진행하되 선택지는 선택하지 않음.")
    hbox:
        label _("화살표 키")
        text _("UI 이동.")
    hbox:
        label _("이스케이프(Esc)")
        text _("게임 메뉴 불러옴.")
    hbox:
        label _("컨트롤(Ctrl)")
        text _("누르고 있는 동안 대사를 스킵.")
    hbox:
        label _("탭(Tab)")
        text _("대사 스킵 토글.")
    hbox:
        label _("페이지 업(Page Up)")
        text _("이전 대사로 롤백.")
    hbox:
        label _("페이지 다운(Page Down)")
        text _("이후 대사로 롤포워드.")
    hbox:
        label "H"
        text _("UI를 숨김.")
    hbox:
        label "S"
        text _("스크린샷 저장.")


screen mouse_help():
    hbox:
        label _("클릭")
        text _("대사 진행 및 UI (선택지 포함) 선택.")
    hbox:
        label _("가운데 버튼이나 휠버튼 클릭")
        text _("UI를 숨김.")
    hbox:
        label _("우클릭")
        text _("게임 메뉴 불러옴.")
    hbox:
        label _("휠 위로")
        text _("이전 대사로 롤백.")
    hbox:
        label _("휠 아래로")
        text _("이후 대사로 롤포워드.")


screen gamepad_help():
    hbox:
        label _("오른쪽 트리거(RT)\nA버튼/아래 버튼")
        text _("대사 진행 및 UI 선택.")
    hbox:
        label _("왼쪽 트리거\n왼쪽 어깨")
        text _("이전 대사로 롤백.")
    hbox:
        label _("오른쪽 범퍼(RB)")
        text _("이후 대사로 롤포워드.")
    hbox:
        label _("D-Pad, 아날로그 스틱")
        text _("UI 이동.")
    hbox:
        label _("Start, Guide, B/Right Button")
        text _("게임 메뉴 불러옴.")
    hbox:
        label _("Y버튼/위 버튼")
        text _("UI를 숨김.")
    textbutton _("조정") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")
    color "#FFF4DD"
    hover_color "#FFD6A0"
    selected_color "#FF8A7A"
    size 26
    bold True
    outlines [(2, "#000000", 0, 0)]

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size 26
    xalign 1.0
    textalign 1.0
    color "#FFD6A0"
    bold True
    outlines [(2, "#000000", 0, 0)]

style help_text:
    color "#FFF4DD"
    size 24
    outlines [(2, "#000000", 0, 0)]


################################################################################
## Confirm 스크린
################################################################################

screen confirm(message, yes_action, no_action):

    modal True
    zorder 200

    add Solid("#00000055")

    fixed:
        xalign 0.5
        yalign 0.5
        xsize 680
        ysize 300

        add Transform("gui/overlay/confirm_panel.png", size=(600, 280)):
            xalign 0.5
            yalign 0.5

        text message:
            xalign 0.5
            ypos 88
            xsize 580
            textalign 0.5
            size 26
            line_spacing 6
            color "#3A3028"
            bold False
            outlines [(1, "#F7F1E3", 0, 0)]

        hbox:
            xalign 0.5
            ypos 195
            spacing 135

            textbutton "네":
                action yes_action
                xsize 165
                ysize 64
                background None
                hover_background Solid("#FFF4DD55")
                text_size 34
                text_color "#2C3E50"
                text_hover_color "#E8736C"
                text_xalign 0.5
                text_yalign 0.5

            textbutton "아니오":
                action no_action
                xsize 165
                ysize 64
                background None
                hover_background Solid("#FFF4DD55")
                text_size 34
                text_color "#2C3E50"
                text_hover_color "#E8736C"
                text_xalign 0.5
                text_yalign 0.5

    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    color "#3A3A3A"
    size 24

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")
    color "#3A3A3A"
    hover_color "#E8736C"
    size 22

style confirm_button is default:
    xsize 220
    ysize 72
    background Solid("#EFE4CF")
    hover_background Solid("#2F4F79")
    padding (20, 12)

style confirm_button_text is default:
    xalign 0.5
    yalign 0.5
    size 30
    color "#2F4F79"
    hover_color "#F8F4EC"
    bold True


################################################################################
## Skip / Notify 스크린
################################################################################

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 9
            text _("넘기는 중")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Solid("#000000CC")
    padding (22, 10)

style skip_text:
    size gui.notify_text_size
    color "#FFFFFF"
    outlines [(2, "#000000", 0, 0)]

style skip_triangle:
    font "DejaVuSans.ttf"
    color "#FFFFFF"
    outlines [(2, "#000000", 0, 0)]


screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos
    xpos 30
    background Solid("#000000CC")
    padding (18, 12)

style notify_text:
    properties gui.text_properties("notify")
    color "#FFF4DD"
    size 26
    bold True
    outlines [(2, "#000000", 0, 0)]


################################################################################
## NVL 스크린
################################################################################

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        if gui.nvl_height:
            vpgrid:
                cols 1
                yinitial 1.0
                use nvl_dialogue(dialogue)
        else:
            use nvl_dialogue(dialogue)

        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:
                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


################################################################################
## 모바일 (small variant) - 데스크톱 이미지 공유
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675


screen quick_menu():
    variant "touch"
    zorder 100

    if quick_menu:
        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("되감기") action Rollback()
            textbutton _("넘기기") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("자동진행") action Preference("auto-forward", "toggle")
            textbutton _("메뉴") action ShowMenu()


style window:
    variant "small"
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style nvl_window:
    variant "small"
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style main_menu_frame:
    variant "small"
    background "gui/overlay/main_menu.jpg"

style game_menu_outer_frame:
    variant "small"
    background "gui/overlay/game_menu.jpg"

style game_menu_navigation_frame:
    variant "small"
    xsize 280

style game_menu_content_frame:
    variant "small"
    left_margin 20
    right_margin 20
    top_margin 10

style game_menu_viewport:
    variant "small"
    xsize 900

style pref_vbox:
    variant "small"
    xsize 600

style radio_button:
    variant "small"
    foreground "gui/button/radio_foreground.png"
    left_padding 60

style check_button:
    variant "small"
    foreground "gui/button/check_foreground.png"
    left_padding 60

style bar:
    variant "small"
    ysize 20
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style slider:
    variant "small"
    ysize 50
    base_bar Frame("gui/slider/horizontal_idle_bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_idle_thumb.png"

style scrollbar:
    variant "small"
    ysize 12
    base_bar Solid("#D5C5A8")
    thumb Solid("#2C3E50")

style vscrollbar:
    variant "small"
    xsize 12
    base_bar Solid("#D5C5A8")
    thumb Solid("#2C3E50")

style slider_vbox:
    variant "small"
    xsize 360

style slider_slider:
    variant "small"
    xsize 340
    ysize 28

    left_bar Frame(Solid("#F08A7A"), 6, 6)
    right_bar Frame(Solid("#F4EBDD"), 6, 6)

    hover_left_bar Frame(Solid("#FFAA98"), 6, 6)
    hover_right_bar Frame(Solid("#FFF4E8"), 6, 6)

    thumb Transform(Solid("#2F4E79"), xysize=(26, 26))
    hover_thumb Transform(Solid("#4C6FA3"), xysize=(28, 28))

################################################################################
## 게임 전용 스크린 (관찰 노트, 조사, 단톡방, 교무실 보고)
################################################################################

screen quick_note_button():
    zorder 100

    fixed:
        xalign 0.98
        yalign 0.04
        xsize 64
        ysize 122

        imagebutton:
            idle Transform("gui/phone_note.png", size=(58, 116))
            hover Transform("gui/phone_note.png", size=(62, 124))
            action Show("observation_note")
            xalign 0.5
            yalign 0.5

        text "관찰\n노트":
            xalign 0.5
            yalign 0.5
            size 15
            text_align 0.5
            color "#1F3F4D"
            bold True
            outlines [(1, "#FFFFFF", 0, 0)]

screen observation_note():
    modal True
    zorder 200
    default note_page = "home"

    add Solid("#00000088")

    fixed:
        xalign 0.5
        yalign 0.5
        xsize 340
        ysize 680

        add Transform("gui/phone_note.png", size=(340, 680))

        frame:
            xpos 46
            ypos 86
            xsize 248
            ysize 508
            padding (16, 14)
            background None

            if note_page == "home":

                vbox:
                    spacing 14
                    xfill True

                    text "관찰 노트":
                        xalign 0.5
                        size 27
                        bold True
                        color "#1F3F4D"

                    text "확인할 내용을 선택하세요.":
                        xalign 0.5
                        size 15
                        color "#6A6A6A"

                    null height 8

                    textbutton "지금까지 본 일":
                        action SetScreenVariable("note_page", "seen")
                        xfill True
                        ysize 62
                        background Solid("#F4EFE3")
                        hover_background Solid("#EAD7CE")
                        text_color "#2F2A26"
                        text_hover_color "#5A302A"
                        text_size 20
                        text_xalign 0.5
                        text_yalign 0.5

                    textbutton "중요한 단서":
                        action SetScreenVariable("note_page", "clue")
                        xfill True
                        ysize 62
                        background Solid("#F4EFE3")
                        hover_background Solid("#DCE9D8")
                        text_color "#2F2A26"
                        text_hover_color "#2F4A32"
                        text_size 20
                        text_xalign 0.5
                        text_yalign 0.5

                    textbutton "친구들 반응":
                        action SetScreenVariable("note_page", "friend")
                        xfill True
                        ysize 62
                        background Solid("#F4EFE3")
                        hover_background Solid("#DDE6F3")
                        text_color "#2F2A26"
                        text_hover_color "#2F3F5A"
                        text_size 20
                        text_xalign 0.5
                        text_yalign 0.5

            else:

                vbox:
                    spacing 12
                    xfill True

                    hbox:
                        xfill True
                        spacing 8

                        textbutton "← 뒤로":
                            action SetScreenVariable("note_page", "home")
                            xsize 66
                            ysize 32
                            background None
                            hover_background Solid("#E7F0F4")
                            text_color "#183B4A"
                            text_hover_color "#2F6F8F"
                            text_size 16
                            text_xalign 0.5
                            text_yalign 0.5

                        if note_page == "seen":
                            text "지금까지 본 일" size 22 bold True color "#183B4A" yalign 0.5
                        elif note_page == "clue":
                            text "중요한 단서" size 22 bold True color "#183B4A" yalign 0.5
                        elif note_page == "friend":
                            text "친구들 반응" size 22 bold True color "#183B4A" yalign 0.5

                    viewport:
                        xfill True
                        ysize 420
                        mousewheel True
                        draggable True
                        scrollbars "vertical"

                        vbox:
                            spacing 10
                            xfill True

                            if note_page == "seen":

                                if note_role:
                                    text "• 발표할 때 일부러 말 못 하게 함" size 18 color "#2F2A26"
                                if note_lunch:
                                    text "• 급식 때 자리가 있는데도 못 앉게 함" size 18 color "#2F2A26"
                                if note_photo:
                                    text "• 허락 없이 사진을 찍고 돌려봄" size 18 color "#2F2A26"
                                if note_bathroom:
                                    text "• 하린이 우는 걸 봄" size 18 color "#2F2A26"
                                if note_note:
                                    text "• 서랍에서 이상한 쪽지를 찾음" size 18 color "#2F2A26"
                                if note_chat:
                                    text "• 단톡방에서 놀리는 말을 봄" size 18 color "#2F2A26"
                                if note_witness:
                                    text "• 체육 시간에 민재가 하린을 일부러 지나침" size 18 color "#2F2A26"

                                if not (note_role or note_lunch or note_photo or note_bathroom or note_note or note_chat or note_witness):
                                    text "아직 적어 둔 일이 없습니다." size 18 color "#4D5960"

                            elif note_page == "clue":

                                if key1_structure:
                                    text "• 교실에서 무슨 일이 있는지 조금 알게 됨" size 18 color "#2F2A26"
                                if key2_stay_with_harin:
                                    text "• 하린 곁에 있어 줌" size 18 color "#2F2A26"
                                if key3_move_with_soyoon:
                                    text "• 소윤과 같이 움직임" size 18 color "#2F2A26"
                                if key4_minjae_pattern:
                                    text "• 민재가 어떻게 행동하는지 봄" size 18 color "#2F2A26"

                                if not (key1_structure or key2_stay_with_harin or key3_move_with_soyoon or key4_minjae_pattern):
                                    text "아직 중요한 단서를 못 찾았습니다." size 18 color "#777777"

                            elif note_page == "friend":

                                if trust_soyun != 0:
                                    text "• 소윤이 마음을 연 정도: [trust_soyun]" size 18 color "#2F2A26"
                                if trust_harin != 0:
                                    text "• 하린이 믿어 준 정도: [trust_harin]" size 18 color "#2F2A26"
                                if trust_minjae != 0:
                                    text "• 민재가 흔들린 정도: [trust_minjae]" size 18 color "#2F2A26"

                                if trust_soyun == 0 and trust_harin == 0 and trust_minjae == 0:
                                    text "아직 크게 달라진 건 없습니다." size 18 color "#777777"

        textbutton "닫기":
            action Hide("observation_note")
            xpos 126
            ypos 610
            xsize 88
            ysize 36
            background Solid("#183B4A")
            hover_background Solid("#2F6F8F")
            text_color "#FFFFFF"
            text_hover_color "#FFFFFF"
            text_size 18
            text_xalign 0.5
            text_yalign 0.5

init:
    transform investigation_soft_in:
        alpha 0.0
        on show:
            alpha 0.0
            ease 0.25 alpha 1.0


screen class_investigation():

    modal True
    tag investigation
    zorder 100

    fixed at investigation_soft_in:

        add "bg_4"

        frame:
            xalign 0.5
            ypos 18
            background Solid("#00000099")
            padding (24, 12)

            text "화면을 눌러 조사해보세요":
                size 28
                color "#FFFFFF"
                outlines [(2, "#000000", 0, 0)]

        # 오른쪽 아래 파란 옷 단발 여학생
        button:
            xpos 750
            ypos 255
            xsize 265
            ysize 395
            background None
            hover_background Solid("#ffffff22")
            mouse "inspect"
            action Return("desk")

        # 그 왼쪽의 학생들
        button:
            xpos 70
            ypos 135
            xsize 575
            ysize 565
            background None
            hover_background Solid("#ffffff22")
            mouse "inspect"
            action Return("back")

        # 칠판 전체a
        button:
            xpos 285
            ypos 40
            xsize 600
            ysize 180
            background None
            hover_background Solid("#ffffff22")
            mouse "inspect"
            action Return("board")

        if loop_no == 2 and not f_minjae_talk_r2:
            button:
                xpos 505
                ypos 105
                xsize 150
                ysize 610
                background None
                hover_background Solid("#FFB34755")
                mouse "inspect"
                action Return("minjae_r2")
                
        frame:
            xpos 980
            ypos 620
            xsize 230
            ysize 68
            background Solid("#000000DD")
            padding (0, 0)

            textbutton "조사 종료":
                action Return("finish")
                xalign 0.5
                yalign 0.5
                background None
                text_size 32
                text_color "#FFFFFF"
                text_hover_color "#FFFFFF"


screen pe_investigation_screen():

    modal True
    tag pe_investigation
    zorder 100

    fixed at investigation_soft_in:

        add "bg_12"

        frame:
            xalign 0.5
            ypos 18
            background Solid("#00000099")
            padding (24, 12)

            text "화면을 눌러 조사해보세요":
                size 28
                color "#FFFFFF"
                outlines [(2, "#000000", 0, 0)]

        # 벤치 + 낙서
        button:
            xpos 20
            ypos 385
            xsize 365
            ysize 270
            background None
            hover_background Solid("#7CCF8055")
            mouse "inspect"
            action Return("bench")

        # 예서 - 포니테일 안경 여학생
        button:
            xpos 350
            ypos 145
            xsize 175
            ysize 545
            background None
            hover_background Solid("#B38CFF55")
            mouse "inspect"
            action Return("yeseo")

        # 민재 - 가운데 회색 후드 남학생
        button:
            xpos 505
            ypos 145
            xsize 155
            ysize 545
            background None
            hover_background Solid("#FFB34755")
            mouse "inspect"
            action Return("minjae")

        # 소윤 - 아이보리색 상하의 긴머리 여학생
        button:
            xpos 650
            ypos 145
            xsize 195
            ysize 545
            background None
            hover_background Solid("#FFF0A655")
            mouse "inspect"
            action Return("soyun")

        # 하린 - 맨 오른쪽 단발머리 파란 옷
        button:
            xpos 885
            ypos 165
            xsize 150
            ysize 520
            background None
            hover_background Solid("#66C1E055")
            mouse "inspect"
            action Return("harin")

        frame:
            xpos 1030
            ypos 620
            xsize 210
            ysize 68
            background Solid("#000000DD")
            padding (0, 0)

            textbutton "조사 종료":
                action Return("finish")
                xalign 0.5
                yalign 0.5
                background None
                text_size 30
                text_color "#FFFFFF"
                text_hover_color "#FFFFFF"


screen pe_investigation_r3():

    modal True
    tag pe_investigation_r3
    zorder 100

    fixed at investigation_soft_in:

        add "bg_12"

        frame:
            xalign 0.5
            ypos 18
            background Solid("#00000099")
            padding (24, 12)

            text "화면을 눌러 상황을 살펴보세요":
                size 28
                color "#FFFFFF"
                outlines [(2, "#000000", 0, 0)]

        if not talk_pe_minjae:
            button:
                xpos 505
                ypos 145
                xsize 155
                ysize 545
                background None
                hover_background Solid("#FFB34755")
                mouse "inspect"
                action Return("minjae_r3")

        if not talk_pe_soyun:
            button:
                xpos 650
                ypos 145
                xsize 195
                ysize 545
                background None
                hover_background Solid("#FFF0A655")
                mouse "inspect"
                action Return("soyoon_r3")

        if not talk_pe_harin:
            button:
                xpos 885
                ypos 165
                xsize 150
                ysize 520
                background None
                hover_background Solid("#66C1E055")
                mouse "inspect"
                action Return("harin_r3")

        if note_witness:
            frame:
                xpos 1010
                ypos 620
                xsize 230
                ysize 68
                background Solid("#000000DD")
                padding (0, 0)

                textbutton "조사 종료":
                    action Return("finish_pe")
                    xalign 0.5
                    yalign 0.5
                    background None
                    text_size 30
                    text_color "#FFFFFF"
                    text_hover_color "#FFFFFF"

        else:
            frame:
                xpos 880
                ypos 620
                xsize 360
                ysize 68
                background Solid("#00000099")
                padding (0, 0)

                text "아직 뭐가 이상한지 확실하지 않다.\n친구들을 한 명씩 더 살펴보자.":
                    xalign 0.5
                    yalign 0.5
                    size 24
                    color "#DDDDDD"
                    outlines [(2, "#000000", 0, 0)]


screen interactive_note():
    modal True
    default unfold_stage = 0

    fixed:

        frame:
            xalign 0.5
            yalign 0.52
            xsize 820
            ysize 560
            background Solid("#00000099")
            padding (30, 28)

            fixed:

                if unfold_stage == 0:

                    add "cg_4":
                        xalign 0.5
                        yalign 0.38
                        xsize 540

                    text "구겨진 종이 뭉치가 떨어져 있다.":
                        size 30
                        color "#ffffff"
                        xalign 0.5
                        yalign 0.80
                        outlines [(2, "#000000", 0, 0)]

                    textbutton "< 종이를 펴 본다 >":
                        xalign 0.5
                        yalign 0.92
                        action [Play("sound", "audio/page_flip.mp3"), SetScreenVariable("unfold_stage", 1)]
                        text_size 35
                        text_color "#c8c8ff"
                        text_outlines [(2, "#000000", 0, 0)]

                elif unfold_stage == 1:

                    add "cg_5":
                        xalign 0.5
                        yalign 0.38
                        xsize 580

                    text "종이를 반쯤 펴자 삐뚤삐뚤한 글씨가 보인다.":
                        size 30
                        color "#ffffff"
                        xalign 0.5
                        yalign 0.80
                        outlines [(2, "#000000", 0, 0)]

                    textbutton "< 조금 더 펴 본다 >":
                        xalign 0.5
                        yalign 0.92
                        action [Play("sound", "audio/page_flip.mp3"), SetScreenVariable("unfold_stage", 2)]
                        text_size 35
                        text_color "#c8c8ff"
                        text_outlines [(2, "#000000", 0, 0)]

                elif unfold_stage == 2:

                    add "cg_6":
                        xpos 70
                        ypos -110
                        xsize 700

                    vbox:
                        xpos 240
                        ypos 195
                        spacing 16

                        text "야, 이거 다 장난인 거 알지?":
                            color "#222222"
                            size 28
                            bold True
                            outlines [(1, "#ffffff99", 0, 0)]

                        text "그러니까 괜히 심각하게 생각하지 마.":
                            color "#222222"
                            size 28
                            bold True
                            outlines [(1, "#ffffff99", 0, 0)]

                        text "괜히 분위기 이상하게 만들지 말고.":
                            color "#222222"
                            size 28
                            bold True
                            outlines [(1, "#ffffff99", 0, 0)]

                    textbutton "< 쪽지를 챙긴다 >":
                        xalign 0.5
                        yalign 0.92
                        action Return()
                        text_size 35
                        text_color "#c8c8ff"
                        text_outlines [(2, "#000000", 0, 0)]


screen class_chat():

    modal True
    tag phone
    zorder 200

    add Solid("#00000066")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 680
        background Solid("#2f3136ee")
        padding (24, 24)

        vbox:
            spacing 18
            xfill True
            yfill True

            text "6학년 3반 단톡방" size 34 color "#FFFFFF" xalign 0.5

            hbox:
                xfill True
                spacing 12

                frame:
                    xfill True
                    ysize 470
                    background Solid("#202225ee")
                    padding (24, 24)

                    viewport:
                        id "chat_vp"
                        draggable True
                        mousewheel True
                        xfill True
                        yfill True
                        yinitial 1.0

                        vbox:
                            spacing 18
                            xfill True

                            text "이전 대화" size 18 color "#888888" xalign 0.5
                            text "[[알림] '예서'님이 '하린'님을 초대했습니다." size 26 color "#FFF000"
                            text "[[예서] @하린 야 너 왜 읽고 대답 안 해?" size 26 color "#DDDDDD"
                            text "[[예서] 야 오늘 하린이 표정 봤냐? 진짜 웃김" size 26 color "#DDDDDD"
                            text "[[민재] ㅋㅋㅋㅋ 캡처한 사람 없음?" size 26 color "#DDDDDD"
                            text "[[준호] 나 있음 이따 보내줌" size 26 color "#DDDDDD"

                            if chat_scroll_depth >= 1:
                                text "[[예서] 말 없으면 인정하는 거다?" size 26 color "#DDDDDD"
                                text "[[민재] 원래 쟤 반응 없잖아 ㅋㅋ" size 26 color "#DDDDDD"
                                text "[[준호] 투명인간임?" size 26 color "#DDDDDD"

                            if chat_scroll_depth >= 2:
                                text "[[예서] 내일도 저러면 사진 더 올릴까?" size 26 color "#DDDDDD"
                                text "[[민재] 적당히 해 ㅋㅋ 근데 웃기긴 함" size 26 color "#DDDDDD"

                vbar:
                    value YScrollValue("chat_vp")
                    ysize 470
                    xsize 18
                    thumb Solid("#29b6f6")
                    base_bar Solid("#4a4a4a")

            if chat_scroll_depth < 2:
                textbutton "이전 메시지 더 보기":
                    action SetVariable("chat_scroll_depth", chat_scroll_depth + 1)
                    xalign 0.5
                    text_size 30
                    text_color "#FFFFFF"
                    text_hover_color "#FFFFCC"
                    background None

            if chat_scroll_depth >= 1:
                textbutton "캡처 저장":
                    action [SetVariable("f_r2_chat_checked", True), Return()]
                    xalign 0.5
                    text_size 30
                    text_color "#98FB98"
                    text_hover_color "#FFFFFF"
                    background None

            textbutton "스마트폰 끄기":
                action Return()
                xalign 0.5
                text_size 28
                text_color "#FF8A8A"
                text_hover_color "#FFFFFF"
                background None


screen messenger_contact_select():

    modal True
    tag phone

    frame:
        xalign 0.5
        yalign 0.5
        xsize 430
        ysize 760
        background Solid("#111418")
        padding (20, 20)

        vbox:
            xfill True
            spacing 22

            text "메시지" xalign 0.5 size 34 color "#FFFFFF"
            text "소윤 프로필을 누르면 개인 채팅이 열린다." xalign 0.5 size 18 color "#B8C0CC"

            null height 10

            frame:
                xfill True
                ysize 150
                background Solid("#1B2027")
                padding (20, 20)

                button:
                    xalign 0.5
                    yalign 0.5
                    background None
                    action Return("soyun")

                    vbox:
                        spacing 10
                        add "images/ui/profile_soyoon.png" xalign 0.5 xsize 90 ysize 90
                        text "소윤" xalign 0.5 size 28 color "#FFFFFF"
                        text "개인 채팅" xalign 0.5 size 18 color "#AAB3BF"


screen soyoon_dm_chat():

    modal True
    tag phone
    default dm_stage = 1

    frame:
        xalign 0.5
        yalign 0.5
        xsize 500
        ysize 640
        background Solid("#0F1115")
        padding (0, 0)

        vbox:
            spacing 0
            xfill True
            yfill True

            frame:
                xfill True
                ysize 88
                background Solid("#1C2430")
                padding (18, 14)

                hbox:
                    spacing 14
                    yalign 0.5

                    add "images/ui/profile_soyoon.png" xsize 52 ysize 52

                    vbox:
                        yalign 0.5
                        spacing 2
                        text "소윤" size 24 color "#FFFFFF"
                        text "개인 채팅" size 16 color "#B9C2CF"

            frame:
                xfill True
                ysize 462
                background Solid("#DCE3EA")
                padding (14, 14)

                viewport:
                    id "dm_vp"
                    draggable True
                    mousewheel True
                    yinitial 1.0
                    xfill True
                    yfill True

                    vbox:
                        xfill True
                        spacing 12

                        if dm_stage >= 1:
                            frame:
                                xalign 1.0
                                background Solid("#FFE08A")
                                padding (14, 10)
                                xmaximum 300
                                text "소윤아." size 22 color "#111111"

                        if dm_stage >= 2:
                            frame:
                                xalign 1.0
                                background Solid("#FFE08A")
                                padding (14, 10)
                                xmaximum 300
                                vbox:
                                    spacing 4
                                    text "나 방금 단톡방 봤어." size 22 color "#111111"
                                    text "아까 운동장에서도 이상했는데," size 22 color "#111111"
                                    text "생각보다 더 심하네." size 22 color "#111111"

                        if dm_stage >= 3:
                            frame:
                                xalign 1.0
                                background Solid("#FFE08A")
                                padding (14, 10)
                                xmaximum 300
                                text "이거 그냥 장난 아니잖아." size 22 color "#111111"

                        if dm_stage >= 4:
                            frame:
                                xalign 0.0
                                background Solid("#FFFFFF")
                                padding (14, 10)
                                xmaximum 300
                                text "..." size 22 color "#111111"

                        if dm_stage >= 5:
                            frame:
                                xalign 0.0
                                background Solid("#FFFFFF")
                                padding (14, 10)
                                xmaximum 300
                                vbox:
                                    spacing 4
                                    text "처음엔 애들이 다 웃길래 나도 가만히 있었어." size 22 color "#111111"
                                    text "근데 점점 너무 심해지는 것 같았어." size 22 color "#111111"

                        if dm_stage >= 6:
                            frame:
                                xalign 0.0
                                background Solid("#FFFFFF")
                                padding (14, 10)
                                xmaximum 300
                                vbox:
                                    spacing 4
                                    text "그때 말하려고 했는데..." size 22 color "#111111"
                                    text "이제 와서 말하면 애들이 이상하게 볼까 봐..." size 22 color "#111111"

            frame:
                xfill True
                ysize 90
                background Solid("#F2F2F2")
                padding (12, 12)

                if dm_stage < 6:
                    button:
                        xfill True
                        ysize 50
                        background Solid("#FFFFFF")
                        hover_background Solid("#F8F8F8")
                        action SetScreenVariable("dm_stage", dm_stage + 1)

                        if dm_stage == 1:
                            text "메시지를 보냈다." size 20 color "#666666" xalign 0.0 yalign 0.5
                        elif dm_stage == 2:
                            text "이거 그냥 장난 아니잖아..." size 20 color "#666666" xalign 0.0 yalign 0.5
                        elif dm_stage == 3:
                            text "답장을 기다린다..." size 20 color "#666666" xalign 0.0 yalign 0.5
                        else:
                            text "입력창을 눌러 계속 보기" size 20 color "#666666" xalign 0.0 yalign 0.5

                else:
                    button:
                        xfill True
                        ysize 50
                        background Solid("#FFFFFF")
                        hover_background Solid("#F8F8F8")
                        action Return("done")

                        text "대화를 닫는다." size 20 color "#666666" xalign 0.0 yalign 0.5


screen teacher_report():
    tag menu
    modal True

    frame:
        xalign 0.5 yalign 0.5
        padding (40, 40)
        background Solid("#3b3b3b")

        vbox:
            spacing 20
            xfill True

            text "선생님께 어떻게 말할까?" size 24 xalign 0.5 color "#ffffff"

            if f_r2_chat_checked or f_r2_soyoon_join:
                textbutton "캡처한 내용이나 같이 본 친구 이야기를 말한다.":
                    action Return("report_done")
                    text_size 20
                    text_color "#c8ffc8"
                    text_hover_color "#ffffff"
                    xalign 0.5
            else:
                text "아직 보여 줄 캡처나 같이 말해 줄 친구가 없다." color "#aaaaaa" xalign 0.5
                textbutton "그래도 교실에서 본 일을 먼저 말한다.":
                    action Return("report_weak")
                    text_size 20
                    text_color "#ffcccc"
                    text_hover_color "#ffffff"
                    xalign 0.5

            textbutton "확실한게 맞을까? 그냥 말하지 말자.":
                action Return("cancel")
                text_size 18
                text_color "#aaaaaa"
                xalign 0.5
