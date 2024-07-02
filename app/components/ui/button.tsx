import Link from 'next/link'
import clsx from 'clsx'

const baseStyles =
    'duration-150 ease-in-out inline-flex items-center justify-center font-medium group'
const styles = {
    solid: '',
    ghost: '',
    secondary: '',
}

const sizeStyles = {
    sm: 'px-2 py-1.5 text-sm',
    md: 'px-5 py-2 text-base',
    lg: 'px-6 py-3 xl:px-7 xl:py-4 text-base xl:text-lg',
}

const colors = {
    solid: {
        dark: 'bg-slate-700 text-white hover:bg-slate-900',
        light: '',
    },

    ghost: {
        dark: 'rounded-lg backdrop-blur-md bg-white/30 py-2 px-3 hover:bg-white/50 hover:shadow-lg',
        light:
            'rounded-lg backdrop-blur-md bg-white/30 py-2 px-3 hover:bg-white/50 hover:shadow-lg',
    },

    secondary: {
        dark: 'text-slate-900 bg-gray-secondary-100 hover:bg-gray-secondary-200/70',
        light: '',
    },
}

interface ButtonProps {
    variant?: 'solid' | 'ghost' | 'secondary';
    size?: 'sm' | 'md' | 'lg';
    color?: 'dark' | 'light';
    className?: string;
    type?: "button" | "submit" | "reset";
    href?: string;
    children?: React.ReactNode;
    disabled?: boolean;
    onClick?: () => void;  // Step 1: Add this line
}

export function Button({
    variant = 'solid',
    size = 'lg',
    color = 'dark',
    className,
    type,
    href,
    children,
    disabled,
    onClick,  // Destructure the onClick prop
    ...props
}: ButtonProps) {
    className = clsx(
        baseStyles,
        styles[variant],
        sizeStyles[size],
        colors[variant][color],
        className,
    )

    return href ? (
        <Link href={href} className={className} {...props}>
            {children}
        </Link>
    ) : (
        <button className={className} onClick={onClick} disabled={disabled} type={type} {...props}>
            {children}
        </button>
    )
}
