import axios, { AxiosInstance } from "axios";

const BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export const apiClient: AxiosInstance = axios.create({
  baseURL: BASE_URL,
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true,
});

/**
 * TODO: Add Request and Response interceptors
 * Request -> Send authentication token
 * Response -> Handle errors
 * Response -> Handle not authentication (401).
 *             Redirect to login page or
 *             refresh the authentication token *
 */
