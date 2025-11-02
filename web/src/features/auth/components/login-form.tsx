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
import { useLogin } from "../hooks/use-auth";
import { GoogleIcon, GitHubIcon } from "./ui/icons";
import { SocialButton } from "./social-button";
import { ArrowRightIcon, Loader2Icon } from "lucide-react";

const formSchema = z.object({
  email: z.email(),
  password: z.string(),
});

export const LoginForm = () => {
  const login = useLogin();
  const form = useForm({
    validationLogic: revalidateLogic(),
    defaultValues: {
      email: "",
      password: "",
    },
    validators: {
      onDynamic: formSchema,
    },
    onSubmit: async ({ formApi }) => {
      if (formApi.state.isValid) {
        login.mutateAsync();
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

            {/* Submit Button */}
            <form.Subscribe
              children={() => (
                <Field className="w-full">
                  <Button
                    type="submit"
                    disabled={login.isPending || form.state.isDefaultValue}
                    className="w-full cursor-pointer"
                  >
                    {login.isPending ? (
                      <>
                        <span className="mr-2">Logging...</span>
                        <Loader2Icon className="animate-spin" />
                      </>
                    ) : (
                      <>
                        <span className="mr-2">Log In</span>
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
