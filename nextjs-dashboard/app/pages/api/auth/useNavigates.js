// utils/useNavigate.js

import { useRouter } from 'next/navigation';

export const useNavigate = () => {
  const router = useRouter();

  const navigateToDashboard = () => {
    router.push('/dashboard');

  // const navigateToLogin = () => {
  //   router.push('/login')
  // }
  };

  return { navigateToDashboard };
};
