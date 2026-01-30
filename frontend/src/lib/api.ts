import type { TestSummary, Test, Result, Answer, ApiResponse } from '@/types';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

async function fetchApi<T>(endpoint: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options?.headers,
    },
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.error?.message || 'API 요청 실패');
  }

  return response.json();
}

// 테스트 목록 조회
export async function getTests(): Promise<ApiResponse<TestSummary[]>> {
  return fetchApi('/tests');
}

// 테스트 상세 조회
export async function getTest(id: string): Promise<ApiResponse<Test>> {
  return fetchApi(`/tests/${id}`);
}

// 테스트 제출
export async function submitTest(id: string, answers: Answer[]): Promise<ApiResponse<Result>> {
  return fetchApi(`/tests/${id}/submit`, {
    method: 'POST',
    body: JSON.stringify({ answers }),
  });
}

// 테스트 좋아요
export async function likeTest(id: string): Promise<{ data: { like_count: number } }> {
  return fetchApi(`/tests/${id}/like`, {
    method: 'POST',
  });
}

// 결과 조회
export async function getResult(id: string): Promise<ApiResponse<Result>> {
  return fetchApi(`/results/${id}`);
}

// 관리자 통계 조회
export interface AdminTestStat {
  id: string;
  title: string;
  category: string;
  play_count_display: number;
  real_play_count: number;
  like_count_display: number;
  real_like_count: number;
}

export async function getAdminStats(key: string): Promise<{ data: AdminTestStat[] }> {
  return fetchApi(`/admin/stats?key=${encodeURIComponent(key)}`);
}
