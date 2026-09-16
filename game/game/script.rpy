############################################################
## script_with_illustration.rpy
## 「복도 끝의 신호」 — 일러스트 설계 반영본 (전 구간)
## - 매핑 테이블 기준: 배경 8종 / 이벤트 CG / t_, h_, s_, m_, y_, j_
## - 대사·내레이션·라벨·메뉴·변수·분기 로직은 일절 수정하지 않음
## - 캐릭터 dialogue 라인 직전에 scene + show 지시문만 정렬·추가
##
## [위치 약속]
##   담임(t)       : center
##   하린(h)       : center  (단, 가해 무리와 같이 있을 땐 right)
##   민재(m)       : left
##   예서(y)       : right
##   소윤(s)       : right   (하린과 단둘일 때는 left/center)
##   준호(j)       : right
############################################################

############################################################
## 캐릭터 정의
############################################################

define n = Character("나", who_color="#3A3A3A")

define h = Character("하린", who_color="#8B4A5A")
define s = Character("소윤", who_color="#4F6F52")
define m = Character("민재", who_color="#2F4F79")
define y = Character("예서", who_color="#9A5A3F")
define j = Character("준호", who_color="#5A5A7A")

define t = Character("담임 선생님", who_color="#2C3E50")
define pt = Character("체육 선생님", who_color="#6A4B2A")
define wt = Character("상담 선생님", who_color="#4A6F73")

define blink_black = Fade(0.08, 0.0, 0.12, color="#000")
define blink_black_long = Fade(0.15, 0.0, 0.28, color="#000")
define white_flash = Fade(0.08, 0.08, 0.45, color="#ffffff")

# 일반 장면/일러스트 전환을 조금 더 부드럽게 조정합니다.
# 회귀 연출의 blink_black / blink_black_long / white_flash는 그대로 유지합니다.
define dissolve = Dissolve(0.70)
define fade = Fade(0.30, 0.10, 0.45)

# 대사가 한 번에 뜨지 않고 자연스럽게 출력되도록 기본 속도를 지정합니다.
define config.default_text_cps = 35


transform wake_blur:
    xalign 0.5
    yalign 0.5
    zoom 1.03
    blur 4.0
    linear 0.6 blur 1.2 zoom 1.01

transform wake_clear:
    xalign 0.5
    yalign 0.5
    zoom 1.0
    blur 0.0



############################################################
## 이미지 선언
## 파일은 game 폴더 또는 images 폴더에 아래 이름으로 존재해야 함
############################################################

# 캐릭터 이미지

image t7 = "images/t7.png"
image t9 = "images/t9.png"
image pt1 = "images/pt1.png"
image y2 = "images/y2.png"
image y3 = "images/y3.png"
image y4 = "images/y4.png"
image y6 = "images/y6.png"
image y8 = "images/y8.png"
image y9 = "images/y9.png"

image h3 = "images/h3.png"
image h4 = "images/h4.png"
image h5 = "images/h5.png"
image h10 = "images/h10.png"
image h16 = "images/h16.png"
image h21 = "images/h21.png"
image h23 = "images/h23.png"
image h25 = "images/h25.png"
image h28 = "images/h28.png"

image j1 = "images/j1.png"
image j2 = "images/j2.png"

image m1 = "images/m1.png"
image m2 = "images/m2.png"
image m3 = "images/m3.png"
image m4 = "images/m4.png"
image m5 = "images/m5.png"
image m7 = "images/m7.png"
image m9 = "images/m9.png"
image m10 = "images/m10.png"
image m12 = "images/m12.png"

image s2 = "images/s2.png"
image s3 = "images/s3.png"
image s6 = "images/s6.png"
image s8 = "images/s8.png"
image s9 = "images/s9.png"
image s10 = "images/s10.png"
image s11 = "images/s11.png"

image t1 = "images/t1.png"
image t4 = "images/t4.png"
image t5 = "images/t5.png"
image t6 = "images/t6.png"


# 종이 / 소품 이미지

image cg_4 = "images/cg_4.png"
image cg_5 = "images/cg_5.png"
image cg_6 = "images/cg_6.png"
# UI 프로필 이미지

image profile_soyoon = "images/ui/profile_soyoon.png"


# 배경 이미지

image bg_1 = "images/bg_1.jpg"

image bg_2 = "images/bg_2.jpg"

image bg_3 = "images/bg_3.jpg"

image bg_4 = "images/bg_4.jpg"


image bg_5 = "images/bg_5.jpg"


image bg_6 = "images/bg_6.jpg"


image bg_7 = "images/bg_7.jpg"


image bg_8 = "images/bg_8.jpg"


image bg_9 = "images/bg_9.jpg"


image bg_10 = "images/bg_10.jpg"


image bg_11 = "images/bg_11.jpg"


image bg_12 = "images/bg_12.jpg"


image bg_13 = "images/bg_13.jpg"

image bg_14 = "images/bg_14.jpg"


image bg_15 = "images/bg_15.jpg"

image pe = "images/pe.png"


image bg_16 = "images/bg_16.jpg"


image bg_17 = "images/bg_17.jpg"

image bg_1_blur = Transform("images/bg_1.jpg", blur=5.0)
image bg_2_blur = Transform("images/bg_2.jpg", blur=5.0)
image bg_4_blur = Transform("images/bg_4.jpg", blur=5.0)
image bg_5_blur = Transform("images/bg_5.jpg", blur=5.0)
image bg_6_blur = Transform("images/bg_6.jpg", blur=5.0)
image bg_7_blur = Transform("images/bg_7.jpg", blur=5.0)
image bg_8_blur = Transform("images/bg_8.jpg", blur=5.0)
image bg_9_blur = Transform("images/bg_9.jpg", blur=5.0)
image bg_10_blur = Transform("images/bg_10.jpg", blur=5.0)
image bg_11_blur = Transform("images/bg_11.jpg", blur=5.0)
image bg_12_blur = Transform("images/bg_12.jpg", blur=5.0)
image bg_14_blur = Transform("images/bg_14.jpg", blur=5.0)
image bg_15_blur = Transform("images/bg_15.jpg", blur=5.0)
image bg_16_blur = Transform("images/bg_16.jpg", blur=5.0)
image bg_17_blur = Transform("images/bg_17.jpg", blur=5.0)
image pe_blur = Transform("images/pe.png", blur=5.0)
image cg_8_blur = Transform("images/cg_8.jpg", blur=5.0)
image cg_h1_blur = Transform("images/cg_h1.jpg", blur=5.0)

# CG 이미지

image cg_1 = "images/cg_1.jpg"
image cg_2 = "images/cg_2.jpg"
image cg_3 = "images/cg_3.jpg"
image cg_7 = "images/cg_7.jpg"
image cg_8 = "images/cg_8.jpg"
image cg_9 = "images/cg_9.jpg"

image cg_b1 = "images/cg_b1.jpg"
image cg_b2 = "images/cg_b2.jpg"
image cg_b3 = "images/cg_b3.jpg"

image cg_h1 = "images/cg_h1.jpg"
image cg_h2 = "images/cg_h2.jpg"

image cg_n1 = "images/cg_n1.jpg"

image cg_s1 = "images/cg_s1.jpg"
image cg_s2 = "images/cg_s2.jpg"
image cg_s3 = "images/cg_s3.jpg"
image cg_s4 = "images/cg_s4.jpg"

image cg_t1 = "images/cg_t1.jpg"
image cg_t2 = "images/cg_t2.jpg"
image cg_t3 = "images/cg_t3.jpg"
image cg_t4 = "images/cg_t4.jpg"


# 조사 화면 이미지

image classroom_r1_investigation = "images/classroom_r1_investigation.png.jpg"

############################################################
## 위치 transform
############################################################

transform center_stage:
    xalign 0.5
    yalign 1.0

transform left_stage:
    xalign 0.25
    yalign 1.0

transform right_stage:
    xalign 0.75
    yalign 1.0


# ------------------------------------------------------------
# 대화 장면용 약한 배경 블러
# ------------------------------------------------------------

transform bg_dialogue_blur:
    blur 2

transform bg_clear:
    blur 0

############################################################
## 시작 라벨
############################################################

label start:

    stop music fadeout 1.0
    # ------------------------------------------------------
    # 1. 시스템 및 신뢰도 초기화
    # ------------------------------------------------------
    $ loop_no = 0
    $ ending_type = ""
    $ trust_soyun = 0
    $ trust_harin = 0
    $ trust_minjae = 0

    # ------------------------------------------------------
    # 2. 교실/운동장 조사 플래그 초기화
    # ------------------------------------------------------
    $ inv_board = False
    $ inv_desk = False
    $ inv_back = False
    $ inv_pe_bottle = False
    $ inv_pe_bench = False
    $ talk_pe_harin = False
    $ talk_pe_minjae = False
    $ talk_pe_soyun = False
    $ talk_pe_yeseo = False
    $ r2_class_inv_initialized = False
    

    # ------------------------------------------------------
    # 3. 회차별 핵심 이벤트 및 선택지 플래그 초기화
    # ------------------------------------------------------
    $ f_minjae_talk_r2 = False
    $ f_r2_chat_with_soyoon = False
    $ f_r2_bath_soyoon_talk = False
    $ f_r2_soyoon_join = False
    $ f_r2_harin_connect = False
    $ f_r3_soyoon_coop = False
    $ f_r3_stay_together = False
    $ f_r3_teacher_support = False

    # ------------------------------------------------------
    # 4. 핵심 열쇠 및 단서 수첩 플래그 초기화
    # ------------------------------------------------------
    $ key1_structure = False
    $ key2_stay_with_harin = False
    $ key3_move_with_soyoon = False
    $ key4_minjae_pattern = False
    $ note_witness = False

    $ note_lunch = False
    $ note_photo = False
    $ note_bathroom = False
    $ note_note = False
    $ note_role = False

    $ chat_scroll_depth = 0
    $ f_r2_chat_checked = False
    $ note_chat = False

    show screen quick_note_button
    jump prologue_1

############################################################
## 프롤로그
############################################################

label prologue_1:
    # ------------------------------------------------------
    # 1. 교실 배경 출력
    # ------------------------------------------------------
    scene bg_1 with fade

    play sound "audio/bell.mp3"

    "종이 울렸다."
    "사물함으로 달려가는 발소리, 필통 지퍼 여는 소리, 의자 끄는 소리가 한꺼번에 터져 나왔다."

    # ------------------------------------------------------
    # 2. 선생님의 단호한 표정 등장
    # ------------------------------------------------------
    # 표 기준: t_1 = "조용. / 얘들아, 수업 시작하기 전에 먼저 말할 게 있어."
    
    stop sound fadeout 1.0
    scene bg_1_blur with dissolve
    show t1 at center_stage with dissolve
    t "조용."
    "선생님의 한마디에 모든 소리가 멈췄다."

    "선생님은 출석부를 품에 안은 채 교실을 한 번 천천히 둘러본 뒤 말을 이었다."
    hide t1 with dissolve
    show t5 at center_stage with dissolve
    t "얘들아, 수업 시작하기 전에 먼저 말할 게 있어."

    # 표 기준: t_2 = "하린이가 오늘부터 다른 학교로 가게 됐다."

    t "하린이가 오늘부터 다른 학교로 가게 됐다."
    hide t5 with dissolve
    "잠깐의 정적."


    scene bg_2 with dissolve
    "그리고 여기저기서 수군거림이 번졌다."

    # ------------------------------------------------------
    # 3. 아이들의 반응
    # ------------------------------------------------------
    scene bg_2_blur with dissolve
    # 표 기준: m_1 = "엥, 갑자기?" 외
  
    show m4 at left_stage with dissolve
    m "엥, 갑자기?"

    # 표 기준: y_1 = "그러고 보니 지난주에도 맨날 결석했잖아."
    show y8 at right_stage with dissolve
    y "그러고 보니 지난주에도 맨날 결석했잖아."
    hide m4 
    hide y8 
    with dissolve

    # 표 기준: j_1 = "그냥 이사간거겠지, 뭐."
    show j1 at center_stage with dissolve
    j "그냥 이사 간 거겠지, 뭐."
    hide j1 with dissolve

    "아이들은 그렇게 말하고 금세 다른 이야기로 넘어갔다."

    # ------------------------------------------------------
    # 4. 하린의 책상 클로즈업 (이벤트 CG)
    # ------------------------------------------------------
    scene cg_1 with dissolve

    "하지만 어쩐지 나는 하린의 자리에 시선이 갔다."
    "하린이 앉던 자리엔 이름표만 덩그러니 남아 있다."

    "언제부터였지."
    "저 자리가 비어 있는 게 당연해진 게."

    scene black
    with fade

    "하린이를 떠올려도 같이 떠오르는 장면이 하나도 없다는 게."

    "그런데 이상하게도, 딱 한 장면만큼은 머릿속에 또렷하게 남아 있었다."

    scene cg_2 with dissolve
    "축 처진 어깨. 어두운 눈. 빨갛게 부어 있던 눈가."
    "그게 내가 마지막으로 본 하린이의 모습이었다."

    scene black
    with fade

    jump prologue_2

label prologue_2:
    scene bg_3
    with fade

    "방과 후. 내 방."
    n "아…"

    play sound "audio/bed_sheets_moving.mp3"
    "가방을 바닥에 내려놓고 침대에 등부터 떨어뜨렸다."
    stop sound
    "천장을 올려다보는데 자꾸만 하린의 빈자리가 눈앞에 겹쳐 보였다."
    n "하린이는 왜 갑자기 전학을 갔을까."
    n "그날 왜 울었는지, 한 번이라도 물어볼걸 그랬나."
    n "…아니다, 내가 물어봤다고 해서 뭐가 달라졌겠어."
    n "그 전에, 나는 하린이에 대해 뭘 알고 있었지."

    "생각이 꼬리에 꼬리를 물다가 툭 끊겼다."
    with blink_black

    "눈꺼풀이 무거워졌다."
    with blink_black

    "하린이 마지막 모습을 떠올리면서 잠이 든다는 게 이상하다는 생각을 마지막으로,"
    with blink_black_long

    "눈앞이 흐려졌다."
    scene black
    with Dissolve(1.0)

    "멀리서 물 흐르는 소리."
    "누군가의 희미한 웃음소리. 짧게 울리는 진동음."
    "의자가 바닥을 날카롭게 긁는 소리가 점점 가까워졌다."
    "그리고"
    "모든 소리가 한순간에 끊겼다."
    scene black
    with fade
    "바로 귀 옆에서, 떨리는 목소리가 들려왔다."

    play sound "audio/heartbeat.mp3"
    scene cg_3 with dissolve
    h "너는… 봤잖아."
    stop sound fadeout 1.0

    jump scene0_investigation

############################################################
## 이하 장면은 기존 script.rpy 본문에 연결
############################################################


############################################################
## 조사 시스템 (1회차 진입)
############################################################

label scene0_investigation:
    scene black
    with fade

    # 눈 뜬 직후: bg_4가 흐릿하고 살짝 확대되어 보임
    scene bg_4_blur at wake_blur
    with white_flash

    pause 0.3

    n "헉!"
    "온몸에 소름이 돋았다."
    "분명 내 방 침대였는데."

    with blink_black

    "눈을 뜨니까 눈부신 햇살이랑 시끌벅적한 소리가 한꺼번에 들어왔다."

    with blink_black

    n "…학교?"
    "나는 내 책상에 엎드려 있었다."

    # 눈을 감았다 뜨면서 정상 크기, 정상 선명도 bg_4로 돌아옴
    scene bg_4 at wake_clear
    with blink_black_long

    n "뭐지? 꿈인가? 나 지금 왜 교실에 있지?"

    jump inv_loop_r1


label inv_loop_r1:

    scene bg_4 at wake_clear
    with dissolve

    if inv_board and inv_desk and inv_back:
        jump inv_done_r1

    hide screen quick_note_button
    call screen class_investigation
    show screen quick_note_button

    if _return == "board":
        scene bg_4 with fade

        if not inv_board:
            $ inv_board = True
            "천천히 고개를 들어 칠판을 봤다."
            "오른쪽 구석에 날짜가 적혀 있었다."
            "< 5월 10일 월요일 >"
            n "5월 10일…?"
            n "말도 안 돼. 당번이 날짜를 안 바꿨나?"
            n "아니, 애초에 방에 있다가 갑자기 학교에 있는 게 말이 안 되잖아."
        else: 
            "칠판은 이미 확인했다."

        jump inv_loop_r1


    elif _return == "desk":
        scene bg_4 with fade

        if not inv_desk:
            $ inv_desk = True
            "무심코 고개를 돌렸다."
            "돌린 채로 한참을 그대로 있었다."
            "하린이가 있었다."
            n "어… 전학, 갔잖아."
            "분명히 갔는데. 언제였는지까지 아는데."
            "하린이는 창가 셋째 줄, 자기 자리에 그대로 앉아 있었다."
            "고개를 푹 숙인 채, 볼펜 끝으로 공책을 눌러 선을 긋고 있었다."
            "반복해서. 같은 자리에. 계속."
            n "…꿈이니까. 꿈이면 이런 것도 보이니까."
        else: 
            "하린이 자리는 이미 확인했다."

        jump inv_loop_r1


    elif _return == "back":

        scene bg_4 with fade

        if not inv_back:
            $ inv_back = True

            play sound "audio/punch.mp3"
            with vpunch
            "퍽."

            scene bg_4_blur with dissolve
            show m2 at center_stage with dissolve

            m "야, 정신 차려. 멍 때리는 거 꼭 오하린 같잖아."

            hide m2 with dissolve
            scene bg_4 with dissolve

            "민재가 내 어깨를 치고 지나갔다."
            "뒤쪽에서 웃음이 터졌다."
        
        else:
            "민재는 이미 친구들에게 돌아갔다."

        jump inv_loop_r1


    elif _return == "finish":
        if not (inv_board and inv_desk and inv_back):
            "아직 다 본 건 아닌 것 같지만,"
            "일단 이 상황이 뭔지부터 생각해 봐야겠다."
        jump inv_done_r1


    else:
        jump inv_loop_r1


label inv_done_r1:
    "몰래 허벅지를 꼬집어봤다. 아프다."
    "웃음소리, 책상에 닿는 팔 느낌, 창문으로 들어오는 바람."
    "모든 게 너무 생생했다."
    n "꿈이… 아니라고?"
    n "진짜 과거로 돌아왔다고? 하린이가 전학 가기 전으로?"
    "머릿속이 하얗게 비었다."
    "그때, 잠들기 전 귓가에 울렸던 하린의 목소리가 다시 떠올랐다."

    scene cg_3 with Dissolve(0.8)
    h "'너는… 봤잖아.'"

    scene bg_4 at wake_clear
    with Dissolve(0.6)

    n "…"
    n "내가 뭘 봤다는 거지? 아직도 꿈을 꾸는 건가?"
    "하지만 저기 하린이가 있다." 
    "돌아가기 전, 내가 마지막으로 봤던 그 모습 그대로."
    n "내가 당장 뭘 할 수 있는 상황이 아니야." 
    n "일단은… 지켜보는 수밖에 없어."

    jump loop1_start

############################################################
## 1회차 — 방관과 무력감의 굴레
############################################################

label loop1_start:
    $ loop_no = 1
    scene bg_4
    with fade

    "오전 수업은 어떻게 지나갔는지도 잘 기억나지 않는다."
    "선생님 말씀을 듣고 있어도 계속 하린이가 신경 쓰였다."
    
    play sound "audio/bell.mp3"
    "어느새 4교시 종료를 알리는 종이 울렸다."

    stop sound fadeout 1.0
    play sound "audio/children.mp3"
    "아이들이 의자를 끌며 우르르 급식실을 향해 빠져나갔다."    
    
    n "…일단 가보자."
    "나 역시 반쯤 떠밀리듯 아이들 틈에 섞여 걸음을 옮겼다."

    stop sound fadeout 1.0

    jump r1_s1_lunch

label r1_s1_lunch:
    $ note_lunch = True

    play sound "audio/children.mp3"
    scene bg_5 with fade
    "급식실은 평소처럼 시끌벅적했다."

    stop sound fadeout 1.0
    "맛있는 냄새와 아이들 떠드는 소리가 뒤섞인 사이,"
    "문득 한쪽 테이블이 눈에 들어왔다."

    scene bg_6
    with dissolve
    "민재랑 예서네 무리가 앉아 있는 6인용 테이블이었다."
    "번호대로라면 하린이가 앉아야 할 자리에는" 
    "예서의 겉옷과 민재의 가방이 놓여 있었다."
    
    scene bg_6_blur with dissolve
    show h23 at center_stage with dissolve

    "하린이는 식판을 든 채 자리 옆을 잠시 서성였다."
    "애들이 짐을 치워주길 기다리는 것 같았지만, 아무도 움직이지 않았다."
    "민재는 어제 본 TV 프로그램 이야기에 열중했고, 예서는 옆에서 깔깔거리며 웃고 있었다."

    hide h23 with dissolve
    scene bg_6 with dissolve

    "하린이가 자리에 앉으려는 듯 한 걸음 다가가자,"
    "조금 전까지 웃고 떠들던 테이블이 잠깐 조용해졌다."
    "하지만 하린이는 잠시 그 자리에 서 있다가,"
    "결국 아무 말 없이 몸을 돌려 멀리 떨어진 구석 자리로 향했다."
    n "(…방금 분위기가 이상했어.)"
    scene bg_6_blur with dissolve
    show s8 at center_stage with dissolve
    # 테이블에 앉아 눈치를 보던 소윤이의 반응 추가
    "그때 예서 옆에 앉아 있던 소윤이가 슬쩍 고개를 들었다."
    "하린이의 뒷모습을 따라가던 시선이 잠시 멈췄다."
    
    n "(그냥 모른 척해도 되는 걸까.)"
    
    hide s8 with dissolve

    menu:
        "친한 애들끼리 앉으려고 그런 거겠지. 나도 내 자리에 앉자.":
            
            scene bg_6
            with dissolve
            
            "나는 그냥 평소 앉던 자리에 앉았다."
            "멀리 떨어진 구석에서 하린이가 혼자 밥을 먹고 있었다."
            "하린이는 평소에도 늘 저쪽에서 혼자 밥을 먹곤 했다."
            "그래서 오늘도 그냥 평소와 다를 것 없는 모습이라고 생각했다."

        "저기 자리 비어 있는데 옷 좀 치워주면 안 돼?":
            n "야, 민재야. 여기 자리 비었는데 짐 좀 치워주면 안 돼?" 
            n "아까 하린이 여기 서 있다가 가던데."
            "내 말에 민재가 고개를 들어 나를 봤다."
            # 표 기준: m_3 = "아, 맞다. 여기 옷 있었네. 야, 김예서! 네 옷 좀 치워."
            scene bg_6_blur
            with dissolve 
            show m7 at center_stage with dissolve
            m "아, 맞다. 야, 김예서! 네 옷 좀 치워."
            hide m7 with dissolve
            "민재가 별일 아니라는 듯 옷을 옆으로 밀었다."
            "하지만 하린이는 이미 저 멀리 구석 자리에 앉은 뒤였다."
            n "(괜히 내가 나선 건가.)"
            "아까까지 떠들썩하던 테이블이 잠깐 조용해진 것 같아 괜히 눈치가 보였다."

        "나도 오늘 혼자인데, 하린이 옆에 가서 앉을까?":
            "나는 슬쩍 방향을 바꿔 하린이가 있는 테이블로 향했다."

            scene bg_6_blur
            with dissolve
           
            "하린이는 식판을 앞에 둔 채 말없이 밥을 먹고 있었다."
            "표정은 어딘가 멍해 보였다."
            show h3 at center_stage with dissolve
           
            "내가 맞은편에 식판을 내려놓자, 하린이가 놀란 듯 고개를 들었다."
            n "나 여기 앉아도 돼? 오늘은 나도 같이 먹을 애가 없어서."
            hide h3 with dissolve
            show h16 at center_stage with dissolve
            h "…응. 앉아."

            "하린이는 조금 당황한 표정이었지만, 작게 고개를 끄덕였다."
            hide h16 with dissolve
            "그 뒤로 특별한 이야기를 나누지는 않았다." 
            "조금 어색했지만, 그렇다고 불편하지도 않았다."
    
    jump r1_s2_photo

label r1_s2_photo:
    $ note_photo = True
    scene black with fade

    scene bg_4 with fade

    "점심시간이 거의 끝나갈 무렵이었다."
    "밥을 먹고 돌아온 아이들은 여기저기 모여 떠들고 있었다."
    "나도 자리에 앉아 멍하니 창밖을 보며 쉬고 있던 참이었다."

    "그때 창가 쪽에서 갑자기 웃음소리가 들렸다."
    "민재가 핸드폰 화면을 주변 아이들에게 보여주고 있었다."

    scene bg_4_blur with dissolve

    # 민재: 사진 보여주며 조롱
    show m9 at left_stage with dissolve
    m "야, 이거 봐. 지난주 체육 시간에 오하린 넘어진 거."
    m "표정 진짜 웃기지 않냐?"


    # 준호: 실없게 웃음
    show j2 at right_stage with dissolve
    j "아, 뭐야 ㅋㅋㅋ 이거 연속으로 찍은 거야?"
    "준호는 별생각 없이 화면을 들여다보며 웃었다."
    "누가 몰래 찍은 사진인지 신경 쓰는 사람은 없어 보였다."
    hide m9
    hide j2
    with dissolve

    # 예서: 말리는 척 동조
    show y2 at center_stage with dissolve
    y "야, 뭐 그런 걸 다 찍어~ 빨리 지워라."
    "말은 그렇게 하면서도 예서는 화면을 힐끗 보며 웃고 있었다."
    "핸드폰은 자연스럽게 옆 사람 손으로 넘어갔다."
    hide y2 with dissolve

    scene bg_4 with dissolve
    n "(저런 사진까지 찍어놓고 같이 보는 사이였나?)"
    n "(하린이는 저거 알고 있는 건가….)"
    "아까 급식실에서 본 모습까지 문득 떠올랐다."
    "별일 아닌 것 같으면서도, 어딘가 계속 마음에 걸렸다."

    # 소윤: 말 못 하고 눈치 보는 컷
    scene bg_4_blur with dissolve
    show s2 at center_stage with dissolve
    "무리 끝에 서 있던 소윤이는 다른 아이들과 조금 달랐다."
    "소윤이는 억지로 웃는 척하고 있었지만, 화면은 제대로 쳐다보지 않았다."
    "다른 아이들의 눈치를 슬쩍 살피더니, 한 발짝 뒤로 물러섰다."
    hide s2 with dissolve

    # 하린은 여기서 꼭 스탠딩을 안 띄워도 되지만,
    # 분위기 강조하고 싶으면 아래 두 줄 사용 가능
    scene bg_4 with dissolve
    "교실 한구석."
    scene bg_4_blur with dissolve
    show h5 at center_stage with dissolve
    "하린이는 자기 자리에 앉아 고개를 숙이고 있었다."
    "손에 쥔 필통 지퍼를 몇 번이나 열었다 닫았다 했다."
    "주변이 시끄러워질수록 하린이의 손만 더 바빠졌다."
    hide h5 with dissolve
    "그 모습을 보고 있자니 괜히 마음 한구석이 답답해졌다."
    scene bg_4 with dissolve

    n "(뭐라도 말해야 하나…)"

    menu:

        "내가 직접 본 것도 아닌데. 괜히 나섰다가 내가 이상한 애 되면 어떡해.":
            scene bg_7
            with dissolve
            "나는 애써 시선을 돌리고 교실 밖으로 나왔다."
            "복도로 나왔는데도 뒤에서 웃음소리가 계속 들려왔다." 
            "조금 마음에 걸렸지만, 다시 돌아가지는 않았다."

        "저건 좀 심하잖아. 지우라고 말하자.":
            n "야, 허락도 안 받고 남의 사진 돌려보는 게 재밌어? 그거 지워."
            "내 말이 끝나자 주변의 웃음소리가 뚝 끊겼다."
            scene bg_4_blur
            with dissolve
            # 민재: 짜증/방어
            show m10 at left_stage with dissolve
            m "아, 왜 오버야? 그냥 장난친 건데."
            "민재는 잠깐 인상을 쓰더니, 갑자기 하린이 쪽을 돌아봤다."
            m "야, 오하린! 내가 네 사진 찍었다!"
            m "미안하다! 이제 말했으니까 됐지?"
            "민재는 일부러 큰 소리로 말하고는 핸드폰을 주머니에 푹 집어넣었다."
            hide m10 with dissolve
            show h4 at right_stage with dissolve
            "아이들의 시선이 이번에는 하린이 쪽으로 향했다."
            "하린이는 고개를 더 숙인 채 가만히 앉아 있었다."
            n "(괜히 하린이를 더 난처하게 만든 건가….)"
            hide h4 with dissolve


        "하린이도 이 분위기 버티기 힘들 것 같다. 같이 나갈까.":
            "나는 하린의 책상 앞으로 걸어가 섰다."
            n "하린아, 잠깐 나갈래? 바람 좀 쐬자."
            scene bg_4_blur
            with dissolve
            show h4 at center_stage with dissolve
            "하린이는 바로 대답하지 않았다."
            "나를 한 번 바라보고, 민재 쪽도 슬쩍 확인했다."
            h "…왜?"
            n "그냥. 여기 좀 시끄럽잖아."
            "하린이는 잠시 망설이다가 천천히 자리에서 일어났다."
            hide h4 with dissolve
            scene bg_7
            with dissolve
            "복도 끝 자판기 앞."
            scene bg_7_blur
            with dissolve
            "하린이는 나와 조금 거리를 둔 채 서 있었다."
            "뽑은 음료수 캔도 따지 않고 손안에서 계속 만지작거렸다."
            n "…아까 괜찮았어?"

            # 하린: 닫힌 반응
            show h3 at center_stage with dissolve
            "하린이는 잠깐 나를 쳐다봤다가 금세 시선을 피했다."
            h "응." 
            h "별거 아니야." 
            n "그래도 걔들이—" 
            h "진짜 괜찮아." 
            "말은 짧았고, 더 묻지 말라는 듯한 목소리였다." 
            "나는 더 이상 아무 말도 하지 못했다."
            hide h3 with dissolve


    scene black with fade

    "그 뒤로도 수업에 좀처럼 집중할 수 없었다."

    scene bg_3 with dissolve
    play sound "audio/bed_sheets_moving.mp3"
    "집에 돌아와 침대에 누웠는데,"
    "낮에 봤던 장면들이 하나씩 다시 생각났다."
    stop sound
    "하린이가 고개를 숙이고 있던 모습."
    "그 옆에서 웃고 떠들던 아이들."
    n "(내가 너무 예민하게 생각하는 건가.)"
    n "(그냥 친한 애들끼리 장난친 걸 수도 있잖아.)"

    "그렇게 생각하고 넘기려는데도 마음이 좀처럼 편해지지 않았다."
    n "(…왜 이렇게 계속 신경 쓰이지.)"
    "나는 한참 뒤에야 겨우 눈을 감을 수 있었다."

    scene black with blink_black
    scene bg_3 with blink_black
    scene black with blink_black
    scene bg_3 with blink_black_long

    scene black with Dissolve(1.0)
    pause 1.0
    "몇 번이나 잠에서 깼다."
    "무슨 꿈을 꿨는지는 기억나지 않았지만, 이상하게 마음은 계속 무거웠다."

    scene black with fade
    pause 1.0
    jump r1_s5_bathroom

label r1_s5_bathroom:
    $ note_bathroom = True

    scene bg_4 with fade
    "다음 날, 화요일 아침."
    "교실 문 앞에 서자 어제 있었던 일들이 다시 떠올랐다."
    "왜 갑자기 이때로 돌아온 건지는 아직도 알 수 없었다."
    "다만 돌아온 뒤로 이상하게 하린이와 관련된 일들만 계속 눈에 걸렸다."
    n "(설마… 하린이 때문에 돌아온 건가?)"
    "물론 아무 근거도 없었다." 
    "그래도 지금으로서는 그것 말고는 짐작 가는 게 없었다." 
    "문을 열자 평소처럼 시끄러운 교실이 눈앞에 펼쳐졌다." 
    "나는 들어서자마자 하린이 자리를 확인했다."
    scene bg_4_blur with fade
    show h23 at center_stage with dissolve
    "하린이는 책상에 엎드려 있었다."
    hide h23 with dissolve

    scene bg_4 with dissolve
    "수업이 시작되고 교과서를 펼치려던 순간,"
    "문득 한 가지 생각이 머리를 스쳤다."

    n "(잠깐….)"
    n "(하린이가 학교에 안 나오기 시작한 게 언제였지?)"

    "기억을 더듬다가 손이 멈췄다."
    n "(수요일.)"
    n "(내일부터 자리가 비었고… 다음 주 월요일에 전학 갔다고 했어.)"

    "그 순간 머릿속이 막막해졌다."
    n "(그럼 오늘 지나면 하린이를 못 보는 거잖아.)"
    "만약 정말 하린이 때문에 이때로 돌아온 거라면," 
    "내일부터는 뭘 확인해야 하는지도, 뭘 해야 하는지도 알 수 없었다."
    n "(아직 왜 돌아온 건지도 모르는데….)" 
    n "(하린이까지 없어지면, 그다음엔 어떡하지?)" 
    "갑자기 시간이 얼마 남지 않은 것처럼 느껴졌다." 
    "1교시 내내 수업에 집중할 수 없었다." 
    "칠판을 보고 있어도 자꾸 시계만 확인하게 됐다."

    play sound "audio/bell.mp3"
    scene bg_7 with fade
    "쉬는 시간 종이 치자마자, 더 이상 못 버티고 무작정 복도로 빠져나왔다."


    stop sound fadeout 1.0
    scene bg_8 with dissolve
    "화장실 앞 복도 끝."
    "창가에 서서 숨을 고르려던 순간, 화장실 문이 열렸다."
    scene bg_8_blur with dissolve
    show s3 at left_stage with dissolve
    "소윤이가 먼저 나왔고,"
    show h10 at right_stage with dissolve
    "잠시 뒤 하린이가 그 뒤를 따라 나왔다."

    
    "가까이서 본 하린이 얼굴에 순간 말문이 막혔다."
    "눈가는 퉁퉁 부어 있었고, 코끝까지 붉어져 있었다."
    "누가 봐도 방금 울고 나온 얼굴이었다."
    hide s3 with dissolve
    show s6 at left_stage with dissolve
    "소윤이는 하린이를 힐끗 보더니,"
    "나와 눈이 마주치자 흠칫하며 고개를 돌렸다."

    "아침부터 머릿속을 맴돌던 생각이 다시 떠올랐다."

    n "(하린이는 내일부터 학교에 안 와.)"

    "왜 이때로 돌아온 건지도 아직 모르는데,"
    "오늘이 지나면 하린이에게 무슨 일이 있었는지 확인할 기회조차 없어질 것 같았다."
    hide s6 
    hide h10 
    with dissolve

    show s8 at left_stage 
    show h5 at right_stage 
    with dissolve
    "하린이는 붉어진 눈으로 바닥만 바라본 채 걸어갔다."
    "소윤이도 내 시선을 피하며 서둘러 지나치려 했다."

    "두 사람의 뒷모습을 바라보다가, 나는 입술을 꾹 깨물었다."

    menu:
        "서둘러 지나가려는 소윤이를 붙잡고 묻는다.":
            hide s8
            hide h5
            with dissolve
            scene bg_8 with dissolve
            n "화장실에서 무슨 일 있었어?" 
            n "너도 하린이랑 같이 있었잖아." 
            "소윤이는 잠깐 당황한 얼굴로 나를 보다가 금세 표정이 굳었다."
            scene bg_8_blur with dissolve
            show s10 at center_stage with dissolve
            s "왜 나한테 물어봐?" 
            s "내가 울린 거 아니야. 난 아무것도 몰라!" 
            n "아니, 그냥 무슨 일 있었는지만—" 
            s "그렇게 궁금하면 네가 직접 물어봐!"
            hide s10 with dissolve
            scene bg_8 with dissolve
            "소윤이는 내 손을 홱 뿌리치고 빠르게 교실 쪽으로 가버렸다." 
            "나는 아무 말도 못 한 채 그 뒷모습만 바라봤다."
            n "(나는 누가 울렸냐고 묻지도 않았는데….)"

        "혼자 걷고 있는 하린이에게 다가가 말을 건다.":
            scene bg_8 with dissolve
            n "하린아… 잠깐만."
            scene bg_8_blur with dissolve
            show h16 at center_stage with dissolve
            "뒤에서 조심스럽게 부르자 하린이가 화들짝 놀라며 돌아봤다." 
            "아직 눈물이 맺힌 채였다." 
            "하린이는 나를 보자 한 걸음 뒤로 물러섰다." 
            n "괜찮아? 방금 화장실에서—"
            hide h16 with dissolve
            show h10 at center_stage with dissolve
            h "…괜찮아." 
            h "그냥 좀 내버려 둬." 
            n "아니, 나는 그냥—" 
            "하린이는 대답 대신 소매로 눈가를 급하게 훔쳤다." 
            h "진짜 괜찮다니까."
            hide h10 with dissolve
            "하린이는 나를 피해 반대쪽 계단으로 빠르게 내려갔다."
            scene bg_8 with dissolve
            "붙잡아야 하나 싶었지만, 차마 따라가지는 못했다."

        "어떻게 해야 할지 모르겠다. 가만히 서 있는다.":
            scene bg_8 with dissolve
            "나는 그 자리에서 쉽게 움직이지 못했다." 
            "누구에게 먼저 말을 걸어야 할지, 무슨 말을 해야 할지도 떠오르지 않았다." 
            "망설이는 사이 소윤이는 교실로 들어가 버렸고," 
            "하린이도 어느새 계단 아래로 사라졌다." 
            "결국 복도에는 나만 남았다." 
            n "(…그냥 이렇게 보내버렸네.)" 
            "뒤늦게 마음이 무거워졌다."

    scene bg_9 with fade
    "그날 3교시부터 하린이의 자리는 비어 있었다."
    "몸이 좋지 않아 조퇴했다는 선생님의 짧은 설명이 전부였다."
    "아침에 떠올렸던 생각이 다시 머릿속을 스쳤다."
    n "(내일부터는 학교에도 안 나오는데….)"
    "결국 오늘도 제대로 알아낸 건 아무것도 없었다."
    "빈자리를 보고 있으니 마음만 더 조급해졌다."
    
    scene black with fade
    pause 0.8
    jump r1_s6_note
# ----------------------------------------------------------
# R1-S6. 수요일 아침 — 결석과 서랍 속의 쪽지
# ----------------------------------------------------------
label r1_s6_note:
    $ note_note = True

    scene bg_9 with fade
    "다음 날, 수요일 아침." 
    "예상했던 대로 하린이의 자리는 비어 있었다." 
    "알고 있었는데도 실제로 빈 책상을 보니 기분이 이상했다." 
    "어제 복도에서 본 하린이의 모습이 자꾸 떠올랐다." 
    "그런데 다른 아이들은 하린이가 오지 않은 걸 별로 신경 쓰지 않는 듯했다." 
    "누구 하나 하린이 이야기를 꺼내지 않았고," 
    "교실은 평소와 다를 것 없이 흘러갔다."

    scene black with fade
    "1교시가 끝난 쉬는 시간."
    "자리에서 일어나다 지우개를 떨어뜨렸다."
    scene cg_1 with dissolve
    "바닥을 구르던 지우개가 하린이의 빈 책상 밑에서 멈췄다."

    scene cg_8 with dissolve
    "몸을 숙여 지우개를 집으려던 순간," 
    "하린이의 책상 아래에 구겨진 종이 한 장이 떨어져 있는 게 보였다." 
    "나는 별생각 없이 그걸 집어 들었다."

    scene cg_8_blur with dissolve

    call screen interactive_note

    scene bg_9 with dissolve
    "종이를 읽는 순간 손끝이 서늘해졌다."
    n "(이게 뭐야….)"
    "누가 장난으로 쓴 걸 수도 있었다."
    "그런데 '분위기 흐리지는 말자'라는 말이 이상하게 마음에 걸렸다."
    n "(대체 누구한테 쓴 거지?)"

    scene cg_2 with dissolve
    "문득 어제 화장실에서 나온 하린이의 얼굴이 떠올랐다."
    "퉁퉁 부은 눈으로 아무 말도 하지 않던 모습."
    scene black with dissolve
    "급식실에서 치워주지 않던 자리."
    "아이들이 웃으며 돌려보던 사진."
    "그리고 지금 손에 들린 쪽지."
    "따로 볼 때는 별일 아닌 것처럼 보였던 일들이 하나씩 이어지기 시작했다."
    n "(설마… 이것도 하린이랑 관련 있는 건가?)"
    "아직 확실한 건 아무것도 없었다."
    "누가 쓴 건지도, 누구에게 쓴 건지도 알 수 없었다."
    "그래도 그냥 버리고 지나치기에는 마음에 걸렸다."
    scene bg_9 with dissolve
    n "(일단 선생님한테 보여드려 보자.)"

    "나는 구겨진 종이를 조심스럽게 접어 손에 쥐었다."
    "그리고 선생님을 찾으러 교실을 나섰다."

    scene bg_10 with fade
    "쉬는 시간, 교무실."

    play sound "audio/door_open.mp3"
    "문을 열고 들어가자 컴퓨터 앞에 앉아 계시던 선생님이 고개를 드셨다."
    stop sound

    scene bg_10_blur with fade
    show t4 at center_stage with dissolve
    t "어, 무슨 일 있니?"
    "막상 선생님 앞에 서니 어디서부터 말해야 할지 모르겠었다."
    "이 쪽지가 정말 하린이와 관련 있는 건지도 확실하지 않았다."
    "괜히 혼자 이상하게 생각한 거면 어쩌지 하는 생각도 들었다."
    "나는 손에 쥔 종이를 한 번 내려다봤다."
    n "저… 선생님."

    "입을 열면서도 목소리가 조금 작아졌다."

    menu:
        "확실한 것도 없는데 괜히 말했다가 이상해질 것 같다. 일단 모른 척하자.":
            n "아… 아니에요. 그냥 교무실 심부름 온 애들 따라왔어요."
            "나는 얼른 쪽지를 쥔 손을 등 뒤로 감췄다."

            hide t4 with dissolve
            show t1 at center_stage with dissolve
            t "그래? 곧 종 치니까 얼른 교실로 돌아가."
            hide t1 with dissolve

            scene bg_10 with dissolve
            "결국 쪽지 이야기는 꺼내지 못했다."
            "확실한 것도 없으니 이게 맞는 선택이라고 생각하려 했지만," 
            "교실로 돌아가는 내내 손에 쥔 종이가 계속 신경 쓰였다."

        "손에 쥔 쪽지를 보여주며, 지금까지 본 것들을 전부 말한다.":
            n "선생님, 하린이 자리 밑에서 이런 게 나왔어요." 
            n "그리고 어제 애들이 하린이 사진을 돌려보고… 급식실에서도 자리에 못 앉게 하고…."
            
            hide t4 with dissolve
            show t7 at center_stage with dissolve
            "선생님의 표정이 금세 진지해졌다." 
            "내가 내민 구겨진 쪽지를 받아 천천히 읽어보셨다." 
            t "이게 하린이 자리 근처에 있었다고?" 
            t "누가 쓴 건지는 봤니?" 
            n "아니요. 그건 못 봤어요." 
            n "근데 민재랑 예서네 애들이 계속 하린이한테 좀 이상하게 해서…." 
            "막상 설명하려니 말이 자꾸 꼬였다." 
            "어제부터 본 장면들이 머릿속에서 뒤섞여 제대로 순서도 잡히지 않았다."
            hide t7 with dissolve

            show t5 at center_stage with dissolve
            t "괜찮아. 천천히 말해도 돼." 
            t "선생님이 무슨 얘기인지 알겠어." 
            "선생님은 쪽지를 다시 한번 내려다보셨다." 
            t "이건 그냥 모른 척하고 넘기면 안 될 것 같다." 
            t "그렇다고 지금 바로 애들을 불러서 따지지는 않을 거야." 
            t "하린이가 더 불편해질 수도 있으니까." 
            t "선생님이 먼저 하린이한테 무슨 일이 있었는지 확인해볼게." 
            t "그리고 네가 본 것도 하나씩 다시 물어볼 테니까," 
            t "기억나는 대로만 말해주면 돼." 
            n "…네." 
            t "말해줘서 고마워. 이제부터는 선생님도 잘 살펴볼게."
            hide t5 with dissolve

        "쪽지를 숨긴 채, 반 분위기가 이상하다고만 돌려서 말한다.":
            n "저기… 요즘 하린이 주변 분위기가 좀 이상한 것 같아서요."
            "선생님이 키보드에서 손을 떼고 나를 바라보았다."

            hide t4 with dissolve
            show t7 at center_stage with dissolve
            t "어떤 점이 이상한 것 같아?"
            n "뭐라고 딱 말하기는 어려운데…." 
            n "애들이 하린이만 좀 빼놓는 것 같기도 하고, 눈치를 주는 것 같기도 해서요." 
            t "직접 들은 말이나 본 일이 있어?" 
            n "조금 있긴 한데… 저도 확실히는 모르겠어요."

            hide t7 with dissolve
            show t5 at center_stage with dissolve
            t "그래. 아직 정확히 모르겠어도 괜찮아." 
            t "선생님이 며칠 동안 좀 더 잘 살펴볼게." 
            t "혹시 또 이상하다고 느껴지는 일이 있으면 그때도 말해줘." 
            n "…네."
            hide t5 with dissolve

    jump r1_end

label r1_end:
    scene black with fade 
    pause 1.0
    scene bg_9 with fade
    "하지만 그날 이후로도 하린이의 자리는 계속 비어 있었다." 
    "선생님은 몇 번이나 빈 책상을 바라보셨고," 
    "반 아이들은 별일 없다는 듯 평소처럼 떠들고 웃었다." 
    "선생님도 하린이에게 연락해 보겠다고 하셨지만," 
    "학교에 나오지 않는 하린이에게 무슨 일이 있었는지 바로 확인하기는 어려워 보였다." 
    "며칠 동안 내가 본 일들이 계속 머릿속을 맴돌았다." 
    "급식실에서 비워주지 않던 자리." 
    "아이들이 돌려보던 사진." 
    "화장실에서 울고 나온 하린이." 
    "그리고 책상 밑에서 발견한 쪽지." 
    "처음에는 하나하나 별개의 일이라고 생각했다." 
    "하지만 이제는 그렇게만 보기 어려웠다." 
    "그리고 며칠 뒤,"

    scene black with dissolve
    "하린이가 결국 전학을 가게 되었다는 소식을 들었다."

    scene bg_3 with fade
    "그날 밤."
    play sound "audio/bed_sheets_moving.mp3"
    "침대에 누워 눈을 감아도 좀처럼 잠이 오지 않았다."

    "텅 빈 하린이의 자리와,"
    "화장실에서 마주쳤던 붉어진 눈이 자꾸 떠올랐다."

    n "(내가 본 건 분명 이상했어.)"
    n "(그런데 결국 하린이는 그대로 학교를 떠났어.)"

    "그럼 나는 왜 이때로 돌아온 걸까."

    n "(내가 뭘 놓친 거지…?)"

    "그 생각을 붙잡은 채 겨우 잠이 들려던 순간,"

    scene black with blink_black
    scene bg_3 with blink_black
    scene black with blink_black
    scene bg_3 with blink_black_long

    play sound "audio/heartbeat.mp3"
    "갑자기 심장이 세게 뛰기 시작했다."

    "그리고 어둠 속에서, 익숙한 목소리가 들렸다."

    scene black with fade
    pause 1.5

    scene cg_7 with fade
    h "이상하다고 느꼈잖아."
    pause 0.7
    h "정말… 그때 한 번뿐이었어?"

    stop sound fadeout 1.0
    scene black with dissolve
    "무슨 뜻인지 물을 틈도 없었다."

    "몸이 아래로 푹 꺼지는 듯한 감각과 함께,"
    "눈앞의 모든 것이 순식간에 어두워졌다."

    scene black with fade
    pause 1.5

    jump loop2_start
############################################################
## 2회차 — 구조를 읽는 눈
############################################################
label loop2_start:
    scene black with fade
    pause 1.0

    $ loop_no = 2

    # 2회차 교실 조사 변수 초기화
    $ inv_board = False
    $ inv_desk = False
    $ inv_back = False
    $ r2_class_inv_initialized = False
    $ f_minjae_talk_r2 = False
    $ key1_structure = False

    # 회귀 직후 연출
    scene bg_4_blur at wake_blur
    with white_flash

    pause 0.3

    n "헉!"

    with blink_black

    "익숙한 교실 소음이 한꺼번에 귓가로 밀려들었다."

    with blink_black

    scene bg_4 at wake_clear
    with blink_black_long # 마지막 길게 뜨기

    "나는 책상에서 황급히 몸을 일으켰다."
    
    n "하아... 하아..."
    
    "떨리는 숨을 겨우 고르며 칠판을 바라봤다."
    "< 5월 10일 월요일 >"
    
    n "…또 돌아왔어."

    "분명 두 번째인데도 쉽게 믿기지 않았다."
    "손끝에 힘이 들어가지 않았다."

    "그 순간, 마지막으로 들었던 하린이의 목소리가 떠올랐다."
    scene cg_7 with dissolve
    "『이상하다고 느꼈잖아. 정말… 그때 한 번뿐이었어?』"
    scene bg_4 with dissolve
    n "(한 번뿐이었냐고…?)"

    "지난 며칠 동안 내가 본 장면들이 머릿속을 빠르게 스쳐 갔다."

    "급식실의 자리."
    "아이들이 돌려보던 사진."
    "화장실에서 울고 나온 하린이."
    "책상 밑에 떨어져 있던 쪽지."

    "나는 그때마다 눈앞에서 벌어진 일만 보고 있었다."

    n "(그럼 내가 못 본 일이 더 있었다는 건가?)"

    "왜 이 시간으로 돌아오는지는 여전히 알 수 없었다."
    "하지만 한 가지는 분명해졌다."

    "지난번과 똑같이 움직여서는 아무것도 알아낼 수 없다."

    "나는 천천히 숨을 들이쉬고 주위를 둘러봤다."

    "교실 뒤쪽에서는 민재와 예서네 무리가 평소처럼 웃고 떠들고 있었다."

    n "(이번에는 조금 더 가까이서 봐야 해.)"
    n "(하린이한테 무슨 일이 있었는지… 내가 못 본 것부터 찾아보자.)"

    "나는 떨리던 손을 천천히 꽉 쥐었다."

    jump inv_loop_r2


label inv_loop_r2:

    if not r2_class_inv_initialized:
        $ inv_board = False
        $ inv_desk = False
        $ inv_back = False
        $ r2_class_inv_initialized = True

    if inv_board and inv_desk and inv_back and f_minjae_talk_r2:
        $ key1_structure = True

        n "(지난번엔 그냥 지나쳤던 것들이 이제야 보인다.)" 
        n "(공책에 남은 흔적도, 애들 반응도… 오늘 갑자기 생긴 건 아닌 것 같아.)" 
        n "(내가 못 본 일이 생각보다 훨씬 많았던 걸까.)" 
        n "(곧 수업 시작이네. 일단 자리로 돌아가자.)"

        jump r2_s1_korean

    hide screen quick_note_button
    call screen class_investigation
    show screen quick_note_button

    if _return == "board":
        scene bg_4 with fade    

        if not inv_board:
            $ inv_board = True
            "칠판 날짜. < 5월 10일 월요일 >"
            n "(정말 또 이날이야….)"
        else:
            "칠판은 이미 확인했다."

        jump inv_loop_r2

    elif _return == "desk":
        scene bg_4 with fade

        if not inv_desk:
            $ inv_desk = True
            "하린이 책상 위에 펼쳐진 공책을 자세히 들여다봤다."
            "연필로 여러 번 세게 눌러 그은 자국 때문에 종이가 군데군데 패여 있었다."

        else:
            "하린의 자리는 이미 확인했다."

        jump inv_loop_r2

    elif _return == "back":
        scene bg_4 with fade

        if not inv_back:
            $ inv_back = True
            "교실 뒤쪽에서는 민재와 예서네 무리가 휴대폰을 보며 웃고 있었다." 
            "떠드는 소리 사이로 하린이 이름이 잠깐 들렸다." 
            n "(지난번에도 저랬지.)" 
            "그때는 대수롭지 않게 넘겼던 웃음소리가 이번에는 다르게 들렸다."
        else:  
            "아이들은 이미 확인했다."
            
        jump inv_loop_r2

    elif _return == "minjae_r2":
        if not f_minjae_talk_r2:
            $ f_minjae_talk_r2 = True

            scene bg_4 with fade
            "무리에서 살짝 떨어져 있는 민재에게 다가갔다."

            n "민재야, 아까 너네 하린이 보면서 웃던데." 
            n "무슨 일 있었어?"

            scene bg_4_blur with dissolve
            show m4 at center_stage with dissolve

            m "어? 아니." 
            m "그냥 애들이랑 얘기하다 웃은 건데?" 
            "민재가 대수롭지 않다는 듯 어깨를 으쓱했다." 
            m "왜? 갑자기 오하린한테 관심 생겼어?"

            hide m4 with dissolve
            scene bg_4 with dissolve
            n "그런 건 아니고." 
            n "하린이가 별로 안 좋아 보이길래 물어본 거야."

            scene bg_4_blur with dissolve
            show m1 at center_stage with dissolve

            m "걔 원래 말도 없고 맨날 저러잖아." 
            m "별거 아니니까 신경 쓰지 마." 
            n "그래? 별거 아니면 됐어." 
            "나는 잠깐 민재를 바라보다가 덧붙였다." 
            n "근데 계속 하린이 얘기하면서 웃으면," 
            n "다른 애들이 보기엔 일부러 그러는 것처럼 보일 수도 있겠다." 
            "민재의 표정이 잠깐 굳었다." 
            m "뭘 일부러 해. 아니라니까." 
            n "알았어. 그냥 그렇다고." 
            "민재는 더 대꾸하지 않고 슬쩍 뒤쪽 무리를 돌아봤다."

            hide m1 with dissolve
            scene bg_4 with dissolve
            
            $ trust_minjae += 1
            n "(적어도 이제는 내가 보고 있다는 걸 알겠지.)"
        else:
            scene bg_4 with fade
            "조금 전 민재에게 물어봤다." 
            "지금 다시 다가가면 오히려 더 경계할 것 같다."

        jump inv_loop_r2

    elif _return == "finish":
        if inv_board or inv_desk or inv_back:
            n "(따로 볼 땐 별일 아닌 것 같았는데….)"
            
            if inv_board and inv_desk and inv_back:
                $ key1_structure = True
                n "(이렇게 놓고 보니까, 뭔가 계속 이어져 있었던 것 같아.)"
                n "(이번엔 그냥 지나치면 안 되겠어.)"
        
        n "(곧 수업 시작이네. 일단 자리로 돌아가자.)"
        jump r2_s1_korean

    else:
        jump inv_loop_r2

# ==========================================================
# R2-S1-2. 2회차 국어 시간 — 익숙한 소외
# ==========================================================
label r2_s1_korean:
    $ note_role = True

    scene black with fade
    pause 0.8

    scene bg_11 with fade

    "2교시 국어 시간." 
    "선생님이 칠판에 '인물 분석 발표'라고 적으셨다."

    scene bg_11_blur with dissolve
    show t9 at center_stage with dissolve

    t "저번 시간에 정한 모둠대로 모여 앉아." 
    t "이번 발표는 모둠원 모두가 참여해야 해."

    hide t9 with dissolve
    scene bg_11 with dissolve

    "교실 여기저기에서 책상과 의자 끄는 소리가 났다." 
    "나도 우리 모둠 애들과 자리를 붙였지만," 
    "대각선 앞쪽에 앉은 아이들이 자꾸 신경 쓰였다." 
    "하린이, 민재, 소윤이, 예서." 
    "민재는 자리에 앉자마자 역할부터 나누기 시작했다."

    # 민재: 역할 분담 시작
    scene bg_11_blur with dissolve
    show m2 at left_stage with dissolve

    m "예서가 발표하고, 소윤이가 자료 조사해." 
    m "나는 대본 짤게."

    show s2 at right_stage with dissolve
    s "어? 그럼 하린이는...?"

    "민재는 잠깐 생각하는가 싶더니 대수롭지 않게 말했다." 
    m "오하린은 자료 정리해서 보내라고 하면 되잖아." 
    m "어차피 발표 같은 거 잘 안 하잖아."

    hide m2
    hide s2
    with dissolve

    show h3 at center_stage with dissolve

    "하린이는 입을 열지 않았다." 
    "책상 아래에서 손가락만 꼼지락거리고 있었다." 
    "선생님은 분명 모두 참여하라고 했는데," 
    "나는 우리 모둠 활동지를 앞에 두고도 자꾸 그쪽이 신경 쓰였다."

    menu:
        "민재의 말에 직접 끼어든다. \"하린이 의견도 들어봐야 하는 거 아냐?\"":
            $ trust_harin += 1
            $ trust_minjae -= 1

            hide h3 with dissolve
            scene bg_11 with dissolve

            n "근데 하린이한테도 한번 물어봐야 하는 거 아냐?" 
            "내 말에 민재가 고개를 돌렸다."

            scene bg_11_blur with dissolve
            show m10 at left_stage with dissolve
            m "아, 넌 네 모둠이나 신경 써. 하린아, 너도 이게 편하지?"
            
            show h16 at right_stage with dissolve
            "갑자기 모두의 시선이 하린이에게 향했다." 
            "하린이는 잠깐 머뭇거리다가 작게 고개를 끄덕였다." 
            h "…응. 난 괜찮아."
            hide m10
            hide h16 
            with dissolve
            scene bg_11 with dissolve

            "민재는 봤냐는 듯 다시 자기 모둠으로 고개를 돌렸다." 
            "하린이도 더는 아무 말 없이 활동지만 내려다봤다." 
            n "(괜히 내가 끼어들어서 하린이를 더 곤란하게 만든 건가….)"

        "소윤이에게 말을 건다. \"소윤아, 너희는 역할 분담 다 끝났어?\"":
            $ trust_soyun += 1

            hide h3 with dissolve
            scene bg_11 with dissolve
            "나는 소윤이 쪽으로 몸을 살짝 기울였다."

            n "소윤아, 너희는 역할 분담 다 끝났어?"

            scene bg_11_blur with dissolve
            show s8 at center_stage with dissolve
            s "어? 아… 응." 
            s "민재가 일단 이렇게 하자고 해서." 
            n "근데 하린이는 자료 정리만 하는 거야?" 
            n "선생님이 다 같이 참여해야 한다고 했잖아." 
            "소윤이는 대답하지 않고 하린이 쪽을 한번 바라봤다." 
            "그러고는 민재 눈치를 슬쩍 살폈다."
            hide s8 with dissolve
            show s3 at center_stage with dissolve
            s "…그러게." 
            s "근데 이미 다 정했으니까…." 
            "소윤이는 말끝을 흐리며 활동지 모서리만 만지작거렸다."
            hide s3 with dissolve
            scene bg_11 with dissolve

            n "(소윤이도 선뜻 괜찮다고 하지는 못하네.)"

        "우리 모둠 일이나 하자. 일단은 지켜보는 수밖에 없어.":
            $ key1_structure = True

            hide h3 with dissolve
            scene bg_11 with dissolve

            "나는 애써 시선을 돌리고 우리 모둠 활동지를 펼쳤다." 
            "옆 모둠에서는 민재와 예서가 계속 이야기를 나누고 있었고," 
            "하린이는 말없이 자기 앞의 종이만 내려다보고 있었다." 
            n "(선생님은 다 같이 참여하라고 했는데….)" 
            "자꾸 신경 쓰였지만, 결국 나는 아무 말도 하지 않았다." 
            n "(조금 더 지켜보자. 아직 내가 모르는 게 있을지도 몰라.)"
    # 공통 마무리
    scene black with fade
    "결국 하린이 모둠의 역할 분담은 처음 정한 그대로 끝났다."

    "하린이는 별다른 말 없이 자기 몫의 활동지만 내려다보고 있었다."

    "수업이 끝날 때까지 그 모습이 계속 마음에 남았다."
    jump r2_s2_lunch

# # ----------------------------------------------------------
# R2-S2. 2회차 점심시간 — 억지로 뭉친 아이들
# ----------------------------------------------------------
label r2_s2_lunch:
    scene black with fade

    play sound "audio/bell.mp3"
       
    scene bg_5 with dissolve
    "오전 수업이 끝나는 종이 울렸다."
    stop sound fadeout 1.0
    "처음 이 날을 겪었을 때는 아무 생각 없이 애들 틈에 껴서 급식실로 갔었다."
    "하지만 이번엔 달랐다." 
    "이번에는 식판을 받자마자 민재네 무리부터 찾았다."
    
    scene bg_6 with dissolve
    "대각선 앞쪽의 6인용 테이블." 
    "민재와 예서, 준호, 소윤이가 모여 앉아 있었다." 
    "그리고 지난번과 똑같이, 남은 한 자리에는 예서의 겉옷과 가방이 놓여 있었다."
    n "(역시 똑같아.)"

    scene bg_5_blur with dissolve
    show h3 at center_stage with dissolve
    "잠시 뒤 하린이가 식판을 들고 다가왔다." 
    "번호대로라면 하린이가 앉아야 하는 자리였다." 
    "하린이가 테이블 앞에 멈춰 서자," 
    "조금 전까지 웃고 떠들던 아이들의 목소리가 잠깐 잦아들었다." 
    "하지만 누구도 의자 위의 짐을 치우지는 않았다." 
    "하린이는 잠시 기다리다가 결국 아무 말 없이 돌아섰다."

    hide h3 with dissolve
    scene bg_6 with dissolve
    "지난번에도 분명 봤던 장면이었다." 
    "그때는 그냥 분위기가 이상하다고만 생각했다." 
    n "(하린이가 자기 자리에 왔는데도 아무도 비켜주지 않았어.)" 
    n "(그리고 하린이도 아무 말 없이 그냥 가버렸고….)" 
    "한 번 알고 나니 전에는 지나쳤던 것까지 눈에 들어왔다." 
    "주변에 앉은 아이들도 잠깐 그쪽을 봤지만," 
    "금세 아무 일도 없었다는 듯 다시 밥을 먹기 시작했다." 
    "내 시선이 테이블 끝에 앉은 소윤이에게 향했다."
    scene bg_6_blur with dissolve
    show s8 at center_stage with dissolve
    "소윤이는 밥을 먹다 말고 멀어지는 하린이를 바라보고 있었다." 
    "그러다 민재 쪽을 한번 살피고는 다시 고개를 숙였다." 
    n "(소윤이는 계속 하린이 쪽을 신경 쓰고 있어.)"
    

    hide s8 with dissolve
    scene bg_6 with dissolve    
    "나는 식판을 든 채 잠시 그 자리에 서 있었다."
    "이번엔 어떻게 해야 할까?"

    menu:
        "나서봤자 피곤해지기만 할 것 같아. 조용히 내 밥이나 먹자.":
            scene bg_6_blur with dissolve
            "나는 결국 시선을 거두고 내 자리에 앉았다." 
            "멀리 떨어진 자리에서 하린이가 혼자 밥을 먹는 모습이 보였다." 
            "괜히 끼어들었다가 일만 커질 수도 있다고 생각했다." 
            "그런데 아까 본 장면이 자꾸 떠올라 밥에 좀처럼 집중할 수 없었다." 
            n "(알면서도 그냥 모른 척한 거잖아….)"
            jump r2_s2_pe

        "다들 너무하잖아. 당장 옷부터 치우라고 따져야겠어.":
            scene bg_6_blur with dissolve
            n "야, 옷 좀 치워! 하린이가 못 앉잖아!"
            "내 목소리가 커지자 근처에 앉아 있던 아이들이 하나둘 이쪽을 쳐다봤다."

            show m10 at center_stage with dissolve
            m "아, 깜짝이야." 
            "민재는 짜증 섞인 얼굴로 의자 위의 짐을 치웠다." 
            m "야, 오하린! 앉을 거면 말을 하지 그랬어."
            hide m10 with dissolve
            "민재가 신경질적으로 겉옷을 낚아채며, 멀어지던 하린이 쪽을 홱 노려보았다."
            show h4 at center_stage with dissolve
            "갑자기 이름이 불린 하린이가 걸음을 멈췄다." 
            "주변의 시선이 자신에게 향하자 하린이는 금세 고개를 숙였다." 
            n "하린아, 자리 비었어." 
            "하린이는 잠깐 망설이다가 작게 고개를 저었다." 
            h "…괜찮아."

            hide h4 with dissolve
            "하린이는 결국 돌아오지 않고 멀리 떨어진 테이블에 자리를 잡았다." 
            "자리는 비워졌는데도, 어쩐지 일이 더 어색해진 것 같았다." 
            n "(내가 너무 크게 말했나….)"
            jump r2_s2_pe

        "소윤이도 볼 수 있게, 하린이 옆으로 가서 앉자.":
            $ trust_soyun += 1
            "나는 식판을 들고 하린이가 있는 구석 자리로 성큼성큼 걸어갔다."
            n "하린아, 나 여기 앉아도 돼?"
            scene bg_6_blur with dissolve
            show h16 at center_stage with dissolve
            "하린이는 갑자기 말을 건 내가 낯선 듯 잠시 나를 바라봤다." 
            h "…왜?" 
            n "그냥. 나도 여기서 먹으려고." 
            "하린이는 잠깐 망설이다가 작게 고개를 끄덕였다."
            hide h16 with dissolve
            show h5 at center_stage with dissolve
            h "…응." 
            "나는 하린이 맞은편에 식판을 내려놓았다." 
            "자리에 앉으며 슬쩍 6인용 테이블 쪽을 바라봤다."
            hide h5 with dissolve
            show s2 at center_stage with dissolve
            "소윤이는 밥을 먹다 말고 이쪽을 바라보고 있었다." 
            "나와 눈이 마주치자 잠시 멈칫하더니, 곧 시선을 내렸다."
            hide s2 with dissolve
            scene bg_6 with dissolve
    
            jump r2_s2_pe

# ----------------------------------------------------------
# R2-S2. 2회차 오후 — 운동장의 그림자
# ----------------------------------------------------------
label r2_s2_pe:
    scene black with dissolve
    pause 0.5
    scene pe with fade

    "5교시 체육 시간." 
    "아이들은 신이 나서 운동장으로 뛰어나갔지만," 
    "나는 점심시간에 본 일이 계속 마음에 걸렸다." 
    "선생님이 호루라기를 불며 아이들을 모았다."
    scene pe_blur with fade
    show pt1 at center_stage with dissolve
    pt "자, 오늘은 2인 1조로 배드민턴 연습한다." 
    pt "각자 짝 정해서 줄 서!"

    hide pt1 with dissolve
    scene pe with dissolve
    "말이 끝나자마자 아이들이 익숙한 친구들끼리 모이기 시작했다." 
    "민재와 준호가 하이파이브를 하며 붙었고," 
    "예서와 소윤이도 자연스럽게 나란히 섰다."

    scene pe_blur with dissolve
    show h5 at center_stage with dissolve
    "하린이는 한동안 그 자리에 서 있었다." 
    "누구에게 먼저 말을 걸지도 못한 채 주변만 슬쩍 살피다가," 
    "조금씩 아이들 무리에서 멀어졌다."
    
    hide h5 with dissolve
    scene pe with dissolve
    n "(지난번에는 내 짝 찾느라 저걸 못 봤구나.)" 
    "기억을 더듬자 뒤늦게 생각났다." 
    n "(결국 짝이 안 남아서 선생님이랑 했었지.)" 
    "친구들이 내 이름을 부르는 소리가 들렸지만," 
    "나는 그대로 하린이 쪽으로 걸어갔다." 
    n "하린아, 나랑 짝 할래?"

    scene pe_blur with dissolve
    show h4 at center_stage with dissolve
    "하린이는 바로 대답하지 않았다." 
    "먼저 예서네 쪽을 한번 바라본 뒤에야 나를 봤다." 
    h "…어?" 
    h "응. 그래."
    hide h4 with dissolve
    scene pe with dissolve

    "다른 코트에서 날아온 셔틀콕 하나가 우리 쪽으로 굴러왔다."

    "하린이가 허리를 숙여 셔틀콕을 집었다."

    "민재 쪽으로 돌려주려고 손을 내밀자,"
    "민재는 손으로 받는 대신 라켓 끝으로 셔틀콕을 툭 쳐서 가져갔다."

    "그러고는 손이 닿기라도 한 것처럼 바지에 손바닥을 몇 번 문질렀다."

    "민재가 뒤를 돌아보자 예서가 입을 가리고 웃었고,"
    "옆에 있던 아이들도 서로 눈을 마주치며 킥킥거렸다."

    "하린이는 잠시 그대로 서 있다가 천천히 손을 내렸다."
    n "(…저런 것도 장난이라고 할 수 있는 건가.)" 
    "직접 욕을 한 것도, 밀친 것도 아니었다." 
    "그래서 멀리서 보면 아무 일도 아닌 것처럼 보일지도 몰랐다." 
    n "(내가 옆에 있다고 끝나는 문제가 아니야.)" 
    n "(내가 못 보고 지나친 일이 얼마나 더 있었던 거지…?)"
    scene black with fade
    jump r2_s2_pe_investigation

############################################################
## R2-S2-PE-INV. 2회차 체육 조사 진입
############################################################
label r2_s2_pe_investigation:
    scene bg_12 with fade

    "잠시 뒤 자유 연습 시간이 시작되었다." 
    "아이들은 금세 여기저기로 흩어졌다." 
    "배드민턴을 계속 치는 애도 있었고, 벤치 근처에 모여 떠드는 애들도 있었다." 
    "아까보다 서로에게 신경 쓰는 사람도 훨씬 적어졌다." 
    n "(지금이면 좀 더 자연스럽게 둘러볼 수 있겠다.)" 
    "나는 라켓을 든 채 천천히 주변을 살폈다." 
    n "(이번엔 눈앞에 보이는 것만 보고 끝내지 말자.)"

    $ inv_pe_bottle = False
    $ inv_pe_bench = False
    $ talk_pe_minjae = False
    $ talk_pe_soyun = False
    $ talk_pe_harin = False
    $ talk_pe_yeseo = False

    jump pe_investigation_loop



############################################################
## R2-S2-PE-INV. 2회차 체육 조사 루프
############################################################
label pe_investigation_loop:

    if inv_pe_bench and talk_pe_yeseo and talk_pe_harin and talk_pe_minjae and talk_pe_soyun:
        jump pe_investigation_finish

    call screen pe_investigation_screen

    if _return == "bench":
        scene bg_12 with fade

        if not inv_pe_bench:
            $ inv_pe_bench = True
            "벤치 옆 모래바닥에 삐뚤빼뚤한 글씨가 눈에 들어왔다." 
            "『오하린 냄새남』" 
            "『투명인간』" 
            "발자국에 지워지지도 않은 채 글씨가 또렷하게 남아 있었다." 
            n "(이런 것까지 있었어…?)" 
            "하린이가 바로 근처에 있는데도 누군가는 이런 말을 아무렇지도 않게 써놓은 모양이었다."
        else:
            "모래바닥의 낙서는 아직 그대로 남아 있었다." 
            "아이들이 몇 번이나 그 주변을 오갔지만," 
            "누구도 별다른 반응을 보이지 않았다."

        jump pe_investigation_loop


    elif _return == "yeseo":
        scene bg_12 with fade

        $ talk_pe_yeseo = True

        "예서는 민재와 몇몇 아이들 사이에 섞여 있었다." 
        "직접 하린이에게 말을 걸거나 장난을 치는 모습은 없었다." 
        "하지만 민재가 하린이 쪽을 보며 웃을 때마다 같이 웃었고," 
        "가끔 하린이를 힐끗 보고는 아무렇지 않게 다시 대화에 끼어들었다." 
        n "(직접 나서지는 않아도, 계속 같이 웃고 있네.)"

        jump pe_investigation_loop


    elif _return == "harin":

        if not talk_pe_harin:
            $ talk_pe_harin = True
            $ f_r2_harin_connect = True

            scene bg_12 with fade
            "하린이는 라켓을 든 채 코트 한쪽에 서 있었다." 
            "내가 다가가자 먼저 내 표정을 살피듯 쳐다봤다." 
            n "하린아, 잠깐 쉴래?" 
            n "물 마시고 와도 되고."

            scene bg_12_blur with dissolve
            show h16 at center_stage with dissolve

            h "아니야… 괜찮아." 
            "하린이는 잠시 머뭇거리다가 운동장 반대편을 바라봤다." 
            h "근데 너… 친구들이 아까 부르던데." 
            h "나 때문에 여기 계속 있을 필요 없어." 
            n "괜찮아. 내가 여기 있고 싶어서 있는 거야." 
            "하린이는 대답하지 않고 라켓 손잡이만 만지작거렸다." 
            h "…그래."

            hide h16 with dissolve
            scene bg_12 with dissolve

            $ trust_harin += 1

            "하린이는 잠시 말이 없었다."
            "그러다 라켓 손잡이를 꽉 감싸고 있던 손가락을 천천히 폈다."

        else:
            scene bg_12 with fade
            "하린이는 조금 진정된 표정으로 라켓을 만지작거리고 있다."
            "아까보다는 긴장이 조금 풀린 것 같았다." 
            "그래도 지금은 더 말을 걸지 않는 편이 나을 것 같다."

        jump pe_investigation_loop


    elif _return == "minjae":

        if not talk_pe_minjae:
            $ talk_pe_minjae = True

            scene bg_12 with fade

            "친구들과 낄낄거리던 민재에게 슬쩍 다가갔다."
            n "민재야, 아까 하린이한테 셔틀콕 받을 때 왜 그랬어?"

            if f_minjae_talk_r2:
                scene bg_12_blur with dissolve
                show m1 at center_stage with dissolve

                m "뭘 왜 그래." 
                n "하린이가 손으로 주려고 했잖아." 
                n "근데 굳이 라켓으로 가져갔잖아." 
                "민재는 대답하기 전에 잠깐 나를 빤히 쳐다봤다." 
                m "그냥 빨리 받으려고 그런 거라니까." 
                n "아침에도 그렇고, 계속 하린이한테 그러니까 물어보는 거야." 
                "민재의 표정이 굳었다." 
                m "너 아까부터 왜 자꾸 나만 보고 있어?" 
                n "나만 보는 게 아니라, 눈에 보이니까." 
                "민재는 입을 열었다가 다시 다물었다." 
                "그러고는 주변에 있던 아이들을 한번 훑어봤다." 
                m "…진짜 별거 아니야." 
                "민재는 더 말하지 않고 친구들 쪽으로 돌아갔다." 
                "그러면서도 내 쪽을 한 번 더 확인하듯 흘끗 바라봤다."

                hide m1 with dissolve
                scene bg_12 with dissolve

                n "(이제는 내가 보고 있다는 걸 의식하는 것 같아.)"

                $ key4_minjae_pattern = True

                "민재는 고개를 숙인 채 한동안 아무 말도 하지 않았다."

            else:
                scene bg_12_blur with dissolve
                show m7 at center_stage with dissolve

                m "아, 뭐래." 
                m "그냥 빨리 받으려고 그런 거지." 
                n "근데 하린이가 손으로 주려고 하고 있었잖아." 
                n "굳이 라켓으로 가져갈 필요는 없었잖아." 
                "민재는 잠깐 나를 쳐다보더니 피식 웃었다." 
                m "그게 뭐가 문제야?" 
                m "네가 셔틀콕 받는 방법 정하게?" 
                n "그런 뜻이 아니라, 좀 이상해 보여서 물어본 거야." 
                m "뭐가 이상해." 
                m "너 오늘 왜 이렇게 별걸 다 신경 쓰냐?" 
                "민재는 대수롭지 않다는 듯 라켓을 어깨에 걸쳤다." 
                m "됐어. 연습이나 해." 

                hide m7 with dissolve
                scene bg_12 with dissolve

                "민재는 그대로 친구들 쪽으로 돌아갔다." 
                "금세 다시 웃고 떠드는 걸 보면 크게 신경 쓰는 것 같지는 않았다." 
                "다만 잠시 뒤,"
                "내가 아직 보고 있는지 확인하듯 이쪽을 한 번 흘끗 봤다." 
                n "(조금은 의식하게 된 건가….)"

            $ trust_minjae += 1

        else:
            scene bg_12 with fade
            "민재는 친구들과 계속 떠들고 있었다."

            "그러면서도 가끔 내가 있는 쪽을 슬쩍 확인했다."

            "지금 다시 말을 걸어도 더 들을 수 있는 건 없을 것 같다."

        jump pe_investigation_loop


    elif _return == "soyun":

        if not talk_pe_soyun:
            $ talk_pe_soyun = True

            scene bg_12 with fade

            "예서 옆에 있던 소윤이와 눈이 마주쳤다." 
            "소윤이는 잠깐 멈칫하더니 먼저 시선을 피했다." 
            n "소윤아, 너도 아까 봤지?" 
            n "민재가 하린이한테 한 거."

            scene bg_12_blur with dissolve
            show s3 at center_stage with dissolve
            s "…응. 봤어." 
            n "너는 그거 어떻게 생각해?" 
            "소윤이는 바로 대답하지 않고 라켓 끝으로 바닥만 툭툭 건드렸다." 
            s "글쎄…." 
            s "민재가 원래 장난을 좀 심하게 치잖아." 
            n "그래도 하린이는 하나도 안 웃던데." 
            "소윤이는 잠깐 하린이 쪽을 바라봤다." 
            s "…응."
            "짧게 대답한 뒤 한동안 아무 말도 하지 않았다." 
            n "소윤아?" 
            s "나도 잘 모르겠어." 
            "소윤이는 애매하게 말을 끝내고 다시 예서 쪽으로 돌아갔다."

            hide s3 with dissolve
            scene bg_12 with dissolve
            n "(아무렇지 않은 건 아닌 것 같은데… 왜 말을 안 하는 거지?)"

            $ trust_soyun += 1

        else:
            scene bg_12 with fade
            "소윤이는 예서 옆에 있으면서도 가끔 하린이 쪽을 바라보고 있었다." 
            "아까보다 더 물어봐도 지금은 제대로 대답하지 않을 것 같다."

        jump pe_investigation_loop


    elif _return == "finish":
        jump pe_investigation_finish


    else:
        jump pe_investigation_loop


label pe_investigation_finish:

    scene bg_12 with fade

    if inv_pe_bench and talk_pe_minjae and talk_pe_soyun:
        n "(급식실에서도 그랬고, 아까 셔틀콕 때도 그랬어.)" 
        n "(하린이한테 저러는 게 오늘 처음은 아닌 것 같아.)" 
        n "(아직 내가 못 본 게 더 있을지도 몰라.)"
        n "(오늘 본 건 잘 기억해두자.)"
    else:
        n "(조금 더 보긴 했는데, 아직은 잘 모르겠어.)"
        n "(그래도 지난번엔 못 봤던 것들이 보이기 시작했어.)"
        "오늘 본 것들은 잊지 않게 기억해두기로 했다."

    jump r2_s3_home
# ----------------------------------------------------------
# R2-S3. 2회차 방과 후 — 보이지 않는 교실 (단톡방)
# ----------------------------------------------------------
label r2_s3_home:
    scene black with fade
    scene bg_3 with fade

    $ chat_scroll_depth = 0
    $ f_r2_chat_checked = False

    play sound "audio/bed_sheets_moving.mp3"
    "학교가 끝나고 집에 돌아왔다." 
    "침대에 누웠는데도 오늘 본 장면들이 하나씩 떠올랐다." 
    "하린이의 자리를 막고 있던 짐." 
    "모둠에서 혼자 빠진 역할." 
    "셔틀콕을 건네던 하린이의 손을 피하던 민재."
    stop sound
    n "(학교에 있는 동안만 해도 이 정도인데….)" 
    
    play sound "audio/cellphone.mp3"
    "징."
    stop sound
    "그때 책상 위에 놓아둔 휴대폰이 짧게 울렸다." 
    "별생각 없이 화면을 확인했다." 
    "평소에는 알림을 꺼두고 거의 들어가지 않던" 
    "'6학년 3반 단톡방'에 새 메시지가 여러 개 쌓여 있었다." 
    n "(단톡방….)" 
    "그러고 보니 지난번에는 여기를 제대로 확인해볼 생각조차 하지 않았다." 
    "나는 몸을 일으켜 휴대폰을 집어 들었다." 
    n "(혹시 여기에도 뭔가 있는 건가?)" 
    "단톡방을 열었다."
    $ quick_menu = False
    call screen class_chat
    $ quick_menu = True

    if f_r2_chat_checked:
        $ note_chat = True
        "마지막 메시지까지 확인하고도 한동안 화면을 그대로 보고 있었다." 
        n "(하린이가 대답도 안 하는데… 계속 불렀어.)" 
        "한 명이 하린이를 태그하면 또 다른 애가 말을 얹고," 
        "대답이 없으면 그것까지 웃음거리로 이어졌다." 
        "하린이가 아무 반응을 하지 않아도 멈추지 않았다." 
        n "(싫다고 말하지 않아도, 아무 말도 안 해도 계속한 거잖아.)" 
        "낮에 봤던 하린이의 모습이 떠올랐다." 
        "급식실에서도 하린이는 그냥 자리를 떠났고," 
        "체육 시간에도 아무 말 없이 물러났다." 
        n "(그때도 그냥 가만히 있었던 게 아니었을지도 몰라.)" 
        "단톡방까지 보고 나니," 
        "하린이가 왜 계속 아무 말도 하지 않았는지 전보다 더 신경 쓰였다." 

    else:
        "몇 개의 메시지만 보고도 손가락이 멈췄다." 
        "하린이를 계속 부르는 메시지와 그 뒤에 붙는 반응들이 마음에 걸렸다." 
        n "(왜 하린이한테 계속 이러는 거지….)" 
        "더 위로 올리면 무슨 일이 있었는지 알 수 있을 것 같았다." 
        "하지만 선뜻 다음 메시지를 열어보지 못했다." 
        n "(이대로 닫으면 또 놓치는 게 생기는 거 아닐까….)"

    menu:
        "소윤이에게 개인톡을 보낸다.":
            $ f_r2_chat_with_soyoon = True
            $ trust_soyun += 1

            "한참 화면만 내려다보다가, 결국 메시지 앱을 열었다."
            "대화 목록 속 소윤의 프로필이 눈에 들어왔다."

            $ quick_menu = False
            call screen messenger_contact_select
            $ quick_menu = True

            if _return == "soyun":
                $ quick_menu = False
                call screen soyoon_dm_chat
                $ quick_menu = True

            "답장은 짧았지만, 평소에는 하지 않던 이야기까지 적혀 있었다." 
            "낮에 몇 번이나 말을 망설이던 소윤이의 모습이 떠올랐다."

            scene black with fade
            pause 1.0

            scene bg_13 with dissolve
            s "..."
            s "처음엔 다들 그러길래 나도 그냥 있었어."
            s "근데 어느 순간부터 너무 심해진 것 같더라고."
            s "그때 뭐라고 하려고 했는데... 이미 너무 늦은 것 같아서."
            s "지금 와서 내가 뭐라고 해봤자 아무것도 안 바뀔 것 같고..."

            scene black with dissolve
            "한동안 아무 말도 할 수 없었다." 
            n "(소윤이도 계속 아무렇지 않았던 건 아니었어.)" 
            "잘못됐다고 느낀 뒤에도," 
            "이미 늦었다고 생각해서 그대로 멈춰 있었던 거였다." 
            n "(근데 정말 늦은 걸까?)" 
            "오늘 단톡방에서 본 메시지들과 낮에 있었던 일들이 다시 떠올랐다." 
            n "(아직 하린이는 여기 있어.)" 
            n "(그럼 아직 할 수 있는 게 있는 거 아닐까?)"

            scene bg_3 with fade
            n "(내일은 소윤이한테도, 하린이한테도 다시 제대로 물어봐야겠어.)"

        "휴대폰을 끄고 내일 직접 확인해 본다.":
            "휴대폰 화면을 껐다." 
            "하지만 방금 본 메시지들이 쉽게 머릿속에서 사라지지 않았다." 
            n "(내가 모르는 일이 아직 더 있는 것 같아.)" 
            "오늘 학교에서 본 것만으로 끝내면 안 될 것 같았다." 
            n "(내일 다시 확인해보자.)"

    jump r2_s4_bathroom


# ----------------------------------------------------------
# R2-S4. 2회차 다음 날 아침 — 화장실 앞 복도
# ----------------------------------------------------------
label r2_s4_bathroom:
    $ note_bathroom = True
    scene black with fade
    pause 0.8
    scene bg_4 with fade
    "다음 날 아침."

    "교실에 들어서자 가장 먼저 하린이 자리를 확인했다."

    "하린이는 와 있었다."

    n "(오늘은 왔어.)"

    "지난번과 같다면 하린이는 내일부터 학교에 나오지 않는다."

    n "(그러면 오늘이 직접 물어볼 수 있는 마지막 날일 수도 있어.)"

    "나는 가방을 내려놓고 자리에 앉았다."

    "수업이 시작됐지만 자꾸 하린이 쪽에 신경이 갔다."

    "어제 학교에서 본 일들."
    "그리고 밤에 확인한 단톡방까지."

    n "(이번에는 화장실 앞에서 그냥 보내면 안 돼.)"
    play sound "audio/bell.mp3"
    "쉬는 시간 종이 울리자 자리에서 일어났다."
    stop sound fadeout 1.0
    scene bg_8 with fade
    "화장실 앞 복도로 가자,"
    "잠시 뒤 문이 열리고 소윤이가 먼저 나왔다."
    
    if f_r2_chat_with_soyoon:

        scene bg_8_blur with dissolve
        show s6 at left_stage with dissolve

        "소윤이는 나를 발견하고 걸음을 잠깐 멈췄다."

        "어젯밤 나눈 이야기가 떠오른 듯 서로 잠시 눈이 마주쳤다."

        "소윤이는 아무 말 없이 옆으로 비켜섰다."

    else:

        scene bg_8_blur with dissolve
        show s6 at left_stage with dissolve

        "소윤이는 나를 보자 잠깐 멈칫했다."

        "그러다 별말 없이 시선을 돌리고 지나가려 했다."

    show h10 at right_stage with dissolve

    "그 뒤에서 하린이가 천천히 걸어 나왔다."

    "눈가가 붉어져 있었다."

    "순간 지난번 이 시간이 그대로 떠올랐다."

    n "(맞아. 이때였어.)"

    "지난번에도 하린이는 이렇게 화장실에서 나왔고,"
    "나는 무슨 일이 있었는지 제대로 알아내지 못했다."

    hide s6 with dissolve

    if f_r2_chat_with_soyoon:

        "어젯밤 소윤이가 했던 말이 떠올랐다."

        s "그때 뭐라고 하려고 했는데... 이미 너무 늦은 것 같아서."

        n "(소윤이도 알고 있었어.)"
        n "(그럼 이번에는 그냥 지나가게 두면 안 돼.)"

    else:

        "어젯밤 단톡방에서 봤던 메시지들이 떠올랐다."

        n "(학교에서 내가 본 것 말고도 계속 있었잖아.)"
        n "(여기서도 뭔가 있었던 걸까?)"

    hide h10 with dissolve

    scene bg_8 with dissolve

    "하린이는 복도 한쪽으로,"
    "소윤이는 반대쪽으로 걸어가기 시작했다."

    n "(지금 어떻게 해야 하지?)"

    menu:

        "서둘러 지나가려는 소윤이를 붙잡고 묻는다.":

            $ f_r2_bath_soyoon_talk = True

            n "소윤아, 잠깐만."

            "나는 교실 쪽으로 가려는 소윤이를 급히 불러 세웠다."

            scene bg_8_blur with dissolve
            show s6 at center_stage with dissolve

            "소윤이는 놀란 얼굴로 나를 돌아봤다."

            n "방금 하린이랑 같이 있었지?"
            n "무슨 일 있었어?"

            if f_r2_chat_with_soyoon:

                "소윤이는 잠시 대답을 망설였다."

                n "어제 네가 한 말 때문에 묻는 거야."
                n "하린이 눈도 빨갛잖아."

                hide s6 with dissolve
                show s3 at center_stage with dissolve

                s "…나도 아까 물어봤어."
                s "무슨 일 있냐고."

                n "하린이가 뭐래?"

                s "아무것도 아니래."
                s "계속 괜찮다고만 하고…."

                "소윤이는 하린이가 걸어간 쪽을 바라봤다."

                s "근데 괜찮아 보이진 않았어."

                n "그럼 이번에는 그냥 지나가면 안 될 것 같아."

                "소윤이는 잠시 말이 없었다."

                s "…응."

            else:

                n "나 어제 단톡방 봤어."
                n "하린이한테 계속 그러고 있었던 것도 봤고."

                "소윤이는 입을 다물었다."

                n "너도 전부터 알고 있었어?"

                hide s6 with dissolve
                show s3 at center_stage with dissolve

                "소윤이는 잠시 망설이다 대답했다."

                s "…처음엔 그냥 애들이 장난치는 줄 알았어."

                s "근데 계속 보다 보니까,"
                s "점점 좀 이상해졌어."

                n "그런데 왜 아무 말도 안 했어?"

                s "그때는 이미 너무 늦은 것 같아서…."

                "소윤이는 말끝을 흐렸다."

                s "갑자기 내가 뭐라고 하는 것도 이상할 것 같았고."

                "잠깐의 침묵이 흘렀다."

                n "그래도 지금은 아직 안 늦은 거 아닐까?"

                "소윤이는 바로 대답하지 않았다."

                s "…모르겠어."

            hide s3
            hide s6
            with dissolve

            scene bg_8 with dissolve

            "소윤이는 잠시 하린이가 사라진 쪽을 바라보다가 교실로 돌아갔다."

            if f_r2_chat_with_soyoon:

                n "(어제보다 조금은 달라졌어.)"
                n "(적어도 이제 그냥 모른 척하고 있지는 않아.)"

            else:

                n "(소윤이도 계속 보고 있었던 거야.)"
                n "(이상하다고 느낀 뒤에도 어떻게 끼어들어야 할지 몰랐던 거고.)"

            $ trust_soyun += 1

            "그사이 하린이는 이미 복도 끝으로 사라지고 없었다."

            n "(이번엔 소윤이 얘기를 들었어.)"
            n "(하지만 하린이한테는 또 아무것도 못 물어봤네.)"


        "혼자 걷고 있는 하린이에게 다가가 말을 건다.":

            $ trust_harin += 1
            $ key2_stay_with_harin = True
            $ f_r2_harin_connect = True

            "나는 소윤이를 지나쳐 하린이가 걸어간 쪽으로 향했다."

            scene bg_8 with dissolve

            n "하린아, 잠깐만."

            scene bg_8_blur with dissolve
            show h16 at center_stage with dissolve

            "하린이는 내 목소리에 놀라 걸음을 멈췄다."

            "뒤를 돌아본 하린이는 나를 가만히 바라봤다."

            n "아까 화장실에서 나온 거 봤어."
            n "무슨 일인지 지금 말하기 싫으면 안 해도 돼."

            "하린이는 아무 대답도 하지 않았다."

            n "근데 그냥 혼자 가게 두고 싶지는 않아."

            hide h16 with dissolve
            show h10 at center_stage with dissolve

            h "…왜 갑자기 그래?"

            "나는 잠깐 말을 고르다가 대답했다."

            n "나도 너무 늦게 본 것 같아."
            n "그래도 이제 알게 된 걸 그냥 넘기고 싶진 않아."

            "하린이는 잠시 나를 바라봤다."

            h "…."

            "그러다 다시 걸음을 옮겼지만,"
            "이번에는 나를 두고 먼저 가버리지는 않았다."

            hide h10 with dissolve

            scene bg_8 with dissolve

            "뒤를 돌아보니 소윤이는 이미 교실 쪽으로 사라지고 없었다."

            n "(소윤이한테는 못 물어봤지만….)"
            n "(지금은 하린이 옆에 있는 게 먼저야.)"


        "둘을 그냥 보내지 않고, 두 사람을 함께 불러 세운다.":

            $ f_r2_bath_soyoon_talk = True
            $ trust_soyun += 1
            $ trust_harin += 1
            $ key2_stay_with_harin = True
            $ f_r2_harin_connect = True

            n "둘 다 잠깐만."

            "서로 반대쪽으로 가던 소윤이와 하린이가 걸음을 멈췄다."

            scene bg_8_blur with dissolve

            show s3 at left_stage
            show h5 at right_stage
            with dissolve

            n "나 어제 단톡방 봤어."

            "하린이가 고개를 들어 나를 바라봤다."

            n "그리고 아까 너희 둘이 같이 나오는 것도 봤고."

            n "지금 무슨 일이 있었는지 다 말하라는 건 아니야."
            n "그냥 아무 일도 없는 것처럼 넘어가고 싶지 않아."

            "잠시 아무도 말을 하지 않았다."

            if f_r2_chat_with_soyoon:

                "소윤이와 눈이 마주쳤다."

                n "소윤아, 어제 네가 한 말도 기억해."

                "소윤이는 잠시 하린이를 바라봤다."

                s "…응."

                s "하린아."
                s "나도 그냥 가면 안 될 것 같아."

                "하린이는 소윤이를 바라봤지만 대답하지 않았다."

            else:

                "소윤이는 하린이와 나를 번갈아 바라봤다."

                n "소윤아, 너도 아까 같이 있었지?"

                s "…응."

                n "둘 다 지금 말하기 싫으면 안 해도 돼."

                "하린이는 아무 말 없이 서 있었고,"
                "소윤이도 더는 말을 잇지 않았다."

            n "나도 아직 어떻게 해야 하는지는 잘 모르겠어."

            n "그래도 하린이가 계속 혼자 있게 두는 건 아닌 것 같아."

            "하린이는 한동안 아무 말도 하지 않았다."

            "그러다 천천히 고개를 들었다."

            h "…나 교실 돌아갈게."

            n "응."

            n "같이 가자."

            "하린이는 거절하지 않았다."

            if f_r2_chat_with_soyoon:

                s "…나도 같이 갈게."

            hide h5
            hide s3
            with dissolve

            scene bg_8 with dissolve

    jump r2_s5_hallway_decision

# ----------------------------------------------------------
# R2-S5. 2회차 쉬는 시간 끝 — 같이 갈 사람을 정한다
# ----------------------------------------------------------

label r2_s5_hallway_decision:

    scene black with fade
    scene bg_7 with dissolve

    play sound "audio/bell.mp3"

    "예비종이 울렸다."

    "복도에 있던 아이들이 하나둘 교실로 돌아가기 시작했다."

    stop sound fadeout 1.0


    if f_r2_bath_soyoon_talk:

        if f_r2_harin_connect:

            "하린이와 소윤이도 교실 쪽으로 걸음을 옮기려 했다."

            "나도 따라가려다 문득 멈춰 섰다."

            n "(이대로 교실로 돌아가면 또 끝나는 거잖아.)"

            "어제 본 단톡방도,"
            "오늘 하린이가 울었던 것도 이미 알고 있었다."

            "나는 소윤이를 바라봤다."

        else:

            "소윤이도 교실로 돌아가려 했다."

            "나는 그 모습을 보다가 걸음을 멈췄다."

            n "(이대로 들어가면 또 아무 일도 없었던 것처럼 지나가.)"

            "어제 단톡방에서 본 것과,"
            "방금 소윤이에게 들은 이야기가 머릿속에 남아 있었다."

            n "(이번에는 여기서 끝내면 안 돼.)"


        scene bg_7_blur with dissolve
        show s2 at center_stage with dissolve

        menu:

            "소윤이에게 같이 교무실에 가자고 제안한다.":

                n "소윤아."

                "소윤이가 나를 돌아봤다."

                n "우리 선생님한테 말하러 가자."

                "소윤이의 표정이 굳었다."

                n "내가 본 것도 말할게."
                n "너는 네가 본 것만 말해주면 돼."

                if trust_soyun >= 2:

                    "소윤이는 바로 대답하지 못하고 교실 쪽을 한번 바라봤다."

                    if f_r2_chat_with_soyoon:

                        n "어제 네가 너무 늦은 것 같다고 했잖아."

                        n "근데 아직 힘들어하는 하린이가 여기 있어."

                        "소윤이는 한동안 말이 없었다."

                    else:

                        "한동안 망설이던 소윤이가 천천히 고개를 들었다."

                    $ f_r2_soyoon_join = True
                    $ key3_move_with_soyoon = True

                    hide s2 with dissolve
                    show s10 at center_stage with dissolve

                    s "…응."

                    s "같이 갈게."

                    hide s10 with dissolve

                    jump r2_s6_report

                else:

                    "소윤이는 한동안 아무 말도 하지 못했다."

                    hide s2 with dissolve
                    show s3 at center_stage with dissolve

                    s "미안해."

                    s "나… 아직은 못 하겠어."

                    n "왜?"

                    s "내가 같이 말했다가,"
                    s "민재랑 예서가 알게 되면 어떡해."

                    "소윤이는 교실 쪽을 힐끗 바라봤다."

                    s "나까지 이상하게 보면…."

                    hide s3 with dissolve
                    scene bg_7 with dissolve

                    n "(소윤이도 무슨 일이 있었는지는 알고 있어.)"
                    n "(그래도 직접 나서는 건 아직 무서운 거야.)"

                    if note_chat or f_r2_harin_connect:

                        menu:

                            "소윤이가 같이 가지 못해도, 혼자 선생님께 말씀드린다.":

                                n "(그래도 내가 직접 본 건 있어.)"
                                n "(혼자라도 가서 말하자.)"

                                jump r2_s6_report

                            "지금은 교무실에 가지 않는다.":

                                "교무실 쪽을 바라보다가 결국 발을 돌렸다."

                                n "(그래, 나도 아직은 못 하겠어.)"

                                "나는 소윤이와 함께 교실 쪽으로 돌아갔다."

                                jump r2_s6_no_report_to_loop3

                    else:

                        n "(내가 제대로 확인한 것도 아직 너무 적어.)"

                        "교무실 쪽으로 가려던 발걸음을 멈췄다."

                        n "(조금 더 알아봐야 해.)"

                        jump r2_s6_no_report_to_loop3


            "소윤이에게 부탁하지 않고 혼자 간다.":

                "소윤이를 바라보다가 더 붙잡지는 않기로 했다."

                hide s2 with dissolve

                n "(소윤이까지 억지로 데려갈 수는 없어.)"

                if note_chat or f_r2_harin_connect:

                    n "(그래도 내가 직접 본 건 말할 수 있어.)"

                    "나는 혼자 교무실 쪽으로 걸음을 옮겼다."

                    jump r2_s6_report

                else:

                    n "(그런데 지금 내가 말할 수 있는 건 너무 적어.)"

                    "몇 걸음 가지 못하고 멈춰 섰다."

                    n "(이대로 가도 제대로 설명하지 못할 것 같아.)"

                    jump r2_s6_no_report_to_loop3


    else:

        "소윤이에게는 결국 제대로 묻지 못했다."

        if f_r2_harin_connect:

            "그래도 조금 전 하린이와 나눈 대화가 계속 마음에 남았다."

            n "(하린이가 아무 말도 안 했다고 해서,"
            n "아무 일도 없었던 건 아니잖아.)"

        elif note_chat:

            "어젯밤 단톡방에서 본 메시지들이 떠올랐다."

            n "(적어도 내가 본 건 분명히 있어.)"

        else:

            "운동장에서 봤던 장면들이 다시 떠올랐다."

            n "(이상한 건 분명한데… 아직 내가 아는 게 너무 적어.)"


        if note_chat or f_r2_harin_connect:

            menu:

                "혼자라도 선생님께 말씀드리러 간다.":

                    n "(같이 말해줄 사람은 없어도,"
                    n "내가 본 것까지 없어지는 건 아니야.)"

                    "나는 교무실 쪽으로 걸음을 옮겼다."

                    jump r2_s6_report

                "지금은 교무실에 가지 않는다.":

                    "교무실 쪽을 바라보다가 결국 발을 돌렸다."

                    n "(조금 더 알아보고 나서 말하자.)"

                    jump r2_s6_no_report_to_loop3

        else:

            menu:

                "그래도 내가 본 장면들을 선생님께 말씀드린다.":

                    n "(확실하게 아는 건 많지 않아.)"
                    n "(그래도 이상하다고 느낀 건 말할 수 있어.)"

                    "나는 망설이다가 교무실 쪽으로 걸음을 옮겼다."

                    jump r2_s6_weak_to_loop3

                "지금은 교무실에 가지 않는다.":

                    "결국 교실 쪽으로 발을 돌렸다."

                    jump r2_s6_no_report_to_loop3
            
label r2_s6_no_report_to_loop3:

    scene black with fade
    pause 0.8

    scene bg_9 with fade

    "다음 날 아침."

    "교실에 들어서자 가장 먼저 하린이 자리가 보였다."

    "비어 있었다."

    "어제 더 알아보겠다고 생각했지만,"
    "결국 누구에게도 제대로 말하지 못한 채 하루가 지나갔다."

    scene cg_1 with dissolve

    n "(이번에는 더 많이 봤는데….)"
    n "(그래도 결국 아무것도 바꾸지 못했어.)"

    scene bg_3 with fade

    "그날 밤."

    "눈을 감아도 하린이의 빈자리만 떠올랐다."

    n "(보기만 해서는 안 돼.)"
    n "(다음에는 더 늦기 전에 움직여야 해.)"

    scene black with blink_black
    scene bg_3 with blink_black
    scene black with blink_black
    scene bg_3 with blink_black_long

    scene black with Dissolve(1.0)
    pause 1.5

    jump loop3_intro


label r2_s6_weak_to_loop3:

    scene black with fade
    pause 0.8

    scene bg_9 with fade

    "다음 날 아침."

    "교실에 들어서자 가장 먼저 하린이 자리가 보였다."

    "비어 있었다."

    "선생님은 몇 번이나 그쪽을 바라보셨고,"
    "민재와 예서도 평소보다 조용했다."

    "하지만 달라진 건 그 정도였다."

    "어제 나는 선생님께 내가 본 일을 말했다."

    "급식실에서 있었던 일도,"
    "체육 시간에 이상하다고 느꼈던 장면도."

    "그런데 막상 설명하려니,"
    "내가 아는 것과 모르는 것이 뒤섞여 있었다."

    scene cg_1 with dissolve

    "하린이의 자리는 끝내 채워지지 않았다."

    n "(말은 했는데….)"

    n "(내가 왜 이상하다고 생각했는지,"
    n "제대로 설명하지 못했어.)"

    "그제야 지난 며칠 동안 봤던 장면들이 다시 떠올랐다."

    n "(따로 본 것만 말해서는 안 됐던 걸까.)"
    n "(내가 놓친 게 아직 더 있었던 걸까.)"

    scene bg_3 with fade

    "그날 밤."

    "눈을 감아도 빈자리만 자꾸 떠올랐다."

    n "(이번에는 가만히 있지는 않았어.)"
    n "(그래도 결과는 똑같아.)"

    "왜 다시 돌아왔는지,"
    "아직도 답을 찾지 못한 것 같았다."

    scene black with blink_black
    scene bg_3 with blink_black
    scene black with blink_black
    scene bg_3 with blink_black_long

    scene black with Dissolve(1.0)
    pause 1.5

    jump loop3_intro
# ----------------------------------------------------------
# R2-S6. 2회차 교무실 보고 — 조건별 보고 장면
# ----------------------------------------------------------

label r2_s6_report:

    scene black with fade
    scene bg_10 with dissolve

    if f_r2_soyoon_join:
        "쉬는 시간이 끝나기 직전, 나와 소윤이는 교무실 앞에 멈춰 섰다."
    else:
        "쉬는 시간이 끝나기 직전, 나는 혼자 교무실 앞에 멈춰 섰다."

    "문 앞에 서자 갑자기 무슨 말부터 해야 할지 막막해졌다."

    "지난번에도 이상하다고 느낀 장면은 있었다."
    "하지만 그때는 하나씩 지나가 버렸고,"
    "결국 왜 이상했는지 나조차 제대로 설명하지 못했다."

    n "(이번에는 달라.)"

    if f_r2_soyoon_join and note_chat:

        "모둠 활동과 급식실에서 있었던 일,"
        "체육 시간에 본 행동까지 직접 봤다."

        "어젯밤에는 단톡방에서 하린이를 계속 불러내고"
        "웃음거리로 삼는 대화도 확인했다."

        "그리고 이번에는 소윤이도 내 옆에 있었다."

        n "(내가 본 것만 있는 게 아니야.)"


    elif f_r2_soyoon_join:

        "학교에서 하린이가 계속 혼자 남게 되는 장면들을 봤다."

        "체육 시간에 민재가 하린이에게 한 행동도,"
        "그걸 지켜보던 아이들의 반응도 기억하고 있었다."

        "그리고 내 옆에는 그 장면들을 함께 본 소윤이가 있었다."


    elif note_chat:

        "학교에서 봤던 일만 있는 게 아니었다."

        "어젯밤 단톡방을 확인하면서,"
        "하린이를 향한 일이 학교가 끝난 뒤에도 이어지고 있다는 걸 알게 됐다."

        "같이 말해 줄 사람은 없었지만,"
        "적어도 내가 직접 본 것들은 분명했다."


    elif f_r2_harin_connect:

        "학교에서 여러 장면을 직접 봤고,"
        "조금 전에는 하린이에게도 말을 걸었다."

        "하린이는 자세한 이야기를 해주지 않았지만,"
        "아무 일도 없다고 넘기기에는 이미 본 게 너무 많았다."


    else:

        "학교에서 이상하다고 느낀 장면들은 분명 있었다."

        "하지만 그게 어떻게 이어지는지,"
        "내가 알고 있는 것과 추측하는 것을 제대로 나눠 말할 자신은 없었다."


    call screen teacher_report


    if _return == "report_done":

        "나는 숨을 한번 고르고 교무실 문을 열었다."

        n "(내가 본 것부터 차근차근 말하자.)"

        jump r2_s6_teacher


    elif _return == "report_weak":

        "나는 선생님께 내가 본 몇 가지 장면을 이야기했다."

        "하지만 막상 입 밖으로 꺼내고 보니,"
        "어떤 일이 언제 있었는지 제대로 이어서 설명하지 못했다."

        scene bg_10_blur with dissolve
        show t6 at center_stage with dissolve

        t "알겠어."
        t "네가 왜 걱정하고 있는지는 알 것 같아."

        t "선생님도 오늘부터 하린이랑 반 분위기를 좀 더 살펴볼게."

        t "이야기해줘서 고마워."

        hide t6 with dissolve

        scene bg_10 with dissolve

        "선생님은 내 말을 그냥 넘기지는 않으셨다."

        "하지만 교무실을 나오면서도 마음이 편해지지는 않았다."

        n "(말하긴 했는데….)"
        n "(내가 본 걸 제대로 다 전한 건 아닌 것 같아.)"

        jump r2_s6_weak_to_loop3


    else:

        "문 앞에서 한참 서 있었지만 결국 들어가지 못했다."

        n "(말해야 하는데….)"

        "나는 결국 교무실에서 몇 걸음 물러났다."

        jump r2_s6_bad_rework
# ----------------------------------------------------------
# R2-S6-BAD. 2회차 실패 결말
# ----------------------------------------------------------

label r2_s6_bad_rework:

    scene black with fade

    "교무실 앞까지 갔지만 결국 문을 열지 못했다."

    "분명 이상한 장면들을 봤고,"
    "어제는 단톡방까지 확인했다."

    "그런데 막상 누군가에게 말해야 하는 순간이 오자"
    "발이 떨어지지 않았다."

    scene bg_9 with fade

    "다음 날 아침."

    "교실은 평소처럼 시끄러웠다."

    "아이들은 떠들면서 수업 준비를 했고,"
    "민재와 예서도 친구들과 이야기를 나누고 있었다."

    "하지만 하린이 자리는 비어 있었다."

    "나는 한동안 그 자리에서 눈을 떼지 못했다."

    scene cg_1 with dissolve

    n "(이번에는 알고 있었는데….)"

    "지난번에는 내가 뭘 놓쳤는지도 제대로 몰랐다."

    "이번에는 달랐다."

    "급식실에서도 봤고,"
    "체육 시간에도 봤고,"
    "학교 밖에서도 계속되고 있다는 걸 알았다."

    n "(그런데 결국 아무한테도 말하지 못했어.)"

    "그 사실이 가장 마음에 남았다."

    scene black with dissolve

    n "(보기만 해서는 아무것도 달라지지 않는구나.)"

    scene black with fade

    centered "{size=34}{color=#FFFFFF99}엔딩{/color}{/size}\n\n{size=54}{color=#E8736C}{b}후회 엔딩: 알고도 멈춰 선 날{/b}{/color}{/size}\n\n{size=28}{color=#FFE1DE}알게 된 뒤에도 행동으로 옮기지 못한 두 번째 기회{/color}{/size}"

    jump r2_retry_menu


# ----------------------------------------------------------
# R2 재도전
# ----------------------------------------------------------

label r2_retry_menu:

    "이번에는 다른 선택을 해보자."

    menu:

        "2회차의 시작(월요일 아침)으로 돌아간다.":

            $ trust_soyun = 0
            $ trust_harin = 0
            $ trust_minjae = 0

            $ key1_structure = False
            $ key2_stay_with_harin = False
            $ key3_move_with_soyoon = False
            $ key4_minjae_pattern = False

            $ f_r2_chat_with_soyoon = False
            $ f_r2_bath_soyoon_talk = False
            $ f_r2_soyoon_join = False
            $ f_r2_harin_connect = False
            $ f_minjae_talk_r2 = False

            $ note_chat = False
            $ note_bathroom = False
            $ f_r2_chat_checked = False
            $ chat_scroll_depth = 0

            $ inv_board = False
            $ inv_desk = False
            $ inv_back = False

            $ inv_pe_bottle = False
            $ inv_pe_bench = False

            $ talk_pe_harin = False
            $ talk_pe_minjae = False
            $ talk_pe_soyun = False

            jump loop2_start


# ==========================================================
# R2-S6. 2회차 교무실 보고 성공
# ==========================================================

label r2_s6_teacher:

    scene black with fade
    scene bg_10 with dissolve

    if f_r2_soyoon_join:

        "나와 소윤이는 교무실 문 앞에 나란히 섰다."

        "소윤이가 잠깐 나를 바라봤다."

        n "들어가자."

        "소윤이는 작게 고개를 끄덕였다."

        "우리는 함께 문을 열었다."

    else:

        "나는 교무실 문 앞에 잠시 서 있었다."

        n "(내가 본 것부터 말하면 돼.)"

        "숨을 한번 고르고 문을 열었다."

    scene bg_10_blur with dissolve
    show t4 at center_stage with dissolve

    t "응? 무슨 일이니?"

    if f_r2_soyoon_join and note_chat:

        "나는 먼저 어젯밤 단톡방에서 본 대화를 선생님께 보여드렸다."

        "그리고 모둠 활동과 급식실,"
        "체육 시간에 있었던 일을 순서대로 이야기했다."

        "소윤이도 옆에서 자신이 직접 본 일을 하나씩 덧붙였다."

        "선생님은 휴대폰 화면과 우리를 번갈아 보며 끝까지 이야기를 들으셨다."

    elif f_r2_soyoon_join:

        "나는 학교에서 직접 본 일들을 순서대로 이야기했다."

        "모둠에서 하린이 의견을 묻지 않았던 일,"
        "급식실에서 자리를 비켜주지 않았던 일,"
        "체육 시간에 있었던 일까지."

        "소윤이도 자신이 옆에서 본 장면들을 조심스럽게 덧붙였다."

        "선생님은 말을 끊지 않고 우리 이야기를 들으셨다."

    elif note_chat:

        "나는 어젯밤 단톡방에서 본 대화를 선생님께 보여드렸다."

        "그리고 학교에서 직접 봤던 일들도 차례대로 설명했다."

        "선생님은 휴대폰 화면을 한동안 확인한 뒤 다시 나를 바라보셨다."

    elif f_r2_harin_connect:

        "나는 학교에서 직접 본 장면들을 차근차근 이야기했다."

        "그리고 아까 하린이에게 말을 걸었던 일도 말했다."

        "하린이가 자세한 이야기를 하지는 않았다는 것도 그대로 말씀드렸다."

        "선생님은 중간에 결론을 내리지 않고 끝까지 들어주셨다."

    else:

        "나는 내가 직접 본 장면부터 하나씩 이야기했다."

        "확실히 아는 것과 내가 짐작한 것을 섞지 않으려고 했다."

        "말이 몇 번 막히긴 했지만,"
        "선생님은 재촉하지 않고 기다려주셨다."

    hide t4 with dissolve
    show t7 at center_stage with dissolve

    t "알겠어."

    t "우선 하린이부터 한번 확인해볼게."

    t "그리고 너희가 말해준 일도 선생님이 따로 살펴보겠다."

    if note_chat:

        t "단톡방 내용은 지금 지우지 말고 그대로 두자."

    t "말해줘서 고마워."

    hide t7 with dissolve

    scene bg_7 with dissolve

    "교무실을 나오니 이미 수업이 시작된 뒤였다."

    "복도에는 사람이 거의 없었다."

    if f_r2_soyoon_join:

        "소윤이는 내 옆에서 한동안 아무 말도 하지 않았다."

        "교실 쪽으로 몇 걸음 걷다가 소윤이가 먼저 입을 열었다."

        scene bg_7_blur with dissolve
        show s3 at center_stage with dissolve

        s "나… 진작 말할걸."

        "나는 잠깐 소윤이를 바라봤다."

        n "그래도 지금 말했잖아."

        "소윤이는 아무 대답 없이 고개를 끄덕였다."

        hide s3 with dissolve
        scene bg_7 with dissolve

    else:

        "혼자 복도를 걸으며 방금 했던 말을 다시 떠올렸다."

        n "(말했어.)"

        "선생님이 어떻게 하실지는 아직 알 수 없었다."

        "그래도 이번에는 내가 본 일을 그대로 전했다."

    scene black with dissolve

    pause 0.5

    scene bg_9 with fade

    "다음 날 아침."

    "교실에 들어서자 가장 먼저 하린이 자리를 확인했다."

    "비어 있었다."

    n "(오늘도 안 왔어….)"

    "잠시 뒤 선생님이 민재를 불러 교실 밖으로 나가셨다."

    "민재가 돌아온 뒤에는 예서도 따로 불려 나갔다."

    "무슨 이야기를 했는지는 들을 수 없었다."

    "다만 두 사람 모두 돌아온 뒤에는 평소보다 말수가 줄어 있었다."

    "주변 아이들도 무슨 일이 있는지 눈치를 보는 듯했다."

    scene cg_1 with dissolve

    "분명 어제와 똑같지는 않았다."

    "선생님이 움직이기 시작했고,"
    "교실에서도 전처럼 아무 일도 없는 듯 넘어가지는 않았다."

    "그런데 하린이는 여기에 없었다."

    n "(말하긴 했어.)"

    n "(이번에는 선생님도 움직였어.)"

    n "(그런데 왜 하린이는 또 안 온 거지…?)"

    scene black with dissolve

    "내가 한 일이 틀렸다고 생각하지는 않았다."

    "하지만 그것만으로는 아직 부족했던 것 같았다."

    scene bg_3 with fade

    "그날 밤."

    "침대에 누우니 오늘 아침의 빈자리가 다시 떠올랐다."

    if f_r2_soyoon_join:

        "교무실에서 어렵게 말을 꺼내던 소윤이의 모습도 생각났다."

    else:

        "교무실에서 내가 했던 말도 하나씩 떠올랐다."

    n "(이번에는 분명 달라졌는데….)"

    n "(그래도 하린이는 학교에 오지 않았어.)"

    "선생님께 알리는 것까지는 했다."

    "그런데 그 전에,"
    "내가 더 할 수 있었던 일이 있었던 건 아닐까."

    n "(내가 아직 놓치고 있는 게 있어.)"

    scene black with blink_black
    scene bg_3 with blink_black
    scene black with blink_black
    scene bg_3 with blink_black_long

    scene black with Dissolve(1.0)

    pause 1.5

    jump loop3_intro

############################################################
## 3회차 — 진정한 연대와 구조의 붕괴
############################################################

label loop3_intro:

    $ loop_no = 3

    $ trust_harin = 1 if key2_stay_with_harin else 0
    $ trust_soyun = 1 if key3_move_with_soyoon else 0

    # 2회차에서 민재가 주인공의 시선을 의식하기 시작했다면
    # 3회차에서도 그 경험을 이어받는다.
    $ trust_minjae = 2 if key4_minjae_pattern else 0

    $ r3_morning_time = 2

    $ r3_action_harin = False
    $ r3_action_soyun = False
    $ r3_action_minjae = False

    $ talk_pe_minjae = False
    $ talk_pe_soyun = False
    $ talk_pe_harin = False

    $ note_witness = False

    # 2회차에서 본 단톡방은 기억으로만 남기고, 3회차의 현재 증거로는 쓰지 않는다.
    $ key_chat_memory = note_chat
    $ note_chat = False

    $ f_r3_soyoon_coop = False
    $ f_r3_stay_together = False
    $ f_r3_teacher_support = False

    # 2회차에서 민재의 행동을 반복해서 짚었다면
    # 3회차 히든 조건으로 이어진다.
    $ f_r3_minjae_weakness = False


    scene black with fade

    "어둠 속에 하린이가 서 있었다."

    scene cg_9 with dissolve

    "눈가는 붉게 부어 있었고,"
    "하린이는 나에게 등을 보인 채 멀어지고 있었다."

    play sound "audio/heartbeat.mp3"

    n "하린아."

    "하린이는 멈추지 않았다."

    n "하린아, 잠깐만!"

    "나는 뒤를 따라가며 손을 뻗었다."

    n "가지 마!"

    stop sound fadeout 1.0

    scene black with fade

    "하지만 거리는 좀처럼 줄어들지 않았다."

    "손이 닿기 직전,"
    "하린이의 모습이 어둠 속으로 사라졌다."


    scene bg_4_blur at wake_blur
    with white_flash

    pause 0.3

    n "헉!"

    with blink_black

    "의자 끄는 소리와 아이들 목소리가 한꺼번에 들려왔다."

    scene black with blink_black

    scene bg_4 at wake_clear
    with blink_black_long

    "나는 급히 휴대폰을 확인했다."

    "< 5월 10일 월요일 >"

    "잠시 화면만 바라봤다."

    n "(또 돌아왔어….)"

    "세 번째였다."

    "나는 천천히 고개를 들어 교실을 둘러봤다."

    "아직 아무 일도 일어나지 않은 월요일 아침."

    "하린이도 자기 자리에 앉아 있었다."

    n "(이번에도 다시 시작이야.)"

    scene black with dissolve

    "지난 두 번이 차례로 떠올랐다."

    "처음에는 이상하다고 느끼면서도 제대로 보지 못했다."

    "두 번째에는 전보다 많은 걸 봤다."

    "급식실에서도,"
    "체육 시간에도,"
    "단톡방에서도."

    "가만히 있지 않고 말을 걸어보기도 했다."

    n "(그런데 결국 하린이는 또 학교에 안 왔어.)"

    "분명 달라진 것도 있었다."

    "그런데 결과까지 바뀌지는 않았다."

    n "(그럼 아직 내가 놓친 게 있다는 거야.)"


    if key1_structure:

        "지난번에 따로따로 보였던 장면들이 떠올랐다."

        n "(한 번 있었던 일이 아니었어.)"
        n "(이번에는 처음부터 놓치지 말자.)"


    if key2_stay_with_harin:

        "하린이에게 다가갔던 순간도 생각났다."

        "하린이는 바로 마음을 열지는 않았지만,"
        "적어도 내가 곁에 있을 때 먼저 자리를 떠나지는 않았다."

        n "(이번에도 내 마음대로 답을 정하지 말자.)"


    if key3_move_with_soyoon:

        "망설이면서도 결국 함께 움직였던 소윤이의 모습이 떠올랐다."

        n "(소윤이도 처음부터 아무 생각이 없었던 건 아니었어.)"


    if key4_minjae_pattern:

        "민재에게 계속 말을 걸었을 때의 반응도 생각났다."

        "두 번째로 행동을 짚었을 때,"
        "민재는 처음과 달리 내가 보고 있는지를 신경 쓰기 시작했다."

        n "(누가 보고 있다는 걸 알면 행동도 달라질 수 있어.)"


    "나는 다시 하린이 쪽을 바라봤다."

    "아직 월요일 아침이었다."

    n "(이번에는 결과가 나온 뒤에 움직이지 말자.)"

    n "(무슨 일이 생기는지 처음부터 보고,"
    n "그때그때 내가 할 수 있는 걸 해보자.)"

    "그리고 나 혼자만 움직이는 것으로 끝내지 않기로 했다."

    n "(소윤이도, 다른 애들도.)"
    n "(보고 있는 사람이 나 하나뿐일 필요는 없잖아.)"

    "아직 무엇을 해야 하린이가 남을 수 있는지는 알 수 없었다."

    "그래도 이번에는 한 가지는 분명했다."

    n "(하린이를 혼자 두지는 않을 거야.)"

    jump r3_s1_morning
# ==========================================================
# R3-S1. 3회차 월요일 아침 — 달라진 시선
# ==========================================================

label r3_s1_morning:

    scene bg_4 with fade

    "익숙한 월요일 아침이었다."

    "민재와 예서 쪽에서는 벌써부터 웃음소리가 들렸고,"
    "하린이는 자기 자리에서 혼자 공책을 보고 있었다."

    "지난번에도 봤던 모습이었다."

    "다만 이번에는 그냥 지나치지 않았다."

    "나는 먼저 하린이 쪽을 보고,"
    "다시 민재와 예서 쪽을 살폈다."

    n "(아직 아무 일도 일어나기 전이야.)"

    n "(이번에는 이상한 일이 생긴 다음에 생각하지 말자.)"
    n "(지금부터 내가 먼저 움직여보자.)"

    jump r3_morning_choice

label r3_morning_choice:
    $ remaining_choices = (0 if r3_action_minjae else 1) + \
                          (0 if r3_action_soyun else 1) + \
                          (0 if r3_action_harin else 1)

    if r3_morning_time <= 0 or remaining_choices == 0:
        "예비령이 울린다. 이제 각자의 자리로 돌아가야 할 시간이다."
        jump r3_s2_class_start

    $ r3_choice_hint = "누구를 불러낼까? (남은 기회: %d번)" % r3_morning_time
    show screen choice_hint(r3_choice_hint)

    menu:
        "민재를 불러낸다." if not r3_action_minjae:
            hide screen choice_hint
            jump r3_morning_minjae_1on1

        "소윤이를 복도로 불러낸다." if not r3_action_soyun:
            hide screen choice_hint
            jump r3_morning_soyoon_1on1

        "하린이에게 조용히 다가간다." if not r3_action_harin:
            hide screen choice_hint
            jump r3_morning_harin_1on1
# ----------------------------------------------------------
# [1] 소윤 — 방관의 관성을 끊기
# ----------------------------------------------------------

label r3_morning_soyoon_1on1:

    $ r3_action_soyun = True
    $ r3_morning_time -= 1

    scene bg_4 with fade

    "예서 옆에서 이야기하고 있던 소윤이를 바라봤다."

    "지난번에는 일이 이미 커진 뒤에야 소윤이에게 말을 걸었다."

    n "(이번에는 그전부터 얘기해보자.)"

    n "소윤아, 잠깐 나랑 얘기 좀 할래?"

    "소윤이는 조금 의아한 얼굴로 나를 바라봤다."

    s "지금?"

    n "응. 금방이면 돼."

    if key3_move_with_soyoon:

        "지난번 소윤이가 어떤 말에 마음을 열었는지 기억하고 있었다."

        n "(몰아붙이지 말자.)"

        $ trust_soyun += 1

    "소윤이는 예서에게 잠깐 다녀오겠다고 말하고 나를 따라 복도로 나왔다."


    scene bg_7_blur with fade
    show s6 at center_stage with dissolve

    s "왜? 무슨 일인데?"

    n "하린이 때문에."

    "소윤이는 잠깐 나를 바라봤다."

    n "요즘 애들이 하린이한테 하는 거 있잖아."
    n "너도 옆에서 본 적 있지?"

    s "…뭐를?"

    n "하린이 빼놓고 자기들끼리 웃거나,"
    n "하린이가 싫어하는 것 같은데도 계속 장난치는 거."

    "소윤이는 바로 대답하지 않았다."

    n "(역시 지금부터 대놓고 말하고 싶지는 않은 거구나.)"

    "나는 더 캐묻지 않고 말을 이었다."

    n "너한테 뭐라고 하려는 건 아니야."

    n "그냥 다음에 또 그런 일이 생기면,"
    n "나 혼자 모른 척하고 싶지 않아서."


    menu:

        "다음에 또 그런 일이 생기면, 우리 같이 얘기해볼래?":

            $ trust_soyun += 2
            $ f_r3_soyoon_coop = True

            show s3 at center_stage with dissolve

            "소윤이는 예상하지 못한 말을 들은 듯 나를 바라봤다."

            s "같이?"

            n "응."

            n "혼자 끼어들기 어려우면,"
            n "나한테 먼저 말해도 되고."

            n "내가 먼저 말하면 옆에 있어줘도 되고."

            "소윤이는 잠깐 교실 쪽을 바라봤다."

            s "…근데 괜히 우리까지 이상해지면 어떡해?"

            n "그럴 수도 있지."

            n "그래도 혼자 하는 것보단 둘이 하는 게 낫잖아."

            "소윤이는 한동안 생각하다가 천천히 고개를 끄덕였다."

            s "…알겠어."

            s "다음에 또 그러면 나도 그냥 있지는 않을게."

            n "응. 그거면 돼."

            hide s3 with dissolve
            scene bg_7 with dissolve

            "아직 아무 일도 해결된 건 아니었다."

            "하지만 이번에는 일이 생긴 뒤에 소윤이를 설득하는 게 아니었다."

            n "(이번엔 처음부터 같이 볼 사람이 생겼어.)"


        "너도 계속 보고만 있으면 결국 똑같은 거야.":

            $ trust_soyun -= 1
            $ f_r3_soyoon_coop = False

            hide s6 with dissolve
            show s10 at center_stage with dissolve

            "소윤이는 바로 표정을 굳혔다."

            s "갑자기 왜 나한테 그래?"

            n "너도 보고 있었잖아."

            s "봤다고 내가 뭘 해야 하는 건 아니잖아."

            n "그렇게 다들 가만히 있으니까 계속 그러는 거잖아."

            s "너도 똑같이 있었으면서 왜 나한테만 그래?"

            "소윤이의 목소리가 조금 커졌다."

            s "난 민재도 아니고 예서도 아니야."

            s "나한테 화낼 거면 나 말고 걔들한테 말해."

            hide s10 with dissolve
            scene bg_7 with dissolve

            "소윤이는 그대로 교실로 돌아가 버렸다."

            n "(또 너무 몰아붙였어.)"

            n "(소윤이를 움직이게 하려면,"
            n "잘못부터 따지는 게 먼저가 아니었는데.)"

    jump r3_morning_choice
# ----------------------------------------------------------
# [2] 민재 — 주동자의 당혹감
# ----------------------------------------------------------

label r3_morning_minjae_1on1:

    $ r3_action_minjae = True
    $ r3_morning_time -= 1

    scene bg_4 with fade

    "교실 뒤쪽에서 친구들과 떠들고 있는 민재를 바라봤다."

    "지난번에 민재에게 몇 번이나 말을 걸었을 때가 떠올랐다."

    n "(처음엔 아무렇지도 않아 했어.)"

    if key4_minjae_pattern:

        n "(근데 내가 계속 보고 있다는 걸 알게 되니까 조금씩 신경 쓰기 시작했지.)"

    n "민재야, 잠깐 나와 봐."

    "민재는 무슨 일이냐는 듯 나를 쳐다봤다."

    m "왜?"

    n "물어볼 게 있어."

    "민재는 귀찮다는 표정을 지으면서도 복도로 따라 나왔다."

    scene bg_7 with fade
    scene bg_7_blur with dissolve

    show m1 at center_stage with dissolve

    n "너 하린이한테 장난칠 때 있잖아."

    m "뭐?"

    n "애들 앞에서 하린이 얘기하면서 웃거나,"
    n "하린이가 싫어하는데도 계속 그러는 거."

    m "갑자기 뭔 소리야."
    m "그냥 장난치는 건데."


    if key4_minjae_pattern:

        "지난번에도 처음에는 똑같이 대답했다."

        n "(여기서 그냥 따지기만 하면 또 웃어넘길 거야.)"

        n "그래. 너는 장난이라고 생각할 수도 있지."

        "민재는 예상과 다른 대답이었는지 잠깐 나를 바라봤다."

        n "근데 다음에 또 그러면 나도 그냥 지나가진 않을 거야."

        m "뭘 어쩌게?"

        n "그냥 볼 거야."

        n "누가 먼저 시작하는지,"
        n "하린이가 싫어하는데도 누가 계속하는지."

        "민재가 대꾸하려다가 잠깐 입을 다물었다."

        n "그러니까 네가 정말 별거 아니라고 생각하면,"
        n "앞으로 안 하면 되잖아."

        hide m1 with dissolve
        show m7 at center_stage with dissolve

        m "아, 알았어."

        m "안 하면 될 거 아냐."

        n "응."

        "민재는 퉁명스럽게 대답하고 교실 쪽으로 돌아섰다."

        "몇 걸음 가다가 한 번 뒤를 돌아 나를 확인했다."

        hide m7 with dissolve
        scene bg_7 with dissolve

        n "(이번에도 신경 쓰기 시작했어.)"

        $ trust_minjae += 2
        $ f_r3_minjae_weakness = True


    else:

        n "하린이는 별로 안 좋아하는 것 같던데."

        m "걔가 뭐라고 했어?"

        n "아니."

        m "그럼 됐잖아."

        n "아무 말 안 한다고 괜찮다는 뜻은 아니잖아."

        "민재는 어이없다는 듯 나를 바라봤다."

        m "너 오늘 갑자기 왜 이래?"

        m "내가 뭐 엄청 잘못한 것처럼 말하네."

        hide m1 with dissolve
        show m7 at center_stage with dissolve

        m "됐어. 나 들어간다."

        "민재는 더 들을 생각이 없다는 듯 교실로 돌아갔다."

        hide m7 with dissolve
        scene bg_7 with dissolve

        n "(역시 그냥 말하는 것만으로는 신경도 안 쓰네.)"

        $ trust_minjae -= 1

    jump r3_morning_choice

# ----------------------------------------------------------
# [3] 하린 — 조용한 신뢰 확보 혹은 성급한 실수
# ----------------------------------------------------------
# [코딩 규칙 요약]
#   - 캐릭터 대사 직전: blur 배경 + show 캐릭터
#   - 내레이션/n 독백: 일반(선명) 배경
#   - 장소 이동: scene ○○ with fade
#   - 같은 장소 내 전환: scene ○○ with dissolve
#   - 날짜 전환: scene black with fade → pause 0.8
#   - 이미지 이름: h1~h15 (언더스코어 없음)
#   - 위치: center_stage / left_stage / right_stage
# ----------------------------------------------------------
# ----------------------------------------------------------
# [3] 하린 — 답을 요구하지 않고 곁에 있기
# ----------------------------------------------------------

label r3_morning_harin_1on1:

    $ r3_action_harin = True
    $ r3_morning_time -= 1

    scene bg_4 with dissolve

    "하린이는 자기 자리에서 혼자 공책을 보고 있었다."

    "지난번에도 처음에는 이렇게 아무 일 없는 것처럼 앉아 있었다."

    if key2_stay_with_harin:

        n "(지난번엔 내가 뭔가 알아내려고 할수록 더 조심스러워했어.)"
        n "(이번에는 먼저 캐묻지 말자.)"

        $ trust_harin += 1

    elif f_r2_harin_connect:

        n "(바로 물어본다고 말해줄 것 같지는 않아.)"

    "나는 하린이 책상 옆으로 다가갔다."

    n "하린아."

    scene bg_4_blur with dissolve
    show h10 at center_stage with dissolve

    "하린이가 고개를 들어 나를 바라봤다."

    h "왜?"

    "주머니에 넣어둔 사탕이 손에 잡혔다."

    menu:

        "별말 없이 사탕 하나를 건넨다.":

            "나는 사탕 하나를 꺼내 하린이 쪽으로 내밀었다."

            n "이거 먹을래?"

            "하린이는 사탕과 내 얼굴을 번갈아 봤다."

            h "…나?"

            n "응. 하나 남아서."

            "하린이는 잠시 망설이다 사탕을 받아 들었다."

            hide h10 with dissolve
            show h16 at center_stage with dissolve

            h "…고마워."

            n "응."

            "나는 바로 다른 이야기를 꺼내지 않았다."

            "하린이도 사탕을 책상 위에 내려놓지 않고 손에 들고 있었다."

            if key2_stay_with_harin:

                n "(지금은 이것만으로도 괜찮아.)"

            n "나중에 쉬는 시간에 같이 있을래?"

            "하린이는 바로 대답하지 않았다."

            "잠시 뒤 아주 작게 고개를 끄덕였다."

            h "…응."

            hide h16 with dissolve
            scene bg_4 with dissolve

            $ trust_harin += 3

            n "(이번에는 하린이가 먼저 말할 수 있을 때까지 기다려보자.)"


        "요즘 애들이 너한테 하는 거 때문에 힘든 거 맞지?":

            n "하린아."

            n "요즘 민재랑 애들이 너한테 하는 거 있잖아."
            n "그거 때문에 요즘 힘든거 맞지?"

            "하린이는 잠시 굳은 채 나를 바라봤다."

            hide h10 with dissolve
            show h4 at center_stage with dissolve

            h "…아니."

            n "근데 내가 보기에는—"

            h "아니라고 했잖아."

            "하린이는 공책으로 시선을 돌렸다."

            "더 이야기하고 싶지 않다는 듯 손가락으로 공책 모서리만 만지작거렸다."

            hide h4 with dissolve
            scene bg_4 with dissolve

            n "(또 내가 먼저 답을 정해놓고 물어봤어.)"

            $ trust_harin -= 1

    jump r3_morning_choice


# ----------------------------------------------------------
# 3단계: 국어 시간 시작 라벨
# ----------------------------------------------------------

label r3_s2_class_start:

    scene black with fade
    pause 0.8

    scene bg_11 with fade

    "1교시 국어 시간."

    "선생님이 칠판에 '역사 인물 분석 발표'라고 적으셨다."

    scene bg_11_blur with dissolve
    show t9 at center_stage with dissolve

    t "자, 지난번 모둠대로 앉아서 역할 정하자."
    t "이번에도 한 사람만 하지 말고 다 같이 참여해야 한다."

    hide t9 with dissolve
    scene bg_11 with dissolve

    "의자 끄는 소리와 함께 아이들이 모둠별로 자리를 옮겼다."

    "나도 내 모둠에 앉았지만,"
    "자꾸 대각선 앞쪽 하린이네 모둠이 눈에 들어왔다."

    "지난번에도 여기서부터 시작됐다."

    "민재가 제일 먼저 활동지를 자기 쪽으로 당겨놓고 입을 열었다."

    scene bg_11_blur with dissolve
    show m2 at left_stage with dissolve

    m "야, 예서가 발표하고 하린이는 자료 정리하면 되겠다."

    # ----------------------------------------------------------
    # [분기] 아침에 소윤이와 협력 약속을 했는지
    # ----------------------------------------------------------

    if f_r3_soyoon_coop:

        "이번에는 민재의 말이 끝나자마자 소윤이가 입을 열었다."

        show s2 at right_stage with dissolve

        s "잠깐만."

        "민재가 말을 멈추고 소윤이를 돌아봤다."

        s "하린이한테도 뭐 하고 싶은지 물어보자."

        $ trust_harin += 2
        $ trust_soyun += 1

        "예서도 소윤이를 쳐다봤다."

        "평소라면 민재가 역할을 정하면 그대로 넘어가던 순간이었다."

        hide m2 with dissolve
        show m4 at left_stage with dissolve

        m "어?"

        s "선생님도 다 같이 참여하라고 했잖아."

        "소윤이 목소리는 크지 않았지만 말을 거두지는 않았다."

        "민재는 잠깐 활동지를 내려다봤다."

        m "아니, 뭐…."

        m "그럼 물어보든가."

        "소윤이는 잠깐 내 쪽을 바라봤다."

        "아침에 복도에서 나눴던 이야기가 떠올랐다."

        "이번에는 내가 먼저 끼어들지 않아도 됐다."

        hide m4
        hide s2
        with dissolve

        scene bg_11 with dissolve

        n "(소윤이가 먼저 말했어.)"

        "그리고 이번에는 모두의 시선이 자연스럽게 하린이에게 향했다."

        jump r3_s2_harin_voice_check


    else:

        "민재는 그대로 역할을 정해 나갔다."

        hide m2 with dissolve

        show m3 at left_stage
        show s3 at right_stage
        with dissolve

        m "예서가 발표하고,"
        m "소윤이는 조사한 거 정리해서 보내."

        m "하린이는 자료 찾아서 모아주면 되고."

        "민재는 활동지에 역할을 하나씩 적어 내려갔다."

        "하린이에게 뭘 하고 싶은지는 묻지 않았다."

        if r3_action_soyun:

            "소윤이는 바로 대답하지 않았다."

            "한번 입을 열려는 듯하다가 멈추고,"
            "하린이 쪽을 잠깐 바라봤다."

            "하지만 결국 민재에게 아무 말도 하지 않았다."

            n "(아침에 얘기하긴 했는데….)"
            n "(아직 먼저 나서는 건 어려운가 봐.)"

        else:

            "소윤이는 민재의 말을 듣고 활동지 쪽으로 시선을 내렸다."

            "그러다 잠깐 하린이 쪽을 바라봤지만,"
            "그대로 아무 말도 하지 않았다."

            n "(이번에도 하린이한테는 아무도 묻지 않네.)"

        "하린이도 자기 역할이 정해지는 동안 아무 말이 없었다."
        hide m3
        hide s3
        with dissolve

        scene bg_11 with dissolve

        n "(이번에는 내가 어떻게 해야 하지?)"

        menu:

            "내가 먼저 하린이 의견을 물어보자고 한다.":

                jump r3_s2_player_intervene

            "일단 하린이가 어떻게 반응하는지 본다.":

                n "(내가 바로 끼어들기 전에, 하린이가 어떻게 하는지 먼저 보자.)"

                jump r3_s2_harin_voice_check


# ----------------------------------------------------------
# [독립 장면] 지원의 직접 개입
# ----------------------------------------------------------

label r3_s2_player_intervene:

    $ trust_harin += 2
    $ trust_soyun += 1

    n "민재야."
    n "하린이한테도 뭐 하고 싶은지 먼저 물어보는 게 낫지 않아?"

    scene bg_11_blur with dissolve

    show m2 at left_stage with dissolve
    show s3 at right_stage with dissolve

    "민재가 말을 멈췄다."

    "소윤이도 고개를 들어 나를 바라봤다."

    "아까 아무 말도 하지 못했던 소윤이는 잠시 나와 하린이를 번갈아 봤다."

    if key4_minjae_pattern and r3_action_minjae:

        hide m2 with dissolve
        show m4 at left_stage with dissolve

        "민재는 바로 대꾸하려다가 잠깐 멈췄다."

        "아침에 내가 했던 말을 신경 쓰는 듯 한 번 내 쪽을 확인했다."

        m "아니, 뭐…."
        m "그냥 빨리 정하려고 한 거지."

        n "그러니까 물어보면 되잖아."

        "민재는 활동지를 내려다보다가 하린이 쪽으로 고개를 돌렸다."

        m "…그래. 그럼 너 뭐 하고 싶은데?"

        "말투는 여전히 퉁명스러웠지만,"
        "이번에는 하린이 대신 역할을 정해버리지는 않았다."

    else:

        hide m2 with dissolve
        show m10 at left_stage with dissolve

        m "야, 넌 너네 모둠이나 신경 써."

        n "그냥 하린이 의견도 물어보자는 거잖아."

        m "하린이는 원래 이런 거 별로 안 좋아하잖아."

        "민재는 곧바로 하린이 쪽을 바라봤다."

        m "너 자료 찾는 거 하면 되지?"

        "갑자기 질문을 받은 하린이에게 모둠 아이들의 시선이 한꺼번에 모였다."

    hide m4
    hide m10
    hide s3
    with dissolve

    scene bg_11 with dissolve

    "고개를 숙이고 있던 하린이가 천천히 얼굴을 들었다."

    jump r3_s2_harin_voice_check
label r3_s2_harin_voice_check:

    if trust_harin >= 5 or (key2_stay_with_harin and trust_harin >= 4):

        # ----------------------------------------------------------
        # 하린이가 자기 의견을 말하는 경우
        # ----------------------------------------------------------

        scene bg_11_blur with dissolve
        show h25 at center_stage with dissolve

        "모두의 시선이 하린이에게 향했다."

        "하린이는 잠시 활동지를 내려다보다가 조심스럽게 입을 열었다."

        h "저… 나 자료 정리 말고,"
        h "대본 같이 짜보고 싶어."

        h "인물 분석하는 거 좋아해."

        hide h25 with dissolve


        if f_r3_soyoon_coop:

            # ----------------------------------------------------------
            # 소윤 협조 O + 하린이 직접 의견 표현
            # ----------------------------------------------------------

            scene bg_11_blur with dissolve
            show s9 at right_stage with dissolve

            s "그래?"
            s "그럼 나랑 같이 해도 되겠다."

            s "나는 자료 찾는 것도 할 수 있어."

            hide s9 with dissolve


            scene bg_11_blur with dissolve
            show m10 at left_stage with dissolve

            "민재가 헛웃음을 쳤다."

            m "갑자기?"
            m "맨날 아무 말도 안 하다가 이제 와서?"

            "하린이가 다시 입을 다물었다."

            s "말했잖아. 대본 하고 싶다고."

            m "아니, 그래서 하는 말이잖아."
            m "하다가 또 말도 안 하고 가만히 있으면 어떡하려고."

            s "그건 해보면 알지."

            "민재는 못마땅한 얼굴로 하린이를 한번 훑어봤다."

            m "…아, 몰라."
            m "하고 싶으면 해."

            hide m10 with dissolve
            scene bg_11 with dissolve

            "민재는 끝까지 못마땅한 티를 냈지만,"
            "소윤이가 물러서지 않자 더 밀어붙이지는 못했다."

            "하린이는 새로 적힌 역할을 한동안 바라봤다."


        else:

            # ----------------------------------------------------------
            # 소윤 협조 X + 하린이 직접 의견 표현
            # ----------------------------------------------------------

            if key4_minjae_pattern and r3_action_minjae:

                scene bg_11_blur with dissolve
                show m4 at left_stage with dissolve

                "민재가 하린이를 보며 입꼬리를 살짝 비틀었다."

                m "네가 대본을?"

                h "…응."

                m "너 원래 이런 거 싫어하잖아."

                "민재가 더 말하려다가 나를 한번 쳐다봤다."

                "그러고는 입 안에서 작게 혀를 찼다."

                m "아, 그래."
                m "하고 싶으면 하든가."

                m "나중에 힘들다고 하지 말고."

                hide m4 with dissolve
                scene bg_11 with dissolve

                "민재는 끝까지 한마디를 덧붙였지만,"
                "이번에는 하린이의 선택 자체를 막지는 못했다."

            else:

                scene bg_11_blur with dissolve
                show m7 at left_stage with dissolve

                "민재가 황당하다는 듯 웃었다."

                m "네가 대본을?"

                m "너 발표 때 말도 잘 안 하잖아."

                "하린이가 잠깐 시선을 내렸다."

                h "…그래도 해보고 싶어."

                m "하다가 분위기 망치지만 마."

                "민재는 옆에 있던 예서를 한번 보며 피식 웃었다."

                m "뭐, 정 하고 싶으면 하든가."

                hide m7 with dissolve
                scene bg_11 with dissolve

                "하린이는 대답하지 않았지만,"
                "자기 역할을 다시 바꾸지는 않았다."

        n "(그래도 이번에는 하린이가 자기 입으로 말했어.)"


    else:

        # ----------------------------------------------------------
        # 하린이가 아직 자기 의견을 말하지 못하는 경우
        # ----------------------------------------------------------

        scene bg_11_blur with dissolve
        show h23 at center_stage with dissolve

        "갑자기 시선이 몰리자 하린이는 한동안 말을 하지 못했다."

        h "…아니야."

        h "나 그냥 자료 하는 게 편해."

        hide h23 with dissolve


        if f_r3_soyoon_coop:

            # ----------------------------------------------------------
            # 소윤 협조 O + 하린이 아직 위축
            # ----------------------------------------------------------

            scene bg_11_blur with dissolve
            show s2 at right_stage with dissolve

            "소윤이는 하린이를 잠시 바라봤다."

            s "…알겠어."

            s "그럼 오늘은 그렇게 하고,"
            s "다음에는 역할 정하기 전에 다 같이 먼저 물어보자."

            hide s2 with dissolve


            if key4_minjae_pattern and r3_action_minjae:

                scene bg_11_blur with dissolve
                show m1 at left_stage with dissolve

                "민재가 바로 입을 열었다."

                m "거봐. 자기가 편하다잖아."

                "그러다 내 시선과 마주치자 말을 조금 줄였다."

                m "…뭐, 다음에는 물어보든가."

                "민재는 활동지에 하린이 이름을 적었다."

                hide m1 with dissolve
                scene bg_11 with dissolve

            else:

                scene bg_11_blur with dissolve
                show m7 at left_stage with dissolve

                "민재가 기다렸다는 듯 바로 끼어들었다."

                m "거봐."
                m "하린이도 이게 편하다잖아."

                s "그래도 다음에는 먼저 물어보자고."

                m "아니, 본인이 괜찮다는데 왜 자꾸 그래?"

                "민재는 하린이 쪽으로 활동지를 돌렸다."

                m "그치?"

                "하린이는 아무 대답 없이 활동지만 바라봤다."

                hide m7 with dissolve
                scene bg_11 with dissolve

            n "(하린이가 괜찮다고 말하니까,"
            n "민재는 그 말을 바로 자기 쪽에 유리하게 쓰고 있어.)"


        else:

            # ----------------------------------------------------------
            # 소윤 협조 X + 하린이 아직 위축
            # ----------------------------------------------------------

            if key4_minjae_pattern and r3_action_minjae:

                scene bg_11_blur with dissolve
                show m7 at left_stage with dissolve

                "민재가 하린이의 대답을 듣자 바로 활동지를 자기 쪽으로 당겼다."

                m "그래. 그럼 됐네."

                "그러다 나를 한번 힐끗 바라봤다."

                m "본인이 편하다잖아."

                "말투는 전보다 조심스러웠지만,"
                "결국 역할은 민재가 처음 정한 그대로 적혔다."

                hide m7 with dissolve
                scene bg_11 with dissolve

            else:

                scene bg_11_blur with dissolve
                show m7 at left_stage with dissolve

                "민재가 피식 웃었다."

                m "거봐."
                m "괜히 사람 불편하게 왜 자꾸 물어봐."

                "민재는 하린이의 대답을 기다렸다는 듯 활동지에 바로 역할을 적었다."

                m "하린이는 자료."
                m "이제 됐지?"

                "하린이는 아무 말도 하지 않았다."

                hide m7 with dissolve
                scene bg_11 with dissolve

                "그 뒤로 누구도 다시 하린이에게 의견을 묻지 않았다."

            n "(결국 이번에도 민재가 정한 대로 됐어.)"

    jump r3_s3_lunch
# ----------------------------------------------------------
# R3-S3. 3회차 점심시간 — 균열의 시작
# ----------------------------------------------------------

label r3_s3_lunch:

    scene black with fade
    pause 0.8

    play sound "audio/bell.mp3"

    scene bg_5 with fade

    "4교시가 끝나고 점심시간이 되었다."

    "급식실은 평소처럼 아이들 목소리와 식판 소리로 시끄러웠다."

    stop sound fadeout 1.0

    "배식을 받고 돌아선 나는 제일 먼저 6인용 테이블 쪽을 확인했다."

    scene bg_6 with dissolve

    "민재, 예서, 준호, 소윤이가 이미 자리를 잡고 있었다."

    "그리고 하린이가 앉아야 할 자리에는"
    "이번에도 예서의 겉옷이 놓여 있었다."

    n "(또 똑같아.)"

    scene bg_5_blur with dissolve
    show h3 at center_stage with dissolve

    "잠시 뒤 하린이가 식판을 들고 다가왔다."

    "하린이는 자기 자리에 놓인 겉옷을 보고 잠깐 멈췄다."

    "하지만 아무도 겉옷을 치우지 않았다."

    "하린이는 잠시 서 있다가 몸을 돌려 급식실 구석 자리로 향했다."

    hide h3 with dissolve

    scene bg_5 with dissolve

    "나는 식판을 고쳐 들었다."

    "이번에는 하린이가 혼자 앉는 걸 멀리서 보고만 있지 않았다."

    "곧바로 하린이 쪽으로 걸어갔다."


    # ----------------------------------------------------------
    # 1. 하린이의 초기 반응
    # ----------------------------------------------------------

    if trust_harin >= 5:

        scene bg_6_blur with dissolve
        show h16 at center_stage with dissolve

        "내가 다가가자 하린이가 고개를 들었다."

        n "여기 앉아도 돼?"

        "하린이는 잠깐 나를 바라보다가 맞은편 빈 의자를 조금 빼주었다."

        h "…응."

        hide h16 with dissolve
        scene bg_6 with dissolve

        "나는 하린이 맞은편에 식판을 내려놓았다."

    else:

        scene bg_6_blur with dissolve
        show h5 at center_stage with dissolve

        "내가 다가가자 하린이가 의아한 얼굴로 나를 바라봤다."

        n "나 여기 앉아도 돼?"

        h "…왜?"

        n "그냥 여기서 먹으려고."

        "하린이는 잠시 망설이다 작게 고개를 끄덕였다."

        h "…응."

        hide h5 with dissolve
        scene bg_6 with dissolve

        "나는 하린이 맞은편에 식판을 내려놓았다."

    "둘이 조용히 밥을 먹기 시작한 지 얼마 지나지 않았을 때였다."


    # ----------------------------------------------------------
    # 2. 소윤이의 행동
    # ----------------------------------------------------------

    if f_r3_soyoon_coop:

        # ----------------------------------------------------------
        # 소윤이가 먼저 작은 행동을 시작함
        # ----------------------------------------------------------

        "멀리 떨어진 6인용 테이블에서 의자 끄는 소리가 났다."

        "고개를 들어보니 소윤이가 식판을 든 채 자리에서 일어나 있었다."

        "그런데 소윤이는 바로 움직이지 못했다."

        "예서가 소윤이를 올려다봤다."

        scene bg_6_blur with dissolve
        show y9 at center_stage with dissolve

        y "야, 이소윤."
        y "어디 가?"

        hide y9 with dissolve

        show s11 at center_stage with dissolve

        "소윤이는 식판을 든 채 잠깐 굳었다."

        s "아… 나는…."

        "말끝이 흐려졌다."

        "소윤이와 눈이 마주쳤다."

        "나는 아무 말 없이 내 옆의 빈 의자를 조금 빼놓았다."

        n "소윤아."

        "소윤이가 나를 바라봤다."

        n "여기 자리 있어."

        "소윤이는 잠깐 그대로 서 있었다."

        "그러고는 예서 쪽을 한번 돌아본 뒤 다시 입을 열었다."

        s "…나 저기서 먹을게."

        hide s11 with dissolve
        scene bg_6 with dissolve

        "소윤이는 식판을 들고 우리 쪽으로 걸어왔다."


        # ----------------------------------------------------------
        # 하린이에게 먼저 묻기
        # ----------------------------------------------------------

        scene bg_6_blur with dissolve
        show s9 at center_stage with dissolve

        "우리 테이블 앞에 도착한 소윤이는 바로 앉지 않았다."

        s "하린아."

        "하린이가 소윤이를 올려다봤다."

        s "나 여기 앉아도 돼?"

        if trust_harin >= 5:

            "하린이는 조금 놀란 얼굴로 소윤이를 바라봤다."

            "잠시 뒤 빈 의자를 한번 보고 작게 고개를 끄덕였다."

            h "…응."

        else:

            "하린이는 바로 대답하지 않았다."

            "소윤이도 재촉하지 않고 기다렸다."

            "나 역시 아무 말도 하지 않았다."

            "잠시 뒤 하린이가 작게 대답했다."

            h "…응."

        hide s9 with dissolve
        scene bg_6 with dissolve

        "그제야 소윤이가 빈 의자에 식판을 내려놓았다."

        "소윤이는 아직 조금 어색한 듯 숟가락만 만지작거렸다."

        n "왔네."

        "소윤이가 나를 힐끗 바라봤다."

        s "…응."


        # ----------------------------------------------------------
        # 3. 민재의 반응
        # ----------------------------------------------------------

        if key4_minjae_pattern and r3_action_minjae:

            "잠시 뒤 민재도 소윤이가 자리를 옮긴 걸 알아챘다."

            scene bg_6_blur with dissolve
            show m7 at center_stage with dissolve

            m "야, 이소윤."
            m "갑자기 왜 거기 가?"

            "소윤이의 손이 잠깐 멈췄다."

            "나는 아무 말 없이 민재를 바라봤다."

            "민재도 나를 쳐다봤다."

            "아침에 복도에서 나눴던 이야기를 신경 쓰는 듯 잠깐 입을 다물었다."

            m "…아, 됐어."
            m "맘대로 해."

            hide m7 with dissolve
            scene bg_6 with dissolve

            "민재는 투덜거리며 다시 자기 식판으로 시선을 돌렸다."

            "소윤이는 잠깐 나를 바라보다 다시 숟가락을 들었다."

        else:

            "잠시 뒤 민재도 소윤이가 자리를 옮긴 걸 알아챘다."

            scene bg_6_blur with dissolve
            show m7 at center_stage with dissolve

            m "야, 이소윤."
            m "갑자기 왜 오하린이랑 먹냐?"

            "민재의 목소리에 근처 아이들 몇 명도 이쪽을 바라봤다."

            hide m7 with dissolve

            scene bg_6_blur with dissolve
            show s11 at center_stage with dissolve

            "소윤이는 숟가락을 들다 멈췄다."

            s "나는 그냥…."

            "아까처럼 말끝이 다시 흐려졌다."

            n "같이 밥 먹는 건데 왜?"

            "민재가 이번에는 나를 쳐다봤다."

            scene bg_6_blur with dissolve
            show m7 at center_stage with dissolve

            m "너한테 물어본 거 아닌데?"

            n "그래도 소윤이가 여기서 먹고 싶어서 온 거잖아."

            "잠깐 정적이 흘렀다."

            hide m7 with dissolve

            show s11 at center_stage with dissolve

            "소윤이는 나를 한번 보고 숨을 작게 들이마셨다."

            s "…응."

            s "나 여기서 먹을 거야."

            hide s11 with dissolve

            show m7 at center_stage with dissolve

            "민재는 소윤이를 잠시 노려보듯 바라봤다."

            m "아, 그래."
            m "맘대로 해."

            hide m7 with dissolve
            scene bg_6 with dissolve

            "민재는 못마땅한 티를 내면서도 더 말하지 않았다."

            "소윤이는 그제야 다시 숟가락을 들었다."


        # ----------------------------------------------------------
        # 4. 세 사람이 함께 먹는 동안
        # ----------------------------------------------------------

        if trust_harin >= 5:

            "처음에는 셋 다 거의 말이 없었다."

            "그러다 소윤이가 반찬 하나를 젓가락으로 가리켰다."

            s "이거 오늘 엄청 맵지 않아?"

            n "맞아. 나도 아까 먹고 놀랐어."

            "하린이는 두 사람의 이야기를 듣다가 반찬을 한번 바라봤다."

            h "…난 괜찮던데."

            n "진짜?"

            "하린이가 아주 작게 웃었다."

            "그 뒤로도 긴 이야기가 오가지는 않았다."

            "그래도 하린이는 식사가 끝날 때까지 먼저 자리를 뜨지 않았다."

        else:

            "소윤이가 합류한 뒤에도 한동안 아무도 말을 하지 않았다."

            "하린이는 여전히 식판만 내려다보고 있었다."

            "소윤이도 괜히 말을 꺼내지 않았다."

            "나는 둘 사이의 정적을 억지로 채우지 않았다."

            "조금 시간이 지나서야 하린이가 다시 숟가락을 들었다."

            n "(아직 바로 편해질 수는 없겠지.)"

            n "(그냥 기다리자.)"


    else:

        # ----------------------------------------------------------
        # 소윤이가 아직 자리에서 움직이지 않는 경우
        # ----------------------------------------------------------

        "나는 밥을 먹다가 6인용 테이블 쪽을 한번 바라봤다."

        "소윤이는 여전히 예서 옆에 앉아 있었다."

        if r3_action_soyun:

            "소윤이는 몇 번이나 우리 쪽을 바라봤다."

            "한번은 식판을 들려는 듯 손을 움직였다가 다시 내려놓았다."

            "예서가 무언가 말하자 소윤이는 다시 고개를 숙였다."

            "결국 자리에서 일어나지는 않았다."

            n "(아침에 이야기했어도 바로 움직이기는 어려운가 봐.)"

        else:

            "소윤이는 민재와 예서의 이야기를 듣다가 가끔 우리 쪽을 바라봤다."

            "하지만 잠시 뒤 다시 원래 자리로 시선을 돌렸다."

            n "(이번에도 소윤이는 저 자리에 남아 있네.)"


        # ----------------------------------------------------------
        # 하린이와 둘만 먹는 경우
        # ----------------------------------------------------------

        if trust_harin >= 5:

            "잠시 조용히 밥을 먹던 하린이가 먼저 입을 열었다."

            scene bg_6_blur with dissolve
            show h25 at center_stage with dissolve

            h "…너 친구들이랑 안 먹어도 돼?"

            n "응."

            n "내가 여기서 먹고 싶어서 온 거야."

            "하린이는 잠시 나를 바라봤다."

            h "…그래."

            hide h25 with dissolve
            scene bg_6 with dissolve

            "하린이는 다시 밥을 먹기 시작했다."

            "조금 뒤에는 먼저 반찬 이야기를 한마디 꺼내기도 했다."

        else:

            "멀리서 웃음소리가 크게 들릴 때마다 하린이는 잠깐씩 숟가락을 멈췄다."

            "결국 식판에는 밥이 꽤 남아 있었다."

            n "더 안 먹어?"

            scene bg_6_blur with dissolve
            show h16 at center_stage with dissolve

            h "응… 그냥 배불러."

            hide h16 with dissolve
            scene bg_6 with dissolve

            n "알겠어."

            "나는 더 먹으라고 재촉하지 않았다."


    # ----------------------------------------------------------
    # 5. 점심시간 마무리
    # ----------------------------------------------------------

    scene bg_5 with dissolve

    "주변 아이들이 하나둘 식판을 들고 퇴식구로 향하기 시작했다."

    "우리도 자리에서 일어났다."


    if f_r3_soyoon_coop:

        if trust_harin >= 5:

            "나와 소윤이가 먼저 식판을 들었다."

            "하린이도 곧 자리에서 일어났다."

            "퇴식구를 나온 뒤에도 세 사람은 자연스럽게 같은 방향으로 걸었다."

        else:

            "하린이는 우리보다 조금 뒤에서 걸었다."

            "나와 소윤이는 먼저 가버리지 않고 천천히 걸었다."

            "잠시 뒤 하린이도 비슷한 속도로 우리 옆까지 따라왔다."

    else:

        if trust_harin >= 5:

            "복도로 나오자 하린이가 이번에는 먼저 내 옆에 섰다."

            "우리는 별말 없이 나란히 교실 쪽으로 걸었다."

        else:

            "하린이는 여전히 나보다 조금 뒤에서 걸었다."

            "나는 앞서가지 않고 하린이 속도에 맞췄다."


    scene bg_7 with dissolve

    "점심시간 하나가 지났을 뿐이었다."

    "아직 그대로인 것도 많았다."

    "그래도 이번에는 하린이가 혼자 밥을 먹게 두지는 않았다."

    if f_r3_soyoon_coop:

        "그리고 소윤이도 처음부터 씩씩했던 건 아니었다."

        "자리에서 일어나고도 망설였고,"
        "민재가 말을 걸었을 때는 다시 대답하지 못했다."

        "그래도 내가 옆에서 한마디 보태자,"
        "이번에는 다시 자기 입으로 말을 이어갔다."

        n "(소윤이가 혼자 다 해내게 할 필요는 없어.)"
        n "(옆에서 같이 움직이면 돼.)"

    n "(다음은 체육 시간이야.)"

    "지난번에는 체육 시간에도 하린이가 계속 혼자 남았다."

    n "(이번에는 그런 일이 생긴 다음에 움직이지 말자.)"
    n "(먼저 보고, 먼저 움직이자.)"

    jump r3_s4_pe

# ----------------------------------------------------------
# R3-S4. 3회차 체육 시간 — 균열의 증명
# ----------------------------------------------------------

label r3_s4_pe:

    $ talk_pe_minjae = False
    $ talk_pe_soyun = False
    $ talk_pe_harin = False
    $ note_witness = False

    scene bg_12 with fade

    "오후 체육 시간."

    "선생님이 오시기 전까지 잠깐 자유 시간이 주어졌다."

    "지난번에는 하린이가 혼자 남은 뒤에야 그 사실을 알아차렸다."

    "이번에는 수업이 시작되기 전부터 운동장 여기저기를 살폈다."

    n "(또 무슨 일이 생긴 다음에 움직이지 말자.)"


label inv_pe_r3:

    call screen pe_investigation_r3


    # ----------------------------------------------------------
    # 민재 확인
    # ----------------------------------------------------------

    if _return == "minjae_r3":

        $ talk_pe_minjae = True

        scene bg_12 with fade
        scene bg_12_blur with dissolve
        show m3 at center_stage with dissolve

        "민재는 준호와 함께 운동장에 굴러다니던 축구공을 주고받고 있었다."

        if key4_minjae_pattern and r3_action_minjae:

            "떠들던 민재가 우연히 나와 눈이 마주쳤다."

            "민재는 잠깐 내 쪽을 보더니 다시 공을 찼다."

            "조금 뒤 준호가 하린이 쪽을 보며 뭔가 말하자,"
            "민재도 따라 보려다가 다시 내 쪽을 한번 확인했다."

            hide m3 with dissolve
            scene bg_12 with dissolve

            n "(아침에 한 말을 아직 신경 쓰고 있네.)"

            n "(그렇다고 완전히 그만둔 건 아니야.)"

        else:

            "민재는 준호와 큰소리로 웃으며 공을 찼다."

            "그러다 몇 번 주변을 둘러봤고,"
            "하린이가 있는 쪽에도 자연스럽게 시선이 갔다."

            hide m3 with dissolve
            scene bg_12 with dissolve

            n "(아직은 평소랑 크게 달라진 게 없어 보여.)"

        jump inv_pe_r3


    # ----------------------------------------------------------
    # 소윤 확인
    # ----------------------------------------------------------

    elif _return == "soyoon_r3":

        $ talk_pe_soyun = True

        scene bg_12 with fade

        if f_r3_soyoon_coop:

            scene bg_12_blur with dissolve
            show s3 at center_stage with dissolve

            "소윤이는 예서와 몇 걸음 떨어진 곳에 서 있었다."

            "예서가 말을 걸면 대답은 했지만,"
            "아까 점심시간처럼 계속 그 자리에 붙어 있지는 않았다."

            "그러다 하린이 쪽을 한번 바라봤다."

            "나와 눈이 마주치자 소윤이는 잠깐 멈칫했다."

            "하지만 이번에는 바로 시선을 피하지 않았다."

            hide s3 with dissolve
            scene bg_12 with dissolve

            n "(아직 편해 보이진 않아.)"

            n "(그래도 이번에는 그냥 모른 척하고 있지는 않아.)"

        else:

            scene bg_12_blur with dissolve
            show s8 at center_stage with dissolve

            "소윤이는 예서 옆에서 이야기를 듣고 있었다."

            "예서가 웃자 소윤이도 잠깐 따라 웃었다."

            "그러다 하린이 쪽을 한번 바라봤다."

            "하린이와 눈이 마주칠 것 같자 소윤이는 다시 예서 쪽으로 고개를 돌렸다."

            hide s8 with dissolve
            scene bg_12 with dissolve

            if r3_action_soyun:

                n "(아침에 이야기했는데도 아직 저 자리에서 움직이진 못했어.)"

            else:

                n "(이번에도 신경은 쓰고 있는 것 같은데….)"

        jump inv_pe_r3


    # ----------------------------------------------------------
    # 하린 확인
    # ----------------------------------------------------------

    elif _return == "harin_r3":

        $ talk_pe_harin = True

        scene bg_12 with fade
        scene bg_12_blur with dissolve
        show h3 at center_stage with dissolve

        "하린이는 구령대 근처에 혼자 앉아 신발 끈을 다시 묶고 있었다."

        "그때 민재가 굴러온 공을 주우러 하린이 쪽으로 다가왔다."

        "민재는 공을 집어 들고 지나가면서 하린이 옆에 무언가를 툭 떨어뜨렸다."

        hide h3 with dissolve
        scene bg_12 with dissolve

        "작게 구겨진 종이였다."

        n "(뭐지?)"

        scene bg_12_blur with dissolve
        show h3 at center_stage with dissolve

        "하린이도 종이를 발견했다."

        "하린이는 민재가 멀어지는 쪽을 한번 바라본 뒤,"
        "서둘러 종이를 주워 손안에 감췄다."

        "주변을 한번 확인한 하린이는 그것을 체육복 주머니에 넣었다."

        hide h3 with dissolve
        scene bg_12 with dissolve

        $ note_witness = True

        n "(민재가 일부러 떨어뜨린 것 같은데….)"

        n "(저게 뭔지 하린이한테 물어봐야겠어.)"

        jump inv_pe_r3


    # ----------------------------------------------------------
    # 조사 종료
    # ----------------------------------------------------------

    elif _return == "finish_pe":

        if not note_witness:

            scene bg_12 with fade

            n "(잠깐.)"
            n "(하린이 쪽은 아직 제대로 못 봤어.)"

            jump inv_pe_r3

        else:

            scene bg_12 with fade

            play sound "audio/whistle.mp3"

            "삐익—."

            "수업 시작을 알리는 선생님의 호루라기 소리가 울렸다."

            stop sound fadeout 1.0

            "아이들이 하나둘 선생님 앞으로 모이기 시작했다."

            n "(쪽지는 수업이 끝나기 전에 확인해봐야 해.)"

            jump r3_s4_partner_event


    else:

        jump inv_pe_r3
# ----------------------------------------------------------
# [핵심 이벤트] 짝꿍 정하기와 쪽지의 진실
# ----------------------------------------------------------

label r3_s4_partner_event:

    scene bg_12_blur with dissolve
    show pt1 at center_stage with dissolve

    pt "자, 두 명씩 짝지어서 스트레칭부터 한다."
    pt "남는 사람 없게 빨리 짝 정해!"

    hide pt1 with dissolve
    scene bg_12 with dissolve

    "아이들이 익숙하게 자기 친구를 찾아 움직이기 시작했다."

    "지난번에는 하린이가 마지막까지 혼자 남은 뒤에야 다가갔다."

    "이번에는 기다리지 않았다."

    "나는 곧바로 하린이 쪽으로 걸어갔다."

    scene bg_12_blur with dissolve
    show h3 at center_stage with dissolve

    n "하린아, 나랑 하자."

    "하린이가 나를 올려다봤다."

    if trust_harin >= 5:

        "하린이는 잠시 나를 바라보다 작게 고개를 끄덕였다."

        h "…응."

    else:

        "하린이는 조금 놀란 얼굴이었지만 거절하지 않았다."

        h "…그래."

    hide h3 with dissolve
    scene bg_12 with dissolve


    # ----------------------------------------------------------
    # 소윤 협력 루트
    # ----------------------------------------------------------

    if f_r3_soyoon_coop:

        "그때 뒤쪽에서 소윤이가 우리 쪽으로 몇 걸음 다가왔다."

        "하지만 가까이 와서는 선뜻 말을 꺼내지 못했다."

        scene bg_12_blur with dissolve
        show s3 at center_stage with dissolve

        "소윤이는 나와 하린이를 번갈아 바라봤다."

        s "저기…."

        "나는 소윤이가 무슨 말을 하려는지 알아차렸다."

        n "소윤아, 같이 할래?"

        s "어?"

        n "셋이 번갈아 하면 되잖아."
        n "선생님한테 한번 물어보자."

        "소윤이는 잠깐 망설이다 하린이 쪽을 바라봤다."

        s "하린아."
        s "너도 괜찮아?"

        if trust_harin >= 5:

            "하린이는 소윤이를 바라보다 작게 고개를 끄덕였다."

            h "…응."

        else:

            "하린이는 바로 대답하지 않았다."

            "소윤이도 더 재촉하지 않았다."

            "잠시 뒤 하린이가 조용히 대답했다."

            h "…응."

        hide s3 with dissolve
        scene bg_12 with dissolve

        "나는 체육 선생님 쪽으로 손을 들었다."

        n "선생님, 저희 셋이 번갈아 해도 돼요?"

        scene bg_12_blur with dissolve
        show pt1 at center_stage with dissolve

        pt "셋?"
        pt "그래. 한 명씩 놀지만 말고 번갈아 해."

        hide pt1 with dissolve
        scene bg_12 with dissolve

        "그제야 소윤이가 우리 옆에 섰다."

        "예서와 민재 쪽에 있던 몇몇 아이들이 이쪽을 한번 쳐다봤다."

        if trust_harin >= 5:

            "처음에는 조금 어색했지만,"
            "셋은 순서를 바꿔가며 스트레칭을 시작했다."

        else:

            "하린이는 아직 말이 없었다."

            "나와 소윤이도 억지로 말을 걸지 않고 차례만 맞춰 움직였다."


    # ----------------------------------------------------------
    # 소윤 비협력 루트
    # ----------------------------------------------------------

    else:

        "나와 하린이는 마주 보고 스트레칭을 시작했다."

        "멀리서 소윤이가 우리 쪽을 한번 바라봤다."

        if r3_action_soyun:

            "소윤이는 잠깐 망설이는 듯했지만,"
            "결국 예서가 부르자 그쪽으로 걸어갔다."

        else:

            "소윤이는 그대로 예서 쪽으로 가 짝을 정했다."

        if trust_harin >= 5:

            "하린이는 잠깐 소윤이 쪽을 바라봤다가 다시 내 쪽으로 시선을 돌렸다."

            n "자, 이번엔 반대쪽."

            h "…응."


    # ----------------------------------------------------------
    # 체육 수업 종료
    # ----------------------------------------------------------

    "그 뒤로 스트레칭이 끝나고 배드민턴 수업이 이어졌다."

    "한참 셔틀콕이 오간 뒤,"
    "수업 종료를 알리는 호루라기 소리가 울렸다."

    "아이들은 라켓과 셔틀콕을 정리함에 넣기 시작했다."

    "나도 라켓을 정리한 뒤 하린이 쪽을 바라봤다."

    "아까 민재가 떨어뜨린 쪽지가 계속 마음에 걸렸다."


    # ----------------------------------------------------------
    # 쪽지 확인
    # ----------------------------------------------------------

    scene black with fade
    pause 0.5

    scene bg_7 with fade

    "아이들이 무리를 지어 교실로 올라갔다."

    "나는 일부러 조금 천천히 걸어 하린이 옆에 섰다."

    if f_r3_soyoon_coop:

        "앞서가던 소윤이가 한번 뒤를 돌아봤다."

        "나는 잠깐 하린이 쪽을 보고는 소윤이에게 먼저 가라는 듯 고개를 끄덕였다."

        "소윤이는 잠시 우리를 바라보다 먼저 계단을 올라갔다."

    "주변 아이들이 조금 멀어진 뒤에야 나는 목소리를 낮췄다."

    n "하린아."

    n "아까 민재가 네 옆에 떨어뜨린 거 있잖아."

    n "그거… 뭐였어?"

    "하린이의 걸음이 잠깐 멈췄다."

    "하린이는 바로 대답하지 않았다."

    n "말하기 싫으면 안 보여줘도 돼."

    "잠시 뒤 하린이는 주머니에 손을 넣었다."

    "그리고 구겨진 종이 한 장을 천천히 꺼냈다."

    "삐뚤빼뚤하게 적힌 글씨가 보였다."

    "『야, 다 장난인 거 알지?"

    "그러니까 괜히 예민하게 받아들이지 말고,"

    "분위기 흐리지는 말자.』"

    "마지막 문장에서 눈이 멈췄다."

    n "(분위기 흐리지는 말자….)"

    "지난번 수요일,"
    "하린이 자리 근처에서 발견했던 쪽지에 적혀 있던 말이었다."

    n "(그때 봤던 쪽지가 이거였구나.)"

    "앞에는 장난이라고 적혀 있었지만,"
    "뒤에는 하린이가 불편하다고 말하지 못하게 만드는 문장이 붙어 있었다."

    "하린이는 내가 쪽지를 읽는 동안 아무 말도 하지 않았다."


    # ----------------------------------------------------------
    # 하린이에게 어떻게 반응할지
    # ----------------------------------------------------------

    menu:

        "이거… 너는 어떻게 하고 싶어? 지금 바로 정하지 않아도 돼.":

            $ trust_harin += 2

            scene bg_7_blur with dissolve
            show h5 at center_stage with dissolve

            "하린이는 한동안 쪽지만 바라봤다."

            h "…잘 모르겠어."

            h "애들은 계속 장난이라고 하니까."

            h "근데 나는 싫었어."

            "하린이는 잠깐 말을 멈췄다."

            h "싫다고 하면 내가 이상한 애 되는 것 같고…."

            h "괜히 나 때문에 애들 분위기 이상해질까 봐."

            hide h5 with dissolve
            scene bg_7 with dissolve

            n "싫었으면 싫었던 거지."

            n "지금 당장 뭘 해야 할지 정하지 않아도 돼."

            n "근데 이걸 네가 혼자 참고 있을 필요는 없어."

            "하린이는 말없이 쪽지를 내려다봤다."

            n "선생님한테 말하는 것도,"
            n "어떻게 말할지도 같이 생각해보자."

            n "그리고 오늘은 나랑 같이 가자."

            n "혼자 가지 말고."

            scene bg_7_blur with dissolve
            show h16 at center_stage with dissolve

            "하린이는 잠시 나를 바라봤다."

            h "…같이?"

            n "응."

            "잠시 뒤 하린이가 작게 고개를 끄덕였다."

            h "…응."

            hide h16 with dissolve
            scene bg_7 with dissolve

            $ f_r3_stay_together = True


        "이건 선생님께 보여드리는 게 좋을 것 같아. 지금 같이 가자.":

            $ trust_harin -= 1

            scene bg_7_blur with dissolve
            show h4 at center_stage with dissolve

            "하린이는 바로 고개를 저었다."

            h "안 돼."

            n "근데 이건 그냥 장난이 아니잖아."

            h "아니, 그냥…."

            "하린이는 급하게 쪽지를 접어 자기 손에 쥐었다."

            h "지금은 싫어."

            h "제발 그냥 모른 척해 줘."

            hide h4 with dissolve
            scene bg_7 with dissolve

            "나는 뒤늦게 입을 다물었다."

            n "(선생님께 알리는 게 잘못된 건 아니야.)"

            n "(하지만 하린이한테 어떻게 하고 싶은지 묻기도 전에 내가 먼저 정해버렸어.)"

            "하린이는 쪽지를 다시 주머니에 넣었다."

            "조금 전보다 나와 거리를 두고 걷기 시작했다."


    # ----------------------------------------------------------
    # 장면 마무리
    # ----------------------------------------------------------

    "우리는 다시 교실 쪽으로 걸었다."

    if f_r3_stay_together:

        "하린이는 여전히 말이 많지 않았다."

        "그래도 계단을 올라가는 동안 내 옆에서 멀어지지는 않았다."

        n "(이번에는 알아낸 뒤에 끝내지 말자.)"

        n "(하린이가 혼자 감당하게 두지 않는 것부터 하자.)"

    else:

        "하린이는 내 옆을 걷고 있었지만,"
        "아까보다 말이 더 줄어 있었다."

        n "(도와주겠다는 마음만으로 되는 건 아니구나.)"

        n "(하린이 말을 먼저 들어야 해.)"

    jump r3_s6_afterschool
label r3_s6_afterschool:

    scene bg_14 with fade

    "종례가 끝나자 아이들이 하나둘 교실을 빠져나갔다."

    "나도 가방을 메고 하린이 자리로 갔다."

    if f_r3_stay_together:

        n "같이 가자."

        "하린이는 잠깐 나를 바라보다 가방을 들었다."

        h "…응."

    "교실에는 어느새 몇 명만 남아 있었다."

    "뒤쪽에는 민재와 예서가 가방을 멘 채 서 있었다."

    if f_r3_soyoon_coop:

        "소윤이도 가방을 멘 채 내 근처에 남아 있었다."

    "우리가 뒷문 쪽으로 향하려던 순간이었다."

    m "야, 오하린."

    "하린이의 걸음이 멈췄다."

    scene bg_14_blur with dissolve
    show m7 at center_stage with dissolve

    m "이거 봐."

    hide m7 with dissolve
    scene bg_14 with dissolve

    "민재가 휴대폰을 꺼내 화면을 몇 번 두드렸다."

    "곧 휴대폰 화면이 우리 쪽으로 돌아왔다."

    "체육 시간에 넘어져 있던 하린이의 사진이었다."

    "지난번에는 아이들 사이에서 웃음거리로 돌았던 사진."

    "이번에는 점심시간 내내 하린이 곁에 있었기 때문에,"
    "아직 꺼내지 못했던 사진이었다."

    scene bg_14_blur with dissolve
    show m7 at left_stage with dissolve
    show y3 at right_stage with dissolve

    "예서가 화면을 보자마자 웃음을 터뜨렸다."

    y "아, 이거 진짜 웃긴데."

    m "그치?"

    m "이거 단톡에 올리면 애들 반응 대박일 것 같은데."

    y "올려 봐."

    "둘은 하린이가 바로 앞에 있는 것도 잊은 것처럼 사진을 보며 웃었다."

    "하린이는 아무 말도 하지 않았다."

    "민재가 그제야 하린이를 바라봤다."

    m "왜."

    m "너도 웃기지 않아?"

    "하린이는 여전히 대답하지 않았다."

    "그러자 민재가 피식 웃었다."

    m "아, 또 왜 그렇게 정색해."

    m "그냥 장난이잖아."

    y "그러니까."
    y "우리끼리 웃자고 하는 건데 뭘."

    "하린이는 가방끈만 꼭 쥔 채 시선을 내렸다."

    m "괜히 그렇게 있으면 우리가 뭐 나쁜 짓 한 것 같잖아."

    hide m7
    hide y3
    with dissolve

    scene bg_14 with dissolve

    "그 말을 듣는 순간, 체육 시간에 본 쪽지가 떠올랐다."

    n "(분위기 흐리지는 말자….)"

    "하린이는 아무것도 하지 않았다."

    "싫다고 말한 것도 아니고, 화를 낸 것도 아니었다."

    "그런데도 민재와 예서는 자기들이 웃는 쪽에 하린이까지 맞춰야 하는 것처럼 말했다."

    n "(자기들은 장난이라고 정해 놓고,)"
    n "(하린이가 같이 웃지 않으면 오히려 하린이가 이상한 사람이 되는 거야.)"
    # ----------------------------------------------------------
    # 하린의 반응
    # ----------------------------------------------------------

    if trust_harin >= 5 and f_r3_soyoon_coop:

        "하린이는 한동안 민재의 휴대폰만 바라봤다."

        "손에 쥔 가방끈이 조금씩 구겨졌다."

        "그러다 하린이가 천천히 고개를 들었다."

        scene bg_14_blur with dissolve
        show h21 at center_stage with dissolve

        h "…난 안 웃겨."

        "민재의 표정이 잠깐 멈췄다."

        h "그 사진 싫어."

        h "지워줘."

        hide h21 with dissolve

        scene bg_14_blur with dissolve
        show m7 at left_stage with dissolve
        show y4 at right_stage with dissolve

        m "뭐?"

        m "야, 그냥 사진 한 장 가지고 왜 그래."

        y "그러니까. 누가 보면 진짜 뭐 한 줄 알겠다."

        scene bg_14 with dissolve

        "하린이는 다시 고개를 숙이지 않았다."

        n "하린이가 싫다고 했잖아."

        n "그럼 지우면 되는 거 아니야?"

        "민재가 나를 노려봤다."

        m "너는 또 왜 끼어드는데?"

        if f_r3_soyoon_coop:

            "옆에 있던 소윤이가 움찔했다."

            "민재와 눈이 마주치자 잠깐 시선을 내렸지만,"
            "이번에는 그대로 물러서지는 않았다."

            scene bg_14_blur with dissolve
            show s11 at center_stage with dissolve

            s "…나도."

            "민재와 예서가 소윤이를 바라봤다."

            s "나도 그거 별로 안 웃겨."

            y "뭐?"

            s "하린이가 싫다잖아."

            "소윤이는 마지막 말을 하고 나서 내 쪽을 한번 바라봤다."

            "나는 소윤이 옆으로 한 걸음 가까이 섰다."

            n "그냥 지워."

            hide s11 with dissolve
            scene bg_14 with dissolve

        if key4_minjae_pattern and r3_action_minjae:

            "민재는 무슨 말을 더 하려다가 나와 눈이 마주쳤다."

            "아침부터 내가 자기 행동을 계속 보고 있었다는 걸 떠올린 듯 잠깐 입을 다물었다."

            scene bg_14_blur with dissolve
            show m7 at center_stage with dissolve

            m "아, 진짜."

            m "장난 좀 친 걸 가지고 다들 왜 이래."

            "민재는 투덜거리며 휴대폰 화면을 몇 번 눌렀다."

            m "됐냐?"

            n "지운 거 보여줘."

            m "아, 지웠다고."

            "민재는 짜증스럽게 화면을 내보였다."

            hide m7 with dissolve

            $ trust_minjae += 2

        else:

            scene bg_14_blur with dissolve
            show m10 at center_stage with dissolve

            m "진짜 웃긴다."

            m "아까까지만 해도 아무 말도 안 하더니 갑자기 왜 다 이래?"

            n "아무 말 안 했다고 좋아했다는 뜻은 아니잖아."

            "민재는 대꾸하지 못하고 입술을 삐죽였다."

            y "야, 그냥 지워."
            y "귀찮아."

            "예서가 먼저 몸을 돌렸다."

            "민재는 못마땅한 얼굴로 휴대폰을 몇 번 누른 뒤 주머니에 집어넣었다."

            hide m10 with dissolve

        scene bg_14 with dissolve

        "민재는 끝까지 자신이 뭘 잘못했는지는 인정하지 않았다."

        m "됐지? 이제?"

        "그러고는 예서와 함께 교실을 나갔다."

        "문이 닫힌 뒤에도 한동안 아무도 말을 하지 않았다."

        "하린이는 민재가 나간 문을 바라보다가 천천히 숨을 내쉬었다."

        n "(이번에는 하린이가 자기 입으로 싫다고 말했어.)"

        n "(그리고 혼자 말하게 두지도 않았어.)"

        jump r3_s7_final_bathroom_talk


    elif trust_harin >= 5:

        # ----------------------------------------------------------
        # 하린의 신뢰는 높지만 소윤의 협력은 없는 경우
        # ----------------------------------------------------------

        "하린이는 휴대폰 화면을 한동안 바라봤다."

        "그러다 아주 작지만 분명한 목소리로 말했다."

        scene bg_14_blur with dissolve
        show h21 at center_stage with dissolve

        h "…그 사진 지워줘."

        hide h21 with dissolve

        show m7 at center_stage with dissolve

        m "왜?"

        m "뭐가 그렇게 싫은데?"

        "하린이는 잠시 입을 다물었다."

        scene bg_14_blur with dissolve
        show h21 at center_stage with dissolve

        h "그냥 싫어."

        h "내 사진이잖아."

        hide h21 with dissolve
        scene bg_14 with dissolve

        "민재가 헛웃음을 쳤다."

        m "와, 진짜 별걸 다 가지고 그러네."

        n "별거 아니면 그냥 지워."

        "민재가 이번에는 나를 바라봤다."

        n "하린이가 싫다고 했잖아."

        if key4_minjae_pattern and r3_action_minjae:

            "민재는 바로 받아치려다가 잠깐 멈췄다."

            "그러고는 혀를 차며 휴대폰을 내려다봤다."

            m "아, 알았어."

            m "지우면 되잖아."

        else:

            m "너는 진짜 계속 끼어든다?"

            n "응."

            n "하린이가 혼자 말하게 두지는 않을 거야."

            "민재는 잠깐 나와 하린이를 번갈아 바라봤다."

            m "…아, 됐어."

        "민재는 끝까지 못마땅한 얼굴로 휴대폰을 만지작거렸다."

        "잠시 뒤 화면을 꺼 주머니에 넣었다."

        "예서는 옆에서 아무 말 없이 그 모습을 보고 있었다."

        "둘은 몇 마디 투덜거리며 교실을 나갔다."

        scene bg_14 with dissolve

        "하린이는 여전히 긴장한 얼굴이었다."

        "그래도 조금 전처럼 고개를 숙이고 있지는 않았다."

        n "(이번에는 하린이가 직접 싫다고 말했어.)"

        jump r3_s7_final_bathroom_talk


    else:

        # ----------------------------------------------------------
        # 아직 하린이의 신뢰가 충분하지 않은 경우
        # ----------------------------------------------------------

        "하린이는 휴대폰 화면을 바라보다가 곧 시선을 내렸다."

        "민재가 피식 웃었다."

        scene bg_14_blur with dissolve
        show m7 at center_stage with dissolve

        m "봐."

        m "또 아무 말도 안 하잖아."

        m "진짜 싫으면 싫다고 하든가."

        hide m7 with dissolve

        scene bg_14 with dissolve

        "하린이의 손이 가방끈을 더 세게 움켜쥐었다."

        "하지만 입은 열리지 않았다."

        n "민재야, 그만해."

        scene bg_14_blur with dissolve
        show m10 at center_stage with dissolve

        m "뭘 그만해."

        m "하린이는 아무 말도 안 하는데 너만 계속 그러잖아."

        hide m10 with dissolve
        scene bg_14 with dissolve

        n "아무 말 안 하는 걸 네 마음대로 괜찮다는 뜻으로 쓰지 마."

        "민재의 표정이 굳었다."

        "하지만 하린이는 여전히 고개를 들지 못했다."

        scene bg_14_blur with dissolve
        show h5 at center_stage with dissolve

        h "…나 그냥 갈래."

        n "같이 가."

        "하린이는 잠깐 나를 바라봤다."

        "이번에는 내 손을 밀어내지는 않았지만,"
        "아무 대답도 하지 않은 채 먼저 문 쪽으로 걸었다."

        hide h5 with dissolve
        scene bg_14 with dissolve

        "나는 하린이 뒤를 따라갔다."

        "뒤에서 민재와 예서가 무언가 작게 이야기하는 소리가 들렸다."

        "이번에는 하린이를 혼자 남겨두지는 않았지만,"
        "하린이가 자기 목소리를 낼 수 있는 데까지는 가지 못했다."

        n "(내가 대신 말하는 것만으로는 안 돼.)"

        n "(하린이가 말할 수 있을 때까지 옆에 있는 것도 필요해.)"

        jump r3_s7_final_bathroom_talk

# ----------------------------------------------------------
# R3-S7. 다음 날 아침 — 화장실 앞 복도 대화
# ----------------------------------------------------------

label r3_s7_final_bathroom_talk:

    scene black with fade
    pause 0.8

    scene bg_8 with fade

    "화요일 아침."

    "쉬는 시간, 나는 화장실 앞 복도를 지나고 있었다."

    "이 시간, 이 장소."

    "지난 두 번에도 똑같은 일이 있었다."

    "잠시 뒤 화장실 문이 열렸다."

    "먼저 나온 건 소윤이었다."


    # ----------------------------------------------------------
    # 소윤의 현재 상태
    # ----------------------------------------------------------

    if f_r3_soyoon_coop:

        scene bg_8_blur with dissolve
        show s3 at center_stage with dissolve

        "소윤이는 몇 걸음 나오다가 나를 발견하고 멈췄다."

        "그리고 다시 화장실 문을 한번 돌아봤다."

        s "…하린이 아직 안에 있어."

        n "응."

        "소윤이는 그대로 교실로 가지 않았다."

        "복도 한쪽으로 비켜서서 잠시 화장실 문을 바라봤다."

        hide s3 with dissolve
        scene bg_8 with dissolve

        n "(지난번에는 그냥 가버렸는데….)"

    else:

        scene bg_8_blur with dissolve
        show s8 at center_stage with dissolve

        "소윤이는 나를 발견하고 잠깐 걸음을 늦췄다."

        "화장실 문을 한번 돌아보기도 했다."

        if r3_action_soyun:

            "아침에 나와 나눴던 이야기가 떠오른 듯 잠시 머뭇거렸다."

        "하지만 결국 아무 말 없이 교실 쪽으로 걸어갔다."

        hide s8 with dissolve
        scene bg_8 with dissolve


    # ----------------------------------------------------------
    # 하린 등장
    # ----------------------------------------------------------

    "잠시 뒤, 다시 화장실 문이 열렸다."

    scene bg_8_blur with dissolve
    show h5 at center_stage with dissolve

    "하린이가 천천히 걸어 나왔다."

    "눈가가 붉어져 있었다."

    n "(또 똑같아.)"

    "지난번에도 소윤이가 먼저 나왔고,"
    "잠시 뒤 하린이가 이런 얼굴로 뒤따라 나왔다."

    "그때는 무슨 일이 있었는지도 제대로 알지 못했다."

    "하지만 이번에는 달랐다."

    "급식실에서 있었던 일도,"
    "민재가 건넨 쪽지도,"
    "어제 사진을 꺼내 들었던 일도 알고 있었다."

    if trust_harin >= 5:

        "하린이는 나를 발견하고 걸음을 멈췄다."

        "이번에는 바로 시선을 피하지 않았다."

    else:

        "하린이는 나를 발견하자 잠깐 멈칫했다."

        "그러고는 시선을 내린 채 지나가려 했다."

    hide h5 with dissolve
    scene bg_8 with dissolve

    if f_r3_soyoon_coop:

        "조금 떨어져 있던 소윤이도 하린이를 바라봤다."

        "다가오지는 못했지만,"
        "이번에는 그대로 자리를 떠나지도 않았다."

    n "하린아."

    "하린이가 다시 걸음을 멈췄다."

    n "잠깐 얘기해도 돼?"

    if trust_harin >= 5:

        "하린이는 잠시 망설이다 내 쪽으로 몸을 돌렸다."

        h "…응."

    else:

        "하린이는 바로 대답하지 않았다."

        "잠시 뒤 아주 작게 고개를 끄덕였다."


    # ----------------------------------------------------------
    # 교무실에 가기 전 선택
    # ----------------------------------------------------------

    menu:

        "선생님께 말씀드리는 건 어때? 내가 같이 갈게.":

            n "어제 있었던 일 말이야."

            n "사진도 그렇고, 쪽지도 그렇고…."

            n "이제 선생님한테 이야기해보는 건 어때?"

            n "혼자 말하기 어려우면 내가 같이 갈게."


            if trust_harin >= 4:

                $ trust_harin += 2
                $ f_r3_teacher_support = True

                scene bg_8_blur with dissolve
                show h21 at center_stage with dissolve

                "하린이는 바로 대답하지 않았다."

                "한동안 바닥만 바라보다가 천천히 입을 열었다."

                h "…나도 어제 계속 생각했어."

                h "사진도 그렇고,"
                h "그 쪽지도 그렇고…."

                h "그냥 아무 말 안 하면 없어질 줄 알았는데."

                "하린이는 잠깐 말을 멈췄다."

                h "계속 똑같은 것 같아."

                n "응."

                h "근데…."

                h "나 혼자 가서는 말 못 할 것 같아."

                n "혼자 안 가도 돼."

                n "내가 옆에 있을게."

                "하린이가 나를 바라봤다."

                h "…진짜 같이 있어줄 거야?"

                n "응."

                "잠시 뒤 하린이가 작게 고개를 끄덕였다."

                h "그럼…."
                h "선생님한테 말씀드려볼래."

                hide h21 with dissolve
                scene bg_8 with dissolve


                # --------------------------------------------------
                # 소윤도 함께 가는 경우
                # --------------------------------------------------

                if f_r3_soyoon_coop:

                    "조금 떨어져 있던 소윤이가 우리 쪽을 바라봤다."

                    "입을 열려다 다시 다물기를 몇 번 반복하더니,"
                    "조심스럽게 몇 걸음 다가왔다."

                    scene bg_8_blur with dissolve
                    show s11 at center_stage with dissolve

                    s "저기…."

                    "하린이가 소윤이를 바라봤다."

                    s "선생님한테 가는 거야?"

                    h "…응."

                    "소윤이는 잠깐 망설였다."

                    s "나도 같이 가도 돼?"

                    h "소윤이도?"

                    s "응."

                    s "어제 민재가 사진 보여준 것도 봤고…."

                    s "그 전부터 있었던 일도 조금은 봤으니까."

                    "소윤이는 마지막 말을 하고 나서 시선을 내렸다."

                    s "내가 본 건 나도 말할게."

                    "하린이는 잠시 소윤이를 바라봤다."

                    h "…응."

                    hide s11 with dissolve
                    scene bg_8 with dissolve

                "우리는 교무실 쪽으로 걸음을 옮겼다."

                "하린이는 여전히 긴장한 얼굴이었다."

                "몇 걸음 걷다가 한 번 멈칫하기도 했다."

                n "괜찮아."

                n "천천히 가도 돼."

                "하린이는 잠시 나를 바라보고 다시 걸었다."

                "이번에는 혼자 교무실로 향하는 게 아니었다."

                jump r3_s8_teacher_room


            else:

                $ trust_harin += 1
                $ f_r3_teacher_support = True

                scene bg_8_blur with dissolve
                show h23 at center_stage with dissolve

                h "…선생님한테?"

                "하린이는 한참 대답하지 못했다."

                h "근데 걔네가 알면 어떡해."

                h "선생님한테 말했다고 더 뭐라고 하면…."

                n "그게 무서운 거구나."

                "하린이가 아주 작게 고개를 끄덕였다."

                h "…응."

                n "그럼 네가 처음부터 다 말하지 않아도 돼."

                n "내가 먼저 내가 본 것부터 말씀드릴게."

                n "하린이는 옆에만 있어도 되고."

                "하린이가 나를 바라봤다."

                n "말할 수 있는 것만 말하면 돼."

                n "중간에 싫으면 멈춰도 되고."

                "하린이는 한참 망설였다."

                scene bg_8_blur with dissolve
                show h5 at center_stage with dissolve

                h "…그럼."

                h "진짜 옆에 있어줘."

                n "응."

                h "…알겠어."

                hide h5 with dissolve
                scene bg_8 with dissolve

                "확신에 찬 대답은 아니었다."

                "그래도 이번에는 혼자 감당하는 대신,"
                "누군가와 함께 이야기해보는 쪽을 선택했다."

                if f_r3_soyoon_coop:

                    "옆에서 기다리고 있던 소윤이가 조심스럽게 입을 열었다."

                    s "나도… 같이 갈게."

                    "하린이는 대답 대신 소윤이를 한번 바라봤다."

                    "그리고 이번에는 싫다고 하지 않았다."

                "우리는 천천히 교무실 쪽으로 향했다."

                jump r3_s8_teacher_room


        "말하기 힘들면 억지로 안 해도 돼. 그냥 네 곁에 있을게.":

            $ trust_harin += 2

            n "지금 당장 선생님한테 말해야 하는 건 아니야."

            n "아직 말하기 힘들면 안 해도 돼."

            n "나는 그냥 네 옆에 있을게."

            "하린이는 아무 말도 하지 않았다."

            "나도 대답을 재촉하지 않았다."

            "복도에 아이들 발소리만 몇 번 지나갔다."


            if trust_harin >= 4:

                $ f_r3_teacher_support = True

                scene bg_8_blur with dissolve
                show h5 at center_stage with dissolve

                "한참 뒤 하린이가 먼저 입을 열었다."

                h "…어제."

                h "민재가 사진 보여줬을 때 진짜 무서웠어."

                h "싫다고 말하면 또 내가 이상한 애 되는 것 같고…."

                h "그냥 가만히 있으면 넘어갈 줄 알았는데."

                "하린이는 손가락을 가만히 맞잡았다."

                h "근데 가만히 있어도 계속 똑같더라."

                n "응."

                "다시 짧은 침묵이 흘렀다."

                h "…선생님한테 말하면."

                h "너도 같이 있어줄 수 있어?"

                n "응."

                n "처음부터 끝까지 같이 있을게."

                "하린이는 잠시 나를 바라봤다."

                h "그럼…."

                h "말해볼래."

                hide h5 with dissolve
                scene bg_8 with dissolve


                if f_r3_soyoon_coop:

                    "조금 떨어져 있던 소윤이가 우리 대화를 듣고 있었다."

                    "소윤이는 쉽게 다가오지 못하고 잠깐 머뭇거렸다."

                    "나는 소윤이와 눈이 마주쳤다."

                    "소윤이는 그제야 천천히 우리 쪽으로 왔다."

                    scene bg_8_blur with dissolve
                    show s11 at center_stage with dissolve

                    s "하린아."

                    h "…응."

                    s "나도 같이 가도 돼?"

                    s "내가 본 것도 있으니까."

                    "하린이는 잠시 생각하다 작게 고개를 끄덕였다."

                    h "…응."

                    hide s11 with dissolve
                    scene bg_8 with dissolve

                "우리는 나란히 교무실 쪽으로 향했다."

                "하린이가 먼저 말하겠다고 정한 뒤에도"
                "걸음은 몇 번이나 느려졌다."

                "나는 재촉하지 않고 그 속도에 맞췄다."

                jump r3_s8_teacher_room


            else:

                $ f_r3_teacher_support = True

                scene bg_8_blur with dissolve
                show h4 at center_stage with dissolve

                h "…고마워."

                h "근데 나 아직 잘 모르겠어."

                h "선생님한테 말하면 더 커질 것 같아서 무서워."

                hide h4 with dissolve
                scene bg_8 with dissolve

                n "응."

                n "그럼 지금 당장 다 말할 필요는 없어."

                "하린이는 나를 바라봤다."

                n "대신 내가 본 것부터 선생님한테 이야기해도 될까?"

                n "하린이 얘기는 네가 말하고 싶은 만큼만 하고."

                "하린이는 한동안 생각했다."

                scene bg_8_blur with dissolve
                show h5 at center_stage with dissolve

                h "…내 이름도 말해야 해?"

                n "선생님이 누구 이야기인지 알아야 도와주실 수는 있을 것 같아."

                n "근데 네가 옆에 있을 때 같이 말할게."

                "하린이는 다시 잠시 고민했다."

                h "…그럼 같이 있어줘."

                n "응."

                hide h5 with dissolve
                scene bg_8 with dissolve

                "하린이는 여전히 불안해 보였다."

                "하지만 이번에는 혼자 숨기는 쪽으로 돌아서지는 않았다."

                "우리는 천천히 교무실 쪽으로 걸어갔다."

                jump r3_s8_teacher_room
# ----------------------------------------------------------
# R3-S8. 교무실 — 이어진 이야기
# ----------------------------------------------------------

label r3_s8_teacher_room:

    scene bg_10 with fade

    $ case_score = 0

    if key1_structure:
        $ case_score += 1

    if note_chat:
        $ case_score += 1

    if note_witness:
        $ case_score += 1

    if f_r3_soyoon_coop:
        $ case_score += 1


    "교무실에 들어서자 담임 선생님이 우리를 바라보셨다."

    scene bg_10_blur with dissolve
    show t5 at center_stage with dissolve

    t "무슨 일이야?"

    hide t5 with dissolve
    scene bg_10 with dissolve

    "하린이는 선생님 앞에 서자 다시 말이 없어졌다."

    "나는 바로 대신 말하지 않고 잠시 기다렸다."

    scene bg_10_blur with dissolve
    show h5 at center_stage with dissolve

    "하린이가 몇 번 입을 열려다 다시 다물었다."

    h "선생님…."

    "목소리가 작게 떨렸다."

    h "저… 말씀드릴 게 있어요."

    hide h5 with dissolve
    scene bg_10 with dissolve

    "선생님은 하린이를 재촉하지 않았다."

    t "응."
    t "천천히 말해도 돼."


    # ----------------------------------------------------------
    # 구체적인 내용이 충분히 이어진 경우
    # ----------------------------------------------------------

    if case_score >= 2:

        "하린이가 어디서부터 말해야 할지 망설이는 동안,"
        "나는 내가 직접 확인한 일부터 하나씩 이야기했다."

        n "선생님, 한 번 있었던 일이 아니에요."

        n "모둠 활동할 때 하린이 의견은 묻지 않고 역할을 정했고,"
        n "급식실에서도 하린이 자리에 물건을 올려놓고 아무도 치워주지 않았어요."

        n "어제는 민재가 하린이 사진을 보여주면서"
        n "그냥 장난인데 왜 그렇게 받아들이냐고 했어요."


        if note_witness:

            n "체육 시간에는 민재가 하린이 옆에 쪽지를 떨어뜨리는 것도 봤어요."

            "나는 하린이를 바라봤다."

            "하린이는 잠시 망설이다 주머니에서 접어둔 쪽지를 꺼냈다."

            scene bg_10_blur with dissolve
            show h5 at center_stage with dissolve

            h "이거예요."

            hide h5 with dissolve
            scene bg_10 with dissolve

            "선생님은 쪽지를 받아 천천히 읽었다."

            "『다 장난인 거 알지?』"

            "『괜히 예민하게 받아들이지 말고, 분위기 흐리지는 말자.』"

            "선생님은 쪽지를 바로 내려놓지 않았다."


        if note_chat:

            n "단톡방에서도 하린이를 계속 부르거나,"
            n "대답이 없는데도 계속 말을 붙이는 일이 있었어요."

            n "그 내용도 확인할 수 있어요."


        if f_r3_soyoon_coop:

            "옆에 있던 소윤이가 한참 망설이다 입을 열었다."

            scene bg_10_blur with dissolve
            show s11 at center_stage with dissolve

            s "저도 봤어요."

            s "민재가 하린이한테 장난이라고 하면서 계속 놀리는 것도 봤고…."

            s "모둠 활동할 때 하린이한테 안 물어보고 역할 정한 것도요."

            "소윤이는 잠깐 말을 멈췄다."

            s "어제 사진 보여준 것도 같이 있었어요."

            hide s11 with dissolve
            scene bg_10 with dissolve


        "선생님은 우리 말을 중간에 끊지 않고 끝까지 들었다."

        "그러다 하린이 쪽을 바라봤다."

        scene bg_10_blur with dissolve
        show t6 at center_stage with dissolve

        t "하린아."

        t "지금까지 이런 일이 계속 있었던 거니?"

        hide t6 with dissolve

        scene bg_10_blur with dissolve
        show h5 at center_stage with dissolve

        "하린이는 잠시 고개를 숙이고 있었다."

        h "…네."

        h "처음에는 그냥 장난인 줄 알았어요."

        h "애들도 계속 장난이라고 했고…."

        h "근데 저는 싫었어요."

        "하린이는 잠깐 말을 멈췄다."

        h "싫다고 말하면 제가 이상하게 구는 것 같아서"
        h "그냥 아무 말 안 했어요."

        hide h5 with dissolve
        scene bg_10 with dissolve

        "교무실 안이 잠시 조용해졌다."

        scene bg_10_blur with dissolve
        show t6 at center_stage with dissolve

        t "알겠어."

        t "말해줘서 고맙다."

        t "우선 하린이랑 조금 더 이야기해볼게."

        t "그리고 지금 말해준 일들도 하나씩 따로 확인하겠다."

        if note_witness:

            t "이 쪽지는 선생님이 확인할 수 있게 그대로 가지고 있자."

        if note_chat:

            t "단톡방 내용도 지금은 지우지 말고 그대로 두고."

        t "민재나 예서한테 바로 가서 따로 이야기할 필요는 없어."
        t "선생님이 먼저 확인할게."

        hide t6 with dissolve
        scene bg_10 with dissolve

        "하린이는 선생님의 말을 듣고도 바로 안심한 얼굴이 되지는 않았다."

        "그래도 조금 전처럼 입을 다문 채 서 있지는 않았다."

        $ f_r3_teacher_support = True


    # ----------------------------------------------------------
    # 아직 확인한 내용이 충분하지 않은 경우
    # ----------------------------------------------------------

    else:

        "나는 지금까지 직접 본 일을 하나씩 이야기했다."

        n "선생님."

        n "하린이가 계속 혼자 빠지는 일이 있었어요."

        n "어제는 민재가 하린이 사진을 보여주면서"
        n "장난인데 왜 그러냐는 식으로 말했고요."

        "선생님은 내 말을 듣다가 하린이에게 시선을 돌렸다."

        scene bg_10_blur with dissolve
        show t5 at center_stage with dissolve

        t "하린아."

        t "네가 이야기해도 괜찮을까?"

        hide t5 with dissolve

        scene bg_10_blur with dissolve
        show h23 at center_stage with dissolve

        "하린이는 한동안 대답하지 못했다."

        h "…잘 모르겠어요."

        h "근데 그냥… 학교에 있는 게 자꾸 불편해요."

        hide h23 with dissolve
        scene bg_10 with dissolve

        "선생님은 더 자세히 말하라고 재촉하지 않았다."

        scene bg_10_blur with dissolve
        show t6 at center_stage with dissolve

        t "알겠어."

        t "그럼 지금 당장 다 이야기하지 않아도 돼."

        t "우선 선생님이 하린이랑 따로 이야기해보고,"
        t "반에서 무슨 일이 있었는지도 조금 더 확인해볼게."

        t "생각나는 게 있으면 나중에 다시 말해줘도 되고."

        hide t6 with dissolve
        scene bg_10 with dissolve

        "선생님은 우리가 말한 내용을 메모해두었다."

        "바로 모든 일이 정리된 건 아니었다."

        "그래도 이번에는 하린이의 이야기가 교무실 안에서 멈추지 않고 받아들여졌다."

        $ f_r3_teacher_support = False


    jump ending_check


# ----------------------------------------------------------
# 엔딩 분기
# ----------------------------------------------------------
label ending_check:
    scene black with fade
    "며칠 뒤. 교실의 공기가 조금씩 바뀌기 시작했다."

    # ------------------------------------------------------
    # 엔딩 판정 기준
    # - 연대: 하린과의 신뢰 + 소윤의 협력 + 교사의 적극 개입이 모두 연결됨
    # - 동행: 소윤과의 연대는 완성되지 않았지만, 하린을 혼자 두지 않는 관계는 만들어짐
    # - 회복: 교사의 개입은 이루어졌지만, 하린과의 관계/회복은 아직 시간이 더 필요함
    # - 침묵: 하린과의 안정적인 연결도, 충분한 지원 구조도 만들어지지 못함
    #
    # 기존에는 teacher_support가 먼저 판정되어 회복 엔딩으로 지나치게 쏠렸기 때문에,
    # '소윤 협력 없음 + 하린과의 동행 관계 형성'을 회복보다 먼저 판정하도록 조정함.
    # ------------------------------------------------------

    # 1. 연대 엔딩
    if f_r3_soyoon_coop and f_r3_teacher_support and trust_harin >= 5:
        jump ending_true

    # 2. 동행 엔딩
    # 소윤과의 집단적 연대는 완성되지 않았지만,
    # 하린의 속도를 존중하며 곁에 남는 선택을 했고 신뢰도 충분히 쌓인 경우.
    elif (not f_r3_soyoon_coop) and f_r3_stay_together and trust_harin >= 4:
        jump ending_normal

    # 3. 회복 엔딩
    # 교사의 적극 개입은 성립했지만, 연대/개인적 신뢰가 완전히 연결되지는 않은 경우.
    elif f_r3_teacher_support and (f_r3_soyoon_coop or trust_harin >= 3):
        jump ending_step_a

    # 4. 동행 보조 판정
    # 교사의 적극 개입까지는 이어지지 않았더라도,
    # 하린을 혼자 두지 않겠다는 관계가 실제로 형성된 경우.
    elif f_r3_stay_together and trust_harin >= 3:
        jump ending_normal

    # 5. 침묵 엔딩
    else:
        jump ending_bad


# ==========================================================
# [경로 1] TRUE END: 완벽한 연대
# ==========================================================
label ending_true:
    $ ending_type = "true"
    scene black with fade
    pause 0.6

    scene bg_3 with fade
    "선생님께 모든 걸 말씀드리고 집에 돌아온 날 밤,"
    play sound "audio/bed_sheets_moving.mp3"
    "나는 침대에 누워서도 한참 잠이 오지 않았다."
    "뭔가 오래 막혀 있던 게 '툭' 하고 빠진 것 같은 기분이었다."
    "이상하게 자꾸 눈물이 날 것 같아서 이불을 머리끝까지 끌어올렸다."
    n "(하린이는… 내일 괜찮을까.)"
    n "(소윤이는 내일도 내 편에 있어 줄까.)"
    n "(…근데 오늘 내가 한 일이 진짜로 뭔가를 바꿀 수 있을까.)"
    stop sound
    scene black with fade
    pause 0.4
    scene bg_16 with fade
    "다음 날 아침. 교문 앞."
    "평소에는 혼자 고개를 숙이고 들어오던 하린이가,"
    "오늘은 소윤이와 나란히 걸어 들어오고 있었다."
    scene bg_16_blur with dissolve
    show s9 at left_stage with dissolve
    show h28 at right_stage with dissolve
    "소윤이가 나를 먼저 보고 손을 크게 흔들었다."
    s "같이 가자!"
    "나는 웃으며 뛰어가 둘 옆에 섰다."
    hide s9
    hide h28
    with dissolve
    scene bg_17 with fade
    "교실에 들어서자 어쩐지 공기가 다르게 느껴졌다."
    "민재와 예서는 각자 따로 앉아 있었다."
    "어제 방과 후에 선생님이 두 사람을 따로 부르셨다고 했다."
    "무슨 이야기가 오갔는지는 모르지만,"
    "아침 자습 시간 내내 둘 다 고개를 들지 않았다."
    "조회 시간에 선생님이 평소보다 조용한 목소리로 말씀하셨다."
    scene bg_17_blur with dissolve
    show t5 at center_stage with dissolve
    t "얘들아. 오늘은 선생님이 다 같이 나누고 싶은 이야기가 있어."
    t "직접 때리거나 욕하지 않아도,"
    t "누군가를 자꾸 밀어내고, 끼워주지 않고, 웃음거리로 만드는 것"
    hide t5 with dissolve
    show t7 at center_stage with dissolve
    t "그것도 분명한 폭력이야."
    t "그리고 보고도 모른 척하는 것은,"
    t "그 폭력이 계속되게 놔두는 일이기도 해."
    "교실이 평소와 다르게 조용했다."
    "오늘은 아무도 그러지 않았다."
    hide t7 with dissolve
    show t1 at center_stage with dissolve
    t "선생님은 오늘부터 하린이 편에, 그리고 이 교실의 모든 사람 편에 설 거야."
    t "누구든 힘들면 혼자 참지 말고 말해줘."
    t "선생님도 놓치는 게 있을 수 있으니까, 너희가 도와줘야 해."
    hide t1 with dissolve
    show h5 at center_stage with dissolve
    "하린이의 어깨가 아주 살짝 떨렸다."
    "내 자리에서도 보였다."
    "고개를 숙인 채로, 하린이가 아주 조용히 눈물을 닦고 있었다."
    "오랫동안 꾹꾹 참아왔던 게 처음으로 터진 것 같은, 그런 눈물이었다."
    hide h5 with dissolve
    scene black with fade
    scene cg_t2 with dissolve
    "그날 오전 수업이 끝난 뒤,"
    "하린이는 담임 선생님의 안내로 위클래스 상담실에 가게 되었다."
    wt "하린아, 여기서는 바로 말하지 않아도 괜찮아."
    wt "천천히 말해도 되고, 말하고 싶지 않은 건 지금 말하지 않아도 괜찮아."
    "위클래스 선생님은 그저 하린이가 안전하다고 느낄 수 있도록 천천히 말을 건네셨다."
    scene black with fade
    pause 0.5
    scene bg_7 with fade
    scene bg_7_blur with dissolve
    show h28 at center_stage with dissolve
    "쉬는 시간."
    "복도를 지나가는데, 멀리서 하린이가 걸어오는 게 보였다."
    "가방을 메고 정면을 바라보며 걸어오는 하린이."
    "예전의 축 처진 어깨와는 달랐다. 고개를 들고, 똑바로 앞을 보고 있었다."
    hide h28 with dissolve
    scene black with fade
    play music "audio/bgm_true_warm.mp3" fadein 2.0 fadeout 1.0
    scene cg_t1 with dissolve
    "점심시간."
    "원래라면 하린이가 구석 자리를 향해 걸어갔을 시간이었다."
    "오늘은 달랐다."
    "하린이가 식판을 들고, 망설임 없이 우리 쪽으로 걸어왔다."
    "소윤이가 자기 옆 의자를 탁, 하고 끌어당겼다."
    s "여기 앉아, 하린아."
    "하린이가 의자에 앉기 전에 아주 짧게 우리를 한 번 쳐다봤다."
    "'나 진짜 여기 앉아도 돼?'"
    "그렇게 묻는 눈빛이었다."
    "소윤이와 나는 동시에 고개를 끄덕였다."
    "하린이가 천천히 자리에 앉았다."
    "그러고는 아주 작은 목소리로 말했다."
    h "...오늘 국, 맛있겠다."
    "그게 뭐라고,"
    "내 코끝이 찡해졌다."
    "그동안 하린이가 급식실에서 먼저 입을 연 걸 본 적이 거의 없었다."
    "'오늘 국 맛있겠다'는 짧은 한마디가"
    "이렇게 큰 말이 될 수 있다는 걸, 나는 오늘 처음 알았다."
    s "맛있지. 나 이거 제일 좋아해."
    h "...응."
    "하린이가 처음으로 아주 작게 웃었다."
    "눈이 살짝 접히는 그런 웃음이었다."
    "모르는 사람은 웃은 건지도 모를 만큼 아주 작은 웃음."
    "그런데 나는 분명히 알아봤다."
    n "(이 웃음을 보려고,)"
    n "(그 많은 시간을 다시 돌아왔던 거구나.)"
    scene black with fade
    pause 0.8
    scene cg_s3 with fade
    "그 뒤로 며칠이 흘렀다."
    "교실이 하루아침에 완벽하게 바뀐 건 아니었다."
    "하린이는 여전히 말수가 적고,"
    "쉬는 시간에 혼자 창밖을 보는 날도 있었다."
    "그래도 분명히 달라진 게 있다."
    "하린이는 혼자 있지 않았다."
    "나와 소윤이가 곁에 있었다."
    "그냥 옆에 있어 주는 것만으로도 달라지는 게 있다는 걸, 이제는 안다."
    scene bg_15 with fade
    "위클래스 선생님도 일주일에 한 번씩 하린이를 만나주신다."
    scene black with fade
    scene cg_t3 with dissolve
    "금요일 방과 후."
    "노을이 교실 바닥까지 길게 드리워져 있었다."
    "나와 소윤이, 하린이는 아무도 없는 교실에서 늦게까지 같이 청소를 했다."
    "하린이가 빗자루를 들고 칠판 앞을 정리하다가 문득 멈추더니 말했다."
    h "있잖아."
    h "나, 학교 오는 게 전보다 덜 무서워."
    h "아침에 교문 들어설 때, 아직도 심장이 좀 빨리 뛰긴 하는데…"
    h "그래도 이제는, 교실 문을 열기 전에 너희 얼굴이 먼저 떠올라."
    "소윤이가 빗자루를 그대로 내리고 하린이를 쳐다봤다."
    "하린이의 눈가가 다시 젖어 있었다."
    "그런데 입꼬리는 분명히 올라가 있었다."
    s "내일도 또 같이 오는거 알지? 문구점 앞에서 만나자!"
    "소윤이가 싱긋, 웃었다."
    h "...응."
    scene black with fade
    n "(내가 대단한 일을 한 건 아니었다.)"
    n "(처음엔 무서웠고,)"
    n "(어떻게 해야 할지 몰라서 한참을 헤맸고,)"
    n "(같은 하루를 몇 번이나 되풀이하고 나서야 겨우 방법을 찾았다.)"
    n "(그렇게 찾은 방법도, 돌이켜보면 별것 아니었다.)"
    n "(하린이가 지나갈 때 한 번 더 쳐다본 것.)"
    n "(식판을 들고 하린이 옆자리에 앉은 것.)"
    n "(소윤이에게 '너도 그렇게 생각했지?'라고 먼저 물어본 것.)"
    n "(선생님께 '이건 그냥 장난이 아니에요'라고 말씀드린 것.)"
    n "(하나하나는 정말 작은 일이었다.)"
    n "(그런데 그 작은 일들이 모이니까,)"
    n "(누군가의 하루가 바뀌었다.)"
    n "(누군가가 다시 웃었다.)"
    n "(그게 내가 이번 일주일 동안 배운 거였다.)"

    stop music fadeout 3.0
    scene black with fade
    pause 0.8

    centered "{size=34}{color=#FFFFFF99}엔딩{/color}{/size}\n\n{size=54}{color=#C8FFC8}{b}연대 엔딩: 함께 지켜낸 교실{/b}{/color}{/size}\n\n{size=28}{color=#F2FFF2}서로의 편이 된 아이들{/color}{/size}"
    pause 2.5

    if key4_minjae_pattern and f_r3_minjae_weakness and note_witness and f_r3_soyoon_coop:
        scene black with fade
        pause 1.0
        centered "{size=34}{color=#FFF4DD}그리고, 며칠 뒤.{/color}{/size}"
        pause 1.8
        centered "{size=30}{color=#FFF4DD}끝났다고 생각했던 이야기는\n아직 한 걸음 더 남아 있었다.{/color}{/size}"
        pause 2.2
        jump ending_hidden
    else:
        jump ending_epilogue


# ==========================================================
# [경로 2] STEP END: 천천히 아물어가는 마음
# ==========================================================
label ending_step_a:
    $ ending_type = "step_a"
    scene black with fade
    pause 0.6

    scene bg_17 with fade
    "선생님은 우리 이야기를 허투루 듣지 않으셨다."
    "단톡방에서 오간 말들, 급식실의 빈자리,"
    "그리고 체육 시간에 하린이 발밑에 떨어졌던 쪽지까지."
    "우리가 확인한 것들을 하나씩 짚어 가며,"
    "그게 왜 단순한 장난이 아니라 누군가를 몰아세우는 일인지"
    "민재와 예서에게도 따로 설명하셨다고 했다."
    scene bg_15 with dissolve
    "위클래스 선생님도 하린이를 직접 만나 주셨다."
    "일주일에 한 번씩, 조용한 상담실에서."
    scene bg_17 with dissolve
    "겉으로 보기에 교실은 많이 달라졌다."
    "민재 무리는 더 이상 대놓고 하린이를 두고 웃지 못했고,"
    "단톡방에서 누군가의 사진을 돌려보는 일도 사라졌다."
    "소윤이도 예전처럼 아무렇지 않은 얼굴로 웃지는 못했다."
    "다만 조심스러워졌을 뿐,"
    "끊어진 사이가 하루아침에 이어진 것은 아니었다."
    "하린이는 여전히 쉽게 웃지 않았다."
    "내가 옆에 앉으면 작게 고개를 끄덕였다."
    "내가 말을 걸면 짧게 대답했다."
    "하지만 먼저 내 이름을 부르거나,"
    "자기 이야기를 꺼내는 일은 드물었다."
    scene cg_t4 with fade
    "점심시간, 하린이는 우리 테이블에 앉았다."
    "그런데 내 바로 옆이 아니라,"
    "한 자리 건너 맞은편이었다."
    "소윤이는 조금 떨어진 자리에서 식판만 내려다보고 있었다."
    "그러다 하린이를 힐끗 보고,"
    "빈 물컵을 조용히 그쪽으로 밀어 주었다."
    "하린이는 소윤이를 제대로 보지 못했다."
    "소윤이도 더 말을 걸지는 못했다."
    "하지만 적어도 이번에는,"
    "아무것도 모르는 척 웃고 있지는 않았다."
    "나는 그 어색한 거리가 자꾸 마음에 걸렸다."
    "문제를 멈추는 일과 마음이 다시 편해지는 일은,"
    "서로 다른 일이라는 생각이 들었다."
    n "(내가 뭔가 부족했던 걸까.)"
    n "(더 천천히 다가갔어야 했나.)"
    n "(아니면, 혼자 '이제 다 해결됐어'라고 믿어 버린 걸까.)"
    scene black with fade
    play music "audio/bgm_step_gentle.mp3" fadein 2.5 volume 0.6
    scene cg_s1 with dissolve
    "그 주 금요일."
    "나는 복도 창가에 혼자 서 있는 하린이를 봤다."
    "체육 수업이 끝난 운동장을 내려다보고 있었다."
    "나는 조심스럽게 다가가 옆에 섰다."
    "아무 말 없이 같이 운동장을 봤다."
    "한참 뒤, 하린이가 먼저 입을 열었다."
    h "있잖아."
    h "네가 선생님한테 말해 준 거… 고마워."
    h "근데 나, 아직도 교실이 조금 무서워."
    h "다들 내 얘기를 하고 있는 것 같고,"
    h "누가 쳐다보면 내가 또 뭘 잘못했나 싶고."
    h "그래서 너한테 다가가는 게 아직 힘들어."
    h "네가 싫어서가 아니야. 그건 진짜 아니야."
    h "그냥 내가… 아직 누구한테든 마음을 다 열 준비가 안 된 것 같아."
    "하린이가 말하는 동안 나는 입술만 깨물고 있었다."
    "뭐라고 대답해야 할지 몰랐다."
    h "미안해."
    n "(미안하다고 말할 사람은 네가 아니잖아.)"
    "그 말을 입 밖으로 꺼내지는 못하고, 대신 천천히 고개를 저었다."
    scene black with fade
    n "(나는 조금 욕심을 부렸던 것 같다.)"
    n "(내가 여기까지 끌고 왔으니까,)"
    n "(이제는 하린이가 웃어 줘야 뭔가 끝난 것 같은 기분이 들어서.)"
    n "(그런데 하린이가 혼자 버텨온 시간은 길었다.)"
    n "(며칠 만에 전부 녹을 리가 없었다.)"
    n "(내가 할 일은,)"
    n "(하린이가 다시 마음을 열 수 있을 때까지,)"
    n "(그 속도에 맞춰 옆에 있어 주는 것이었다.)"
    n "(내가 원하는 속도가 아니라, 하린이가 편한 속도로.)"
    scene black with fade
    scene cg_s2 with dissolve
    "그날 오후."
    "하교 시간에 하린이가 먼저 내게 와서 우유를 하나 건넸다."
    "급식실에서 남은 거라고, 작게 웃으며."
    "그리고 하린이는 먼저 뒤돌아 교실을 나갔다."
    "평소처럼 천천히, 조용히."
    "그런데 그 뒷모습이 예전과는 달랐다."
    "예전에는 문 앞에서 한 번도 돌아보지 않았는데,"
    "오늘은 복도로 나가기 전에 잠깐 멈춰 서서,"
    "나를 보고 손을 조금 들었다."
    n "(아직은 어색해.)"
    n "(한 자리 건너에 앉은 거리도,)"
    n "(나한테 한마디 하고 먼저 돌아서는 그 몇 걸음도.)"
    n "(근데 괜찮아.)"
    n "(하린이는 지금 아물고 있는 중이니까.)"
    n "(상처는 원래 시간이 걸리는 거니까.)"
    n "(나는 그 옆에서, 급할 것 없이 기다려 주면 돼.)"

    stop music fadeout 3.0
    scene black with fade
    pause 0.8
    centered "{size=34}{color=#FFFFFF99}엔딩{/color}{/size}\n\n{size=54}{color=#A0D8E6}{b}회복 엔딩: 천천히 아물어 가는 마음{/b}{/color}{/size}\n\n{size=28}{color=#EAF8FF}하린이가 편한 만큼 가까워지는 길{/color}{/size}"
    pause 2.5
    jump ending_epilogue


# ==========================================================
# [경로 3] NORMAL END: 동행
# ==========================================================
label ending_normal:
    $ ending_type = "normal"
    scene black with fade
    pause 0.6

    scene bg_17 with fade
    "소윤이는 끝까지 같이 나서 주지 않았다."
    "나는 그게 한동안 서운했다."
    "분명히 같이 봤는데,"
    "분명히 같이 느꼈는데,"
    "소윤이는 끝내 '난 잘 몰라'라는 얼굴을 하고 있었다."
    "나 혼자 말하면"
    "괜히 내가 예민한 애가 되는 것 같았고,"
    "내가 본 게 맞는지도 자꾸 자신이 없어졌다."
    "그래도 선생님께 말씀드린 건"
    "후회하지 않았다."
    "선생님도 하린이가 안심할 수 있도록 계속 상황을 살피셨다."
    "하지만 어른의 개입만으로 교실의 모든 관계가 하루아침에 달라지지는 않았다."
    "대놓고 놀리는 말은 줄었지만,"
    "먼저 하린이에게 다가가는 아이도 없었다."
    "조별 활동을 할 때면"
    "누군가는 하린이 옆자리를 슬쩍 피했고,"
    "쉬는 시간에는"
    "하린이가 혼자 책을 읽는 날이 더 많았다."
    "점심시간에도 여전히"
    "교실 한쪽 구석 자리에 앉았다."
    scene black with fade
    pause 0.6
    scene cg_s4 with fade
    "달라진 건 하나뿐이었다."
    "그 구석 자리 맞은편에"
    "내가 있었다."
    "처음 며칠은"
    "무슨 말을 해야 할지 몰랐다."
    "괜찮냐고 계속 묻는 것도 이상했고,"
    "힘내라고 말하는 것도 싫었다."
    "그래서 그냥 밥을 먹었다."
    "급식에 나온 반찬 이야기를 하고,"
    "수학 숙제를 깜빡했다는 이야기를 하고,"
    "주말에 본 영상 이야기를 했다."
    "하린이도 처음에는"
    "고개만 끄덕였다."
    "그러다 어느 날,"
    "내가 싫어하는 반찬을 보고 먼저 웃었다."
    h "너 그거 또 안 먹지?"
    n "어떻게 알았어?"
    h "맨날 남기잖아."
    "별것도 아닌 말이었다."
    "그런데 하린이가 나를 보고 먼저 말한 게"
    "괜히 오래 기억에 남았다."
    "매일 같이 있었던 것도 아니다."
    "어떤 날은 하린이가 먼저 말했다."
    h "오늘은 혼자 먹고 싶어."
    "예전 같았으면"
    "내가 귀찮아졌나 싶었을 것이다."
    "하지만 이제는 그냥 말했다."
    n "응. 그래."
    "그리고 내 자리로 돌아갔다."
    "미안해하지도 않고,"
    "서운해하지도 않았다."
    "다음 날이 되면"
    "다시 하린이 맞은편에 앉았다."
    "하린이도 아무 설명 없이"
    "내가 앉을 자리를 조금 비켜 주었다."
    "그게 우리 둘의 방식이었다."
    "꼭 붙어 있지 않아도 됐고,"
    "매번 괜찮냐고 확인하지 않아도 됐다."
    "혼자 있고 싶다고 하면 혼자 있게 두고,"
    "같이 있고 싶은 날에는 옆에 있었다."
    "그렇게 며칠이 지나고,"
    "몇 주가 지났다."
    "하린이가 갑자기 밝아진 것도 아니었다."
    "교실 문 앞에서 잠깐 멈추는 날도 있었고,"
    "민재 무리가 크게 웃으면"
    "괜히 어깨를 움츠리는 날도 있었다."
    "그럴 때마다"
    "내가 할 수 있는 건 별로 없었다."
    "그냥 옆에 서 있거나,"
    "'같이 들어갈래?' 하고 묻는 정도였다."
    scene black with fade
    pause 0.5
    play music "audio/bgm_normal_quiet.mp3" fadein 2.0 volume 0.5
    scene bg_7 with fade
    "어느 날 방과 후."
    "노을이 길게 드리운 복도에서"
    "하린이가 내 소매 끝을"
    "아주 살짝 잡아당겼다."
    scene bg_7_blur with dissolve
    show h23 at center_stage with dissolve
    h "나… 어제 학교 안 오고 싶었어."
    "나는 걸음을 멈췄다."
    h "아침에 진짜로 가방 안 쌀 뻔했어."
    h "그냥 하루쯤 안 가면 안 되나 싶었어."
    h "엄마한테 배 아프다고 할까도 생각했고."
    "하린이는 내 소매를 잡은 채"
    "바닥만 보고 있었다."
    hide h23 with dissolve
    show h28 at center_stage with dissolve
    h "근데 네가 어제 '내일 봐'라고 했던 게 자꾸 생각났어."
    h "진짜 별말도 아니었는데."
    h "계속 생각나더라."
    h "아무도 날 안 기다릴 줄 알았는데,"
    h "한 명은 기다리고 있을지도 모른다고 생각하니까…"
    h "못 빼먹겠더라."
    hide h28 with dissolve
    scene bg_7 with dissolve
    "나는 바로 대답하지 못했다."
    "기뻐해도 되는 말인지 몰랐다."
    "하린이가 학교에 오기 싫을 만큼 힘들었다는 건"
    "달라지지 않았으니까."
    "그래서 그냥 말했다."
    n "내일도 볼 거잖아."
    "하린이가 잠깐 나를 바라봤다."
    "그리고 아주 작게 웃었다."
    h "응."
    "나는 소매를 잡은 하린이 손을 떼어 내지 않았다."
    "그대로 둘이 복도를 걸었다."
    scene black with fade
    n "(반 전체를 한 번에 바꾸지는 못했어.)"
    n "(민재 무리는 여전히 자기들끼리 웃고 떠들고,)"
    n "(소윤이는 여전히 두 자리 건너에 앉아 있고,)"
    n "(하린이도 쉬는 시간엔 아직 혼자 책을 읽어.)"
    n "(내가 모르는 곳에서는)"
    n "(아직 무슨 일이 있는지도 몰라.)"
    n "(교실 전체를 바꾸는 건,)"
    n "(아직 나한테는 너무 벅찬 일인 것 같아.)"
    n "(내가 할 수 있는 일도 생각보다 적었어.)"
    n "(하린이 대신 싸워 줄 수도 없고,)"
    n "(하린이 마음을 내가 괜찮게 만들 수도 없어.)"
    n "(그런데 다 해결해야만)"
    n "(돕는 건 아니었나 봐.)"
    n "(혼자 있고 싶을 때는 기다려 주고,)"
    n "(같이 있고 싶은 날에는 옆에 있고,)"
    n "(내일 보자고 말하고,)"
    n "(진짜 다음 날 다시 만나는 것.)"
    n "(누군가한테는 그 정도만 있어도,)"
    n "(학교에 올 이유가 되는구나.)"
    n "(내가 하린이를 구해 준 건 아니야.)"
    n "(그냥 힘든 동안 혼자 견디게 두지 않았을 뿐이야.)"
    n "(교실 전체는 아니어도,)"
    n "(하린이 한 명은 혼자 두지 않았어.)"
    n "(그거 하나만큼은 잘한 것 같아.)"

    stop music fadeout 3.0
    scene black with fade
    pause 0.8
    centered "{size=34}{color=#FFFFFF99}엔딩{/color}{/size}\n\n{size=54}{color=#FFFFC8}{b}동행 엔딩: 혼자 두지 않은 용기{/b}{/color}{/size}\n\n{size=28}{color=#FFFBE8}한 사람이 곁에 남아 준 날들{/color}{/size}"
    pause 2.5
    jump ending_epilogue


# ==========================================================
# [경로 4] BAD END: 여전히 추운 교실
# ==========================================================
label ending_bad:
    $ ending_type = "bad"
    scene black with fade
    pause 0.6

    scene bg_17 with fade
    "선생님은 내 말을 허투루 듣지 않으셨다."
    "쉬는 시간마다 교실에 오셨고,"
    "하린이 자리를 바꿔 주셨고,"
    "민재와 예서에게도 따로 주의를 주셨다."
    "하린이를 상담실에 몇 번이나 데려가 이야기를 나누셨다."
    "그런데 선생님 앞에서는 모든 게 조용했다."
    "민재와 예서는 '저희는 아무것도 안 했는데요?'라는 얼굴로 선생님을 바라봤고,"
    "하린이는 '괜찮아요'라고만 했다."
    "소윤이는 끝까지 나와 눈을 마주치지 않았다."
    "선생님이 아무리 물어봐도,"
    "아무도 대답하지 않으면 거기서 멈출 수밖에 없었다."
    "선생님이 못 본 게 아니라,"
    "우리가 보여드리지 않은 거였다."
    "같이 말해 줄 사람이 없었다."
    "나 혼자 본 것들은,"
    "말로 옮기려고 할수록 자꾸 작아졌다."
    "분명히 있었던 일인데,"
    "입 밖으로 꺼내 놓으면 '그게 그렇게 큰일이야?' 정도의 크기가 됐다."
    "나중에는 내가 무엇을 봤는지도 흐릿해졌다."
    n "(내가 본 건 진짜였는데.)"
    n "(왜 나만 점점 이상한 애가 되는 거지.)"
    scene black with fade
    "며칠 뒤."
    "민재가 방과 후에 꺼내 보였던 그 사진이,"
    "반 단톡방에 올라왔다."
    "'아 잘못 보냄'이라는 한 줄과 함께."
    "실수가 아니라는 건 모두가 알았다."
    "그래도 아무도 그 말을 하지 않았다."
    "ㅋㅋㅋㅋ 하는 댓글만 줄줄이 달렸다."
    "웃는 사람은 여섯 명이었고,"
    "아무 말도 하지 않은 사람은 스무 명이 넘었다."
    "나도 그 스무 명 안에 있었다."
    n "(뭐라고 쓰지.)"
    n "(이거 아니라고, 지우라고.)"
    n "(…그러면 다음은 나겠지.)"
    "몇 글자 썼다가 지웠다."
    "다시 썼다가, 또 지웠다."
    "선생님께 이 화면을 보여드릴 생각도 했다."
    "캡처 버튼 위에서 손가락이 멈췄다."
    "그러는 사이 민재가 사진을 지웠다."
    "지워진 건 화면뿐이었다."
    "남은 건 아무것도 없었다."
    "내가 캡처하지 않았으니까."
    scene cg_b2 with dissolve
    "그날 하린이는 학교에 오지 않았다."
    "그다음 날도."
    "그다음 날도."
    scene black with fade
    play music "audio/bad_end.mp3" fadein 2.0 fadeout 1.0
    scene cg_b1 with dissolve
    "어느 쉬는 시간, 나는 하린이의 빈자리 앞에 서 있었다."
    "운동장에서 나는 소리가 유난히 크게 들렸다."
    "교실에서는 아무도 하린이를 묻지 않았다."
    "그게 제일 무서웠다."
    "'어? 하린이 왜 안 와?'"
    "'무슨 일 있었어?'"
    "그런 말 한마디가 누구의 입에서도 나오지 않았다."
    "어제까지 하린이 이름을 입에 달고 살던 민재도,"
    "오늘은 아무 일 없다는 듯 다른 애 얘기를 하고 있었다."
    "교실은 하린이가 없어도 아무 데도 비어 보이지 않았다."
    "책상 하나가 남았을 뿐이었다."
    scene bg_3 with fade
    "집에 와서 하린이에게 메시지를 보냈다."
    "'괜찮아?'"
    "지웠다."
    "'미안해.'"
    "그것도 지웠다."
    "결국 '내일 봐'라고 보냈다."
    "내일 볼 수 있을지도 모르면서."
    "숫자 1은 그날 밤에도, 다음 날 아침에도 사라지지 않았다."
    scene bg_7 with fade
    "복도에서 소윤이와 마주쳤다."
    "소윤이는 나를 보고 멈칫했다."
    "뭔가 말하려는 것 같았다."
    "하지만 곧 고개를 숙이고 지나갔다."
    "나도 붙잡지 않았다."
    "우리 둘 다, 각자의 이유로 입을 다물었다."
    "그리고 며칠 뒤,"
    "하린이가 전학을 간다는 이야기를 들었다."
    "인사는 없었다."
    scene cg_b1 with dissolve
    "다음 주 월요일, 그 자리에는 아무것도 놓여 있지 않았다."
    "청소 당번은 그 책상도 똑같이 닦고 지나갔다."
    n "(왜 이렇게 된 걸까.)"
    n "(…알 것 같아.)"
    n "(나 혼자 아는 것만으로는 아무것도 멈출 수 없었어.)"
    n "(같이 봐 줄 사람이,)"
    n "(같이 말해 줄 사람이 필요했어.)"
    n "(그런데 나는 소윤이가 말해도 괜찮다고 느끼게 해 주지 못했어.)"
    n "(하린이한테는 너무 앞서 나갔고.)"
    n "(급해서, 무서워서, 빨리 끝내고 싶어서.)"
    stop music fadeout 3.0
    scene bg_3 with fade
    "그날 밤, 나는 이불 속에서 오래 뒤척였다."
    "내일도 교실은 조용할 것이다."
    "민재도, 예서도, 소윤이도 제자리에 있을 것이다."
    "바뀐 건 자리 하나뿐이었다."
    "한 명이 사라졌는데 아무것도 달라지지 않는 교실."
    n "(다음엔 더 천천히.)"
    n "(혼자 앞서가지 말고,)"
    n "(누가 말할 수 있게 옆에 먼저 서 있자.)"
    "무거운 눈을 감았다."
    "베개가 젖어 있었다."

    scene black with fade
    pause 2.5
    centered "{size=34}{color=#FFFFFF99}엔딩{/color}{/size}\n\n{size=54}{color=#E8736C}{b}침묵 엔딩: 아직 차가운 교실{/b}{/color}{/size}\n\n{size=28}{color=#FFE1DE}함께 말하지 못해 남겨진 자리{/color}{/size}"
    pause 3.0
    jump ending_epilogue


# ==========================================================
# [경로 5] HIDDEN END: 장난과 폭력의 무게
# ==========================================================
label ending_hidden:
    $ ending_type = "hidden"
    scene black with fade
    pause 0.8

    scene cg_b3 with dissolve
    "하린이가 조금씩 학교에 적응해 가는 동안에도,"
    "교실의 모든 문제가 한꺼번에 사라진 것은 아니었다."
    "선생님은 민재와 예서를 따로 만나 계속 이야기를 나누셨고,"
    "위클래스에서도 상담이 몇 번 더 이어졌다고 했다."
    "하린이는 예전보다 덜 움츠러들었지만,"
    "민재와 같은 공간에 있을 때면 여전히 시선을 들지 못했다."
    "나는 그게 당연하다고 생각했다."
    "하린이가 괜찮아지는 것과,"
    "민재가 자기 잘못을 아는 것은"
    "서로 다른 일이니까."
    scene black with fade
    pause 0.6
    scene bg_14 with fade
    "그 일이 있고 두 주쯤 지난 어느 날."
    "6교시가 끝나고 아이들이 거의 다 빠져나간 교실."
    "나는 가방을 챙기고 있었다."
    "그때, 뒷문 쪽에서 누가 작게 내 이름을 불렀다."
    scene bg_14_blur with dissolve
    show m12 at center_stage with dissolve
    m "...야. 잠깐."
    hide m12 with dissolve
    scene bg_14 with dissolve
    "민재였다."
    "나는 놀라서 돌아봤다."
    "민재는 평소처럼 가방끈을 한쪽 어깨에만 걸친 채 서 있었다."
    "늘 웃고 있거나 찌푸리고 있던 얼굴이,"
    "오늘은 어느 쪽도 아니었다."
    scene bg_14_blur with dissolve
    show m5 at center_stage with dissolve
    m "혹시… 하린이한테 말 좀 전해 줄 수 있어?"
    m "…아니다. 그러면 안 되지."
    m "내일 방과 후에, 하린이랑 잠깐 얘기할 수 있을까."
    m "네가 옆에 있어도 돼."
    hide m5 with dissolve
    scene black with fade
    pause 0.8
    play music "audio/bgm_hidden_reflective.mp3" fadein 3.0 volume 0.5
    scene cg_h1 with fade
    "다음 날 방과 후."
    "교실 뒤쪽, 사물함이 있는 구석."
    "하린이, 소윤이, 나, 그리고 민재가 서 있었다."
    "소윤이는 내가 부르지 않았는데도 와 있었다."
    "하린이 옆에 서서, 아무 말 없이."
    "민재는 한참 동안 바닥만 봤다."
    "어떻게 입을 떼야 하는지 모르는 사람처럼."
    "그러다 겨우 작게 말했다."
    m "...하린아."
    m "그동안 내가 했던 거. 진짜 미안해."
    "하린이는 대답하지 않았다."
    "옆에 선 소윤이도 말이 없었다."
    "민재는 그 침묵을 견디면서 말을 이어갔다."
    m "처음엔 그냥…"
    m "애들 웃기려고 한 거였어."
    m "네가 아무 반응이 없으니까 더 쉬워 보였고,"
    m "애들이 웃어 주니까 내가 뭐라도 된 것 같았어."
    m "한 번은 그만하고 싶다고 생각했어."
    m "근데 그만두면 내가 이상한 애가 될 것 같아서 무서웠어."
    m "그래서 계속했어. 계속."
    "민재의 목소리가 조금씩 떨렸다."
    m "지금 생각하면 다 변명이야."
    m "내가 너한테 한 건 장난이 아니었어."
    m "그냥 괴롭힘이었어. 그게 맞아."
    m "…네가 나 용서 안 해도 돼."
    m "용서받으려고 하는 말 아니야."
    m "그냥, 내가 한 짓이 뭐였는지,"
    m "너한테 제대로 말은 해야 될 것 같아서."
    scene cg_h1_blur with dissolve
    show h3 at center_stage with dissolve
    "하린이는 여전히 말이 없었다."
    "고개를 들지도 않았다."
    "민재는 고개를 숙인 채로 그 자리에 서 있었다."
    "한참 뒤, 하린이가 아주 작게 말했다."
    hide h3 with dissolve
    show h21 at center_stage with dissolve
    h "…나 네가 미웠어."
    h "진짜 많이 미웠어."
    h "지금도 미워."
    "민재는 고개를 들지 않았다."
    h "…용서는 못 해. 아직은."
    hide h21 with dissolve
    show h3 at center_stage with dissolve
    h "그래도, 말해 줘서…"
    h "말해 줘서 고마워."
    hide h3 with dissolve
    scene cg_h1 with dissolve
    "민재는 허리를 굽혀 인사하고,"
    "아무 말도 하지 못한 채 교실을 나갔다."
    scene black with fade
    n "(나는 민재를 그냥 나쁜 애라고 생각했었다.)"
    n "(그게 편했다.)"
    n "(나쁜 애면 더 생각 안 해도 되니까.)"
    n "(근데 오늘 본 민재는 잘 모르겠다.)"
    n "(나쁜 애 같기도 하고, 아닌 것 같기도 하고.)"
    n "(확실한 건 하나였다.)"
    n "(자기가 뭘 했는지 하린이 앞에서 똑바로 말했다는 거.)"
    n "(나 같으면 저렇게 못 했을 것 같다.)"
    n "(용서할지 말지는 하린이가 정하는 거다.)"
    scene bg_17 with fade
    scene bg_17_blur with dissolve
    show t5 at center_stage with dissolve
    "그날 종례 시간, 선생님이 평소처럼 짧게 말씀하셨다."
    t "얘들아, 사과는 한 번으로 끝나지 않아."
    t "진짜 사과는 그 뒤의 행동으로 증명되는 거야."
    t "말만 하고 다시 똑같이 굴면, 그건 사과가 아니라 변명이야."
    hide t5 with dissolve
    show t6 at center_stage with dissolve
    t "그러니까 사과를 받은 사람도,"
    t "'고마워, 다 괜찮아'라고 억지로 말하지 않아도 돼."
    t "미운 건 미운 거야. 그 마음도 네 거야."
    hide t6 with dissolve
    scene bg_17 with dissolve
    scene bg_17_blur with dissolve
    show h10 at center_stage with dissolve
    "나는 슬쩍 하린이 쪽을 봤다."
    "하린이는 가방을 꼭 안은 채 고개를 숙이고 있었다."
    "어깨가 조금 떨리는 것 같았다."
    hide h10 with dissolve
    scene black with fade
    pause 0.4
    scene cg_h2 with dissolve
    "며칠 뒤, 하교 준비를 마치고 교실을 나서려던 때였다."
    "복도에 하린이와 민재가 조금 떨어져 마주 서 있었다."
    "나는 그대로 문 앞에 멈춰 섰다."
    m "…저번에 한 말, 형식적으로 한 거 아니야."
    m "네가 바로 괜찮아져야 한다고 생각하지도 않아."
    m "근데 내가 한 일은 안 잊을 거야."
    m "앞으로는 진짜로 다르게 행동할게."
    "하린이는 한동안 대답하지 않았다."
    h "…나 아직 하나도 안 괜찮아."
    h "네 말 듣고 바로 괜찮아질 수도 없어."
    h "근데…"
    h "네가 진짜로 바뀌는지,"
    h "그건… 조금 더 보고 싶어."
    "민재는 아무 말도 하지 못하고 잠깐 눈만 깜빡였다."
    m "응."
    m "그렇게 해."
    "민재는 더 변명하지 않았다."
    "하린이도 웃지 않았다."
    "둘은 그대로 조금 더 서 있다가,"
    "각자 반대쪽으로 걸어갔다."
    n "(용서는 바로 되는 게 아니다.)"
    n "(하린이는 밉다고 말했고,)"
    n "(그러면서도 민재 말을 끝까지 들었다.)"
    n "(그건 하린이가 정한 거였다.)"

    stop music fadeout 3.0
    scene black with fade
    pause 0.8
    centered "{size=34}{color=#FFFFFF99}엔딩{/color}{/size}\n\n{size=54}{color=#C8C8FF}{b}성찰 엔딩: 사과는 끝이 아니라 시작{/b}{/color}{/size}\n\n{size=28}{color=#F0F0FF}장난이라고 부른 폭력의 무게{/color}{/size}"
    pause 2.5
    jump ending_epilogue


# ==========================================================
# 에필로그 — 공통
# ==========================================================
label ending_epilogue:
    scene black with fade
    pause 0.6

    "텅 빈 교실."
    "창가로 햇빛이 길게 들어온다."
    "하린이의 자리가 보인다."

    if ending_type == "bad":
        scene bg_14 with fade
        "오늘, 그 자리는 비어 있다."
        "그리고 그 비어 있음이, 어떤 교실에서는 너무 조용하게 넘어간다."
    else:
        scene bg_14 with fade
        "오늘, 그 자리엔 희미한 온기가 남아 있다."
        "책가방을 두고 간 하린이의 흔적이다."
        "이제 더 이상 비어 보이지 않는 자리."


    n "안녕?"
    n "여기까지 나랑 하린이의 이야기를 함께해 줘서 고마워."
    n "처음엔 그냥 '운이 나쁜 애' 이야기라고 생각했을 수도 있어."
    n "원래 교실은 이런 곳이니까, 하고 넘겼을지도 모르지."
    n "하지만 하린이는 운이 나빴던 게 아니야."
    n "우리가 한 번 덜 쳐다보고,"
    n "한 번 덜 물어보고,"
    n "한 번 덜 옆에 앉았던 그 순간들이 쌓여서,"
    n "누군가를 조금씩 교실 밖으로 밀어내고 있었던 거야."
    n "네가 게임을 하면서 멈칫했던 순간들 기억나?"
    n "'이거 말해도 되나?'"
    n "'내가 끼어들어도 되나?'"
    n "'내가 너무 오버하는 건가?'"
    n "그때 네가 고른 선택이,"
    n "이 이야기의 결말을 만든 거야."

    play music "audio/bgm_epilogue_soft.mp3" fadein 4.0 volume 0.6

    if ending_type == "true":
        n "이번엔 끝까지 갔어. 너랑 내가 함께."
        n "아주 크게 바뀐 건 아니지만,"
        n "하린이가 다시 웃었어."
        n "그거면 충분해."
    elif ending_type == "hidden":
        n "이번엔 끝까지 갔어. 그리고 한 걸음 더 갔어."
        n "그 사람이 자기가 한 일을 똑바로 볼 수 있게 만드는 것"
        n "그것까지가 우리가 해낸 일이야."
    elif ending_type == "step_a":
        n "이번엔 한 사람을 밀어내던 분위기를 멈추게 했어."
        n "근데 하린이의 마음은 아직 아물고 있는 중이야."
        n "그건 우리가 '실패한' 게 아니라,"
        n "원래 시간이 걸리는 일이야."
        n "조급해하지 말자. 지금 충분히 잘하고 있어."
    elif ending_type == "normal":
        n "이번엔 교실 전체를 바꾸진 못했어."
        n "근데 하린이 한 명은 혼자 두지 않았어."
        n "그거, 생각보다 엄청난 일이야."
        n "한 사람의 진심이 한 사람을 붙잡을 수 있다는 거."
    else:
        n "이번엔 끝까지 가지 못했어."
        n "근데 괜찮아. 여기서 포기하지만 않으면 돼."
        n "다음엔, 더 천천히. 더 제대로."
        n "혼자 뛰어들지 말고, 옆에 함께할 사람을 먼저 만들자."


    n "이 이야기는 여기서 끝나는 이야기가 아니야."
    n "어디선가 비슷한 순간이 또 올 거야."
    n "누가 말을 못 하고 있을 때."
    n "누가 웃고 있는데 눈이 안 웃고 있을 때."
    n "누가 급식실에서 혼자 구석 자리로 걸어갈 때."
    n "그때,"
    n "그냥 지나칠지, 한 번 더 볼지."
    n "말을 걸어 볼지, 옆에 앉아 볼지."
    n "그건 네가 선택하는 거야."
    n "그 선택이 무겁다고 느껴질 수도 있어."
    n "근데 기억해 줘."
    n "네가 내민 아주 작은 손이,"
    n "누군가한테는 다시 학교에 올 수 있는 이유가 될 수도 있다는 걸."

    if ending_type == "bad":
        scene black with fade
        pause 0.6
        n "나는 아직 이 장면을 끝이라고 생각하지 않을 거야."
        n "다음에는 혼자 서두르지 않고, 함께 말할 사람을 만들 거야."
    else:
        scene black with fade
        pause 0.6
        n "나는 이제 다시 시간을 돌리지 않아도 돼."
        n "이번엔 너와 함께 끝까지 왔으니까."

    n "그럼, 또 봐."

    hide screen quick_note_button
    stop music fadeout 5.0
    scene black with fade
    pause 5.0
    jump project_finish

############################################################

label project_finish:    
    scene black with dissolve
    "PROJECT FINISHED: 복도 끝의 신호"
    "제작: 젼쌤"
    return

