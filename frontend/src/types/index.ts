// API 공통 타입 정의

export interface ApiResponse<T> {
  data: T;
  meta?: {
    cached?: boolean;
    generated_at?: string;
  };
}

export interface ApiError {
  error: {
    code: string;
    message: string;
    details?: Array<{
      field: string;
      message: string;
    }>;
    retry_after?: number;
  };
}

// Test 관련 타입
export interface TestSummary {
  id: string;
  title: string;
  description: string;
  thumbnail_url: string | null;
  category: 'personality' | 'love' | 'career' | 'fun';
  question_count: number;
  play_count: number;
  like_count: number;
}

export interface Question {
  id: string;
  order_num: number;
  content: string;
  image_url: string | null;
  choices: Choice[];
}

export interface Choice {
  id: string;
  order_num: number;
  content: string;
}

export interface Test extends TestSummary {
  questions: Question[];
}

// Result 관련 타입
export interface Answer {
  question_id: string;
  choice_id: string;
}

export interface Result {
  id: string;
  test_id: string;
  result_type: string;
  result_title: string;
  result_content: string;
  result_image_url: string | null;
  share_code: string;
}
