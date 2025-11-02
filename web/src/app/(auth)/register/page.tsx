import { AuthLayout } from "@/features/auth/components/auth-layout";
import { RegisterForm } from "@/features/auth/components/register-form";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Register - Health Vision",
};

export default function RegisterPage() {
  return (
    <AuthLayout
      imgSrc="/images/register_art.jpg"
      imgAlt="Register Art"
      title="Create your account"
      description="Start your journey with Health Vision today."
      forwardText="Already have an account? "
      forwardTitle="Sign in"
      forwardHref="/login"
    >
      <RegisterForm />
    </AuthLayout>
  );
}
