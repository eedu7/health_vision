import { AspectRatio } from "@/components/ui/aspect-ratio";
import Image from "next/image";
import Link from "next/link";

interface Props {
  title: string;
  description: string;
  children: React.ReactNode;
  imgSrc: string;
  imgAlt: string;
  forwardHref: string;
  forwardText: string;
  forwardTitle: string;
}

export function AuthLayout({
  children,
  imgSrc,
  imgAlt,
  title,
  description,
  forwardHref,
  forwardText,
  forwardTitle,
}: Props) {
  return (
    <main className="grid grid-cols-2 gap-x-4 py-2 px-4 h-screen w-full max-w-7xl mx-auto">
      <div className="flex flex-col justify-between p-2">
        <div className="flex flex-col space-y-4 justify-center items-start h-full w-full">
          <div className="space-y-4">
            <h1 className="text-4xl font-bold font-mono">{title}</h1>
            <h2 className="font-semibold font-mono text-gray-500">
              {description}
            </h2>
          </div>
          {children}
        </div>
        <p className="flex items-center gap-x-1 justify-start">
          {forwardText}
          <Link
            href={forwardHref}
            className="text-blue-600 hover:text-blue-700 hover:underline underline-offset-2"
          >
            {forwardTitle}
          </Link>
        </p>
      </div>
      <AspectRatio ratio={16 / 9} className="bg-muted rounded-lg">
        <Image
          src={imgSrc}
          alt={imgAlt}
          fill
          className="h-full w-full rounded-lg object-cover dark:brightness-[0.2] dark:grayscale"
        />
      </AspectRatio>
    </main>
  );
}
