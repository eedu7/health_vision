import { AuthLayout } from "@/features/auth/components/auth-layout";
import { RegisterForm } from "@/features/auth/components/register-form";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Register - Health Vision",
};

export default function RegisterPage() {
  return (
    <AuthLayout
      imgSrc="/images/login_art.png"
      imgAlt="Login Art"
      title="Welcome back"
      description="Today a new day. Sign up to start"
      forwardText="Already have an account? "
      forwardTitle="Sign in"
      forwardHref="/login"
    >
      <RegisterForm />
    </AuthLayout>
  );
}
