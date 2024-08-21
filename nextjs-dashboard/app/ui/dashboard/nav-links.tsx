'use client';
 
import {
  ShoppingCartIcon,
  ShoppingBagIcon,
  HomeIcon,
  BookOpenIcon,
  
  
} from '@heroicons/react/24/outline';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import clsx from 'clsx';
 
// ...

const navLinks = [
  { name: 'Home', href: '/', icon: HomeIcon },
  { name: 'Book', href: '/dashboard/books', icon: BookOpenIcon },
  { name: 'Cart', href: '/dashboard/cart', icon: ShoppingCartIcon },
  { name: 'Orders', href: '/dashboard/orders', icon: ShoppingBagIcon},
 
  // Add more links as needed
];
 
export default function NavLinks() {
  const pathname = usePathname();
 
  return (
    <>
      {navLinks.map((link) => {
        const LinkIcon = link.icon;
        return (
          <Link
            key={link.name}
            href={link.href}
            className={clsx(
              'flex h-[48px] grow items-center justify-center gap-2 rounded-md bg-gray-50 p-3 text-sm font-medium hover:bg-sky-100 hover:text-blue-600 md:flex-none md:justify-start md:p-2 md:px-3',
              {
                'bg-sky-100 text-blue-600': pathname === link.href,
              },
            )}
          >
            <LinkIcon className="w-6" />
            <p className="hidden md:block">{link.name}</p>
          </Link>
        );
      })}
    </>
  );
}