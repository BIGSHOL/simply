"""
AI 서비스 - OpenAI API 연동

Phase 2, T2.3: AI 결과 생성 API
"""
import json
from openai import OpenAI
from app.core.config import settings


def generate_result(
    test_title: str,
    test_description: str,
    questions_with_answers: list[dict],
) -> dict:
    """
    OpenAI API를 사용하여 심리 테스트 결과 생성

    Args:
        test_title: 테스트 제목
        test_description: 테스트 설명
        questions_with_answers: [{question, selected_choice}, ...]

    Returns:
        {
            "result_type": "유형명 (예: INFJ)",
            "result_title": "결과 타이틀",
            "result_content": "상세 결과 설명"
        }
    """
    if not settings.openai_api_key:
        # API 키가 없으면 Mock 결과 반환
        return _generate_mock_result(test_title)

    client = OpenAI(api_key=settings.openai_api_key)

    # 프롬프트 구성
    prompt = _build_prompt(test_title, test_description, questions_with_answers)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """당신은 심리 테스트 결과를 분석하는 전문가입니다.
사용자의 답변을 분석하여 재미있고 통찰력 있는 결과를 제공합니다.
결과는 반드시 JSON 형식으로 반환하세요.

반환 형식:
{
    "result_type": "유형명 (간결하게, 예: INFJ, 열정적인 리더형)",
    "result_title": "결과 타이틀 (흥미를 끄는 한 문장)",
    "result_content": "상세 결과 설명 (2-3단락, 장점/특징/조언 포함)"
}"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            response_format={"type": "json_object"},
            temperature=0.7,
            max_tokens=1000,
        )

        result = json.loads(response.choices[0].message.content)
        return {
            "result_type": result.get("result_type", "분석 완료"),
            "result_title": result.get("result_title", "당신의 결과가 나왔어요!"),
            "result_content": result.get("result_content", "결과 생성에 실패했습니다."),
        }

    except Exception as e:
        print(f"OpenAI API error: {e}")
        return _generate_mock_result(test_title)


def _build_prompt(
    test_title: str,
    test_description: str,
    questions_with_answers: list[dict],
) -> str:
    """프롬프트 구성"""
    # 연애 유형 테스트 전용 프롬프트
    if "연애 유형" in test_title or "나의 연애 유형은" in test_title:
        return _build_love_test_prompt(questions_with_answers)

    # 일반 테스트 프롬프트
    qa_text = "\n".join([
        f"Q{i+1}. {qa['question']}\n→ 선택: {qa['selected_choice']}"
        for i, qa in enumerate(questions_with_answers)
    ])

    return f"""다음 심리 테스트 결과를 분석해주세요.

테스트: {test_title}
설명: {test_description}

사용자의 답변:
{qa_text}

위 답변을 바탕으로 사용자의 유형과 특성을 분석해주세요."""


def _build_love_test_prompt(questions_with_answers: list[dict]) -> str:
    """연애 유형 테스트 전용 프롬프트"""
    qa_text = "\n".join([
        f"Q{i+1}. {qa['question']}\n→ 선택: {qa['selected_choice']}"
        for i, qa in enumerate(questions_with_answers)
    ])

    return f"""당신은 MZ세대를 위한 연애 유형 심리테스트의 결과 분석 전문가입니다.

## 역할
- 사용자의 연애 유형 테스트 결과를 바탕으로 개인화된 분석 리포트를 작성합니다.
- 심리학적 인사이트를 제공하되, 가볍고 재미있는 톤으로 전달합니다.
- 부정적인 표현을 피하고, 모든 특성을 긍정적이고 건설적으로 해석합니다.

## 말투 가이드
- MZ세대가 공감할 수 있는 캐주얼하고 위트있는 말투를 사용합니다.
- 너무 진지하거나 딱딱한 표현을 피합니다.
- 적절한 비유와 은유를 사용합니다.
- 공감을 이끌어내는 표현을 사용합니다.

사용자의 답변:
{qa_text}

위 답변을 바탕으로 사용자의 연애 유형과 특성을 분석해주세요.

응답 구조에 다음을 포함해주세요:
1. 인트로 (유형 소개, 2-3문장)
2. 당신의 연애 DNA (핵심 특성 3가지)
3. 연애할 때 이런 모습 (구체적 상황 예시)
4. 이런 점이 매력적이에요 (강점 2-3가지)
5. 이것만 주의하면 완벽! (성장 포인트 1-2가지, 긍정적 표현)
6. 오늘의 연애 한마디 (짧고 임팩트 있는 조언)"""


def _generate_mock_result(test_title: str) -> dict:
    """Mock 결과 생성 (API 키 없을 때 사용)"""
    return {
        "result_type": "탐구형 분석가",
        "result_title": f"당신은 깊이 있는 통찰력을 가진 분석가예요!",
        "result_content": f"""### 당신의 특징

{test_title}에 대한 답변을 분석한 결과, 당신은 **탐구형 분석가** 유형이에요.

**장점**
- 상황을 객관적으로 바라보는 능력이 뛰어납니다
- 논리적인 사고를 바탕으로 문제를 해결합니다
- 깊이 있는 통찰력으로 본질을 꿰뚫어봅니다

**조언**
때로는 직감을 믿고 행동하는 것도 좋아요. 분석도 중요하지만, 마음이 이끄는 대로 움직여보세요!""",
    }
