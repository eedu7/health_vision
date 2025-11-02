import { useMutation } from "@tanstack/react-query";
import { loginApi, logoutApi, registerApi } from "../api";

export const useLogin = () => {
  return useMutation({
    mutationKey: ["loginUser"],
    mutationFn: async () => {
      await new Promise((res) => setTimeout(res, 1000));
      await loginApi();
    },
  });
};

export const useRegister = () => {
  return useMutation({
    mutationKey: ["registerUser"],
    mutationFn: async () => {
      await new Promise((res) => setTimeout(res, 1000));
      await registerApi();
    },
  });
};

export const useLogout = () => {
  return useMutation({
    mutationKey: ["logoutUser"],
    mutationFn: async () => {
      await new Promise((res) => setTimeout(res, 1000));
      await logoutApi();
    },
  });
};
