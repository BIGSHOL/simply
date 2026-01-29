/**
 * TestQuestion 컴포넌트
 *
 * Phase 2, T2.2: 테스트 진행 화면
 */
import Image from 'next/image';
import TestChoice from './TestChoice';
import type { Question, Answer } from '@/types';

interface TestQuestionProps {
  question: Question;
  selectedAnswer?: Answer;
  onAnswer: (answer: Answer) => void;
}

export default function TestQuestion({
  question,
  selectedAnswer,
  onAnswer,
}: TestQuestionProps) {
  const handleSelect = (choiceId: string) => {
    onAnswer({
      question_id: question.id,
      choice_id: choiceId,
    });
  };

  return (
    <div className="flex flex-col gap-6">
      {/* 질문 */}
      <div className="text-center">
        {question.image_url && (
          <div className="mb-4 relative w-full aspect-video rounded-xl overflow-hidden">
            <Image
              src={question.image_url}
              alt=""
              fill
              className="object-cover"
            />
          </div>
        )}
        <h2 className="text-lg font-semibold text-[#111827]">
          {question.content}
        </h2>
      </div>

      {/* 선택지 목록 */}
      <div className="flex flex-col gap-3">
        {question.choices.map((choice) => (
          <TestChoice
            key={choice.id}
            choice={choice}
            isSelected={selectedAnswer?.choice_id === choice.id}
            onSelect={handleSelect}
          />
        ))}
      </div>
    </div>
  );
}
