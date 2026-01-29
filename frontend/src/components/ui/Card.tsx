/**
 * Card 컴포넌트
 *
 * Phase 1, T1.2: 메인 레이아웃 & 라우팅
 */
import { forwardRef, HTMLAttributes } from 'react';

export interface CardProps extends HTMLAttributes<HTMLDivElement> {
  variant?: 'default' | 'result';
  padding?: 'none' | 'small' | 'medium' | 'large';
}

const Card = forwardRef<HTMLDivElement, CardProps>(
  (
    { children, variant = 'default', padding = 'medium', className = '', ...props },
    ref
  ) => {
    const baseStyles = 'rounded-2xl transition-shadow';

    const variantStyles = {
      default:
        'bg-white border border-[#E5E7EB] shadow-sm hover:shadow-md',
      result:
        'bg-gradient-to-br from-[#667eea] to-[#764ba2] text-white shadow-lg',
    };

    const paddingStyles = {
      none: '',
      small: 'p-3',
      medium: 'p-4',
      large: 'p-6',
    };

    return (
      <div
        ref={ref}
        className={`${baseStyles} ${variantStyles[variant]} ${paddingStyles[padding]} ${className}`}
        {...props}
      >
        {children}
      </div>
    );
  }
);

Card.displayName = 'Card';

export default Card;
