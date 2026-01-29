/**
 * ShareButtons 컴포넌트 - SNS 공유 버튼
 *
 * Phase 3, T3.3: 공유 기능
 */
'use client';

interface ShareButtonsProps {
  shareUrl: string;
  title: string;
  description?: string;
}

export default function ShareButtons({ shareUrl, title, description }: ShareButtonsProps) {
  const encodedUrl = encodeURIComponent(shareUrl);
  const encodedTitle = encodeURIComponent(title);
  const encodedDesc = encodeURIComponent(description || '');

  const shareLinks = {
    twitter: `https://twitter.com/intent/tweet?url=${encodedUrl}&text=${encodedTitle}`,
    facebook: `https://www.facebook.com/sharer/sharer.php?u=${encodedUrl}`,
    kakao: null, // 카카오는 SDK 필요
  };

  const handleKakaoShare = () => {
    // 카카오 SDK가 로드되어 있는지 확인
    if (typeof window !== 'undefined' && (window as any).Kakao) {
      const Kakao = (window as any).Kakao;
      if (!Kakao.isInitialized()) {
        // 카카오 앱 키가 필요 (환경변수로 관리)
        const kakaoKey = process.env.NEXT_PUBLIC_KAKAO_JS_KEY;
        if (kakaoKey) {
          Kakao.init(kakaoKey);
        }
      }

      if (Kakao.isInitialized()) {
        Kakao.Share.sendDefault({
          objectType: 'feed',
          content: {
            title: title,
            description: description || 'AI 심리 테스트 결과를 확인하세요',
            imageUrl: `${window.location.origin}/images/og-image.png`,
            link: {
              mobileWebUrl: shareUrl,
              webUrl: shareUrl,
            },
          },
          buttons: [
            {
              title: '결과 보기',
              link: {
                mobileWebUrl: shareUrl,
                webUrl: shareUrl,
              },
            },
          ],
        });
        return;
      }
    }

    // 카카오 SDK 없으면 클립보드 복사
    handleCopyLink();
  };

  const handleCopyLink = async () => {
    try {
      await navigator.clipboard.writeText(shareUrl);
      alert('링크가 복사되었습니다!');
    } catch {
      prompt('링크를 복사하세요:', shareUrl);
    }
  };

  const openShareWindow = (url: string) => {
    window.open(url, '_blank', 'width=600,height=400,scrollbars=yes');
  };

  return (
    <div className="flex flex-col items-center gap-4">
      <p className="text-sm text-[#6B7280]">결과를 친구에게 공유하세요</p>

      <div className="flex gap-3">
        {/* 카카오톡 */}
        <button
          onClick={handleKakaoShare}
          className="w-12 h-12 rounded-full bg-[#FEE500] flex items-center justify-center hover:opacity-80 transition-opacity"
          aria-label="카카오톡으로 공유"
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="#3C1E1E">
            <path d="M12 3C6.48 3 2 6.58 2 11c0 2.8 1.86 5.27 4.68 6.68-.15.56-.95 3.56-.98 3.8 0 0-.02.17.09.24.11.07.24.01.24.01.31-.04 3.64-2.39 4.22-2.79.57.08 1.16.13 1.75.13 5.52 0 10-3.58 10-8 0-4.42-4.48-8-10-8z"/>
          </svg>
        </button>

        {/* 트위터/X */}
        <button
          onClick={() => openShareWindow(shareLinks.twitter)}
          className="w-12 h-12 rounded-full bg-black flex items-center justify-center hover:opacity-80 transition-opacity"
          aria-label="X(트위터)로 공유"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="white">
            <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
          </svg>
        </button>

        {/* 페이스북 */}
        <button
          onClick={() => openShareWindow(shareLinks.facebook)}
          className="w-12 h-12 rounded-full bg-[#1877F2] flex items-center justify-center hover:opacity-80 transition-opacity"
          aria-label="페이스북으로 공유"
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
            <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
          </svg>
        </button>

        {/* 링크 복사 */}
        <button
          onClick={handleCopyLink}
          className="w-12 h-12 rounded-full bg-[#6B7280] flex items-center justify-center hover:opacity-80 transition-opacity"
          aria-label="링크 복사"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="white">
            <path d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" fill="none"/>
          </svg>
        </button>
      </div>
    </div>
  );
}
