"""
연애 유형 테스트 점수 계산 및 분류 서비스

Phase 1, T1-LOVE.1: 점수 계산 로직
"""

# 5개 측정 차원
DIMENSIONS = ["proactivity", "expression", "independence", "commitment", "romance"]

# 문항별 차원 매핑 및 점수
# 각 문항 ID -> (차원, {'A': 점수, 'B': 점수})
QUESTION_DIMENSION_MAP = {
    # 적극성 문항 (5개)
    1: ("proactivity", {"A": 2, "B": 0}),
    4: ("proactivity", {"A": 2, "B": 0}),
    8: ("proactivity", {"A": 2, "B": 0}),
    12: ("proactivity", {"A": 2, "B": 0}),
    17: ("proactivity", {"A": 2, "B": 0}),

    # 감정표현 문항 (4개)
    2: ("expression", {"A": 2, "B": 0}),
    5: ("expression", {"A": 2, "B": 0}),
    9: ("expression", {"A": 2, "B": 0}),
    14: ("expression", {"A": 2, "B": 0}),

    # 독립성 문항 (4개) - Q3, Q20은 역코딩
    3: ("independence", {"A": 0, "B": 2}),
    7: ("independence", {"A": 2, "B": 0}),
    16: ("independence", {"A": 2, "B": 0}),
    20: ("independence", {"A": 0, "B": 2}),

    # 헌신도 문항 (3개)
    10: ("commitment", {"A": 2, "B": 0}),
    13: ("commitment", {"A": 2, "B": 0}),
    18: ("commitment", {"A": 2, "B": 0}),

    # 로맨스 문항 (4개)
    6: ("romance", {"A": 2, "B": 0}),
    11: ("romance", {"A": 2, "B": 0}),
    15: ("romance", {"A": 2, "B": 0}),
    19: ("romance", {"A": 2, "B": 0}),
}

# 차원별 최대 점수 (정규화용)
MAX_SCORES = {
    "proactivity": 10,   # 5문항 * 2점
    "expression": 8,     # 4문항 * 2점
    "independence": 8,   # 4문항 * 2점
    "commitment": 6,     # 3문항 * 2점
    "romance": 8,        # 4문항 * 2점
}


def calculate_dimension_scores(answers: list[dict]) -> dict[str, int]:
    """
    답변에서 5차원 점수 계산 (0-100 스케일)

    Args:
        answers: [{"question_id": 1, "choice": "A"}, ...]

    Returns:
        {"proactivity": 80, "expression": 100, ...}
    """
    # 원점수 초기화
    raw_scores = {
        "proactivity": 0,
        "expression": 0,
        "independence": 0,
        "commitment": 0,
        "romance": 0,
    }

    # 답변을 dict로 변환 (빠른 조회)
    answer_map = {ans["question_id"]: ans["choice"] for ans in answers}

    # 각 문항의 점수 합산
    for question_id, (dimension, scores) in QUESTION_DIMENSION_MAP.items():
        choice = answer_map.get(question_id)
        if choice in scores:
            raw_scores[dimension] += scores[choice]

    # 0-100 스케일로 정규화
    normalized_scores = {}
    for dimension in DIMENSIONS:
        raw = raw_scores[dimension]
        max_score = MAX_SCORES[dimension]
        normalized = round((raw / max_score) * 100)
        normalized_scores[dimension] = normalized

    return normalized_scores


def classify_love_type(scores: dict[str, int]) -> str:
    """
    5차원 점수로 20개 유형 중 하나 분류

    Args:
        scores: {"proactivity": 80, "expression": 100, ...}

    Returns:
        "straight_shooter", "romance_express", ...
    """
    # 각 차원의 High(50 이상) / Low(50 미만) 분류
    proactivity = scores["proactivity"]
    expression = scores["expression"]
    independence = scores["independence"]
    commitment = scores["commitment"]
    romance = scores["romance"]

    is_proactive = proactivity >= 50
    is_expressive = expression >= 50
    is_independent = independence >= 50
    is_committed = commitment >= 50
    is_romantic = romance >= 50

    # 1단계: 적극성 극단값 기반 분류
    if proactivity >= 80:
        # 매우 적극적
        if expression >= 63 and romance >= 63:
            return "romance_express"  # 03. 로맨틱 폭주기관차
        if expression >= 63 and independence <= 50:
            return "straight_shooter"  # 01. 직진 러버
        if romance >= 63:
            return "mood_creator"  # 14. 로맨틱 무드메이커
        return "straight_shooter"  # 01. 직진 러버 (기본)

    if proactivity <= 20:
        # 매우 소극적
        if expression <= 37 and commitment >= 50:
            return "careful_observer"  # 18. 신중한 관찰자
        if independence >= 38:
            return "slow_burner"  # 17. 슬로우 버너
        return "slow_burner"  # 17. 슬로우 버너 (기본)

    # 2단계: 감정표현 기반 분류
    if expression >= 88:
        if romance >= 38:
            return "sweet_talker"  # 12. 말로 하는 사랑꾼
        if commitment >= 50:
            return "emotion_translator"  # 05. 감정번역가
        return "sweet_talker"  # 12. 말로 하는 사랑꾼 (기본)

    if expression <= 25:
        if proactivity >= 40:
            return "tsundere_expert"  # 04. 츤데레 마스터
        if romance <= 37:
            return "honest_lover"  # 13. 팩폭 애정러
        return "tsundere_expert"  # 04. 츤데레 마스터 (기본)

    # 3단계: 독립성 기반 분류
    if independence >= 88:
        if commitment <= 50:
            return "free_spirit"  # 08. 자유영혼 연인
        return "independent_lover"  # 10. 독립형 연애러

    if independence <= 25:
        if commitment >= 50:
            return "devoted_partner"  # 09. 헌신형 파트너
        if expression >= 50:
            return "touch_fairy"  # 11. 스킨십 요정
        return "devoted_partner"  # 09. 헌신형 파트너 (기본)

    # 4단계: 헌신도 기반 분류
    if commitment >= 84:
        if romance >= 50:
            return "devoted_partner"  # 09. 헌신형 파트너
        if romance <= 50:
            return "practical_lover"  # 19. 현실주의 연인
        return "steady_lover"  # 07. 안정 추구형 연인

    if commitment <= 33:
        if romance >= 50:
            return "thrill_collector"  # 06. 설렘 수집가
        return "free_spirit"  # 08. 자유영혼 연인

    # 5단계: 로맨스 기반 분류
    if romance >= 88:
        if proactivity >= 50:
            return "romance_express"  # 03. 로맨틱 폭주기관차
        return "emotional_dreamer"  # 20. 감성 몽글러

    if romance <= 25:
        if independence >= 50:
            return "practical_lover"  # 19. 현실주의 연인
        return "daily_companion"  # 16. 일상 동반자

    # 6단계: 복합 조합 분류
    if is_proactive and not is_expressive:
        return "push_pull_master"  # 02. 밀당 장인

    if not is_proactive and is_expressive and is_romantic:
        return "emotional_dreamer"  # 20. 감성 몽글러

    if is_independent and not is_committed:
        return "long_distance_pro"  # 15. 장거리 전문가

    if not is_independent and is_committed:
        return "steady_lover"  # 07. 안정 추구형 연인

    if not is_romantic and is_committed:
        return "daily_companion"  # 16. 일상 동반자

    # 기본값: 중립적 유형
    return "steady_lover"  # 07. 안정 추구형 연인


# 20개 유형 메타데이터
LOVE_TYPE_METADATA = {
    "straight_shooter": {
        "id": "straight_shooter",
        "code": "01",
        "name": "직진 러버",
        "english_name": "Straight Shooter",
        "subtitle": "좋으면 좋다고, 눈빛으로 이미 고백 완료",
        "emoji": "🚀",
        "hashtags": ["#직진본능", "#솔직한게매력", "#기다림은나의적"],
        "compatible_types": ["thrill_collector", "mood_creator"],
    },
    "push_pull_master": {
        "id": "push_pull_master",
        "code": "02",
        "name": "밀당 장인",
        "english_name": "Push & Pull Master",
        "subtitle": "밀고 당기기의 예술, 연애 심리전의 프로",
        "emoji": "🎭",
        "hashtags": ["#밀당마스터", "#연애심리전", "#궁금증유발러"],
        "compatible_types": ["straight_shooter", "romance_express"],
    },
    "romance_express": {
        "id": "romance_express",
        "code": "03",
        "name": "로맨틱 폭주기관차",
        "english_name": "Romance Express",
        "subtitle": "사랑 앞에선 브레이크 따윈 없다",
        "emoji": "🚂",
        "hashtags": ["#로맨틱폭주", "#이벤트장인", "#사랑표현1등"],
        "compatible_types": ["thrill_collector", "touch_fairy"],
    },
    "tsundere_expert": {
        "id": "tsundere_expert",
        "code": "04",
        "name": "츤데레 마스터",
        "english_name": "Tsundere Expert",
        "subtitle": "입으론 퉁퉁, 마음은 콩닥콩닥",
        "emoji": "😤",
        "hashtags": ["#츤데레모먼트", "#행동으로증명", "#알면알수록"],
        "compatible_types": ["straight_shooter", "emotion_translator"],
    },
    "emotion_translator": {
        "id": "emotion_translator",
        "code": "05",
        "name": "감정번역가",
        "english_name": "Emotion Translator",
        "subtitle": "네 마음 내가 다 알아, 말 안 해도",
        "emoji": "🔮",
        "hashtags": ["#공감력만렙", "#감정읽기전문", "#네마음내마음"],
        "compatible_types": ["tsundere_expert", "steady_lover"],
    },
    "thrill_collector": {
        "id": "thrill_collector",
        "code": "06",
        "name": "설렘 수집가",
        "english_name": "Thrill Collector",
        "subtitle": "심장 뛰는 순간이 사는 이유",
        "emoji": "✨",
        "hashtags": ["#설렘덕후", "#심쿵모먼트", "#짜릿한연애"],
        "compatible_types": ["romance_express", "free_spirit"],
    },
    "steady_lover": {
        "id": "steady_lover",
        "code": "07",
        "name": "안정 추구형 연인",
        "english_name": "Steady Lover",
        "subtitle": "요란한 불꽃보다 오래가는 촛불이 좋아",
        "emoji": "🕯️",
        "hashtags": ["#안정이최고", "#루틴연애", "#편안한사랑"],
        "compatible_types": ["emotion_translator", "devoted_partner"],
    },
    "free_spirit": {
        "id": "free_spirit",
        "code": "08",
        "name": "자유영혼 연인",
        "english_name": "Free Spirit",
        "subtitle": "사랑해도 내 하늘은 지켜야 해",
        "emoji": "🦋",
        "hashtags": ["#자유로운연애", "#나도중요", "#건강한거리두기"],
        "compatible_types": ["independent_lover", "push_pull_master"],
    },
    "devoted_partner": {
        "id": "devoted_partner",
        "code": "09",
        "name": "헌신형 파트너",
        "english_name": "Devoted Partner",
        "subtitle": "네가 행복하면 나도 행복해",
        "emoji": "🤲",
        "hashtags": ["#헌신적인사랑", "#네가중심", "#사랑에올인"],
        "compatible_types": ["steady_lover", "emotion_translator"],
    },
    "independent_lover": {
        "id": "independent_lover",
        "code": "10",
        "name": "독립형 연애러",
        "english_name": "Independent Lover",
        "subtitle": "연애해도 나는 나, 너는 너",
        "emoji": "🏔️",
        "hashtags": ["#독립적연애", "#나다움지키기", "#함께하지만각자"],
        "compatible_types": ["free_spirit", "honest_lover"],
    },
    "touch_fairy": {
        "id": "touch_fairy",
        "code": "11",
        "name": "스킨십 요정",
        "english_name": "Touch Fairy",
        "subtitle": "사랑은 말보다 손끝에서 느껴지는 것",
        "emoji": "🤗",
        "hashtags": ["#스킨십러버", "#포옹이좋아", "#터치로전하는사랑"],
        "compatible_types": ["romance_express", "devoted_partner"],
    },
    "sweet_talker": {
        "id": "sweet_talker",
        "code": "12",
        "name": "말로 하는 사랑꾼",
        "english_name": "Sweet Talker",
        "subtitle": "매일 사랑한다 말해도 부족해",
        "emoji": "💬",
        "hashtags": ["#달달한연애", "#말로하는사랑", "#연애말모이"],
        "compatible_types": ["tsundere_expert", "emotion_translator"],
    },
    "honest_lover": {
        "id": "honest_lover",
        "code": "13",
        "name": "팩폭 애정러",
        "english_name": "Honest Lover",
        "subtitle": "진짜 사랑은 솔직함에서 시작돼",
        "emoji": "📢",
        "hashtags": ["#솔직한게매력", "#팩트폭행", "#진짜를원해"],
        "compatible_types": ["independent_lover", "free_spirit"],
    },
    "mood_creator": {
        "id": "mood_creator",
        "code": "14",
        "name": "로맨틱 무드메이커",
        "english_name": "Mood Creator",
        "subtitle": "분위기 만드는 건 내가 책임질게",
        "emoji": "🌙",
        "hashtags": ["#무드메이커", "#데이트장인", "#분위기장인"],
        "compatible_types": ["straight_shooter", "thrill_collector"],
    },
    "long_distance_pro": {
        "id": "long_distance_pro",
        "code": "15",
        "name": "장거리 전문가",
        "english_name": "Long Distance Pro",
        "subtitle": "거리가 뭐예요, 마음이 가까우면 됐지",
        "emoji": "✈️",
        "hashtags": ["#장거리연애", "#마음의거리", "#신뢰가바탕"],
        "compatible_types": ["free_spirit", "steady_lover"],
    },
    "daily_companion": {
        "id": "daily_companion",
        "code": "16",
        "name": "일상 동반자",
        "english_name": "Daily Companion",
        "subtitle": "특별한 이벤트보다 매일의 '밥 먹었어?'가 좋아",
        "emoji": "🏠",
        "hashtags": ["#일상연애", "#소소한행복", "#평범한게좋아"],
        "compatible_types": ["steady_lover", "devoted_partner"],
    },
    "slow_burner": {
        "id": "slow_burner",
        "code": "17",
        "name": "슬로우 버너",
        "english_name": "Slow Burner",
        "subtitle": "천천히, 하지만 확실하게 빠져드는 중",
        "emoji": "🐢",
        "hashtags": ["#슬로우러브", "#천천히깊게", "#스며드는사랑"],
        "compatible_types": ["push_pull_master", "steady_lover"],
    },
    "careful_observer": {
        "id": "careful_observer",
        "code": "18",
        "name": "신중한 관찰자",
        "english_name": "Careful Observer",
        "subtitle": "좋아하기 전에 일단 분석부터",
        "emoji": "🔍",
        "hashtags": ["#신중한연애", "#분석형", "#이성적사랑"],
        "compatible_types": ["slow_burner", "steady_lover"],
    },
    "practical_lover": {
        "id": "practical_lover",
        "code": "19",
        "name": "현실주의 연인",
        "english_name": "Practical Lover",
        "subtitle": "로맨스보다 우리 미래가 궁금해",
        "emoji": "📊",
        "hashtags": ["#현실적연애", "#실용주의", "#함께하는미래"],
        "compatible_types": ["daily_companion", "devoted_partner"],
    },
    "emotional_dreamer": {
        "id": "emotional_dreamer",
        "code": "20",
        "name": "감성 몽글러",
        "english_name": "Emotional Dreamer",
        "subtitle": "눈 마주치면 시작되는 내 머릿속 드라마",
        "emoji": "💭",
        "hashtags": ["#감성연애", "#몽글몽글", "#드라마같은사랑"],
        "compatible_types": ["romance_express", "sweet_talker"],
    },
}
