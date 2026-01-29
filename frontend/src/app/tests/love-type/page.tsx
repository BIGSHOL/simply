/**
 * 연애 유형 테스트 - 랜딩 페이지
 * Phase 1, T1-LOVE.3
 */
import Link from 'next/link';

export default function LoveTypeLandingPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-pink-100 via-purple-100 to-pink-100">
      <div className="max-w-4xl mx-auto px-4 py-12">
        {/* 헤더 */}
        <div className="text-center space-y-4 mb-12">
          <div className="flex justify-center space-x-2 text-4xl">
            <span className="animate-bounce">♡</span>
            <span className="animate-bounce animation-delay-100">♡</span>
            <span className="animate-bounce animation-delay-200">♡</span>
            <span className="animate-bounce animation-delay-300">♡</span>
            <span className="animate-bounce animation-delay-400">♡</span>
          </div>

          <h1 className="text-4xl md:text-5xl font-bold text-gray-800">나의 연애 유형은?</h1>

          <p className="text-xl text-gray-600">
            3분만에 알아보는 나의 연애 DNA!
            <br />
            20가지 유형 중 당신은 어떤 러버일까요?
          </p>

          <div className="inline-flex items-center space-x-2 bg-pink-500 text-white px-4 py-2 rounded-full text-sm font-medium">
            <span>🔥</span>
            <span>23만명이 참여했어요</span>
          </div>
        </div>

        {/* 히어로 섹션 */}
        <div className="bg-white rounded-2xl shadow-xl p-8 mb-8 text-center space-y-6">
          <div className="text-6xl">💕</div>

          <div className="space-y-2">
            <h2 className="text-2xl font-bold text-gray-800">연애 성향 5가지 차원 분석</h2>
            <p className="text-gray-600">
              적극성, 감정표현, 독립성, 헌신도, 로맨스 5개 차원으로 당신을 분석해요
            </p>
          </div>

          <div className="grid grid-cols-2 md:grid-cols-5 gap-4 max-w-2xl mx-auto">
            {[
              { emoji: '🎯', label: '적극성' },
              { emoji: '💬', label: '감정표현' },
              { emoji: '🆓', label: '독립성' },
              { emoji: '💍', label: '헌신도' },
              { emoji: '💕', label: '로맨스' },
            ].map((dim) => (
              <div key={dim.label} className="text-center space-y-2">
                <div className="text-3xl">{dim.emoji}</div>
                <div className="text-sm text-gray-700 font-medium">{dim.label}</div>
              </div>
            ))}
          </div>
        </div>

        {/* CTA 버튼 */}
        <div className="text-center space-y-4">
          <Link
            href="/tests/love-type/play"
            className="inline-block bg-gradient-to-r from-pink-500 to-purple-500 text-white text-xl font-bold px-12 py-5 rounded-full shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-200"
          >
            내 연애 유형 알아보기
            <div className="text-sm font-normal mt-1 opacity-90">(약 3분 소요)</div>
          </Link>

          <p className="text-sm text-gray-600">20개 문항 | A/B 선택형 | 무료</p>
        </div>

        {/* 결과 티저 */}
        <div className="mt-12">
          <h3 className="text-center text-lg font-bold text-gray-800 mb-6">
            20가지 유형 미리보기
          </h3>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {[
              { name: '직진 러버', emoji: '💘' },
              { name: '밀당 장인', emoji: '🎭' },
              { name: '로맨틱 폭주기관차', emoji: '🚂' },
              { name: '???', emoji: '❓' },
            ].map((type, index) => (
              <div
                key={index}
                className="bg-white rounded-xl p-4 text-center space-y-2 shadow-md hover:shadow-lg transition-shadow"
              >
                <div className="text-4xl">{type.emoji}</div>
                <div className="text-sm font-medium text-gray-700">{type.name}</div>
              </div>
            ))}
          </div>
        </div>

        {/* 안내 문구 */}
        <div className="mt-12 text-center space-y-2">
          <p className="text-sm text-gray-600">
            ✨ 솔직하게 답할수록 정확한 결과가 나와요
          </p>
          <p className="text-sm text-gray-600">
            💡 본능적으로 선택하면 약 3분 안에 완료돼요
          </p>
        </div>
      </div>
    </div>
  );
}
