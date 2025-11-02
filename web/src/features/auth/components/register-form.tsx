"use client";

import { Button } from "@/components/ui/button";
import {
  Field,
  FieldError,
  FieldGroup,
  FieldLabel,
  FieldSeparator,
  FieldSet,
} from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { useForm, revalidateLogic } from "@tanstack/react-form";
import z from "zod";
import { useRegister } from "../hooks/use-auth";
import { GoogleIcon, GitHubIcon } from "./ui/icons";
import { SocialButton } from "./social-button";
import { ArrowRightIcon, Loader2Icon } from "lucide-react";

const formSchema = z
  .object({
    email: z.email(),
    password: z
      .string()
      .min(12, `Password must be at least 12 characters`)
      .max(32, `Password must not exceed 32 characters`)
      .refine((val) => /[A-Z]/.test(val), {
        message: "Password must contain at least one uppercase letter",
      })
      .refine((val) => /[a-z]/.test(val), {
        message: "Password must contain at least one lowercase letter",
      })
      .refine((val) => /\d/.test(val), {
        message: "Password must contain at least one number",
      })
      .refine((val) => /[@$!%*?&]/.test(val), {
        message:
          "Password must contain at least one special character (@$!%*?&)",
      }),
    confirmPassword: z.string(),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: "Passwords do not match",
    path: ["confirmPassword"],
  });

export const RegisterForm = () => {
  const register = useRegister();
  const form = useForm({
    validationLogic: revalidateLogic(),
    defaultValues: {
      email: "",
      password: "",
      confirmPassword: "",
    },
    validators: {
      onDynamic: formSchema,
    },
    onSubmit: async ({ formApi }) => {
      if (formApi.state.isValid) {
        register.mutateAsync();
      }
    },
  });
  return (
    <div className="w-full">
      <form
        onSubmit={(e) => {
          e.preventDefault();
          form.handleSubmit();
        }}
        className="w-full max-w-md"
      >
        <FieldGroup>
          {/* Email Field */}
          <FieldSet>
            <form.Field
              name="email"
              children={(field) => (
                <Field>
                  <FieldLabel htmlFor={field.name}>Email</FieldLabel>
                  <Input
                    name={field.name}
                    value={field.state.value}
                    onBlur={field.handleBlur}
                    onChange={(e) => field.handleChange(e.target.value)}
                    type="email"
                    placeholder="new@example.com"
                    required
                    aria-describedby={`${field.name}-error`}
                    aria-required="true"
                  />
                  {!field.state.meta.isValid &&
                    !field.state.meta.isDefaultValue && (
                      <FieldError id={`${field.name}-error`} role="alert">
                        {field.state.meta.errorMap.onDynamic?.map(
                          (error, index) => (
                            <em className="block" key={index}>
                              {error.message}
                            </em>
                          ),
                        )}
                      </FieldError>
                    )}
                </Field>
              )}
            />

            {/* Password Field */}
            <form.Field
              name="password"
              children={(field) => (
                <Field>
                  <FieldLabel htmlFor={field.name}>Password</FieldLabel>
                  <Input
                    type="password"
                    placeholder="************"
                    minLength={12}
                    maxLength={32}
                    required
                    name={field.name}
                    value={field.state.value}
                    onBlur={field.handleBlur}
                    onChange={(e) => field.handleChange(e.target.value)}
                    aria-describedby={`${field.name}-error`}
                    aria-required="true"
                  />
                  {!field.state.meta.isValid &&
                    !field.state.meta.isDefaultValue && (
                      <FieldError id={`${field.name}-error`} role="alert">
                        {field.state.meta.errorMap.onDynamic?.map(
                          (error, index) => (
                            <em className="block" key={index}>
                              {error.message}
                            </em>
                          ),
                        )}
                      </FieldError>
                    )}
                </Field>
              )}
            />

            {/* ConfirmPassword Field */}
            <form.Field
              name="confirmPassword"
              children={(field) => (
                <Field>
                  <FieldLabel htmlFor={field.name}>Confirm Password</FieldLabel>
                  <Input
                    type="password"
                    placeholder="******"
                    required
                    name={field.name}
                    value={field.state.value}
                    onBlur={field.handleBlur}
                    onChange={(e) => field.handleChange(e.target.value)}
                    aria-describedby={`${field.name}-error`}
                    aria-required="true"
                  />
                  {!field.state.meta.isValid &&
                    !field.state.meta.isDefaultValue && (
                      <FieldError id={`${field.name}-error`} role="alert">
                        {field.state.meta.errorMap.onDynamic?.map(
                          (error, index) => (
                            <em className="block" key={index}>
                              {error.message}
                            </em>
                          ),
                        )}
                      </FieldError>
                    )}
                </Field>
              )}
            />

            {/* Submit Button */}
            <form.Subscribe
              children={() => (
                <Field className="w-full">
                  <Button
                    type="submit"
                    disabled={register.isPending || form.state.isDefaultValue}
                    className="w-full cursor-pointer"
                  >
                    {register.isPending ? (
                      <>
                        <span className="mr-2">Registering...</span>
                        <Loader2Icon className="animate-spin" />
                      </>
                    ) : (
                      <>
                        <span className="mr-2">Register</span>
                        <ArrowRightIcon name="arrow-right" />
                      </>
                    )}
                  </Button>
                </Field>
              )}
            />
          </FieldSet>
          <FieldSeparator children={<p className="text-gray-500">or</p>} />
          {/* TODO: Add Social Button */}
          <SocialButton />
        </FieldGroup>
      </form>
    </div>
  );
};
