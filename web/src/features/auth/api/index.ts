// TODO: Implement login API
export const loginApi = async () => {
  return {
    success: true,
    message: "Login successful",
    data: {
      user: {
        id: "123",
        email: "user@example.com",
        name: "John Doe",
      },
    },
  };
};

// TODO: Implement register API
export const registerApi = async () => {
  return {
    success: true,
    message: "Registration successful",
    data: {
      user: {
        id: "456",
        email: "newuser@example.com",
        name: "Jane Doe",
      },
    },
  };
};

// TODO: Implement logout API
export const logoutApi = async () => {
  return {
    success: true,
    message: "Logout successful",
  };
};
