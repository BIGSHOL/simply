'use client';

import { useState, useEffect } from 'react';
import { getAdminStats, type AdminTestStat } from '@/lib/api';

export default function AdminPage() {
  const [key, setKey] = useState('');
  const [authenticated, setAuthenticated] = useState(false);
  const [stats, setStats] = useState<AdminTestStat[]>([]);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const savedKey = sessionStorage.getItem('admin_key');
    if (savedKey) {
      fetchStats(savedKey);
    }
  }, []);

  async function fetchStats(adminKey: string) {
    setLoading(true);
    setError('');
    try {
      const res = await getAdminStats(adminKey);
      setStats(res.data);
      setAuthenticated(true);
      sessionStorage.setItem('admin_key', adminKey);
    } catch {
      setError('인증 실패: 키를 확인해주세요');
      sessionStorage.removeItem('admin_key');
      setAuthenticated(false);
    } finally {
      setLoading(false);
    }
  }

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!key.trim()) return;
    fetchStats(key.trim());
  }

  function handleLogout() {
    sessionStorage.removeItem('admin_key');
    setAuthenticated(false);
    setStats([]);
    setKey('');
  }

  async function handleRefresh() {
    const savedKey = sessionStorage.getItem('admin_key');
    if (savedKey) {
      fetchStats(savedKey);
    }
  }

  const categoryLabel: Record<string, string> = {
    personality: '성격',
    love: '연애',
    career: '직장',
    fun: '재미',
  };

  if (!authenticated) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <form onSubmit={handleSubmit} className="w-full max-w-sm">
          <div className="bg-white rounded-xl shadow-sm border border-[#E5E7EB] p-8">
            <h2 className="text-xl font-bold text-[#111827] mb-2 text-center">
              관리자 인증
            </h2>
            <p className="text-sm text-[#6B7280] mb-6 text-center">
              관리자 키를 입력해주세요
            </p>
            <input
              type="password"
              value={key}
              onChange={(e) => setKey(e.target.value)}
              placeholder="관리자 키 입력"
              className="w-full px-4 py-3 border border-[#D1D5DB] rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-[#6366F1] focus:border-transparent mb-4"
              autoFocus
            />
            {error && (
              <p className="text-sm text-red-500 mb-4">{error}</p>
            )}
            <button
              type="submit"
              disabled={loading || !key.trim()}
              className="w-full py-3 bg-[#6366F1] text-white rounded-lg font-medium text-sm hover:bg-[#4F46E5] disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              {loading ? '확인 중...' : '로그인'}
            </button>
          </div>
        </form>
      </div>
    );
  }

  const totals = stats.reduce(
    (acc, s) => ({
      play_count_display: acc.play_count_display + s.play_count_display,
      real_play_count: acc.real_play_count + s.real_play_count,
      like_count_display: acc.like_count_display + s.like_count_display,
      real_like_count: acc.real_like_count + s.real_like_count,
    }),
    { play_count_display: 0, real_play_count: 0, like_count_display: 0, real_like_count: 0 }
  );

  return (
    <div>
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-xl font-bold text-[#111827]">
          테스트 통계
          <span className="text-sm font-normal text-[#6B7280] ml-2">
            총 {stats.length}개
          </span>
        </h2>
        <div className="flex gap-2">
          <button
            onClick={handleRefresh}
            className="px-4 py-2 text-sm text-[#6366F1] border border-[#6366F1] rounded-lg hover:bg-[#EEF2FF] transition-colors"
          >
            새로고침
          </button>
          <button
            onClick={handleLogout}
            className="px-4 py-2 text-sm text-[#6B7280] border border-[#D1D5DB] rounded-lg hover:bg-[#F3F4F6] transition-colors"
          >
            로그아웃
          </button>
        </div>
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-[#E5E7EB] overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="bg-[#F9FAFB] border-b border-[#E5E7EB]">
                <th className="text-left px-4 py-3 font-medium text-[#6B7280]">테스트명</th>
                <th className="text-center px-4 py-3 font-medium text-[#6B7280]">카테고리</th>
                <th className="text-right px-4 py-3 font-medium text-[#6B7280]">표시 참여수</th>
                <th className="text-right px-4 py-3 font-medium text-[#6366F1]">실제 참여수</th>
                <th className="text-right px-4 py-3 font-medium text-[#6B7280]">표시 좋아요</th>
                <th className="text-right px-4 py-3 font-medium text-[#6366F1]">실제 좋아요</th>
              </tr>
            </thead>
            <tbody>
              {stats.map((stat) => (
                <tr key={stat.id} className="border-b border-[#F3F4F6] hover:bg-[#F9FAFB]">
                  <td className="px-4 py-3 text-[#111827]">{stat.title}</td>
                  <td className="text-center px-4 py-3">
                    <span className="inline-block px-2 py-0.5 rounded-full text-xs bg-[#EEF2FF] text-[#6366F1]">
                      {categoryLabel[stat.category] || stat.category}
                    </span>
                  </td>
                  <td className="text-right px-4 py-3 text-[#6B7280]">
                    {stat.play_count_display.toLocaleString()}
                  </td>
                  <td className="text-right px-4 py-3 font-semibold text-[#111827]">
                    {stat.real_play_count.toLocaleString()}
                  </td>
                  <td className="text-right px-4 py-3 text-[#6B7280]">
                    {stat.like_count_display.toLocaleString()}
                  </td>
                  <td className="text-right px-4 py-3 font-semibold text-[#111827]">
                    {stat.real_like_count.toLocaleString()}
                  </td>
                </tr>
              ))}
            </tbody>
            <tfoot>
              <tr className="bg-[#F9FAFB] border-t-2 border-[#E5E7EB]">
                <td className="px-4 py-3 font-bold text-[#111827]">합계</td>
                <td></td>
                <td className="text-right px-4 py-3 font-medium text-[#6B7280]">
                  {totals.play_count_display.toLocaleString()}
                </td>
                <td className="text-right px-4 py-3 font-bold text-[#6366F1]">
                  {totals.real_play_count.toLocaleString()}
                </td>
                <td className="text-right px-4 py-3 font-medium text-[#6B7280]">
                  {totals.like_count_display.toLocaleString()}
                </td>
                <td className="text-right px-4 py-3 font-bold text-[#6366F1]">
                  {totals.real_like_count.toLocaleString()}
                </td>
              </tr>
            </tfoot>
          </table>
        </div>
      </div>
    </div>
  );
}
