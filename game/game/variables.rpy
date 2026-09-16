############################################################
## variables.rpy
## 게임 내 상태 관리, 신뢰도 및 분기 플래그
############################################################

# ==========================================
# 1. 시스템 및 루프 상태
# ==========================================
default loop_no = 0
default ending_type = ""

# ==========================================
# 2. 핵심 수치 (신뢰도)
# ==========================================
default trust_soyun = 0
default trust_harin = 0
default trust_minjae = 0

# ==========================================
# 3. 핵심 열쇠
# ==========================================
default key1_structure = False
default key2_stay_with_harin = False
default key3_move_with_soyoon = False
default key4_minjae_pattern = False

# ==========================================
# 4. 1회차 조사 및 선택 플래그
# ==========================================
default inv_board = False
default inv_desk = False
default inv_back = False


# ==========================================
# 5. 2회차 조사 및 선택 플래그
# ==========================================
default inv_pe_bottle = False
default inv_pe_bench = False
default talk_pe_harin = False
default talk_pe_minjae = False
default talk_pe_soyun = False

default f_minjae_talk_r2 = False
default f_r2_chat_with_soyoon = False
default f_r2_bath_soyoon_talk = False
default f_r2_soyoon_join = False
default f_r2_harin_connect = False

# ==========================================
# 6. 3회차 아침 행동 플래그
# ==========================================
default r3_morning_time = 2
default r3_action_harin = False
default r3_action_soyun = False
default r3_action_minjae = False

# ==========================================
# 7. 3회차 엔딩 직결 플래그
# ==========================================
default note_witness = False

default f_r3_soyoon_coop = False
default f_r3_minjae_weakness = False
default f_r3_stay_together = False
default f_r3_teacher_support = False

# ==========================================
# 8. 관찰 노트 및 UI 플래그
# ==========================================
default note_lunch = False
default note_photo = False
default note_bathroom = False
default note_note = False
default note_role = False
default note_chat = False

default chat_scroll_depth = 0
default f_r2_chat_checked = False

# ==========================================
# 9. 보조 판정값
# ==========================================
default case_score = 0