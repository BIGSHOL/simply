/**
 * Button 컴포넌트
 *
 * Phase 1, T1.2: 메인 레이아웃 & 라우팅
 */
import { forwardRef, ButtonHTMLAttributes } from 'react';

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'large' | 'medium' | 'small';
  fullWidth?: boolean;
  isLoading?: boolean;
}

const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      children,
      variant = 'primary',
      size = 'medium',
      fullWidth = false,
      isLoading = false,
      className = '',
      disabled,
      ...props
    },
    ref
  ) => {
    const baseStyles =
      'inline-flex items-center justify-center font-semibold rounded-xl transition-all focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2';

    const variantStyles = {
      primary:
        'bg-[#6366F1] text-white hover:bg-[#4F46E5] focus-visible:ring-[#6366F1] disabled:bg-gray-300 disabled:cursor-not-allowed',
      secondary:
        'bg-transparent text-[#6366F1] border-2 border-[#6366F1] hover:bg-[#E0E7FF] focus-visible:ring-[#6366F1] disabled:border-gray-300 disabled:text-gray-300 disabled:cursor-not-allowed',
      ghost:
        'bg-transparent text-[#6B7280] hover:underline focus-visible:ring-[#6366F1] disabled:text-gray-300 disabled:cursor-not-allowed',
    };

    const sizeStyles = {
      large: 'h-[52px] px-6 text-base',
      medium: 'h-11 px-5 text-sm',
      small: 'h-10 px-4 text-sm font-normal', // 40px for better touch target
    };

    const widthStyles = fullWidth ? 'w-full' : '';

    return (
      <button
        ref={ref}
        className={`${baseStyles} ${variantStyles[variant]} ${sizeStyles[size]} ${widthStyles} ${className}`}
        disabled={disabled || isLoading}
        {...props}
      >
        {isLoading ? (
          <span className="flex items-center gap-2">
            <svg
              className="animate-spin h-4 w-4"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                className="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="4"
              />
              <path
                className="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              />
            </svg>
            로딩 중...
          </span>
        ) : (
          children
        )}
      </button>
    );
  }
);

Button.displayName = 'Button';

export default Button;
