import { AuthLayout } from "@/features/auth/components/auth-layout";
import { LoginForm } from "@/features/auth/components/login-form";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Login - Health Vision",
};

export default function LoginPage() {
  return (
    <AuthLayout
      imgSrc="/images/login_art.png"
      imgAlt="Login Art"
      title="Welcome back"
      description="Today a new day. Sign in to start"
      forwardText="Don't have an account? "
      forwardTitle="Sign up"
      forwardHref="/register"
    >
      <LoginForm />
    </AuthLayout>
  );
}
