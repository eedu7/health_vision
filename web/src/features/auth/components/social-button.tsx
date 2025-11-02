import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { GitHubIcon, GoogleIcon } from "./ui/icons";

export const SocialButton = () => {
  return (
    <Field>
      <Button
        type="button"
        variant="outline"
        size="icon"
        disabled
        className="cursor-pointer w-fit"
      >
        <GoogleIcon />
        Google
      </Button>
      <Button
        type="button"
        variant="outline"
        size="icon"
        disabled
        className="cursor-pointer w-fit"
      >
        <GitHubIcon /> Github
      </Button>
    </Field>
  );
};
