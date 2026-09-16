############################################################
## 복도 끝의 신호 - 시스템 함수
############################################################

init python:

    def reset_r1_flags():
        store.f_r1_lunch_with_harin = False
        store.f_r1_photo_leave_with_harin = False
        store.f_r1_pe_with_harin = False
        store.f_r1_bath_call_harin = False
        store.f_r1_bath_ask_soyoon = False
        store.f_r1_bath_teacher_try = False
        store.f_r1_note_show_soyoon = False
        store.f_r1_note_tell_teacher = False

    def reset_r2_flags():
        store.key1_structure = False
        store.key2_stay_with_harin = False
        store.key3_move_with_soyoon = False

        store.f_r2_role_intervene = False
        store.f_r2_lunch_public_stop = False
        store.f_r2_lunch_with_harin = False
        store.f_r2_cleaning_intervene = False
        store.f_r2_cleaning_with_harin = False
        store.f_r2_chat_checked = False
        store.f_r2_chat_long_checked = False
        store.f_r2_chat_with_soyoon = False
        store.f_r2_bath_harin_talk = False
        store.f_r2_bath_soyoon_talk = False
        store.f_r2_soyoon_join = False
        store.f_r2_soyoon_partial = False
        store.f_r2_teacher_with_soyoon = False
        store.f_r2_teacher_alone = False

        store.chat_scroll_depth = 0
        store.teacher_report_selected = []

    def reset_r3_flags():
        store.f_r3_harin_spoke_role = False
        store.f_r3_public_stop_count = 0
        store.f_r3_support_count = 0
        store.f_r3_teacher_with_harin = False
        store.f_r3_wee_connected = False
        store.f_r3_review_pass = False
        store.teacher_report_selected = []

    def reset_notes():
        store.note_role = False
        store.note_lunch = False
        store.note_photo = False
        store.note_pe = False
        store.note_cleaning = False
        store.note_chat = False
        store.note_note = False
        store.note_bathroom = False

    def reset_all_game_state():
        reset_r1_flags()
        reset_r2_flags()
        reset_r3_flags()
        reset_notes()
        store.loop_no = 1
        store.ending_type = None

    def evaluate_r2_keys():
        # 열쇠 1: 반복 구조 확인
        if store.f_r2_chat_long_checked:
            store.key1_structure = True
        else:
            store.key1_structure = False

        # 열쇠 2: 당사자 곁으로 직접 감
        if store.f_r2_bath_harin_talk:
            store.key2_stay_with_harin = True
        else:
            store.key2_stay_with_harin = False

        # 열쇠 3: 함께 움직일 사람을 만듦
        if store.f_r2_soyoon_join:
            store.key3_move_with_soyoon = True
        else:
            store.key3_move_with_soyoon = False

    def can_go_loop3():
        return store.key1_structure and store.key2_stay_with_harin and store.key3_move_with_soyoon

    def evaluate_r3_true_end():
        return (
            store.f_r3_harin_spoke_role and
            store.f_r3_teacher_with_harin and
            store.f_r3_wee_connected and
            store.f_r3_review_pass
        )