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
      description="Sign in to continue your Health Vision experience."
      forwardText="Don't have an account? "
      forwardTitle="Create one"
      forwardHref="/register"
    >
      <LoginForm />
    </AuthLayout>
  );
}
